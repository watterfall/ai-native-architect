#!/usr/bin/env python3
"""
validate_skills.py — the skill-quality gate: make the writing-skills bar mechanical.

Every skill in this plugin is a SKILL.md whose frontmatter is the agent-facing
interface — the `description` is what a future agent reads to decide whether to
load the skill at all. The Superpowers `writing-skills` standard fixes that
interface: the frontmatter stays under 1024 characters (the agentskills.io spec
cap), and the description leads with "Use when ..." naming only *triggering
conditions* — never a summary of the skill's own workflow (a workflow summary
becomes a shortcut agents take instead of reading the skill body).

This script makes the deterministic half of that bar a check the loop can RUN,
so the prose contract and the artifact cannot quietly drift. It does NOT replace
judgment: whether a description's triggers are the *right* triggers stays a human
/ micro-test call. The tool does the mechanical part (parse, count, gate); the
substantive "do these triggers fire on the right tasks" call stays human.

ERROR (block, exit 1) — the Run-1 production floor:
  E_NO_FRONTMATTER     no `---` YAML frontmatter block
  E_NO_NAME / E_NO_DESC required frontmatter field missing
  E_NAME_INVALID       name has chars outside [A-Za-z0-9-]
  E_FM_TOO_LONG        frontmatter body > 1024 chars (spec cap)
  E_DESC_NOT_USE_WHEN  description does not start with "Use when"

WARN (surface, don't block — the later-run targets; --strict promotes to ERROR):
  W_DESC_LONG          description > 500 chars (writing-skills target)
  W_DESC_WORKFLOW_LEAK description summarises a workflow (contains -> / arrow chains)
  W_BODY_LONG          SKILL.md body > 500 words (token budget)
  W_VERSION_DRIFT      plugin.json / marketplace.json / CHANGELOG versions disagree
  W_ORPHAN_REFS        a references/*.md file is never mentioned in SKILL.md by any means
  W_DEAD_REF           a relative markdown link in SKILL.md does not resolve

USAGE   python3 validate_skills.py [SKILL.md ...]   # default: all skills/*/SKILL.md
        python3 validate_skills.py --strict         # WARN counts as failure
        python3 validate_skills.py --self-test
EXIT    0 = clean.  1 = findings (ERROR, or any WARN under --strict).  2 = usage error.  Stdlib only.
"""

import sys
import os
import re
import glob

FM_CHAR_LIMIT = 1024
DESC_CHAR_TARGET = 500
BODY_WORD_TARGET = 500

NAME_RE = re.compile(r"^[A-Za-z0-9-]+$")
LEAK_RE = re.compile(r"→|->|\bthen\b.*\bthen\b")
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
VERSION_RE = re.compile(r'"version"\s*:\s*"([^"]+)"')
SEMVER_RE = re.compile(r"(\d+\.\d+\.\d+)")


class Finding:
    def __init__(self, level, code, reason, detail=""):
        self.level, self.code, self.reason, self.detail = level, code, reason, detail


