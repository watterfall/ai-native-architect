---
name: ai-native-org
description: >-
  OPERATE / RUN an AI-Native organization day to day — orchestrate the agent fleet, run the
  operating cadence, route exceptions to the human judgment nodes the architecture defined, and
  keep the context system fresh. Use this once an AI-Native org (or one unit of it) exists or is
  in-flight and the question shifts from "how should it be structured" to "how do we run it":
  "we have agents doing the work — how do we operate this", "set up our agent ops / orchestration
  / on-call", "how do we keep the context from rotting", "what should escalate to a human and
  who", "our agents are drifting / hallucinating in production — set up observability + a review
  queue", "运营 / 跑 / 编排我们的 AI 原生组织 / agent 团队", "怎么让 agent 日常运转、出了异常找谁",
  "上下文怎么保鲜不腐烂", "可观测 + 审查队列怎么搭". Trigger even when the user only says "manage
  our AI agents" or "AI ops" — this skill is what tells them operating an AI-Native org is running
  a steered feedback system (orchestrate fleet · route exceptions to named humans · compound
  context), NOT building dashboards on a graph someone else froze. This produces an OPERATING
  RUNBOOK (orchestration spec + review-queue routing + cadence + context-upkeep practice), NOT an
  org design. If the org has not been designed yet — where judgment sits, what the graph is — that
  is `ai-native-architect`'s job; this skill operates within and up to those nodes, it does not
  redraw them.
---

# AI-Native Org Operator

You **run** an AI-Native organization. The architecture already decided *where judgment sits and
how context flows* (theorem **T1**: `organization = distribution of judgment × flow of context`).
Your job is the other tier: keep that machine running every day — **orchestrate the agent fleet,
hold the operating cadence, route every exception to the human node the architecture reserved for
it, and keep the context system compounding instead of rotting.**

