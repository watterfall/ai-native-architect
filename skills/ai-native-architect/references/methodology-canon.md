# Methodology Canon — the faithful vocabulary

Distilled from the canonical drawing set **"AI Native 组织方法论"** (SPEC.V, SHEET 00–18, five
acts, five instruments). Use these exact terms when you design — they are load-bearing, not
decoration. Source of truth: the full single-file canon. This file is the part an architect needs
in working memory.

## Table of contents
- T1 — the theorem
- The five acts / SHEET map
- The three (four) forces that make this possible now
- The six foundational worldviews (M.01–M.06)
- Operator as orchestrator
- The seven-principle skeleton
- The four-layer substrate (with tools)
- The seven sovereign-operator pillars (one-person / tiny org)
- Instrument & citation codes

---

## T1 — the theorem
> **组织 = 判断的分布 × 上下文的流动**
> **organization = distribution of judgment × flow of context.**
> *Scale is a free variable; management is the engineering of these two structures.*

Two corollaries you will use constantly:
- **Throughput is a property of the graph, not of a node.** Equip every employee with AI and
  end-to-end throughput barely moves, because bottlenecks live in the *shape of the graph*, not in
  node speed. (This is why "add AI" fails and "redraw" works.)
- **Coherence is the purpose; scale is a choice.** An org can be N=1. "An organization must be
  many people" is a hidden assumption to be *proven*, not assumed.

## The five acts / SHEET map
- **ACT I · Symptom (SHEET 00–02)** — three base assumptions fail at once. SHEET 00 defines terms
  ("what AI Native is NOT"); the symptom is "buy AI at scale, end-to-end barely speeds up."
- **ACT II · The Core (SHEET 03–04)** — one thesis (T1, SHEET 03) and its sixteen proofs-by-negation
  (the 16 bottlenecks, SHEET 04).
- **ACT III · Construction (SHEET 05–08)** — worldviews · pillars · the four-layer substrate.
- **ACT IV · Testing (SHEET 09–14)** — verified samples, four cross-sections, documented traps,
  boundaries, and the N=1 limiting solution (one-person company).
- **ACT V · Action (SHEET 15–17)** — idea → moat, the four startup stages, the six-month
  construction plan, the construction toolkit (workflow-graph modeling). SHEET 18 = the closing
  architectural commitment.

Canonical usage flow: **① Diagnose first (SHEET 04) → ② Judge fit (SHEET 13 Fit/Unfit) →
③ Build to the drawings (SHEET 15–16, six-month plan).** This skill's Steps 0–8 implement it.

## The three (four) forces — why this is possible *now*
The convergence that makes AI-Native more than a slogan (ACT I):
1. **Coase boundary, redrawn.** A firm exists because internal coordination was cheaper than the
   market (Coase 1937; Williamson, Jensen–Meckling on agency cost). AI agents collapse the three
   costs that set that boundary — **search** (RAG / vector stores make org memory instant),
   **negotiation** (agent-to-agent protocols: MCP, A2A), and **monitoring** (real-time
   observability makes remote async supervision beat on-site). So the make-vs-buy boundary gets
   redrawn toward the market: native orgs are smaller and outsource more. *Williamson caveat:* this
   holds for activities in **deep, competitive** markets; **asset-specific, thin-market,
   relationship-specific** nodes still carry hold-up risk — keep or hedge them in-house rather than
   assuming AI-lowered search cost makes every supplier substitutable.
