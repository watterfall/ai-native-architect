# AI-Native Architecture Blueprint — <ORG / VENTURE NAME>

> Fill every section. Keep claims and evidence unmixed; label inferences as falsifiable. If the
> Scope Verdict is out-of-scope, stop after § 1 with the honest redirect — do not fabricate § 2–9.
> Grounded in "AI Native 组织方法论" (T1: organization = distribution of judgment × flow of context).

## 1. Scope verdict
- **Track:** A (greenfield) · B (brownfield carve-out) · OUT-OF-SCOPE (AI-enablement) · BOUNDARY
  (emotional-labor-led).
- **Rationale:** <why this classification — 2–4 sentences>
- *(If OUT-OF-SCOPE: deliver the honest AI-enablement-≠-AI-Native verdict and the two real options
  from fit-and-scope.md, then stop. If BOUNDARY: state what AI assists vs. where the human must
  lead, then continue with that constraint.)*

## 2. Venture frame
- **Value & customer:** <what value, for whom>
- **Core loop:** <intake → … → delivered value, one line>
- **Unit of coherence:** <what holds it together; per T1, coherence is the purpose, scale a choice>
- **(Brownfield) the carve-out:** <the independent ground; how it runs alongside legacy; the
  contrast strategy>

## 3. T1 for this org (one line)
> **Judgment distribution:** <the few human judgment nodes> · **Context flow:** <the compounding
> context system>.

## 4. Bottleneck diagnostic
- **Brownfield:** hit table of the 16 (hit / partial / clear + one line of evidence each), **hit
  count = N/16**, and the one-sentence conclusion (why this is a carve-out, not a graft).
- **Greenfield:** design-rule table — for each of the 16, the rule that keeps you from importing it
  (you may compress to the ones that bite this domain, but show you considered all 16).

## 5. Workflow graph(s)
For the core loop (and 2–3 loops if the org is larger), per `templates/workflow-graph.md`:
- **YAML** (nodes typed agent/human/policy; edges with trigger+feeds; judgment_anchors;
  policy_gates).
- **Mermaid** diagram.
- **Brownfield:** show **before (serial relay) → after (parallel fan-out)** and name the serial
  edges you deleted.
- **Runnable, not decorative (depth module 2):** parallel branches *and judgment fan-outs* reconverge
  at a **join node with an explicit wait-set** before any delivery/irreversible node; any gate with >1
  inbound edge declares a `join_policy` (`all` / `quorum:n` / `mutually_exclusive_by:<guard>`); every
  "writes back / learns" claim is an actual `feeds:` edge; every branch (incl. escalation/refusal/
  disagreement) ends in a named node; each `feeds:` store says what's written and what reads it.
- One line: where did the bottleneck move *to* (it should land on a human judgment, not a hand-off).

## 6. Four-layer substrate
| Layer | Concrete choice for this org | Why it's load-bearing here |
|---|---|---|
| **Model** | <≥1 frontier + open-weight, behind a swap abstraction> | not single-vendor (would be API-dependent) |
| **Agent** | <orchestration + runtime + integrations> | where execution lives |
| **Context** | <vector / KG / decision logs + freshness practice> | what makes the agents *yours* |
| **Observability** | <logs/traces/evals/alerts + human review queue> | or you scale failure |

Match weight to size — name what you deliberately defer for a tiny org, and when you'd add it.

## 7. Org form, roles & the Coase boundary
- **Human roles (few):** <role → the judgment it anchors>. Operator stance: orchestrator. Guard the
  sign-off nodes against rubber-stamping (what makes the human actually scrutinize?).
- **Coase boundary:** <which activities stay in-house / agent-run vs. bought from the market, given
  collapsed search/negotiation/monitoring costs — but keep thin-market / relationship-specific /
  high-trust nodes in-house (asset-specificity & hold-up risk)>.
- **Regulated & physically-irreversible actions:** <legal/licensure/compliance steps and any
  physical/identity/safety irreversibilities, each with a named accountable human; boundary caveat
  on any agent-initiated outreach to vulnerable people>.
- **Worldview / pillar check:** <which of the six worldviews and (if N=1/tiny) seven pillars hold;
  any deliberately violated, and why>.

## 8. Construction plan, economics & exit criteria
- **Phased ≈6-month plan:** Phase 1 (usually: instrument *one* core loop end-to-end with
  observability) → … with an **exit criterion per phase** (what proves it before you scale).
- **Economics & capability (compute and tie out — depth module 1):**
  - **Opportunity sized from the brief's own numbers**, each headline **recomputed inline** (e.g.
    `6% × $34M = ~$2M/yr`; `22 × $16k = $352k`) and components summing to the stated range. No
    placeholder variables (`$X/M/N`).
  - **One external anchor/proxy per load-bearing input**, a **low/base/high band** on the two most
    fragile inputs, and **the one input whose error flips the recommendation** + a Phase-1 test of it.
  - **Build cost + monthly run cost**; a **per-unit margin line net of run cost** (price − marginal cost).
  - **Who builds & maintains it** (off-the-shelf path for a non-technical team, or the one role to
    hire/contract — don't assume engineers that aren't there).
  - **A single closed ROI / payback figure** tied to the bottleneck. On a fork, numbers on *each* option.
- **Traps to avoid:** <over-automating judgment · context rot · observability-last · graph-drawing
  for its own sake · others specific to this org>.
- **Falsifiable risks:** <the conditions under which this design would be wrong>.

> **§9 is an internal trigger list — do NOT reproduce it as a box-list in the deliverable.** Weave the
> fired modules into §2–8 where they are load-bearing; the reader should meet the regulatory instrument
> inside the gate that needs it, the moat race inside the strategy, the transfer price inside the
> carve-out. Surface only what *this* domain summons.

## (internal) Depth triggers — integrate into §2–8, don't print as boxes
`references/depth-checklists.md`: **1** economics-that-compute (always) · **2** graph executability +
human-NO terminals · **3** regulatory grounding *incl. instrument-of-record + third-party-harm vectors*
· **4** residual-harm traced to the *last human harmed* · **5** transition + *cooperation telemetry* ·
**6** *two-sided* moat race + adversary-wins counterfactual (nonprofits → capture/survival-resistance) ·
**7** beneficiary *voiced* outcome + exit right · **8** *priced* keep/buy ledger + transfer price.

## 9. Why this is AI-Native and future-leading
A tight **prose** argument (no scorecard, no "X/5"): the scarcity inversion realized *here* — what
judgment is genuinely scarce and concentrated, what context compounds into the core asset, how capability
scales without headcount, the live learning loop, and why the whole thing would be *incoherent without
AI*. Name where you deliberately protect the scarce-and-sacred human/trust/mission core rather than
automate into it (that restraint is correct, not a gap).

**Future-trajectory (2–3 lines):** how this architecture *compounds as the curves advance* — what gets
stronger automatically (context moat deepens; cheaper models widen the agent layer; A2A dissolves more of
the Coase boundary) and what must stay un-frozen (swappable models, a live learning loop).

## 10. Redraw-vs-graft — one honest line
> Delete the AI: does this collapse back into a normal org chart with the same roles and hand-offs?
> **<No + why>** (must be No — agents the default worker, humans the justified exception).

*(Internal pre-delivery check, not printed: verify the 5 essence properties hold; verify canon codes are
named where load-bearing and the pillars/forces were considered. If the design embodies only 2–3 essence
properties, push it before delivering. Do not print the score or a pillar roll-call.)*
