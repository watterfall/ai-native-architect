#!/usr/bin/env python3
"""
council.py — the 5-role adversarial review gate, made repeatable.

`references/_core/council.md` defines the quality gate every skill (and, in a
lighter form, every deliverable) passes before shipping: five independent strict
reviewers — kernel-fidelity, domain-expertise, skeptic/collapse-to-enablement,
operability, human-boundary — each scoring 0–10, with

    PASS = mean >= 8.5 AND no single dimension < 8.0.

That gate logic and the role prompts were re-derived by hand on every run. This
script makes them deterministic and consistent:

  --scaffold [artifact]   print the five reviewer prompts, ready to dispatch as
                          parallel subagents (each blind to the others).
  <scores.json>           aggregate role scores into a PASS/FAIL verdict, naming
                          the BINDING (lowest, gate-blocking) dimensions and their
                          top_fix so the next iteration knows exactly what to fix.

Scores file shape — either a list:
    [{"dimension": "kernel-fidelity", "score": 9.0, "top_fix": "..."},
     {"dimension": "skeptic", "score": 7.5, "top_fix": "compounding context is prose"}]
  or a flat object: {"kernel-fidelity": 9.0, "skeptic": 7.5, ...}

EXIT  0 = PASS.  1 = FAIL.  2 = usage/parse error.   Stdlib only.
"""

import sys
import json

MEAN_BAR = 8.5
DIM_FLOOR = 8.0

ROLES = [
    ("kernel-fidelity",
     "Does the work embody the kernel — the scarcity inversion and the five essence "
     "properties (scarce-concentrated judgment, compounding context, capability "
     "decoupled from headcount/effort, self-improvement, incoherent-without-AI)? Or "
     "is it AI-enablement relabeled? Penalize any banned framing (means/ends "
     "sloganeering; the six surfaces narrated as a pipeline)."),
    ("domain-expertise",
     "Reviewing as a senior practitioner of THIS surface (engineer / designer / "
     "researcher / educator / innovator / operator): is the domain craft sound, "
     "specific, and current — or generic filler any LLM would emit without the "
     "skill? Are the named tools/methods real and apt?"),
    ("skeptic-collapse-to-enablement",
     "Adversarial. Try HARD to refute the AI-native claim: find a path where "
     "deleting the AI leaves the same old process, where a human is silently on "
     "every edge, or where 'compounding context' is prose with no real feed. "
     "Default to REFUTED if uncertain — the work survives only if you cannot make "
     "the refutation stick."),
    ("operability",
     "Can a real practitioner RUN this and get the stated work product? Are the "
     "steps executable, the outputs concrete (a file, not a vibe), the trigger "
     "description accurate and appropriately pushy? Is SKILL.md lean (<~500 lines, "
     "progressive disclosure, depth in references)? Would two different inputs "
     "produce two genuinely different outputs (not a template)?"),
    ("human-boundary",
     "Did it honor the stop-lines (judgment-execution.md §止步线)? Did it avoid "
     "over-automating the sacred / desirable-difficulty / trust core? Are judgment "
     "nodes real gates (full verdict set, named negative path, genuine scrutiny — "
     "not a rubber stamp)? Is the emotional-labor boundary respected and flagged, "
     "not over-claimed?"),
]


def scaffold(artifact):
    target = artifact or "<artifact path>"
    print("# Council review — dispatch these five as PARALLEL subagents, each blind "
          "to the others.\n#"
          " Each returns JSON: {dimension, score (0-10), evidence (quote the "
          "artifact), top_fix}.\n"
          f"# Calibrate strict: the canonical org methodology / a top-tier "
          f"practitioner's work = 10.\n# Target under review: {target}\n")
    for i, (dim, brief) in enumerate(ROLES, 1):
        print(f"--- reviewer {i}: {dim} ---")
        print(f"You are an independent, strict reviewer scoring ONLY the "
              f"'{dim}' dimension of {target}.")
        print(brief)
        print("Read the artifact plus references/_core/ (kernel.md, "
              "redraw-vs-graft.md, judgment-execution.md, canon-vocab.md). Score "
              "0-10, justify with a direct quote, and give the single highest-"
              "leverage fix. Return only the JSON object.\n")
    print(f"# Gate: PASS = mean >= {MEAN_BAR} AND no dimension < {DIM_FLOOR}. "
          "Then run:  council.py scores.json")


