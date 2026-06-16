# The credibility ledger — grade, don't score; route, don't delete

The ledger is the load-bearing evidence artifact of an AI-native research finding. When generation is
near-infinite, every claim must pass a balance **before** it costs human attention. The ledger's product
is **not a score** — it is a **disposition** (what to do next with each claim) plus a **grade** (how
strong its evidence is), with the human's **vouch verdict** on top. This file is the how-to for SKILL
Step 4 and the verdict block of Step 5.

## Rule 0 — keep claims and evidence unmixed (`canon-vocab.md` §evidence discipline)
Every row records the **claim** and the **evidence** in *separate* columns, never fused. A claim is one
of: definition / mechanism / proposition / framework / **evidence (with measurement basis)** /
**inference (falsifiable)** / action. Fusing claim and evidence is how a directional signal gets read as
a law and how "everyone says X" gets mistaken for "X is established." Label inferences as falsifiable;
when you cite an empirical marker, note its register (self-reported / model-predicted / observational —
*not* a fact).

## Rule 1 — two axes, never one "credibility score"
Grade each load-bearing claim on **two independent axes**:

1. **Evidence strength (Ⅰ–Ⅴ)** — the *checkable* axis. A weak score has a clear, outsourceable
   disposition: **go get more evidence** (run replication, fetch raw data, check the evidence chain).
   This is a left-of-gradient action — agents and graph rules can do it.
2. **Distance-from-paradigm (near ↔ far)** — the *constitutive* axis. Far-from-paradigm is **not** a
   defect and **not** a virtue; it is a signal that needs a *human* to judge — paradigm-outside noise, or
   paradigm-level re-framing? There is no "補" for this axis; you cannot fetch your way out of it.

**Why not one score.** Collapsing the axes commits the kernel-fork conflation error (`the-fork-and-the-
gradient.md`) at the claim level: the only proxy a single score (or an AI scoring its own work) can use
for "novelty" is *distance from the existing distribution* — which scores the genuinely new as
"outlier / untrustworthy." That is exactly the structural bias that makes AI peer-review reward
in-paradigm and punish paradigm-level work. Two axes keep the two *actions* clean: weak evidence → fetch
evidence (left action); far paradigm → human judges (right action).

## The five-tier evidence register (Ⅰ strongest → Ⅴ weakest)
Use this exact register for the *evidence strength* axis; cite the basis in the row.

| Grade | What it is | Disposition cue |
|---|---|---|
| **Ⅰ** | Pre-registered / multi-site replication / RCT or equivalent load-bearing primary anchor | Strongest; safe to integrate |
| **Ⅱ** | Single strong primary study; large observational / bibliometric (causal must be cautious) | Integrate with the observational≠causal caveat |
| **Ⅲ** | Model prediction · single non-replicated study · third-party independent assessment | Cite *as* "model-predicted" / "single study"; do not state as fact |
| **Ⅳ** | Practitioner / first-party self-report (e.g. a lab's own claim about its system) | Directional signal, needs an independent check |
| **Ⅴ** | Argument / extrapolation / constitutive claim (no direct empirical anchor) | Mark as argument; pair with a leading indicator + falsification condition |

Discipline that keeps the finding from one-shot falsification: **record "已发生 / 正在发生 / 推演"
(happened / happening / extrapolated) separately**, and keep a Ⅱ-grade primary anchor distinct from a
Ⅴ-grade frontier proposition. A first-party "our system passed peer review" is Ⅳ (+ Ⅲ if independently
assessed) — a real signal, not a causal experiment; a "near-infinite materials discovered" result is a
primary anchor, but the *qualifier* ("the vast majority are element substitutions inside known structure
types") is its true contribution to the thesis.

## The four-quadrant disposition (the matrix that earns the instrument its keep)
Cross the two axes; the product is a **disposition**, not a grade:

```
                      NEAR paradigm                 FAR from paradigm
  STRONG evidence │ vouch · integrate (human    │ human looks hard · likely a
  / traceable     │ need not read each one)      │ re-framing → escalate
  ────────────────┼──────────────────────────────┼───────────────────────────────
  WEAK evidence   │ doubt · in-paradigm noise    │ ★ SUSPEND + targeted evidence-
  / untraceable   │ (human need not read)        │   seeking — NEVER delete
```

Three cells are intuitive. The instrument's whole value is the fourth — **weak × far.** A single
credibility score (and naive intuition) kills it: "implausible *and* unsupported, delete." But nearly
every paradigm shift is born exactly here — at birth its evidence is necessarily thin and its frame is
"far" (special relativity vs. the ether both started as fits to the *same* data; natural selection's
original mechanism was later shown wrong yet the idea survived because it was *useful*). A score-only
system would have deleted them all. The correct disposition is a **third action, not binary believe/
disbelieve: suspend, and go find the one piece of evidence that distinguishes "it is noise" from "it is
a re-framing."** An instrument that makes this cell *delete* is hypernormal science's automatic
strangler; one that makes it *suspend + targeted evidence-seeking* is a balance that can actually catch
a paradigm shift.

The ledger sorts **how much human bandwidth to spend**, not how true each claim is. When generation runs
at thousands/hour, reading each one is physically impossible; the balance's value is doing the
"which ones no human needs to read" triage so the scarce attention lands only on the two cells that
need it (strong×far, weak×far).

## Replication: the verifier, and routing errors instead of deleting them
Replication is the load-bearing gate that separates a self-correcting loop from a generator. When a
claim hits the wall, **route it three ways — never delete:**

- **Replicates → integrate** into the base, carrying its evidence edges.
- **Wrong → refutation base** (recorded, not deleted — a negative result is information).
- **Reveals a blind spot → spawn a new eval.** A claim that won't replicate may be wrong *or* may expose
  a gap in current evaluation methods. The blind-spot branch is the *most valuable* one: the error
  becomes a guardrail and a new node type, so the next pass makes the mistake less often. This is the
  error-flows-back loop, identical in shape to engineering's "failure → new test."

A system that only deletes noise is an open-loop generator; one that flows every wall-hit back into a new
rule is a self-correcting research loop. Record the routing outcome as a ledger row (it `feed`s the base).

## The human verdict on top (the stop-line — `judgment-execution.md` §止步线)
A grade is **drafted** by the tool; the **final credibility verdict is signed by a human**: "this is what
I am willing to vouch for, at this grade, in this frame." The verdict carries a full disposition set —
**{vouch / vouch-with-caveats / withhold}** — and a non-vouch verdict terminates in a *named* place:
a caveated-finding section, a refutation-base entry, or a re-open-question edge. A "withhold" with
nowhere to go silently strands the very claim the ledger exists to handle. **Never offload this verdict
to the score.**

## What the ledger feeds (③ context as infrastructure)
Each row is a real write-back: the claim, the unmixed evidence + its register, both axis values, the
disposition, the replication routing outcome, and the signed verdict. These rows *are* the credibility
ledger section of the dossier and they accumulate into the evidence base, so the next research pass
inherits the conflict edges and the refutation entries rather than re-deriving them.