2. **Agency theory, extended** — agents change who can be delegated to and how cheaply.
3. **Cybernetics, returning** (Beer's "Brain of the Firm") — the org as a steered, feedback-driven
   system rather than a hierarchy of approvals.
4. **The economics of judgment scarcity** — when generation/execution approach zero marginal cost,
   *judgment* becomes the scarce, valuable input. Design around the scarcity, not the abundance.

Early empirical markers (self-reported): Anysphere ~$2B ARR at ~300 people (~$6M/head, ~10× a SaaS
giant); Cognition to a ~$26B post-money on <$20M cumulative net burn pre-acquisition. Treat as
directional evidence of the Coase boundary compressing toward the market, not as laws.

## The six foundational worldviews (M.01–M.06)
The lenses every native design must satisfy:
- **M.01 Organization-as-workflow-graph** — the workflow graph is the truth; the org *is* its graph.
- **M.02 Agent-as-the-default-role** — the default worker is an agent, not a person. Humans are the
  exception you justify.
- **M.03 Context-as-the-core-asset** — the durable asset is the context system, not headcount.
- **M.04 Continuous-learning-as-the-operating-system** — the org learns as its OS (decision logs,
  evals, feedback loops), not as an occasional retro.
- **M.05 Humans-as-judgment-anchors** — humans decide what's worth doing and own consequences.
- **M.06 Organization-as-a-living-system** — emergence, fitness landscapes, an immune system,
  mycelial resource reallocation, a self-improving loop (Kauffman NK; Argyris–Schön / OODA).

> Codes M.01–M.06 index the six worldviews in canon order; M.03/M.04 are the context/learning pair
> the template references for `feeds:` (compounding context). Use the *names* in deliverables.

## Operator as orchestrator
The human operator's stance is **orchestrator** — composing and steering a network of agents and
context — not a manager supervising people. In the limit (N=1) the operator is the sole judgment
node and the entire "headcount" is leverage.

## The seven-principle skeleton (the "骨架")
The methodology's operating principles (ACT III). A native design should be able to point to each:
1. **AI-first as default** — AI is the default way work gets done, not an add-on.
2. **Workflow as code** — workflows are explicit, versioned artifacts, not tribal habit.
3. **Context engineering as systematic practice** — context is built and maintained deliberately.
4. **Multi-model architecture** — many models behind an abstraction, swappable.
5. **Observability before scale** — you instrument before you grow, or you scale failure.
6. **Humans as judgment & responsibility anchors** — the human role is judgment and accountability.
7. **Continuous evolution** — the org is expected to keep changing shape.

## The four-layer substrate (ACT III; bottom → top)
A native org runs on four infrastructure layers. Specify all four, or it isn't native.
1. **Model layer** — the foundation: multiple foundation models, typically ≥1 frontier API
   provider *plus* open-weight models for sovereign workflows, behind an abstraction so models are
   swappable. *Without it you are not AI-Native, you are API-dependent.* (Tools: frontier APIs +
   open-weight; a routing/abstraction layer.)
2. **Agent layer** — where workflow execution happens: orchestration frameworks (LangGraph,
   CrewAI, AutoGen, or custom), agent runtimes, and the integration layer to tools, databases, and
   external systems. (Tools: LangGraph · CrewAI · AutoGen · Letta · Pydantic AI · Inngest.)
3. **Context layer** — what makes agents organization-specific: vector databases, knowledge graphs,
   decision logs, and the engineering practice that keeps them fresh. *Without it your agents are
   generic; with it they become uniquely yours.* (Tools: Pinecone · Weaviate · Chroma · Qdrant ·
   Glean · Sana · Notion AI.)
4. **Observability layer** — what keeps the system continuously learnable: logs, traces,
   evaluations, alerts, and a review queue that routes issues back to humans. *Without it you are
   scaling failure faster than humans can correct it.* (Tools: LangSmith · Helicone · Arize ·
   W&B Weave · Galileo · Braintrust.)

Tool names are illustrative of each layer's *function*; choose by fit, but never drop a layer.

## The seven sovereign-operator pillars (N=1 / tiny org — SHEET 14)
For one-person and very small orgs, the limiting-solution pillars. "The limiting solution is not a
universal prescription" — use as a litmus, not a mandate:
1. **The sovereign operator** — one accountable judgment node.
2. **Un-scaling as design** — deliberately refuse headcount growth as the default lever.
3. **Compounding leverage** — agents + context + audience compound instead of staff.
4. **Build in public** — distribution and trust as a compounding asset.
5. **Niche focus** — win a defensible niche rather than a broad market.
6. **Strategic refusal** — saying no is a design tool (to scope, customers, features).
7. **Life before business** — the org serves the operator's life; resilience over growth, profit
   as oxygen (a means of staying alive), not the goal.

## Instrument & citation codes
- **M.01–M.06** — the six worldviews (above). **B.01–B.16** — the sixteen bottlenecks
  (see `bottleneck-diagnostic.md`); B.01 = serial dependency chain is canonical.
- **Pillars** — the seven sovereign-operator pillars above; the canon also references operating
  pillars by number (e.g., the *policy-gate / irreversible-action* pillar) — preserve such
  references rather than inventing new numbering.
- **R1–R47** — the canon's five-tier-graded citation register (the appendix). When you cite an
  empirical marker, note it is self-reported / directional unless graded otherwise.
- **Drawing types** — every canonical sheet is one of: definition / mechanism / proposition /
  framework / evidence (with measurement basis) / inference (falsifiable) / action. Keep your
  *claims* and your *evidence* unmixed the same way — label inferences as falsifiable.
