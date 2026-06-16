# The self-improving loop, JIT planning, and the Learn write-back

The build runs as a loop — **Specify → Plan → Execute → Verify → Integrate → Learn** — not a waterfall. This
file is the depth on the two steps engineers most often get wrong: **Plan** (do it JIT, and know when to
stop) and **Learn** (the write-back that makes the loop self-improving instead of fake).

## JIT planning — the plan is disposable

Plan **just-in-time**: generate the plan for the *next increment* cheaply, treat it as throwaway, and
**re-plan** when reality diverges. Do not write a big up-front design (BDUF) and then defend it as conditions
change. *Why:* under abundant generation a plan is cheap to regenerate, so the expensive thing is no longer
"planning twice" — it is **letting a long autonomous run accumulate twenty unverified steps before a human
looks** (the snowball). Short plans + frequent verification beat one long plan + late verification.

Practically:
- Plan the smallest increment that produces a verifiable result, then run the loop and check.
- When the agent hits an unspecified fork, that is a signal the **spec** is missing a clause (`spec-driven.md`)
  — amend the spec, don't let the agent guess and move on.
- Keep increments inside one blast-radius tier where you can, so a bad increment is cheap to discard.

## Knowing when to stop — the companion discipline

JIT planning's twin is **knowing when to stop** handing work to the agent. Name, up front, the increments you
will *not* let run unattended — anything that touches a judgment node (`judgment-nodes.md`) or crosses the
trust boundary (`trust-boundary.md`). "Abundant execution is not licence." The skill is not "run the agent
until it's done"; it is "run the agent abundantly up to the line, then stop and judge." The stop is not
timidity — it is the kernel's *essence-is-not-maximalism*: you offload the work that is merely *in the way* of
the point, never the work whose *doing* is the point.

## Context is not "more" — assemble the right small subset

A planning-and-execution discipline that matters at every loop turn: **context-rot is real.** Accuracy is
**non-monotonic** in context length — past a peak, the more you cram into the window, the *lower* the
accuracy. So the move is not "give the agent everything"; it is **retrieval-style assembly** — put the *right
small subset* into the window for *this* increment (the relevant spec clause, the touched interfaces, the
failing eval — not the whole repo). This is context *engineering*, and it is why a queryable codebase
(M.03 — "the codebase becomes queryable infrastructure") beats a giant dumped context.

## The Learn write-back — what makes the loop real (not prose)

**This is the step that, skipped, turns the whole loop into a faster typewriter.** Every meaningful pass must
`feed` a retrievable, compounding artifact — a *real edge*, not a sentence:

- A **new eval** that pins the exact regression you just hit → it now blocks that class forever, at near-zero
  cost (this is how Review-tier work moves down to Delegate-tier permanently — see `delegate-review-own.md`).
- A **decision-log entry** on an architectural call *and its why* → the next pass (human or agent) doesn't
  relitigate it or quietly contradict it.
- A **spec amendment** → the spec stays at its rung instead of rotting to Spec-First.
- A **checker / lint rule** or an **updated permission manifest** → the structure that gates the work gets
  stricter where you learned it needed to be.

*Why this is the whole game:* this is the self-improving property (M.04) that makes the build's second pass
structurally smarter than its first. A rival copies your tools in months but cannot copy an eval suite and a
decision log that have compounded for two years. If your Learn step produces only a paragraph in a summary and
no durable artifact, the loop does not exist — it's prose. The test: *can you point at the file the lesson was
written into, and the thing downstream that reads it back?* If not, go back and write the edge.

[Source: this volume's loops / JIT-planning / context sheets and Graziano, AI-Native Engineering (JIT planning
and "knowing when to stop"; Continuous AI); Anthropic, *Effective Context Engineering for AI Agents*
(non-monotonic accuracy in context length, retrieval-style assembly).]
