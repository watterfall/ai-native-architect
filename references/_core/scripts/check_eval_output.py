#!/usr/bin/env python3
"""
check_eval_output.py — verify the MECHANICAL half of a skill's eval contract.

Each skill's evals/evals.json declares, beside the subjective `pass_criterion`
(the 5-lens council gate, scored by council.py), a `mechanical_checks` block: the
structural invariants the skill's OUTPUT must satisfy on every run — the named
work product is present, the required artifacts exist, the stop-line is surfaced,
etc. Those are deterministic — a grep can decide them. This script runs them
against a supplied skill-output file, so the structural floor is machine-verified
and the council's scarce judgment is spent only on what actually needs judgment.
That division IS the kernel: hand the abundant mechanical check to a tool, keep
the scarce judgment.

It does NOT execute the skill (there is no runner) and it does NOT replace the
council — it gates the mechanical half only. A run that passes every check can
still fail the council; a run that fails one has a concrete, named defect. The
patterns are a structural floor, deliberately permissive — they catch absence,
not quality.

A `mechanical_checks` entry: {id, desc, match, patterns}
  match = "all"   — every pattern must appear (case-insensitive substring)
        | "any"   — at least one pattern appears
        | "regex" — at least one pattern matches via re.search (case-insensitive, multiline)

USAGE   python3 check_eval_output.py <evals.json> --output <skill-output-file>
        python3 check_eval_output.py <evals.json>          # dry run: list the checks
        python3 check_eval_output.py --self-test
EXIT    0 = all checks pass (or dry list).  1 = a check failed.  2 = usage error.  Stdlib only.
"""

import sys
import os
import re
import json


def run_check(check, text):
    pats = check.get("patterns", [])
    mode = check.get("match", "all")
    low = text.lower()
    if mode == "regex":
        return any(re.search(p, text, re.I | re.M) for p in pats)
    if mode == "any":
        return any(p.lower() in low for p in pats)
    return all(p.lower() in low for p in pats)  # default: all


def check_output(evals, text):
    """Return [(check, passed)] for the evals.json's mechanical_checks."""
    return [(c, run_check(c, text)) for c in evals.get("mechanical_checks", [])]


def _byid(results):
    return {c["id"]: passed for c, passed in results}


def _read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def report(skill, evals, text):
    checks = evals.get("mechanical_checks", [])
    print(f"\n=== {skill} ===")
    if not checks:
        print("  (no mechanical_checks declared)")
        return 0
    if text is None:  # dry run — list only
        for c in checks:
            print(f"  • {c['id']} — {c.get('desc', '')}  "
                  f"[{c.get('match', 'all')}: {c.get('patterns')}]")
        return 0
    fails = 0
    for c, passed in check_output(evals, text):
        print(f"  [{'ok  ' if passed else 'FAIL'}] {c['id']} — {c.get('desc', '')}")
        if not passed:
            print(f"         expected ({c.get('match', 'all')}): {c.get('patterns')}")
            fails += 1
    return fails


# ---- self-test fixtures -----------------------------------------------------

SELF_EVALS = {
    "skill_name": "demo",
    "mechanical_checks": [
        {"id": "dual", "desc": "both blocks", "match": "all", "patterns": ["yaml", "mermaid"]},
        {"id": "ledger", "desc": "a ledger", "match": "any", "patterns": ["credibility ledger", "盲点"]},
        {"id": "verdict", "desc": "verdict token", "match": "regex",
         "patterns": [r"self-test[\s\S]{0,20}(yes|no)"]},
    ],
}
SELF_PASS = "```yaml``` plus ```mermaid```; a credibility ledger; self-test: No."
SELF_FAIL = "only a yaml block; no second diagram; nothing else here."


def self_test():
    print("SELF-TEST")
    p = _byid(check_output(SELF_EVALS, SELF_PASS))
    f = _byid(check_output(SELF_EVALS, SELF_FAIL))
    cases = [
        ("all-pass output passes every check", all(p.values())),
        ("fail output fails dual (missing mermaid)", not f["dual"]),
        ("fail output fails ledger (any-of, none present)", not f["ledger"]),
        ("regex verdict matches on pass", p["verdict"]),
        ("regex verdict fails when absent", not f["verdict"]),
    ]
    ok = True
    for label, res in cases:
        print(f"  {'ok  ' if res else 'FAIL'} {label}")
        ok = ok and res
    print("  RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main(argv):
    if "--self-test" in argv:
        return self_test()
    evals_path = output_path = None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--output":
            i += 1
            output_path = argv[i] if i < len(argv) else None
        elif not a.startswith("--") and evals_path is None:
            evals_path = a
        i += 1
    if evals_path is None:
        print(__doc__)
        return 2
    try:
        with open(evals_path, encoding="utf-8") as fh:
            evals = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        print(f"cannot load {evals_path}: {e}")
        return 2
    skill = evals.get("skill_name", os.path.basename(evals_path))
    if output_path is None:
        report(skill, evals, None)
        print("\n(dry run — pass --output <file> to verify against a real skill output)")
        return 0
    text = _read(output_path)
    if text is None:
        print(f"cannot read output {output_path}")
        return 2
    fails = report(skill, evals, text)
    print(f"\nSUMMARY: {fails} mechanical check(s) failed. {'FAIL' if fails else 'PASS'}.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
