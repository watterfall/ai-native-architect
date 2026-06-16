# Operating cadence — the rhythm of a steered org

A native org isn't run by an annual plan cascaded down a hierarchy; it's run as a **steered,
feedback-driven system** (cybernetics returning — one of the forces that make this possible *now*).
The cadence is the rhythm at which the org senses, decides, acts, and writes back. Getting it right
is what lets a small org out-run a large one: its feedback loop is tighter.

## The VSM mapping — why agents make this cadence runnable

Stafford Beer's **Viable System Model** (1972, *Brain of the Firm*) says any organization that
sustains itself needs five subsystems:

- **S1 — operation** (execution)
- **S2 — coordination** (conflict avoidance between operating units)
- **S3 — control** (resource allocation, short-term optimization)
- **S4 — intelligence** (scanning the environment, long-term exploration)
- **S5 — policy** (identity, values)

VSM was widely tried in the 1980s and failed to go mainstream — **because humans could not sustain
in real time the feedback density S2 and S3 demand.** AI removes exactly that constraint. The native
mapping:

| subsystem | who runs it in a native org |
|---|---|
| **S1 operation** | generative agent fleet (execution) |
| **S4 intelligence** | generative/exploration agents (scanning, candidate-generation) |
| **S2 coordination** | telemetry — the observability layer's signals coordinating the fleet |
| **S3 control** | guardrails + real-time control on the agent layer |
| **S5 policy** | **humans** — identity, values, what the org is *for* |

The operator's cadence is the act of running S2/S3 at machine speed (let telemetry + guardrails
coordinate and control the fleet continuously) while holding S5 (the human-only node) deliberately,
not reactively. This is why a native org can run on a *very short* planning horizon — Anthropic is
reported to operate on a "~90-day maximum planning horizon" rather than annual strategy, leaning on
real-time S2/S3 feedback density to stay aligned (directional, from exec interviews/press — not an
independently verified law; treat as an empirical marker, not proof). The point survives the
caveat: **alignment comes from feedback density, not from a long plan.**

## Three cadence bands — set them for this org

Specify, for each band, *what runs* and *who/what touches it*:

1. **Continuous (machine time)** — the fleet executing, telemetry flowing, guardrails firing,
   monitoring agents scoring against evals, items queuing. No standing human attention; humans are
   summoned only by the review queue. This is S1/S2/S3 running on their own.
2. **Tight loop (hours–days)** — the orchestrator's operating loop (scope → dispatch → clear
   escalations → write context back → tune the fleet). Escalations ruled on here. Evals reviewed,
   thresholds tuned, context-debt test checked. This is where the org *improves itself* between
   cycles — the band that replaces the weekly status meeting (B.10 meeting/sync tax: a native org
   reads state from telemetry, it doesn't reconstruct it in a meeting).
3. **Deliberate (weeks–quarter)** — the S5 human work: what's worth doing at all, the org's
   identity and values, the relationships that are the moat, whether a judgment node is mis-placed
   (a design-change request to the architect). Short by traditional standards — the feedback density
   below it does the alignment a long plan used to attempt.

## The cadence anti-patterns (watch for these)

- **The reconstituted status meeting.** If the tight loop has become a meeting where humans manually
  reconstruct what the fleet did, your telemetry isn't doing S2/S3 — you've grafted a feedback ritual
  onto a system that should self-report. State should be *readable*, not *reported* (B.10).
- **The annual plan returns.** If the deliberate band has swollen into a long forward plan that the
  tight loop just executes, you've lost the native cadence — feedback density, not plan length, is
  what aligns a native org. A long horizon also freezes you at today's capability instead of riding
  the curves.
- **The operator becomes the bottleneck.** If every tight-loop cycle routes through one human for
  every item, you've put a single-threaded human on the critical path (B.06 / B.15). The cadence
  should leave the operator clearing *escalations*, not *everything*.
- **Cadence pressure crosses the stop-line.** When throughput targets tempt the runbook to
  auto-resolve trust/safety items to "keep cadence," the cadence is wrong, not the stop-line. Slow
  the band, add a human, or escalate up — never auto-resolve the sacred core (see
  `review-queue-routing.md`).

## Feeds (what the cadence writes back)
- The tight loop's tuning decisions `feed:` the eval suite and dispatch rules — each cycle leaves the
  fleet measurably better than the last (self-improvement made operational).
- The deliberate band's identity/value calls `feed:` the policy layer (S5) and, where they re-place
  a node, a **design-change request** to `ai-native-architect` — the operator surfaces design drift,
  doesn't silently re-architect.