def split_frontmatter(text):
    """Return (fm_body, body) where fm_body is the text between the first '---'
    fence and the next. (None, text) if there is no terminated frontmatter."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return None, text  # unterminated frontmatter


def extract_field(fm_body, key):
    """Extract a top-level YAML value for `key`. Handles 'key: value', quoted
    values, and block scalars (key: >- / | with indented continuation). Returns
    the (folded) value string, or None if the key is absent."""
    lines = fm_body.splitlines()
    kre = re.compile(r"^" + re.escape(key) + r":\s*(.*)$")
    for idx, line in enumerate(lines):
        m = kre.match(line)
        if not m:
            continue
        rest = m.group(1).strip()
        if rest in (">", ">-", ">+", "|", "|-", "|+", ""):
            collected = []
            for cont in lines[idx + 1:]:
                if cont.strip() == "":
                    continue
                if re.match(r"^\s+", cont):
                    collected.append(cont.strip())
                else:
                    break
            return " ".join(collected).strip()
        if (rest.startswith('"') and rest.endswith('"')) or \
           (rest.startswith("'") and rest.endswith("'")):
            rest = rest[1:-1]
        return rest.strip()
    return None


def _ref_surfaced(name, body):
    """True if `name` (a reference filename) is mentioned in the body as a whole
    path-segment / token — a markdown link, an inline-code path, or a list entry —
    not merely as a substring of a *different* filename (`canon.md` ⊄ `mycanon.md`)."""
    return re.search(r"(?<![\w.\-])" + re.escape(name) + r"(?![\w])", body) is not None


def check_refs(body, skill_dir):
    findings = []
    rel = [l for l in MD_LINK_RE.findall(body)
           if not l.startswith(("http://", "https://", "#", "mailto:"))]
    refs_dir = os.path.join(skill_dir, "references")
    ref_files = ([f for f in os.listdir(refs_dir) if f.endswith(".md")]
                 if os.path.isdir(refs_dir) else [])
    # A reference is "surfaced" if its filename appears as a whole token anywhere in
    # the body — a markdown link, an inline-code path (`../../references/_core/x.md`),
    # or a "references on demand" list. Only a file mentioned by NO means is orphaned.
    orphaned = [f for f in ref_files if not _ref_surfaced(f, body)]
    if orphaned:
        findings.append(Finding("WARN", "W_ORPHAN_REFS",
            "reference file(s) never mentioned in SKILL.md by any means — likely orphaned.",
            f"{len(orphaned)} of {len(ref_files)}: " + ", ".join(sorted(orphaned))))
    for l in rel:
        target = l.split("#", 1)[0]
        if not target:
            continue
        if not os.path.exists(os.path.normpath(os.path.join(skill_dir, target))):
            findings.append(Finding("WARN", "W_DEAD_REF",
                "relative markdown link does not resolve.", l))
    return findings


def check_skill_text(text, skill_dir=None):
    """Core check over SKILL.md text. Returns a list of Finding."""
    findings = []
    fm, body = split_frontmatter(text)
    if fm is None:
        findings.append(Finding("ERROR", "E_NO_FRONTMATTER",
            "SKILL.md must open with a '---' YAML frontmatter block."))
        return findings
    fm_chars = len(fm)
    if fm_chars > FM_CHAR_LIMIT:
        findings.append(Finding("ERROR", "E_FM_TOO_LONG",
            "frontmatter body exceeds the spec cap; the description is almost "
            "always the overflow — tighten it.", f"{fm_chars} > {FM_CHAR_LIMIT}"))
    name = extract_field(fm, "name")
    desc = extract_field(fm, "description")
    if name is None:
        findings.append(Finding("ERROR", "E_NO_NAME", "frontmatter is missing `name`."))
    elif not NAME_RE.match(name):
        findings.append(Finding("ERROR", "E_NAME_INVALID",
            "name must use only letters, numbers, and hyphens.", name))
    if desc is None:
        findings.append(Finding("ERROR", "E_NO_DESC", "frontmatter is missing `description`."))
    else:
        if not desc.lstrip().lower().startswith("use when"):
            findings.append(Finding("ERROR", "E_DESC_NOT_USE_WHEN",
                'description must start with "Use when" and name only triggering '
                "conditions — not what the skill does.", desc[:80]))
        if len(desc) > DESC_CHAR_TARGET:
            findings.append(Finding("WARN", "W_DESC_LONG",
                "description over the writing-skills length target.",
                f"{len(desc)} > {DESC_CHAR_TARGET}"))
        if LEAK_RE.search(desc):
            findings.append(Finding("WARN", "W_DESC_WORKFLOW_LEAK",
                "description appears to summarise a workflow (arrow/step chain) — "
                "agents follow the summary instead of reading the skill.", desc[:80]))
    words = len(body.split())
    if words > BODY_WORD_TARGET:
        findings.append(Finding("WARN", "W_BODY_LONG",
            "SKILL.md body over the writing-skills word target (token budget).",
            f"{words} words"))
    if skill_dir is not None:
        findings += check_refs(body, skill_dir)
    return findings


def _read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def check_version_consistency(repo_root):
    pj = _read(os.path.join(repo_root, ".claude-plugin", "plugin.json")) or ""
    mk = _read(os.path.join(repo_root, ".claude-plugin", "marketplace.json")) or ""
    ch = _read(os.path.join(repo_root, "CHANGELOG.md")) or ""
    found = {}
    m = VERSION_RE.search(pj)
    if m:
        found["plugin.json"] = m.group(1)
    m = VERSION_RE.search(mk)
    if m:
        found["marketplace.json"] = m.group(1)
    m = SEMVER_RE.search(ch)
    if m:
        found["CHANGELOG.md"] = m.group(1)
    if len(set(found.values())) > 1:
        return Finding("WARN", "W_VERSION_DRIFT",
            "plugin version disagrees across manifests.",
            "; ".join(f"{k}={v}" for k, v in found.items()))
    return None


def report(label, findings):
    errs = sum(f.level == "ERROR" for f in findings)
    warns = sum(f.level == "WARN" for f in findings)
    print(f"\n=== {label} ===")
    if not findings:
        print("  clean — frontmatter + description meet the bar")
    for f in findings:
        print(f"  [{f.level}] {f.code}" + (f"  ({f.detail})" if f.detail else ""))
        print(f"        {f.reason}")
    return errs, warns


def default_targets():
    here = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(here, "..", "..", ".."))
    return repo_root, sorted(glob.glob(os.path.join(repo_root, "skills", "*", "SKILL.md")))


# ---- self-test fixtures -----------------------------------------------------

GOOD = ("---\nname: good-skill\n"
        "description: Use when a triggering condition appears and you must decide "
        "whether to load this skill.\n---\n# Good Skill\nShort body.\n")
NO_FM = "# no frontmatter here\nbody\n"
NOT_USE_WHEN = "---\nname: x\ndescription: Produce a blueprint of the org.\n---\nbody\n"
BAD_NAME = "---\nname: Bad Name!\ndescription: Use when x.\n---\nbody\n"
LONG_FM = "---\nname: x\ndescription: Use when " + ("x" * 1100) + "\n---\nbody\n"
LEAK = "---\nname: x\ndescription: Use when building; Specify -> Plan -> Ship.\n---\nbody\n"
BLOCK = ("---\nname: x\ndescription: >-\n  Use when the trigger appears\n"
         "  across two folded lines.\n---\nbody\n")


def _has(findings, code):
    return any(f.code == code for f in findings)


def self_test():
    print("SELF-TEST")
    cases = [
        ("GOOD has no ERROR", not any(f.level == "ERROR" for f in check_skill_text(GOOD))),
        ("E_NO_FRONTMATTER", _has(check_skill_text(NO_FM), "E_NO_FRONTMATTER")),
        ("E_DESC_NOT_USE_WHEN", _has(check_skill_text(NOT_USE_WHEN), "E_DESC_NOT_USE_WHEN")),
        ("E_NAME_INVALID", _has(check_skill_text(BAD_NAME), "E_NAME_INVALID")),
        ("E_FM_TOO_LONG", _has(check_skill_text(LONG_FM), "E_FM_TOO_LONG")),
        ("W_DESC_WORKFLOW_LEAK", _has(check_skill_text(LEAK), "W_DESC_WORKFLOW_LEAK")),
        ("block-scalar Use-when accepted",
         not _has(check_skill_text(BLOCK), "E_DESC_NOT_USE_WHEN")),
        ("ref surfaced via inline-code path", _ref_surfaced("taste.md", "see `references/taste.md`")),
        ("ref surfaced via _core path", _ref_surfaced("kernel.md", "read ../../references/_core/kernel.md")),
        ("substring filename is not a false match", not _ref_surfaced("canon.md", "only `mycanon.md` here")),
    ]
    ok = True
    for label, passed in cases:
        print(f"  {'ok  ' if passed else 'FAIL'} {label}")
        ok = ok and passed
    print("  RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main(argv):
    flags = {a for a in argv if a.startswith("--")}
    args = [a for a in argv if not a.startswith("--")]
    if "--self-test" in flags:
        return self_test()
    strict = "--strict" in flags
    if args:
        repo_root, files = None, args
    else:
        repo_root, files = default_targets()
    if not files:
        print("no SKILL.md files found")
        return 2
    total_err = total_warn = 0
    for path in files:
        text = _read(path)
        if text is None:
            print(f"cannot read {path}")
            total_err += 1
            continue
        skill_dir = os.path.dirname(os.path.abspath(path))
        label = os.path.relpath(path, repo_root) if repo_root else path
        e, w = report(label, check_skill_text(text, skill_dir=skill_dir))
        total_err += e
        total_warn += w
    if repo_root:
        vf = check_version_consistency(repo_root)
        if vf:
            _, w = report("repo / versions", [vf])
            total_warn += w
    fail = total_err > 0 or (strict and total_warn > 0)
    print(f"\nSUMMARY: {total_err} error(s), {total_warn} warning(s) across "
          f"{len(files)} skill(s). {'FAIL' if fail else 'PASS'}"
          f"{' (strict)' if strict else ''}.")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
