# The five reusable instruments

"What good means" must become *tools you can run today*, not slogans. These five instruments turn
the method into reusable machinery; use them across projects instead of reinventing per brief.
The first three encode "good"; the last two route work and decisions.

---

## Instrument 1 · Design tokens as code — make "good" machine-enforceable
A named, single-source value file (color/space/type/radius/contrast/motion) shipped as code, with
a **lint** that fails on violations. This is the hard-rule layer: it constrains generation from
the first draft and pre-screens mechanical defects so human judgment is spent on what tooling
can't reach. Full treatment in `design-tokens-as-code.md`.

## Instrument 2 · The design system as a two-layer guardrail — hard rules + soft criteria
The system upgrades from a *post-hoc doc* to a *pre-generation guardrail*, cut into two layers:
**hard rules** (machine-checkable "on-brand," enforced by lint) and **soft criteria**
(constitutive "for these people," held by the human via the scorecard). Never push a soft
criterion into the hard layer. Built from `templates/design-system-spec.md`.

## Instrument 3 · The taste scorecard — decompose "good" into item-by-item criteria
Score candidates on empathy / hierarchy / voice / restraint / distinctiveness (+ pacing for
motion). Turns "I don't like it" into a *named direction* the generator can act on, and turns
intuition into something teachable and feed-back-able. Full treatment in `taste-engine.md`.

## Instrument 4 · The candidate-spread protocol — make "generate more versions" a reusable judgment process
The repeatable loop **spec → spread → critique → steer → converge → distill**, with the rule that
spread means *directional diversity*, not high count, and the loop must *close* (judgment feeds
back) or every round restarts from the mean. Full treatment in `candidate-spread-loop.md`.

---

## Instrument 5 · The generation × taste allocator — triage every kind of decision

The blanket word "design" hides many different decisions. This allocator forces you to break it
**decision by decision** and ask each two questions — which is itself the act of externalizing
taste from intuition. Two axes:

- **Axis 1 — can it be generated / ruled?** *Yes* = judge-able from the artifact alone. *No* =
  needs knowledge of the user/context.
- **Axis 2 — does it need constitutive taste?** *No* = mechanical/determinate. *Yes* = good/bad is
  a judgment.

Crossing them gives four cells, each with a clear verdict:

| | **Axis2 = No** (mechanical) | **Axis2 = Yes** (needs taste) |
|---|---|---|
| **Axis1 = Yes** (generable/rule-able) | **→ Hand to generation.** Fill states, responsive, apply the system, alignment/export — the machine does it all. | **→ Design-system rule.** Machine-checkable *yet value-laden*: palette, spacing scale, contrast thresholds. Humans set the rule once; the machine enforces it. |
| **Axis1 = No** (needs context) | **→ Context-fact question.** No taste, but needs facts: these users' real flows, devices, constraints. Humans establish the facts, then feed generation. | **→ Human taste — keep here.** For whom, has soul, on-target. The far end of the verifiability gradient; **not outsourceable to generation.** |

**How to use it:** run a real project's decisions through it — *filling states, the primary
palette, information hierarchy, brand voice, alignment/spacing* — and see which cell each lands
in. The value is not a single answer; it is being forced to disaggregate "design" and locate the
*few* decisions that fall in the bottom-right cell. Those — and only those — are where your scarce
judgment belongs. Everything in the top-left is the abundant work to hand off; the off-diagonal
cells are "set a rule once" or "go get the facts."

This is the routing complement to the stop-line: the bottom-right cell *is* the stop-line drawn
per-decision. If you find yourself hand-judging something that belongs top-left, you're wasting
scarce judgment; if you find yourself auto-generating something that belongs bottom-right, you've
crossed the stop-line.

---

## The one-line compression (pin it on the wall)

> **Generation handles "many"; people handle "right"; and the standard for "right" must be written
> down by people and grow sharper with each round of judgment.**

That line holds all four principles (system-first · generate-many-judge-hard · write-down-what's-
good · hold-the-human-and-the-heterogeneous) and the mirror image of the three failure modes
(mistaking *fast* for the win · *generation in place of judgment* · *treating taste as
computable*). At any concrete step, ask: *am I helping generation produce more, or helping myself
state the standard for "right" more clearly?* The former the machine increasingly does for you;
the latter is forever your work — and forever where the value of the craft now lives.
