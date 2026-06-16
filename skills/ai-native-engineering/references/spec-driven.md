# Spec-driven development — the spec ladder

The spec is the **control surface for abundant generation.** Agents follow it; an absent or ambiguous spec
is exactly where they "guess at every fork, and a guessed local optimum is often a global debt." This file
covers *what* to put in a spec and — more importantly — *what status* the spec holds in the work.

## A spec is two conditions, not one

"Machine-checkable" is the spec's **form** condition: it says what shape the spec must take so a verifier can
read it. That is necessary but not sufficient. The deeper condition is the spec's **status** — how the team
(and the agents) treat it. Same words on the page, but one team's spec is alive and another's hasn't been
touched in three months, because they sit at different rungs of the ladder.

> A spec that is *machine-checkable but that nobody treats as the source* fails. A spec that is *treated as
> the source but is all prose a machine can't verify* fails. You need both: form **and** status.

## The spec ladder (SDD maturity, three rungs)

1. **Spec-First** — write the spec, then write the code, then shelve the spec. The real source of truth stays
   the code; the spec rots. (This is most "we wrote a spec" efforts. Weakest.)
2. **Spec-Anchored** — spec and code coexist, and the spec is the **authoritative reference**. Code that
   drifts from the spec is treated as a thing that needs explaining (and usually fixing). The spec is a live
   contract, not a relic.
3. **Spec-as-Source** — the spec is the **only** source of truth. Code is either generated from the spec or
   answerable to it; to change behavior you change the spec *first*, then regenerate or re-derive. (Strongest;
   the most fully AI-Native rung, because generation flows *from* the spec rather than the spec describing
   already-written code.)

**Aim as high up the ladder as the stakes justify.** A throwaway script lives fine at Spec-First. A
load-bearing service or anything an agent will regenerate repeatedly wants Spec-Anchored at least, ideally
Spec-as-Source — because that is what makes the agent's regenerations *converge* instead of drift.

## What goes in `SPEC.md`

- **Intent** — what this builds and *why*. The "why" is load-bearing: it lets the agent (and the next human)
  make unspecified micro-decisions in the right direction.
- **Non-goals** — what this explicitly does *not* do. Omitting non-goals is how agents scope-creep efficiently.
- **Acceptance criteria** — the conditions that make it "done," written so they can be turned into checks.
  Each criterion should be traceable to an eval or a test where possible (this is the seam to `verification.md`).
- **Risk boundaries** — the actions/states that are dangerous or irreversible, flagged here so they surface in
  `JUDGMENT.md` and `PERMISSIONS.md`. The spec is where risk is first *named*, not buried later.
- **Interfaces / contracts** — the shapes other code depends on (the seams the human reviews in the
  Delegate/Review/Own model).

## The living-document discipline

The spec is updated **before** behavior changes, not after. When the Learn step of the loop produces a
decision ("we will reject inputs over N"), it amends the spec — that is the spec staying at its rung instead
of sliding down to Spec-First-rot. A spec that only gets written once is, by definition, Spec-First.

## Why this is the AI-Native move (not just "good documentation")

Pre-AI, the spec described work a human would then do by hand; its quality mattered, but the human filled
gaps with judgment in real time. With abundant generation, the agent fills those gaps *at scale and at speed*
— so the spec's precision and *status* now directly determine output quality. The spec stops being
documentation and becomes the **steering input** of the whole build. That is the kernel's "judgment retreats
to a few nodes" expressed at the front of the loop: you move human judgment up out of line-by-line
implementation and into the spec, where it directs everything generated downstream.

[Source: this volume's spec-driven-development sheets + Graziano, AI-Native Engineering (SDD three-rung
maturity). The three-rung ladder and the form-vs-status distinction are the load-bearing claims.]