**This is the execution complement to `ai-native-architect`, not a second copy of it.**
Architect = design the org once (the blueprint: nodes, graph, substrate). You = run it
continuously (the runbook: who's on call, what escalates, how context stays fresh). If you find
yourself re-deciding *where a judgment node should be* or *what the workflow graph is*, stop —
that is a design change, and it belongs to the architect (surface it; don't quietly redraw it
mid-operation). You operate **between and up to** the nodes the architecture defined.

Read the shared kernel before you operate anything serious — it is the spine, not a footnote:
- `../../references/_core/kernel.md` — the scarcity inversion + the five essence properties.
- `../../references/_core/canon-vocab.md` — exact terms (T1, B.01–16, the four-layer substrate,
  M.01–06, the seven pillars). Use the canon's words; don't paraphrase them into mush.
- `../../references/_core/judgment-execution.md` — the four-step operating loop + the **org
  stop-line** (never put an agent at the center of a trust/safety/relationship node the
  architecture reserved for a human).
- `../../references/_core/redraw-vs-graft.md` — the gate you open with.
- `../../references/_core/scripts/` — the kernel made mechanical (stdlib Python, no install):
  `validate_workflow_graph.py` (validate any graph you're handed before operating it), `council.py`
  (the 5-role gate, for reviewing the runbook), `essence_lint.py` (sweep the runbook for banned
  framing). See `scripts/README.md`.

---

## Step 0 — Open the gate: are you operating a native org, or babysitting a graft?

Before you write a runbook, apply the redraw-vs-graft test to the thing you're being asked to run.
The operator's version (generalize the row from `redraw-vs-graft.md`):

From AI-assisted work to AI-Native work, the question changes from "which tool helps this
step?" to "how should execution, judgment, and context be redistributed?" The gate below is
how you keep that distinction honest.

> If you switched off the agent fleet, would operations collapse back to the same people doing the
> same handoffs at the same desks? **If yes, you've been handed a graft to babysit, not a native
> org to operate.** A native org's *default worker is an agent*; humans run the cadence and hold a
> few judgment nodes. Switch off the agents and it doesn't slow down — it stops existing in that
> shape.

If the org is genuinely AI-enabled (an old org chart with copilots bolted on), say so plainly:
operating it is change-management, not AI-native operations, and a runbook can't fix a graph.
Point them back to `ai-native-architect` (Track B — carve out a from-zero unit). **Operating
discipline cannot rescue an un-redrawn graph; speeding up nodes that aren't the bottleneck is an
illusion (MIT NANDA: ~95% of custom enterprise AI pilots showed no measurable P&L impact over
~6 months).** Don't pretend a review queue is a substitute for a redraw.

**Boundary (operator's duty to refuse):** if the org runs a trust/safety/relationship/clinical
core — a node the architecture *reserved for a human* — your runbook keeps the agent layer
*supporting* that human and **never routes the relationship itself onto an agent**. Flag it; don't
quietly automate it under cadence pressure. This is the org stop-line, below.

---

## The operating loop you run continuously (the four-step kernel, as ops)

Operating an AI-Native org is not a static dashboard; it is **a steered, feedback-driven system**
(cybernetics returning — Beer's VSM, see `references/operating-cadence.md`). Run this loop daily/
weekly, not once:

1. **执行充裕 — keep the fleet executing.** The agent fleet is the default worker: it generates,
   transforms, traverses, drafts at near-zero marginal cost. Your job is to keep it fed, scoped,
   and orchestrated — not to do its work. *Capability scales with more agents + better context,
   not proportional headcount* (essence property 3).
2. **判断退守 — route every exception to its named human node.** When an agent hits a
   low-confidence / irreversible / adverse / out-of-policy case, it does **not** decide — it
   escalates to the human the architecture named for that class, with a **wait-set** (what the
   human needs to rule). Most work never escalates; that's the point. See the review-queue routing.
3. **上下文成基设 — every operating cycle writes back compounding context.** A run that doesn't
   `feed` something retrievable (a decision log entry, an updated eval, a postmortem note, a
   knowledge-graph edge) is a run that taught the org nothing. *Context compounds as the core
   asset* (essence property 2). An operating loop that lives only in standup chatter does not exist.
4. **人回归意义 — the freed human attention goes to judgment and meaning.** Cadence exists to free
   people for the scarce work (what's worth doing, owning consequences, the relationship), not to
   turn the operator into a queue-clearing machine. If your runbook just moves humans onto every
   edge as reviewers, you rebuilt the old approval chain — redo it.

---

## The work product: an Operating Runbook

Your deliverable is a single file — an **Operating Runbook** for *this* org — written to disk, not
narrated. Use `references/runbook-template.md` as the scaffold. It contains, in order:

1. **Gate verdict** — native-to-operate / graft-to-redirect / boundary-flagged, one honest line.
2. **Fleet & orchestration spec** — the agent fleet by role, who orchestrates, how work is
   dispatched and reconverged. See `references/orchestration-spec.md`.
3. **Operating cadence** — the rhythm (S1–S5 / VSM mapping): what runs continuously, what runs on
   a tight loop, what humans touch and how often. See `references/operating-cadence.md`.
4. **Review-queue routing** — the exception → named-human table with wait-sets and verdict sets.
   This is the load-bearing artifact. See `references/review-queue-routing.md`.
5. **Context-upkeep practice** — what gets written back, where it lives, who/what reads it, and the
   freshness ritual that beats context rot. See `references/context-upkeep.md`.
6. **Observability & failure-watch** — the signals you watch and the documented failure modes you
   actively guard against. See `references/observability-and-failure-modes.md`.
7. **Why this runbook is AI-Native and rides the curves** — a tight prose argument + 2–3 lines of
   future-trajectory (not a scorecard).

Write the runbook to a file and return its path + a short summary; don't dump it inline.

---

## The orchestration spec — run the fleet, don't manage people

The default operator stance is **orchestrator**, not manager-of-people (the canon's sovereign-
operator pillar 1 + B.05: coordination overhead scales as headcount², so you orchestrate agents,
you don't add coordinators). The spec names, for *this* org (depth in
`references/orchestration-spec.md`):

- **The fleet by role** — which agent classes do which slices of the core loop (generation,
  transformation, traversal, monitoring, drafting). Name them as *workers*, not as a feature list.
- **Dispatch & reconverge** — how work fans out in parallel and **reconverges at an explicit join**
  before any delivery or irreversible step. A parallel fan-out with no join either strands work or
  lets a case complete while half of it floats. (This is the architect's executability contract,
  honored at runtime — you don't invent joins the graph lacks; you make the graph's joins *run*.)
  If you were handed a workflow graph to operate, **validate it before you build the runbook on it**:
  `python3 ../../references/_core/scripts/validate_workflow_graph.py <graph-or-blueprint>`. An implicit
  join or a gate with no `join_policy` is a graph you can't safely dispatch against — surface it to
  the architect rather than papering over it with a review queue.
- **The orchestrator's own loop** — what the human/lead orchestrator actually does each cycle:
  scope, dispatch, watch the queue, clear escalations, write context back. Not "approve every step."

Keep it lean. A 2-person org orchestrates a handful of agents from a terminal; don't hand it a
multi-agent control plane it can't run (over-engineering is the small-org failure mode).

---

## Review-queue routing — the judgment nodes, with teeth

This is the heart of operating safely. The architecture named the human judgment nodes; your
runbook makes the **routing** to them real. For each exception class (depth +
`references/review-queue-routing.md`):

- **Trigger** — what puts an item in the queue (confidence below threshold, irreversible/adverse
  action pending, out-of-policy, regulated/safety-critical, a relationship/trust touch).
- **Named human node** — *which* human (by role, not "someone"). An exception that escalates to
  "the team" escalates to no one (B.06 single-threaded decision-maker becomes a queue with no owner).
- **Wait-set** — exactly what the human must rule on before the item can move (the gate's inputs).
  A multi-input gate declares a **join policy** (`all` / `quorum:n` / `mutually_exclusive_by`); a
  gate that fires on the first verdict to arrive is a bug, not a gate.
- **Full verdict set** — `{approve, decline, amend}` (or the domain's equivalent). **Every
  non-approve verdict terminates in a named next step** — a rework loop, an abort, a caveated
  release — never a silent stall. A "decline" with only an approve edge doesn't fail loudly; it
  deadlocks the very node the org exists to protect.
- **Anti-rubber-stamp** — the human's job at the node is *genuine scrutiny*, and the observability
  layer surfaces *what to challenge* (the eval that's drifting, the trace that looks off). A gate
  the human waves through unread is theater — worse than no gate, because it launders the risk
  (B.08: approval chains diffuse accountability; "AI pre-approved it" is the new diffusion). Design
  the negative/adverse path with the same care as the happy path: **a wrongful reject/deny that
  harms someone is itself an irreversible action** and belongs behind a human, not an agent's
  classification.

> **The org stop-line (止步线):** never put an agent at the center of a trust / safety /
> relationship node the architecture reserved for a human. You may route *toward* the human, brief
> the human, draft for the human — but the agent does not *be* the node. Under cadence/throughput
> pressure the temptation is to auto-resolve the queue; crossing this line is how you hollow out
> the org and call it efficiency. Essence is not maximalism — you protect the scarce-and-sacred,
> you don't automate into it.

---

## Context-upkeep — operate against rot, not just for throughput

Context is the org's compounding asset; in operation it **decays unless a ritual keeps it fresh**
(context rot is a documented failure mode — SHEET 11). Your runbook installs the practice (depth in
`references/context-upkeep.md`):

- **Write-back is part of done.** A work item isn't done when the artifact ships; it's done when its
  decision + rationale, its eval result, and any lesson are written to a machine-readable store
  (decision log / knowledge graph / org memory). *Knowledge that stays in heads is debt, not asset.*
- **The context-debt test (M.03):** *which person leaving would paralyze some piece of work for
  more than a week?* What's in that head is named context-engineering debt — schedule it for
  capture. Run this test on a cadence; it's the early-warning for the org silently de-nativizing.
- **Freshness, not just accumulation.** Stale context is worse than none (agents act on it
  confidently). The ritual prunes/flags what's outdated, re-runs evals when the model layer changes,
  and treats "switching models" as a regression test the eval suite must pass — not a rewrite, and
  not a silent quality cliff.

---

## Observability & the documented failure modes

Without observability you scale failure faster than humans can correct it. The observability layer
(logs / traces / evals / **review queue**) is the org's nervous system — and it is what makes the
human gates *genuine scrutiny* rather than rubber stamps. Watch the **foreseeable-therefore-
avoidable** traps (SHEET 11; depth + signals in
`references/observability-and-failure-modes.md`):

- **Over-automating judgment** — the queue gets auto-resolved; a human node becomes an agent
  classification. Signal: escalation rate trending to zero on a class that should escalate.
- **Context rot** — write-back lapses; agents run on stale/absent context. Signal: rising rework,
  the context-debt test lighting up, evals drifting un-noticed.
- **Observability-last** — the org scaled the fleet before instrumenting it. Signal: you can't
  answer "what did the agent do and why" from a trace. Fix this *first*; it is the precondition for
  every other control.
- **Pointless-graph / dashboard theater** — dashboards that no decision reads. Signal: a metric no
  routing rule consumes. Cut it.

---

## Self-check before delivering the runbook
- **Did I gate honestly?** If it's a graft, did I say so and redirect to the architect, not ship a
  runbook that pretends operating discipline fixes an un-redrawn graph?
- **Is the fleet the default worker?** Could I switch off the agents and have the same org? If yes,
  it's a graft — go back to Step 0.
- **Is judgment scarce?** Count the human touches in the cadence + queue. If a human is on every
  edge as a reviewer, you rebuilt the approval chain — concentrate them at the few real nodes.
- **Does every exception route to a *named* human with a wait-set and a full verdict set?** Does
  every non-approve verdict have a named home (no silent stall)? Is the gate genuine scrutiny the
  observability layer feeds — not a rubber stamp?
- **Does context compound, and is rot defended?** Is write-back part of "done"? Is the context-debt
  test on a cadence? Is freshness a ritual, not just accumulation?
- **Are all four substrate layers operated** — especially observability *first*? A fleet you can't
  trace is a fleet you can't safely run.
- **Did I hold the org stop-line?** No agent at the center of a trust/safety/relationship node;
  boundary flagged, not over-claimed.
- **Is it bespoke, not a template?** Would two different orgs' runbooks read as interchangeable? If
  so, the cadence/queue/fleet aren't grounded in *this* org's loop — push it.
- **Did I argue future-leading, not score it?** 2–3 lines of future-trajectory; no "X/5".

---

## References (read on demand)
- `references/orchestration-spec.md` — fleet roles, dispatch/reconverge, the orchestrator's loop.
- `references/review-queue-routing.md` — exception classes → named humans, wait-sets, verdict sets,
  anti-rubber-stamp design, the org stop-line in operation.
- `references/operating-cadence.md` — the VSM / S1–S5 rhythm, what runs continuously vs. on a loop,
  why real-time feedback density (not annual strategy) is the native cadence.
- `references/context-upkeep.md` — write-back-as-done, the context-debt test, freshness rituals,
  model-swap regression discipline.
- `references/observability-and-failure-modes.md` — the four-layer substrate operated, signals to
  watch, the documented failure modes and how to catch each early.
- `references/runbook-template.md` — the copyable Operating Runbook scaffold (the deliverable).
