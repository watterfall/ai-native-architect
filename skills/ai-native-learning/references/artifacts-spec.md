# Artifacts spec — the reflection store and the interaction template

These are the protocol's **compounding-context layer**. Per the kernel, a loop that lives only in prose
**does not exist** — so every artifact here is specified as real fields with a real write-back edge, not
a vibe. The output of a learning system is not notes; it is **transferable capacity**, and these
artifacts are the evidence that cognitive structure was rebuilt.

## The reflection store (反思库) — field spec

Records *deviation, not answers.* It is the testing-effect and the diff-of-your-own-mind made
operational. A minimum viable entry:

```yaml
entry:
  date: 2026-06-16
  capacity: "debug an unfamiliar React render loop"      # ties to the one capacity
  prompt_or_task: "why does this component re-render on every keystroke?"
  self_answer: |                                          # WRITTEN BEFORE ASKING AI — load-bearing
    My hypothesis: a new object/array literal in props each render breaks memoization.
  what_actually_happened: |
    Close: it was an inline arrow in onChange, not the object. Missed the function-identity case.
  deviation: "I only checked value-identity, not function-identity"   # the WHY, not the answer
  transfer_hook: [ "referential-equality", "useCallback vs useMemo" ]  # links to related errors
  next_review: 2026-06-23                                 # spacing — the process reminds you
```

**Non-negotiable fields and why:**
- **`self_answer`** — the learner's hypothesis, produced *before* the agent answers. This is the single
  most important field: it forces the learner's cognition onto the field first and pins the agent to the
  verify seat. A reflection store *without* a written self-answer is theater — it logs answers, not
  deviation, and the loop never ran.
- **`deviation` + the *why*** — record where you were wrong and why, never "the correct answer." The
  answer is abundance-able; the deviation is the constitutive trace.
- **`transfer_hook`** — links this entry to related errors. This is what turns the store from a flat log
  into a compounding asset (see below).
- **`next_review`** — bakes spacing into the process, turning "I must remember to review" (willpower)
  into "the store reminds me on schedule" (process).

**The write-back edge (name it explicitly):** *what* gets written — a deviation entry after every
error-correction loop and every challenge of an AI output; *what reads it back* — the learner on the
`next_review` date (spaced retrieval) and the agent when asked to quiz the learner on past blind spots.
If you can't name both ends, the store isn't a system, it's a label.

## The interaction template — self-answer first as default route

The reflection store's `self_answer` field is the artifact; the **interaction template** is how it
becomes the *default route* rather than a daily act of restraint. The template for any AI interaction
the learner wants to learn from:

1. **Self-answer** — write your hypothesis/first attempt before the prompt.
2. **Demand reasons** — ask the agent for its *reasoning*, not just the conclusion, so you can challenge
   it (feeds the challenge-hit-rate dashboard signal).
3. **Leave a reflection** — log the deviation back into the store.

Hardened into the toolflow, "self-answer first, demand reasons, leave a reflection" turns "I must resist
asking straight for the answer" (restraint) into "I ask that way by default" (process). This is the
willpower-to-process relocation from `scaffold-and-resistance.md`, instantiated.

## Compounding mechanics — why the store grows more valuable with use

"Compounding" must be a concrete scene, not a nice word. Picture the store running for a year:
- **Month 1** — a scatter of errors; value nearly *linear* (one logged, one gained).
- **Mid-run** — `transfer_hook`s start linking errors that recur in different guises into *patterns*. A
  new entry is no longer "+1"; it activates a re-understanding of a whole *class* of error, lifting the
  value of old entries too.
- **Later** — the whole store becomes a **mirror**: the learner can diff their mental model from three or
  six months ago, seeing which blind spots cleared and which biases held. This "see your own cognition
  change" capacity is **structural, emergent from the whole** — no single entry can give it.

This is exactly how *infrastructure* differs from a *tool*: a tool's value is fixed; infrastructure's
value grows **non-linearly** with use. It is also why the protocol stresses **start small but keep
going** — compounding's precondition is *time*; a grandly built store abandoned in three days never
reaches the compounding moment. The asset compounding here is the learner's *own cognitive trajectory* —
a moat a better model cannot hand them.

## The same-source principle (why plain text, not a smarter notes app)

"Same-source for people and machines" is not "use some AI-capable notes app" — that demotes a principle
into product selection. Its real meaning: **the learner and the agent read/write one carrier that the
learner can reread directly and that is not locked behind any proprietary format.** Why it's load-bearing,
from the contrary: if cognitive traces settle into a private black box reachable only through its own AI
interface, a mediator the learner doesn't control stands between them and their own past thinking. Plain
text (Markdown and the like) excludes that mediator — readable by any tool, diffable, versionable. The
value of plain text is not that it's "simple"; it's that it collapses the distance between the learner
and their cognitive trajectory to zero.

## What "infrastructure" precisely means here

Calling the scaffold "infrastructure" is not rhetoric — it matches three defining traits: **(1) runs in
the background without consuming attention** (a mature store is like running water — there when opened,
not a daily decision); **(2) compounds** (each trace lifts the whole base's value non-linearly via
transfer hooks); **(3) defines the default path** (its greatest power is changing default behavior
rather than relying on willpower — once "self-answer before asking" is the default route, resisting
convenience becomes going with the current).
