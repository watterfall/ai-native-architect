# The candidate-spread loop (DSN 07) — spread, then converge

This is the kernel's four steps in design's material, run as a *closing* loop. The shape:

> **spec → spread → critique → steer → converge → distill → (feed back to spec)**

It is the same loop engineering runs as spec-driven development (SDD) — with **one crucial
difference**: engineering's verifier is largely *machine-checkable* (tests pass / they don't),
while design's verifier is **constitutive taste**, which sits at the far end of the verifiability
gradient and cannot be fully mechanized. So the converge step stays human in a way SDD's green
build does not. Knowing this is what stops you from quietly handing the verdict to the model.

## Why the loop must *close*

The single most common way the loop fails silently: candidates pile up and nothing flows back.
Without feedback, **every round restarts from the mean** — you regenerate variations of the same
average thing and mistake motion for progress. The closing edge (distill → feed back into the
spec / system) is what makes round *n+1* land in a narrower, sharper band than round *n*. An open
loop is not a slow loop; it is a loop that never compounds.

## The steps, with the why

### ① Spec — frame what "right" means (human)
Write the discriminating spec *before* generating (see `taste-engine.md`). The order is
load-bearing: generate-first means you spend scarce judgment cleaning up divergent comps instead
of steering. Even a minimal spec — for-whom, the job, one feeling, the explicit *not* — narrows
the very first round into the right band.

### ② Spread — generate directionally diverse candidates (agent)
Hand the abundant work to agents. **The point is directional diversity, not high count.** Five
drafts down five genuinely different roads (e.g. *editorial / brutalist / warm-handmade /
data-dense / quiet-minimal*) teach you far more than fifty drafts clustered around the mean. A
high count of near-identical comps is the loop spinning, not spreading. Prompt for *named,
contrasting directions*; if every candidate looks like a sibling, your spread collapsed and you
are sampling the mean repeatedly.

This is also where states, responsive variants, and exports get generated — pure machine work.

### ③ Critique — judge against the scorecard (human, AI-assisted)
Score each candidate on the taste scorecard (empathy / hierarchy / voice / restraint /
distinctiveness). AI may **help you articulate** the critique ("which axis makes you hesitate —
hierarchy, voice, or pacing?") and may simulate how a class of users might react — that is
collaboration. It must not produce the *verdict*. A model's "score" is at bottom a fit to the
mean; let it referee and you let the mean define good.

### ④ Steer — give the generator a *direction*, not a redo (human)
A "revise" must name the axis to move on ("more editorial restraint; kill the gradient; tighten
the hierarchy so the price isn't competing with the headline"). "Make it better" / "one more"
with no stated direction is the loop spinning — the tell that you should **stop and rewrite the
spec**, because you have lost what you are looking for.

### ⑤ Converge — press the button, state the reason (human — the judgment node)
The irreducible node. Full verdict set: `{ship, revise-with-direction, kill-and-respread}`. The
human presses converge and writes *why this one won* — which discriminating criteria it satisfied,
what it refused, who it is for. This sentence is the deliverable's taste rationale and the seed of
the next round's spec.

### ⑥ Distill — feed judgment back (context becomes infrastructure)
Close the loop with a *real* write-back, not a mental note:
- the winning rationale → **decision log** (so the next brief inherits it);
- any newly-discovered hard criterion → a **token / lint rule** in the design system;
- any newly-discovered soft criterion → a sharpened line in the **taste scorecard**;
- rejected directions → a "tried, didn't fit, because…" note (so you don't respread into them).

Each of these is a `feed` edge. If you can't point to the artifact a step wrote, that step didn't
happen.

## Walking the loop on a real brief (it generalizes)

The loop used nothing specific to any one medium. A landing-page brief and a motion brief run the
*same* six steps; only the scorecard's medium-specific axes differ (motion adds **pacing/rhythm**,
which no machine check reaches). When you walk it, narrate the judgment at ③–⑤, not the pixels —
the pixels are the abundant part.

## The hidden degeneration to guard against

"Optimize only the measurable" happens *automatically* unless you prevent it: the machine-checkable
axes (contrast, spacing, alignment) get maxed because they're easy, and the unmeasurable axis (is
this *right for these people*) silently drops out — yielding a flawless interface no one wants.
The loop guards against this only if the converge step keeps a human holding the unmeasurable axis.
That is the whole reason the node stays human.
