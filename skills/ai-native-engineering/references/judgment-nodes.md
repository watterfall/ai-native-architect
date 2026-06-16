# Judgment nodes — the irreducible human gates (and the stop-line)

This is the engineering form of "judgment retreats to a few nodes" (`../../references/_core/judgment-execution.md`).
Build `JUDGMENT.md` here: the map of which actions an agent may take freely, and which require a human
sign-off, with each gate having real teeth.

## The stop-line (the one rule you do not cross)

> **Never let an agent's classification *be* the sign-off on an irreversible or adverse action.**

An agent's confidence score, label, or "this looks safe" is an **input** to a human's decision — it must
never *be* the decision. The moment a build ships something irreversible because an agent classified it as
fine, you have offloaded the exact judgment the node exists to protect. This is the offloading you do not do,
no matter how good the classifier's accuracy looks.

## Grade every action: reversibility × blast radius

The map is built by tiering, not by intuition:

| | low blast radius | high blast radius |
|---|---|---|
| **easily reversed** | **Delegate** — structure (types/tests/lint/verifier) handles it; never bother a human | structure + automatic rollback; alert, don't gate |
| **irreversible** | structure + rollback path; gate only if radius is non-trivial | **HUMAN CONFIRMATION GATE** — the few nodes that get a person |

Actions that almost always land in the irreversible × high-radius cell: **production deploy · data
deletion/migration · money movement · sending external communications · granting access/credentials · any
action with legal, safety, or livelihood exposure.**

## Each node is a real gate, not a label

A judgment node only counts if it has teeth:

- **Full verdict set** — declare `{approve, reject, amend}`. Every **non-approve verdict terminates in a
  named next step** — `reject → rollback / abort node`, `amend → re-spec → regenerate`, `escalate → named
  human`. A gate with only an approve edge silently stalls on a "no," which is the worst failure for the very
  node you built to protect.
- **The adverse path is gated too.** An **irreversible adverse outcome is itself an irreversible action**: a
  wrongful reject/fail/deny that harms a third party (a destroyed dataset, a wrongly auto-closed account, a
  bad auto-revert) belongs behind a human node, designed with the *same* care as the positive path. Route
  near-threshold / low-confidence cases into mandatory human review — do not let the agent's quiet "no" be
  final either.
- **Genuine scrutiny, not a rubber stamp.** The human's job at the node must be made *real* by what the
  eval/observability layer surfaces: the diff, the failing eval, the blast-radius estimate, the spec clause at
  risk. If the human has nothing concrete to challenge, the gate is theater — worse than no gate, because it
  launders agent output as human-approved.

## The density trap — fewer real gates beat many theatrical ones

The intuitive error is to gate *everything* "to be safe." This **manufactures unsafety through vigilance
decay**: a human who clicks approve ten thousand times will, on the ten-thousand-and-first — the one that
truly should be stopped — click approve out of habit. More approval is not more safe. Safety comes from
putting the human at the **right few** nodes and letting structure handle the rest, so that when a gate does
fire, the human is actually awake and judging. Switching from *density* to *tiering* is the whole move:
low-radius reversible work goes to structure and never interrupts a person; only the irreversible × high-radius
tier gets an explicit confirmation gate.

## `JUDGMENT.md` scaffold

```markdown
# Judgment-node map — <build name>

## Stop-line
An agent classification is never the sign-off on an irreversible/adverse action.

## Auto (Delegate) — structure-gated, no human
- <action> — gate: <types|tests|lint|verifier>, rollback: <path>
- ...

## Human confirmation gates (irreversible × high radius)
### Node: <action, e.g. production deploy>
- trigger: <when this fires>
- verdict set: {approve, reject, amend}
  - approve → <proceed>
  - reject  → <named: rollback / abort>
  - amend   → <named: re-spec → regenerate>
- adverse path: <how a wrongful deny is caught / who reviews near-threshold cases>
- what the human reviews: <diff | failing eval | blast-radius estimate | spec clause>
- accountable human: <named role>
```

[Source: this volume's boundaries + failure sheets (reversibility × blast radius tiering; vigilance decay)
and `_core/judgment-execution.md` (verdict sets, adverse-path symmetry, the engineering stop-line).]
