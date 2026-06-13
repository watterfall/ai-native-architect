# The 16 Structural Bottlenecks — diagnostic (SHEET 04)

These sixteen bottlenecks are **native to the structure of the traditional organization itself**.
Tools cannot reach them; "transformation" cannot route around them; only redrawing from the bottom
eliminates them. Each is a **proof-by-negation of T1**: each shows that throughput is a property of
the *graph*, not of a node, so speeding up nodes (which is all "adding AI" does) cannot help.

The codes B.01–B.16 index SHEET 04 in canon order for diagnostic convenience (B.01 = serial
dependency chain is canonical; the others follow the sheet's sequence).

## How to use this

**Brownfield (Track B — diagnosing the legacy org):** for each bottleneck, mark hit / partial /
clear and give one concrete line of evidence from the org. Sum to a **hit count 0–16**. A high
count is not a to-do list for fixing the old org — it is the *argument that the old org cannot be
fixed in place*, justifying a from-zero carve-out unit. The single most decisive tell: end-to-end
throughput did not improve after the org "added AI," and queues pile up at hand-offs.

**Greenfield (Track A — designing a new org):** invert each one. State the **design rule** that
prevents importing it. Greenfield's whole advantage is the freedom not to build these in; make the
avoidance explicit so it doesn't creep back via old habits.

## The sixteen

| # | Bottleneck | What it is (the structural defect) | Greenfield design rule (invert it) |
|---|---|---|---|
| **B.01** | Serial dependency chain | Work moves as a relay; total time = sum of stages; flow efficiency often <15%. | Default to parallel fan-out; a serial edge must be justified, not assumed. |
| **B.02** | Quadratic coordination tax | Coordination cost grows ~n²; every added head taxes everyone. | Coordinate through shared context + agents, not n-to-n human sync; keep human n tiny. |
| **B.03** | Executive bandwidth ceiling | All decisions route through a few overloaded humans; a hard throughput cap. | Push decisions to agents + policy gates; reserve humans for the few irreducible judgments. |
| **B.04** | Hierarchical signal decay | Information degrades as it climbs/descends layers. | Flatten; let context flow directly through a system, not through layers of retelling. |
| **B.05** | Functional silos & local optima | Departments optimize locally; the whole is sub-optimal. | Organize around end-to-end value loops, not functions; one graph, shared context. |
| **B.06** | Synchronous coordination tax | Meetings to sync; calendars become the bottleneck. | Async by default; agents + decision logs replace status meetings. |
| **B.07** | Tacit knowledge lock-in | Knowledge lives in heads and chats; lost when people leave/are busy. | Knowledge settles into the context layer as a first-class asset (M.03). |
| **B.08** | Approval chains & diffused accountability | Long approval chains; no one owns the outcome. | A few explicit judgment anchors own consequences; policy gates only for irreversible acts. |
| **B.09** | Headcount-as-capacity | More output ⇒ hire more people; capacity scales with payroll. | Capacity scales with agents + context (compounding leverage), not headcount. |
| **B.10** | Planning cadence mismatch | Annual/quarterly plans vs. a fast-moving world. | Continuous evolution; short loops, instrument and adapt rather than plan-and-freeze. |
| **B.11** | Experiment cost & risk aversion | Each experiment is expensive ⇒ few are run ⇒ risk aversion. | Near-zero-marginal-cost agent experiments; make trying cheap and frequent. |
| **B.12** | Metric theater | Proxies get gamed; activity measured instead of value. | Observability on real outcomes + decision logs; instrument value, not motion. |
| **B.13** | Trust-radius collapse | Trust doesn't scale past a small group; control replaces it. | Keep the human trust radius tiny by design; delegate scale to agents under policy gates. |
| **B.14** | Power gradient & agenda capture | Power and agenda concentrate; ideas filtered by status. | Flat judgment distribution; context + evidence visible to all nodes. |
| **B.15** | Motivation crowding-out | Extrinsic controls crush intrinsic motivation. | Few humans, doing the judgment work that is intrinsically meaningful; automate the drudgery. |
| **B.16** | Niche lock-in | The org is captured by its current niche/position and cannot move. | Treat the org as a living system (M.06); design for re-pointing, not permanence. |

## Reading the count (brownfield)
- **0–3 hits:** unusually healthy; confirm the diagnostic wasn't run too gently. Still: AI-Native is
  about *kind*, not degree — even a healthy org cannot be *grafted* into native form.
- **4–9 hits:** typical incumbent. The bottlenecks are structural; adding AI will not move
  throughput. Carve-out (Track B) is the path.
- **10–16 hits:** the structure *is* the problem. Any in-place "transformation" is theater. The only
  AI-Native move is a from-zero unit; everything else is the adjacent change-management methodology.

Whatever the count, the diagnostic's job is the same: convert "we should add AI" into the correct
question — **"what would this look like if we redrew the graph from zero?"**
