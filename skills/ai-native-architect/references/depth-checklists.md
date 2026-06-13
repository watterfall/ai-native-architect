# Depth modules — apply the ones your case triggers

A blueprint that names a human behind a gate but never prices the decision, names the law, or designs
the failure path is *topology without depth*. These nine modules add the depth. **They are conditional
— apply only the ones your case triggers, and match weight to size** (a 2-person greenfield does not
need a make-vs-buy ledger or a regulatory-grounding table; forcing all nine onto a tiny org is the
over-engineering trap). Each module names its TRIGGER. When triggered, fold its output into the
relevant blueprint section.

## Quick trigger map
| Module | Trigger |
|---|---|
| 1. Economics that compute | **always** (it's the deciding artifact) |
| 2. Graph executability contract | whenever you draw a workflow graph |
| 3. Regulatory grounding | scope verdict flags regulated / litigation-exposed / safety-critical |
| 4. Residual-harm & adverse-event protocol | any node whose wrong call harms a third party |
| 5. Human transition & tacit-capture | an incumbent workforce, or a retiring/tacit-knowledge holder |
| 6. Moat stress-test | defensibility matters (most ventures with competitors) |
| 7. Beneficiary service contract | there is an end customer / caller / patient / beneficiary |
| 8. Incentive-compatibility & make-vs-buy pricing | non-trivial sign-off liability or a real Coase keep/buy call |
| 9. Canon completeness | **always** (light) |

---

## 1. Economics that compute (always)
A cost/ROI section shaped correctly but left as algebra is indistinguishable from hand-waving. So:
- **Size the opportunity from the brief's own numbers first.** Compute the bottleneck's annual dollar
  value before quoting any build cost (e.g. 6% loss × $34M = ~$2M/yr recoverable; 180k calls × loaded
  SPI-minutes saved; $15k × teardowns/yr). Show the one-line arithmetic.
- **No placeholder variables.** Never ship `$X/hour × M ≈ payback in N months`. If a number isn't in
  the brief, state the assumption explicitly and plug a defensible value.
- **One per-unit margin line**, not just a payback count: price − marginal cost per unit (per teardown /
  per linen-pound / per call), so a leverage claim is proven on margin, not only on volume.
- **On a fork (out-of-scope redirect or option menu), each option still carries** an order-of-magnitude
  cost band + the single ROI metric — so "which do you want?" is a decision the operator can price, not
  a blank check. Gating honestly ≠ shipping a thin memo.
- **Tie out the arithmetic.** Recompute every headline figure inline from its inputs (`22 × $16k =
  $352k`), and make component figures *sum to the stated range* — a number that contradicts its own
  inputs destroys the whole case's credibility. A flagged `[ASSUMP]` is not a closed number.
- **Anchor and bound the load-bearing inputs.** For each input the ROI rests on, give a one-line
  *external anchor or proxy* ("comparable decommissioning studies run $X–Y"; "ACCME module revenue
  benchmarks ~$Z") even if it's a stated range, not a citation. Show the headline ROI as a **low / base
  / high band** driven by the two most fragile inputs, and **name the one input whose error would flip
  the recommendation**, with a cheap Phase-1 test aimed at *that* input. Single-point ROIs on
  self-generated plugs are not decision-grade.

## 2. Graph executability contract (when a graph is drawn)
The runnability properties you are proudest of ("the gate can't fire on the first verdict in") must be
*encoded*, not narrated:
- **Joins are first-class nodes** carrying an explicit `join_inputs: [...]` wait-set; the design is wrong
  if a listed upstream edge is missing from that set.
- **Any node with >1 inbound edge into a gate declares a `join_policy`:** `all` / `quorum:n` /
  `mutually_exclusive_by:<guard>`. The bare two-parallel-edges-into-a-gate pattern is forbidden (it
  releases on whichever verdict arrives first — the exact failure you claim to prevent).
- **Every conditional / escalation / refusal / disagreement branch terminates in a named node.** No
  control-flow path may dead-end in prose ("else escalate" with no target).
- **Every human/community judgment node declares its full verdict set `{approve, decline, amend}`, and
  each non-approve verdict terminates in a named node** (renegotiate / abort / caveated-finding) or a
  named re-entry edge. A human or community "NO" wired with only a YES edge into an `all`-join does not
  fail loudly — it *silently deadlocks* the join, the worst failure for the one node the design exists
  to protect (a community withholding consent, an expert refusing to sign). State what the join does on
  a negative verdict (route-to-named-abort, never wait-forever).

## 3. Regulatory grounding (regulated / litigation-exposed / safety-critical)
Naming *who* is accountable is not naming *which law* they must satisfy. For each regulated/irreversible
node, add three fields beyond the accountable human:
- **Governing regime by name** — the specific evidentiary standard, statute, or accreditation the node
  must satisfy.
- **Instrument-of-record** — the actual *document a court / regulator / accreditor reads first* that
  effects the liability allocation: the engagement-letter scope-of-reliance + liability cap, the
  ITPGRFA **SMTA** / Nagoya **PIC-MAT**, the **ACCME Standards for Integrity** COI/commercial-firewall
  attestation, the MTA/BAA. Naming the regime is necessary but not sufficient — name the signed
  instrument, because that is what is subpoenaed. ("We named the law" → "we named the document.")
- **Record obligation** — retention period + immutability + litigation-hold / discovery posture.
- **Liability transfer** — what is insured (E&O / professional-liability / cyber) vs. structurally
  retained, plus the vendor BAA / indemnity chain.
- **Third-party-harm vectors** — enumerate the parties an output can harm *besides* your counterparty
  (a named contractor/OEM blamed in a forensic dossier → defamation / negligent misstatement; a
  patient treated per a wrongly-certified CME module → care harm; biopiracy / unauthorized ex-situ
  transfer of restricted material), and which instrument addresses each.

Domain→regime starter table (extend per case): forensic/expert → **Daubert / FRE 702, CPR Part 35,
spoliation, e-discovery retention; engagement-letter reliance cap**; clinical/health → **HIPAA (BAA,
breach-notification), EMTALA, standard-of-care, state licensure**; accredited CME → **ACCME/ANCC
accreditation + the 2020 Standards for Integrity and Independence (commercial-support firewall,
ineligible-company influence, faculty COI), credit reporting to boards/PARS**; genetic-resource /
Indigenous → **Nagoya ABS (PIC-MAT), ITPGRFA (SMTA), CARE/OCAP® data governance, ABS Clearing-House**;
healthcare-linen → **HLAC/AAMI hygienically-clean accreditation, OSHA bloodborne, SLA/indemnity**;
automated outreach → **TCPA consent**; financial → **SOX, SEC, lending/fair-use rules**.

## 4. Residual-harm & adverse-event protocol (adverse outcome harms a third party)
The gate is *prevention*; it assumes the gated human is the reliable last line. Design the path for when
that human is **also** wrong — that residual is what actually produces dead callers, denied legitimate
claims, infected patients. For each safety-critical / high-stakes-adverse node:
- **Trace harm to the *last human harmed*, not the institutional counterparty.** Name the flesh-and-blood
  victim if the output is wrong (the patient treated per a wrongly-certified module — not "the
  accreditor"; the vessel crew or the blamed contractor — not "the regulator"; the farming household —
  not "the funder"). Set the **error budget against that victim's worst case**, and give them a duty
  owed + a notify/appeal path that does **not** depend solely on the same accountable signer's goodwill.
  This is **full weight, never "light,"** wherever a patient / crew / community is reachable.
- A **named owner of the harm** — distinct from whoever *authorized* the act.
- A **detection → disclosure → remediation loop wired as a real edge** (generalize "worsening symptom
  re-opens the case": a wrong outcome must be detectable and route to remediation + the harmed party).
- A stated **error / false-negative budget** and the duty owed to the harmed third party (appeal,
  correction, mandatory reporting).
- An honest **liability / insurance** line.

## 5. Human transition & tacit-capture (incumbent workforce or retiring knowledge-holder)
You can design the target-state system perfectly and still have the org reject it. The people whose heads
hold the moat (B.07) are exactly the people whose leverage the design dissolves — so "why would they
cooperate?" is load-bearing. Add:
- The **tacit-capture workflow** — *how* the knowledge is elicited, not just where it's stored: shadow
  the expert, structured failure-mode interviews, capture-at-point-of-override as a required rationale
  field. An asserted write-back edge is not a capture plan.
- The **incentive / political design** — status, comp, role-after, who loses leverage, and what makes
  externalizing their knowledge worth their while.
- The **trust-building rollout** — shadow → assist → gate, with who pilots it and why they'll champion it
  (often: ship the work they *hate* first, at zero risk, to earn trust).
- The explicit **"design is correct but the org rejects it" failure mode** and its mitigation.
- **Cooperation telemetry + recovery (not just a static failure-mode line).** Disengagement detected
  *after* knowledge has walked is too late — especially on a retirement clock. Name **2–3 leading
  indicators** that fire *before* the loss (capture-entries-per-person trending down; override-rationale
  decaying toward rubber-stamp; shadow-session no-shows; attrition spikes in the threatened cohort), a
  **named owner** who watches them, and a **defined recovery move per signal** (re-open the comp/status
  conversation, slow the rollout, escalate to the community council). This makes adoption a steered
  feedback loop — consistent with M.06 organization-as-a-living-system — not a one-time assertion.
  Note: capture-rate ≠ cooperation. An agent can keep improving on a stale corpus while every human has
  quietly stopped contributing; watch the *people* signal, not only the *context* signal.

## 6. Moat stress-test (defensibility / survival matters)
A compounding internal asset is only a moat if a competitor's fastest copy-path is slower than your
compounding rate. Test it from the outside — and run the clock from *both* sides, don't just declare
victory:
- **Name the most likely attacker and their cheapest copy-path** (incumbent with deeper archives; a
  vendor selling the same off-the-shelf stack; a PE roll-up that *acquires the accounts* rather than
  copies the tech; a vendor lobbying your funder).
- **Run the two-sided race in measurable units.** State *their* realistic **time-to-adoption with the
  customer** (not just time-to-build the tooling), and *your* compounding rate in a real unit
  (override-rate decline, dossiers-to-trust, audit-acceptances accumulated). Show whether your
  accumulated lead exceeds their adoption time *at the moment they commit* — don't assert "you win."
- **The adversary-wins counterfactual.** Name the single exogenous event that collapses the moat (the
  accreditor blesses AI-CME; the incumbent acquires you for the dataset; the anchor donor exits) and
  the hedge. A moat with no named failure condition hasn't been stress-tested.
- **The switching cost / data network effect** that makes a customer who used you once unwilling to leave.
- **For nonprofits / regulated / public-interest orgs, this module is not N-A — it is reframed as
  capture- and survival-resistance.** The defensibility question becomes: who could absorb the mission
  or defund it (a CGIAR/Svalbard-class institution; a withdrawing anchor donor; a board that mandates
  the wrong thing), and does the compounding asset (community trust, accreditor trust, evidence base)
  buy survival faster than the threat arrives? Same race, different prize.

## 7. Beneficiary service contract (there is an end beneficiary)
Protecting the end party at the decision boundary is the *defensive* half; prove the redesign makes their
experience *better*, not just the operator more efficient:
- **1–2 end-party-facing metrics** with a target and an accountable owner (caller answer-time /
  abandonment; OR-window on-time %; insurer turnaround-with-defensibility).
- **An end-party-*voiced* outcome signal** the beneficiary themselves produces — distinct from any
  operator-controlled throughput proxy the operator can quietly tune (a community satisfaction /
  knowledge-return measure on *their* terms; a clinician usefulness signal; a regulator's own published
  verdict). "We will serve you well" is not verifiable; "you tell us whether we did" is.
- **A beneficiary exit / portability right** with a named owner (data portability, relationship
  hand-back, a community veto or repatriation path) — so trust is *structurally enforceable*, not just
  promised. Watch the case where you sell the end party's lock-in *to the operator* as a moat: a
  data-network-effect that captures the beneficiary cuts against them. Let them verify and walk away.
- The **degraded-mode / human-touch fallback** the beneficiary experiences when the AI path fails or
  saturates.
- Any **equity-of-access gap** (language, after-hours, the caller still on hold).

## 8. Incentive-compatibility & make-vs-buy pricing (real sign-off liability or Coase call)
Two economics gaps the topology hides:
- **Incentive-compatibility at every policy gate:** name the **residual claimant** on the decision and
  the liability/comp consequence of a wrong sign-off. Making judgment *visible* (dashboards) is not
  making it *costly to fake*. Align the signer's payoff with downstream accuracy (E&O allocation, blind
  re-audits scored against the signer, liability that can't be delegated to the model/vendor).
- **Price the Coase keep/buy call as a number, not a direction.** For every node on the boundary,
  carry three figures and let the call *fall out of them*, not out of the moat label: (1) rent/buy
  annual cost; (2) build/keep cost (or the asset-specific premium of keeping); (3) a **hold-up discount
  = P(hold-up) × switching-cost-if-locked**. Renting an asset-specific input can create ongoing
  bilateral hold-up that justifies owning even at higher headline cost — that only shows up once it's
  priced. For a brownfield carve-out, make a **transfer price the default device**: the unit charges
  the legacy org a per-unit internal fee against a stated legacy marginal cost (this is what makes
  "independent P&L" real and the competitive contrast measurable in dollars the board already trusts);
  name who arbitrates it. When there's genuinely no live keep/buy auction (e.g. a sovereignty-bound or
  grant-constrained node), state the exemption *with the numbers that would have been compared*, not as
  an assertion — the priced ledger is the floor even when the conclusion is "keep by mandate."

## 9. Canon completeness (always, light)
Faithful vocabulary, fully deployed — not bare tags:
- **Name each code alongside its code:** `M.03 Context-as-the-core-asset`, not bare `M.03`; `B.07
  Tacit-knowledge lock-in`, not bare `B.07`. (The canon says "use the names in deliverables.")
- **Run the full checklists and mark each item** `applied` / `N-A because…` / `deliberately-violated
  because…` — so an omission is a visible decision, never a silent drop. This applies to the **seven
  pillars** (don't quietly skip pillar 7 "Life before business" for a solo founder) and the **four
  forces** (Coase is force 1; agency, cybernetics, and **judgment-scarcity economics** are 2–4 and are
  usually dropped — judgment-scarcity is the philosophical core of "where the bottleneck moves to").
- When you cite **M.06 (organization-as-a-living-system)** or the judgment-scarcity force, give one
  sentence of its actual content doing work in *this* design, not just the label.
- Don't invent pillar numbering; preserve the canon's references.
