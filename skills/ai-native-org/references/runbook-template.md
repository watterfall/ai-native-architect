# Operating Runbook — template

Copy this into the org's runbook file and fill it for *this* org. Keep it bespoke: a runbook that
would read identically for two different orgs hasn't grounded its cadence/queue/fleet in this org's
actual loop. Write prose and tables that hold together as one operator's reasoning — don't narrate
your own conformance ("here I put a judgment node…"). The reader should *infer* the rigor.

---

## 0 · Gate verdict
One honest line: **native-to-operate** / **graft-to-redirect** (→ `ai-native-architect`, Track B) /
**boundary-flagged** (human-core node present; runbook supports, never automates it).
*Why:* operating discipline cannot rescue an un-redrawn graph; name what you're actually running.

## 1 · The org in one frame
- Core loop being operated (intake → … → delivered value), one sentence.
- The human judgment nodes the **architecture** defined (you operate up to them; you don't redraw
  them). List by name/role.
- The four-layer substrate as it exists today (model / agent / context / observability), one line
  each — note any layer that's missing or thin (observability-last is the one to fix first).

## 2 · Fleet & orchestration spec  → `orchestration-spec.md`
- Fleet by role (table: class · does the abundant work of · output goes to).
- Dispatch & reconverge: how work fans out and at which **join nodes** it reconverges before
  delivery/irreversible steps (with wait-sets / join policy).
- The orchestrator's own cycle (scope → dispatch → watch queue → clear escalations → write-back →
  tune). Sized to the org (don't over-build the control plane).

## 3 · Operating cadence  → `operating-cadence.md`
- The three bands (continuous / tight loop / deliberate): what runs in each, who/what touches it.
- The VSM / S1–S5 mapping for this org (agents at S1/S4; telemetry+guardrails at S2/S3; humans at
  S5). State the planning horizon and *why feedback density, not plan length, aligns it*.

## 4 · Review-queue routing  → `review-queue-routing.md`  ← load-bearing
Fill the routing table — one row per exception class, every column:

| Trigger | Named human node (role) | Wait-set | Join policy | Verdict set | Each verdict → named next step | SLA / fallback |
|---|---|---|---|---|---|---|
| _low-confidence ≥ class X_ | | | | `{approve, decline, amend}` | approve→… · decline→_named abort/rework_ · amend→… | |
| _irreversible action pending_ | | | | | | |
| _irreversible adverse outcome (third-party harm)_ | | | | | | |
| _regulated / safety-critical_ | _named accountable human (+ regime)_ | | | | | |
| _trust / relationship / safety touch_ | _human-reserved node_ | | n/a | | _escalate up, never auto-resolve_ | |

- **Org stop-line (止步线):** state it explicitly for this org — which node(s) an agent must never
  *be*, and the fallback that holds under cadence pressure (escalate up, not auto-resolve).
- Anti-rubber-stamp: how the observability layer feeds the human *what to challenge* at each gate.

## 5 · Context-upkeep practice  → `context-upkeep.md`
- Write-back-as-done: what's written (decision+rationale / eval result / lesson), to which store,
  read back by whom/what.
- The context-debt test on a cadence (which person leaving paralyzes work >1 week → capture task).
- Freshness ritual: pruning, eval-on-model-swap (regression test, not rewrite), staleness flags.

## 6 · Observability & failure-watch  → `observability-and-failure-modes.md`
- The signals watched (each naming the routing rule it feeds — cut any that feeds none).
- The documented failure modes guarded, with the early signal for each:
  over-automating judgment · context rot · observability-last · dashboard theater · approval-chain
  ghost.

## 7 · Why this is AI-Native and rides the curves
Tight prose (not a scorecard): what judgment is scarce *here*, what context compounds *here*, why
the org would be incoherent without the fleet. Then 2–3 lines of **future-trajectory**: how it
compounds as the curves advance (deeper context moat, cheaper models through the swap abstraction,
A2A dissolving more of the boundary) and what must stay un-frozen (swappable models + a live learning
loop). *(Verify the five essence properties internally; argue, don't print "X/5".)*