def load_scores(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    rows = []
    if isinstance(data, dict) and "roles" in data:
        data = data["roles"]
    if isinstance(data, dict):
        for dim, score in data.items():
            rows.append({"dimension": dim, "score": float(score), "top_fix": ""})
    elif isinstance(data, list):
        for r in data:
            rows.append({"dimension": r.get("dimension", "?"),
                         "score": float(r.get("score")),
                         "top_fix": r.get("top_fix", "")})
    else:
        raise ValueError("scores must be a list of {dimension,score} or an object")
    return rows


def aggregate(rows):
    if not rows:
        print("no scores provided")
        return 2
    scores = [r["score"] for r in rows]
    mean = sum(scores) / len(scores)
    below = [r for r in rows if r["score"] < DIM_FLOOR]
    passed = (mean >= MEAN_BAR) and not below

    print("\nCouncil verdict")
    print("=" * 52)
    for r in sorted(rows, key=lambda x: x["score"]):
        flag = "  <- BELOW FLOOR" if r["score"] < DIM_FLOOR else ""
        print(f"  {r['dimension']:34} {r['score']:5.2f}{flag}")
    print("-" * 52)
    print(f"  mean {mean:.2f}  (bar {MEAN_BAR})   floor {DIM_FLOOR}")
    print("=" * 52)

    if passed:
        print("RESULT: PASS")
        return 0

    print("RESULT: FAIL")
    if mean < MEAN_BAR:
        print(f"  - mean {mean:.2f} is below the {MEAN_BAR} bar")
    if below:
        print("  - a dimension below the floor blocks regardless of the mean:")
    # binding = the lowest-scoring dimension(s); fix these first.
    lowest = min(scores)
    binding = [r for r in rows if r["score"] <= max(lowest, DIM_FLOOR - 0.01)
               and r["score"] < DIM_FLOOR] or [r for r in rows if r["score"] == lowest]
    print("\n  Binding weaknesses to fix before re-running the full panel:")
    for r in binding:
        fix = r["top_fix"] or "(no top_fix recorded — re-run the reviewer for one)"
        print(f"    * {r['dimension']} ({r['score']:.2f}): {fix}")
    return 1


def self_test():
    pass_rows = [{"dimension": d, "score": s, "top_fix": ""} for d, s in
                 [("kernel-fidelity", 9.0), ("domain-expertise", 8.8),
                  ("skeptic", 8.5), ("operability", 9.0), ("human-boundary", 8.6)]]
    fail_rows = [
        {"dimension": "kernel-fidelity", "score": 9.0, "top_fix": ""},
        {"dimension": "skeptic", "score": 7.5,
         "top_fix": "compounding context is prose, not a real feed"},
        {"dimension": "operability", "score": 9.0, "top_fix": ""},
        {"dimension": "domain-expertise", "score": 8.8, "top_fix": ""},
        {"dimension": "human-boundary", "score": 8.6, "top_fix": ""}]
    print("SELF-TEST: passing panel ->")
    rc_pass = aggregate(pass_rows)
    print("\nSELF-TEST: failing panel (one dim < 8.0) ->")
    rc_fail = aggregate(fail_rows)
    ok = (rc_pass == 0) and (rc_fail == 1)
    print("\n  RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main(argv):
    flags = {a for a in argv if a.startswith("--")}
    args = [a for a in argv if not a.startswith("--")]
    if "--self-test" in flags:
        return self_test()
    if "--scaffold" in flags:
        scaffold(args[0] if args else None)
        return 0
    if not args:
        print(__doc__)
        return 2
    try:
        rows = load_scores(args[0])
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(f"cannot read scores: {e}")
        return 2
    return aggregate(rows)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
