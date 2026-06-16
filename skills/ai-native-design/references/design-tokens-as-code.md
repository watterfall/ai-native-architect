# Design tokens as code + the two-layer guardrail

## Why the artifact becomes code (de-canvasing)

The thing that does the work in AI-native design is **not the tool's cleverness — it is the
artifact's form**. When a design lives on an opaque canvas, an agent can't read it, diff it,
critique it, or regenerate it. When it lives as **code** (HTML/CSS/JSX, a token file, component
specs), it moves *into reach of agents*. That is what "de-canvasing" means — not an aesthetic
preference but a structural one: the artifact becomes readable, diffable, and re-generatable.

"Graphics as code" is no new invention — it is a long-standing undercurrent (SVG, CSS, generative
art, parametric design) that AI has now detonated, because the moment the artifact is code, the
abundant-generation loop can run on it. So: **deliver design in code-shaped form by default.**

## Tokens — making "good" machine-enforceable

A **design token** is a named, single-source value for a design decision: `color.brand.primary`,
`space.4`, `type.scale.lg`, `radius.card`, `contrast.min`, `motion.duration.base`. Tokens are the
layer of "good" that a machine *can* enforce. Ship them as a real file (JSON / CSS custom
properties / a TS module), not a Figma swatch library, so:

- generation is constrained to the palette/scale from the first draft (no random hex, no off-grid
  spacing);
- a lint rule can *fail the build* on violations (off-token color, sub-threshold contrast,
  off-scale spacing);
- the system is diffable and reviewable like any code.

Minimum useful token set (expand per project — don't over-build a one-off):
```
color:   brand.primary, brand.ink, surface, surface.alt, accent, danger
type:    family.display, family.text, scale.{sm,base,lg,xl,2xl}, weight.{normal,bold}
space:   scale.{1,2,3,4,6,8,12}   (one ratio, not ad-hoc px)
radius:  {none, card, pill}        (radius is a voice decision — don't default everything round)
contrast: min (e.g. 4.5:1 body, 3:1 large)   ← machine-checkable red line
motion:  duration.{fast,base,slow}, ease.{standard, entrance, exit}
```

## The two-layer guardrail — hard rules + soft criteria

The single most important structural idea: **the design system upgrades from a *post-hoc
document* into a *pre-generation guardrail*.** It stops being "the doc we write after shipping"
and becomes "the constraint we generate inside of." And it has **two layers** — the same spec,
cut in two:

| Layer | Holds | Form | Who enforces |
|---|---|---|---|
| **Hard rules** | "**on-brand** / on-system" — the machine-checkable floor | tokens + **lint** that fails the build | the **machine** |
| **Soft criteria** | "**is this for these people**" — the constitutive taste | the **taste scorecard** (prose criteria) | the **human** |

The hard layer holds *don't drift off-brand*; the soft layer holds *is this right for people*.
**Never push a soft criterion into the hard layer.** Forcing "has soul / on-target / for-whom"
into lint is the classic degeneration: you optimize every checkable metric to a maximum and get a
flawless interface no one wants — because you optimized the measurable and silently dropped the
unmeasurable. Soft criteria stay with the human *by design*, not by omission.

## Same move as architecture's "structure as guardrail"

This is the *same principle* as the organization face's "structure as guardrail," not an analogy:
in both, you encode the constraints up front so the abundant generation happens *inside* a band
you trust, and the scarce human judgment is spent at the edge the encoding can't reach. Tokens +
lint are to design what policy gates + the substrate are to the org: the part of "good" you make
the machine hold, so the human can hold the part that's irreducibly theirs.

## Tokens as compounding context

Tokens and the scorecard are not just constraints — they are **the context that compounds**. Each
round of the loop can write a new token (a hard criterion discovered) or sharpen a scorecard line
(a soft criterion discovered). Over many rounds the system encodes more and more of *your*
fingerprint, so the next first-draft already lands close to it. This is the design face's version
of "context as the core asset": the system is what makes the agents *yours*, and it deepens as a
moat the longer you run the loop.
