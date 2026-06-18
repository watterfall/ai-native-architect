#!/usr/bin/env python3
"""
essence_lint.py — catch the canon's banned house-style before it ships.

The kernel and canon forbid specific framings and "attestation" tells, and ask
deliverables to DEMONSTRATE rigor rather than narrate their own conformance
(judgment-execution.md §"Demonstrate, don't attest"; canon-vocab.md §"six
surfaces, no pipeline"; kernel.md §essence-test). Every skill's self-check
re-lists these from memory. This linter makes the mechanical half deterministic,
so a deliverable can be swept in one pass and the model spends its judgment on
the parts that actually need judgment.

It flags, with line numbers and the reason:
  - means/ends sloganeering ("efficiency is the means, people are the end");
  - the six surfaces narrated as a one-way pipeline (org -> ... -> innovation);
  - a printed essence SCORECARD ("5/5", "essence: 4/5") instead of a prose argument;
  - self-narration / attestation tells ("per the kernel", "judgment node here",
    "named, not a footnote", "join_policy: all so the gate cannot fire");
  - placeholder algebra left unfilled ("$X/hr × M ≈ payback in N months").

This is a LINT, not a judge — it catches the deterministic surface tells. The
substantive "is the kernel actually the spine" call stays human / council.

USAGE   python3 essence_lint.py <file> [more files...]
        python3 essence_lint.py --self-test
EXIT    0 = clean.  1 = findings.  2 = usage error.   Stdlib only.
"""

import sys
import re

# (compiled-pattern, code, human reason). Patterns are case-insensitive.
RULES = [
    (re.compile(r"efficiency is the means|people are the end|"
                r"效率是手段|人(是|才是)目的|means to an end.*people"),
     "BANNED_MEANS_ENDS",
     "means/ends sloganeering is banned house-style — the six surfaces are not "
     "means vs. end. Re-express as the one inversion in this surface's material."),

    (re.compile(r"(组织|org)\s*(→|->|then|to)\s*(工程|engineering).*"
                r"(创新|innovation)|"
                r"engineering\s*(→|->)\s*design\s*(→|->)\s*research|"
                r"six surfaces.*pipeline|pipeline of (the )?six surfaces"),
     "BANNED_PIPELINE",
     "the six surfaces are 'six faces of one kernel, no first and no last' — "
     "don't narrate them as a sequence/pipeline."),

    (re.compile(r"\b(essence|kernel|essence test|essence properties)\b[^.\n]{0,40}"
                r"\b[0-5]\s*/\s*5\b|\b[0-5]\s*/\s*5\b\s*(essence|properties)"),
     "BANNED_ESSENCE_SCORECARD",
     "print the essence as a tight PROSE argument, not 'X/5'. Verify the five "
     "properties internally; argue why the work is future-leading."),

    (re.compile(r"per the kernel\b|as the canon (requires|demands|says)|"
                r"judgment node here|named,?\s*not a footnote|"
                r"join_policy:\s*all so (the|this)|"
                r"so the gate cannot fire on the first|"
                r"\bkernel essence\b\s*[:=]|in (full )?conformance with the canon"),
     "ATTESTATION_TELL",
     "demonstrate rigor; don't narrate your own conformance. The reader should "
     "INFER the rigor because the work holds together — cut the self-narration."),

    (re.compile(r"\$[XYZN]\b|\$[XYZN]\s*/\s*(hr|hour|yr|year|unit|mo)|"
                r"[×x]\s*[MN]\b|≈\s*payback|payback (in|≈)\s*[A-Z]\b|"
                r"\bin N (months|weeks|days)\b|\$_+|\$<[^>]+>"),
     "PLACEHOLDER_ALGEBRA",
     "never ship placeholder algebra — compute from the brief's own numbers, or "
     "state the assumption and plug a defensible value."),
]

# substrings that, if present on the matched line, suppress the finding (so a
# rule that quotes the banned phrase to forbid it isn't itself flagged):
SUPPRESS_HINTS = ("banned", "do not", "don't", "never ", "forbid", "instead of",
                  "no \"", "no '", "avoid ", "not allowed", "house-style",
                  "no pipeline", "no means", "not a pipeline", "no first and no last")


class Finding:
    def __init__(self, line_no, code, text, reason):
        self.line_no, self.code, self.text, self.reason = line_no, code, text, reason


def lint_text(text):
    """Scan by paragraph (consecutive non-blank lines), not by physical line. A
    paragraph that contains a suppress hint anywhere (a sentence forbidding the
    phrase, or a heading like "no pipeline") is meta-discussion — skip it whole.
    This stops the canon files, which DEFINE the bans, from flagging themselves
    when the forbidding verb wraps onto a different line than the quoted phrase."""
    findings = []
    lines = text.splitlines()
    i, n = 0, len(lines)
    while i < n:
        if not lines[i].strip():
            i += 1
            continue
        start = i
        while i < n and lines[i].strip():
            i += 1
        para = lines[start:i]
        if any(h in " ".join(para).lower() for h in SUPPRESS_HINTS):
            continue
        for off, line in enumerate(para):
            for pat, code, reason in RULES:
                if pat.search(line):
                    findings.append(Finding(start + off + 1, code,
                                            line.strip()[:90], reason))
    return findings


def report(path, findings):
    print(f"\n=== {path} ===")
    if not findings:
        print("  clean — no banned framing or attestation tells found")
        return 0
    for f in findings:
        print(f"  L{f.line_no:<5} {f.code}")
        print(f"        > {f.text}")
        print(f"        {f.reason}")
    print(f"  {len(findings)} finding(s)")
    return len(findings)


SELF_TEST_DIRTY = """\
Efficiency is the means, people are the end.
The system runs org -> engineering -> design -> research -> learning -> innovation.
Kernel essence: 5/5 — one line each.
We put a judgment node here, per the kernel, named, not a footnote.
Payback: $X/hr × M ≈ payback in N months.
This line is fine and should not be flagged at all.
"""


def self_test():
    findings = lint_text(SELF_TEST_DIRTY)
    codes = {f.code for f in findings}
    expected = {"BANNED_MEANS_ENDS", "BANNED_PIPELINE", "BANNED_ESSENCE_SCORECARD",
                "ATTESTATION_TELL", "PLACEHOLDER_ALGEBRA"}
    print("SELF-TEST")
    for f in findings:
        print(f"  L{f.line_no} {f.code}: {f.text}")
    missing = expected - codes
    print("  expected all 5 rule codes; missing:", missing or "none")
    # the last line must NOT produce a finding
    clean_line_flagged = any(f.line_no == 6 for f in findings)
    ok = (not missing) and (not clean_line_flagged)
    print("  RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main(argv):
    flags = {a for a in argv if a.startswith("--")}
    args = [a for a in argv if not a.startswith("--")]
    if "--self-test" in flags:
        return self_test()
    if not args:
        print(__doc__)
        return 2
    total = 0
    for path in args:
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as e:
            print(f"cannot read {path}: {e}")
            total += 1
            continue
        total += report(path, lint_text(text))
    print(f"\nSUMMARY: {'findings' if total else 'clean'} — {total} total.")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
