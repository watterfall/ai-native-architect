# Methodology canon — the shared, exact vocabulary

Distilled from the canonical drawing set **"AI Native 组织方法论"** (SPEC.V, SHEET 00–18). These terms
are load-bearing, not decoration — use them exactly; don't paraphrase the canon into mush. This file is
the shared vocabulary both tiers reference; the architect skill carries deeper architecture-specific
references alongside it.

## T1 — the theorem (the org surface's compression of the kernel)
> **组织 = 判断的分布 × 上下文的流动**
> **organization = distribution of judgment × flow of context.** Scale is a free variable.

Two corollaries used constantly on every surface:
- **Throughput is a property of the graph, not of a node.** Speed up every node and end-to-end
  throughput barely moves; bottlenecks live in the *shape* of the work, not node speed. (Why "add AI"
  fails and "redraw" works.)
- **Coherence is the purpose; scale is a choice.** The N=1 limit proves it.

## The 16 structural bottlenecks (SHEET 04 · B.01–B.16)
Each is a proof-by-negation of T1 — a defect tools can't reach and "transformation" can't route around.
Brownfield: score the hit count. Greenfield: invert each into a design rule (don't build it in).
B.01 serial dependency chain · B.02 information siloing · B.03 approval-chain latency · B.04 context loss
at hand-offs · B.05 coordination overhead (∝ headcount²) · B.06 single-threaded decision-makers · B.07
tacit-knowledge lock-in · B.08 onboarding lag · B.09 headcount-as-capacity · B.10 meeting/sync tax · B.11
rework from late feedback · B.12 priority thrash · B.13 institutional memory decay · B.14 handoff
queueing · B.15 specialist bottlenecking · B.16 niche/skill lock-in.
*(Names are the canonical set; B.01 = serial dependency chain is canonical. Use names, not just codes.)*

## The four-layer substrate (specify all four, or it isn't native)
1. **Model layer** — multiple foundation models (≥1 frontier API + open-weight for sovereign workflows)
   behind a swap abstraction. *Single-vendor = API-dependent, not native.*
2. **Agent layer** — orchestration + runtimes + tool/data integrations.
3. **Context layer** — vector store / knowledge graph / decision logs + the practice that keeps them
   fresh. *This is what makes the agents yours.*
4. **Observability layer** — logs, traces, evals, alerts, a review queue routing issues back to humans.
   *Without it you scale failure faster than humans can correct it.*

## The six foundational worldviews (M.01–M.06)
- **M.01 Organization-as-workflow-graph** — the graph is the truth.
- **M.02 Agent-as-the-default-role** — the default worker is an agent; humans are the justified exception.
- **M.03 Context-as-the-core-asset** — the durable asset is the context system.
- **M.04 Continuous-learning-as-the-operating-system** — the work learns as its OS (decision logs, evals,
  feedback), not as an occasional retro.
- **M.05 Humans-as-judgment-anchors** — humans decide what's worth doing and own consequences.
- **M.06 Organization-as-a-living-system** — emergence, fitness landscapes, an immune system, a
  self-improving loop (Kauffman NK; Argyris–Schön / OODA).

## The seven sovereign-operator pillars (N=1 / tiny — a litmus, not a mandate)
1 sovereign operator · 2 un-scaling as design · 3 compounding leverage (agents + context + audience) ·
4 build in public · 5 niche focus · 6 strategic refusal · 7 life before business (profit as oxygen, not
the goal).

## The three (four) forces — why this is possible *now*
1. **Coase boundary redrawn** — AI collapses search / negotiation / monitoring costs, pushing make-vs-buy
   toward the market. *Williamson caveat:* holds for **deep, competitive** markets; asset-specific,
   thin-market, relationship-specific nodes keep hold-up risk — keep or hedge them.
2. **Agency theory extended** — agents change who can be delegated to, and how cheaply.
3. **Cybernetics returning** (Beer's "Brain of the Firm") — the work as a steered, feedback-driven system.
4. **Economics of judgment scarcity** — when generation approaches zero marginal cost, judgment is the
   scarce, valuable input. Design around the scarcity, not the abundance.

## Evidence discipline (keep claims and evidence unmixed)
Every claim is one of: definition / mechanism / proposition / framework / **evidence** (with measurement
basis) / **inference** (falsifiable) / action. Label inferences as falsifiable. When citing an empirical
marker (e.g. Anysphere ~$2B ARR at ~300 people; Cognition's valuation on low net burn), note it is
self-reported / directional, not a law. Grade load-bearing citations (the canon uses a five-tier register
R1–R47).

## The six surfaces (no pipeline, no means/ends)
组织 / engineering / design / research / learning / innovation — **six faces of one kernel, mutually
coupling, no first and no last; enter from any face.** Never frame them as a sequence or as
means→ends ("efficiency is the means, people are the end"); that framing is banned house-style.
