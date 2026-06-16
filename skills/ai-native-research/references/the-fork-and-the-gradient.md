# The fork and the gradient — where research's judgment goes

This is the deep structure of the research surface. The shared kernel says judgment retreats to a few
nodes (`../../../references/_core/kernel.md` step ②). On the research surface that retreat **forks**, and
the fork is the source of every operating rule in this skill. Read it before you triage a question or
grade a claim.

## The fork: one step ②, two branches with opposite fates

Engineering's scarce judgment is **"对不对" (right/wrong)** — epistemic, has tests, machine-checkable,
so it will be automated. Research's scarce judgment slides further and splits:

- **Machine-checkable judgment → folds back into ① abundance.** In-paradigm question-asking, retrieval,
  standard experiment design — *finding the nearest-neighbour checkable gap in a data-rich region.* This
  is structurally a search problem ("good question = identify the most valuable gap on the knowledge
  frontier," and once "valuable" is narrowed to "checkable by existing data, nearest to the known," it
  is nearest-neighbour search on a knowledge graph). AI is good at it and it parallelizes. It does **not**
  stay reserved for humans — it becomes one more automated execution. Its scarcity is a *temporary
  capability threshold*: what needs a human this year may be eaten by a stronger graph agent next year.
- **Constitutive judgment → sinks to ④ the value bedrock.** Paradigm-level re-framing ("change the
  frame, ask what the old frame cannot") and "which truth is worth knowing." No prior frame to borrow,
  no nearest neighbour to follow, no machine-checkable right/wrong proxy. Its scarcity is **structural**,
  not a capability gap — so a stronger model does not move it left.

**Why you must cut here, or the thesis half-falsifies itself.** If you treat "asking questions" as one
solid block "forever human," reality refutes you on the spot: AI already poses plenty of decent,
checkable in-paradigm questions. The honest move is to concede the in-paradigm half to abundance and
locate the real scarcity in the paradigm-level half — which lands *outside* AI's training distribution
(a Kuhnian paradigm shift has no in-distribution sample). Cutting here makes the thesis *more*
robust: it no longer bets on the falsifiable strong claim "question-asking is forever human," it bets
on the precise, durable one — **the paradigm-level half is not abundified by a stronger model.**

**Conflating the two branches errs in both directions at once.** Guard the checkable branch as "the
last bastion of human dignity" → you never abundify execution, stay trapped in work-hours. Surrender the
constitutive branch as "automatable anyway" → you hand value judgment to the generation layer's default
bias. Seeing the fork clearly *is* seeing "which scarcities time dissolves and which it doesn't" — the
source of every disposition rule downstream.

## The gradient: a continuous axis, not a clean line

"In-paradigm / paradigm-level" reads like a binary, but the truth is a **continuous verifiability
gradient**: from "has a benchmark, right/wrong is machine-checkable" at one end, smoothly to "no
right/wrong, only belonging — worth to whom under which value frame" at the other. The middle is a large
grey zone (checkable, but the *criterion itself* needs value weighting — "how much evidence is enough"
varies by domain).

Drawing it as a gradient matters because **the abundance frontier keeps moving right.** Today's "pose a
good in-paradigm question" may be eaten by a strong knowledge-graph agent next year. So the thesis does
**not** bet that any specific task is "forever human." It bets that the **rightmost segment —
constitutive value judgment — does not move left**, because its scarcity is the structural fact "no
machine-checkable right/wrong," not a capability threshold.

A rough placement of real research actions on the gradient (left = abundified, right = scarce):

```
MACHINE-CHECKABLE · abundified  →→→ [frontier moving right] →→→  CONSTITUTIVE · scarce
param sweep · lit-search/RAG · in-paradigm hypothesis · novelty-vs-noise · worth-knowing
AI Feynman (rediscovers known eqns)              │ no neighbour to follow │ right end, stays put
                                          frontier eating this cell now
```

Seeing it as continuous prevents two symmetric errors: **shoving the right end into the left** (handing
"where should research go" to AI) and **clutching an already-eaten left cell on the right** (a human still
hand-chasing citations a graph agent could fetch).

## Operating consequences (what this fork buys you downstream)

- **Question triage (SKILL Step 2)** is the fork applied at the question level: in-paradigm → batch to
  agents; paradigm-level → human writes the direction + falsification conditions first.
- **The two-axis credibility balance** (`credibility-ledger.md`) is the fork applied at the claim level:
  *evidence strength* is the checkable axis (補-able, route to evidence-seeking); *distance-from-paradigm*
  is the constitutive axis (route to a human). Collapsing them into one score re-commits the conflation
  error and lets "distance from the known" masquerade as "low credibility."
- **The worth-knowing pivot** (`worth-knowing.md`) is the right end of the gradient falling out of
  epistemology into axiology — the volume's deepest move and the hand-off to innovation.

## Evidence discipline for this file's own claims (`canon-vocab.md` §evidence)
This fork is a **constitutive argument** (grade Ⅴ), supported by an epistemic-revolution review and by
strong side-evidence that the generation layer has a conservative bias (the 41.3M-paper bibliometric:
individual output up, topic coverage −4.63%, observational ⇒ causal-cautious, grade Ⅱ). State the
falsification condition plainly: **if "which truth is worth knowing" can be losslessly formalized,
aggregated, or handed to a system to decide, the thesis falls.** Leading indicator to watch: whether
"change-the-frame" contributions stay a low fraction of AI-led research over time. A claim that names
the condition that would overturn it is a claim; one that can't is a slogan.
