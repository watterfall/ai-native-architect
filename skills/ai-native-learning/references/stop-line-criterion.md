# The stop-line criterion — drawing the offload-boundary (交与不交)

This is the deciding artifact of an AI-native learning protocol and the **sharpest stop-line in the
whole system**. Get it right and everything downstream (scaffold, store, dashboard) follows; get it
wrong and you build a faster way to not learn.

## Why a criterion, not a list

Writing "what AI can't do" as a fixed list ages in one model release — every upgrade pushes more
cognition into "AI can do it stably," and the list must be redrawn. Give a **criterion** that lets the
learner judge any new capability on the spot. The criterion has **two dimensions, neither dispensable.**

- **Dimension 1 · Outsourceability** — can the agent do this cognition stably and machine-checkably?
  This dimension **drifts ever-leftward** as models improve. In the AI era it is *high for almost
  everything* — which is exactly why it cannot be the deciding dimension on its own.
- **Dimension 2 · Constitutiveness** — *would the atrophy of this capacity harm the root of the
  learner's judgment?* Is doing it the thing that grows the cognitive structure the activity exists to
  build? This dimension **does not date.** It is what actually decides handing-off.

## The four cells (FIG L.6)

Plot the capacity on the two axes:

```
constitutiveness
  high │  (B) keep, but           │  (D) THE DANGER ZONE
       │      it's also hard       │      tempting AND lethal —
       │      to offload anyway    │      AI can, offloading atrophies it
       │──────────────────────────┼──────────────────────────
  low  │  (A) outsource freely     │  (C) outsource freely
       │      (and it's yours      │      (low stakes, high
       │       anyway)             │       convenience win)
       └──────────────────────────┴──────────────────────────
            low  ◄──── outsourceability ────►  high
```

Only **cell D — high-outsourceability × high-constitutiveness — is the true danger zone.** The agent
*can* do it (tempting) and offloading *atrophies the root of judgment* (lethal). **The stop-line is
cell D's border.** It drifts left as models improve (more capabilities enter "AI can"), but the
*criterion* that locates the border never dates. This is why you ship a criterion, not a list.

## The irreducible human judgment node — make it central

> **Which difficulty is *desirable* and must stay with the human?**

This is the one judgment node the whole protocol exists to protect. The rule (from
`../../../references/_core/judgment-execution.md`): **never offload the desirable difficulty — if the
agent does the struggle, the human doesn't learn.** Offloading the desirable difficulty *destroys the
very capability the activity exists to build.* On the surface of cognition the detector and the
detected are the same thing, so no external verification can catch the loss after the fact — which is
why this stop-line is sharper than any other surface's.

A node with teeth: every "keep with the human" entry must name *how* it stays with the human — a
concrete mechanism, not an intention. The three mechanisms (see `scaffold-and-resistance.md`):
self-answer-first, periodic removal drill, delayed-help window.

## The offload-boundary template (交与不交)

Produce this two-column table for the specific capacity, derived by running the criterion on each step:

| Hand to the agent · abundance-able (cells A/C) | Keep with the learner · inside the stop-line (cell D) |
|---|---|
| Fact lookup, retrieval, summarizing | The **desirable difficulty** — the productive-struggle band |
| Boilerplate, syntax recall, format conversion | **Problem decomposition** (the core of *asking*) |
| In-paradigm, machine-checkable derivation | The **first hypothesis / first attempt** (before any prompt) |
| Generating drafts, examples, explanations — **only at the verify seat, after the learner's attempt** | **From-scratch reproduction** (recall, not recognition) |
| Repetitive, low-value-load execution | **Challenge hit-rate, value judgment, intuition, taste, deep thinking** |

## Three worked judgments (run the criterion out loud)

A criterion is only landed once run. Show the reasoning, with different verdicts:

- **Case 1 · Have AI generate the project's boilerplate.** High outsourceability, **low**
  constitutiveness (boilerplate is not the root of judgment; not remembering it costs nothing) →
  cell A/C, **outsource freely.**
- **Case 2 · Have AI do a first-pass decomposition of a domain problem.** High outsourceability, but
  **high** constitutiveness — problem decomposition is the core of the *asking* capacity; offload it
  long-term and the ability to spot real problems hollows out → **cell D, inside the stop-line.**
  Handling: the learner decomposes first, *then* AI adds the angles they missed (the flow rule).
- **Case 3 · Have AI do an arithmetic the learner is already fluent in.** High outsourceability, **low**
  constitutiveness (long internalized; removal test passes easily) → **outsource freely, without
  guilt.** This is Bjork's caveat: forcing friction onto an already-solid capacity is *undesirable*
  difficulty, i.e. self-harm.

The difference across the three is *entirely* in the **constitutiveness** dimension — outsourceability
is high in almost all of them (the AI era's signature). What decides handing-off is "would its atrophy
harm the root of judgment."

## The two-sided seam with taste

"Taste" appears here and on the design surface, on its two sides. **Learning produces and guards
taste** (the cultivation side — taste is the intuition many lived "good vs. not-good" judgments
deposit; it is a cell-D capacity that atrophies if outsourced). **Design applies taste** (the
application side — it assumes taste already exists in the person judging). Without learning guarding
the source, design has no ruler to use. State this seam when the learner also designs; it's why the
learning surface is the series' critical conscience.
