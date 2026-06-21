---
name: ai-native-research
description: >-
  Use when someone wants to answer a research question, run a literature review or evidence
  synthesis, vet AI-generated claims or hypotheses, decide which finding to trust, integrate
  scattered results, build a knowledge graph, or judge whether a result replicates — "is this
  claim credible", "what does the evidence say", "synthesize these papers", "帮我做个文献综述",
  "这个结论可信吗", "这些 AI 生成的发现哪个值得信", "这个研究方向值得做吗". Trigger even on "research this for me".
---

# AI-Native Research

You **do research** the AI-native way: traverse, generate, and synthesize at scale, then **vouch for
what is credible and decide what is worth knowing.** You are not making the old research pipeline
faster, and you are not designing a research organization (that is `ai-native-architect`). You are
producing a **research finding plus the evidence artifacts that make it trustworthy.**

This skill is the **research surface** of one shared kernel. Read the kernel as the spine of the work:
`../../references/_core/kernel.md` (the scarcity inversion, the four-step loop, the five-property
essence test) and `../../references/_core/judgment-execution.md` (how the execution tier runs the loop
and where its stop-lines are). Use the exact shared vocabulary from
`../../references/_core/canon-vocab.md` — don't paraphrase it into mush.

## The one move this surface makes — read this first

For decades the scarce resource in science was **人时** (person-hours: who can read, compute, run
experiments, write up). When retrieval, experiment execution, analysis, and even batch hypothesis
generation become near-free and massively parallel, **producing a result stops being the bottleneck**
— but the bottleneck doesn't vanish, it **moves**. It lands first on **提对问题 (asking the right
question)** and then retreats further, to **deciding which answer is worth believing and which truth
is worth knowing.**

So the first cut this skill makes is to redefine "research" away from *"produce something
publishable"* toward *"land a truth that is worth believing and worth knowing into a traceable
structure."* The first kind's scarcity is work-hours; the second kind's scarcity is **judgment.**

**The research stop-line (止步线) — generalize the shared rule (`judgment-execution.md` §止步线) to
this surface):**
> Traversal, synthesis, and drafting are abundant — hand them to agents fully. **Never offload *what
> is worth knowing* and the *final credibility verdict.*** A claim's grade can be drafted by a tool;
> the verdict that "this is what I, in this value frame, am willing to vouch for" must be signed by a
> human. Cross that line and you have a high-speed generator, not research.

## The kernel on this surface — why the bottleneck moves *and forks*

Engineering judges code: its scarce judgment is **"对不对" (right/wrong)** — epistemic, machine-checkable,
so it will be largely automated. Research judges truth, and its scarce judgment slides further: first
"what question," then "which answer to believe," and finally **"which truth is worth knowing"** — which
**falls out of epistemology into axiology** (value). That last step is what makes research the *deepest*
surface, and it forks the kernel's step ② (judgment retreats) into two branches with **opposite fates**:

- **Machine-checkable judgment → folds back into ① abundance.** In-paradigm question-asking, retrieval,
  standard experiment design: finding the nearest-neighbour checkable gap in a data-rich region. AI is
  good at this and it parallelizes. It does *not* stay "reserved for humans" — it becomes one more
  automated execution. Its scarcity is a temporary capability threshold.
- **Constitutive judgment → sinks to ④ the value bedrock.** Paradigm-level re-framing and "which truth
  is worth knowing": in sparse, value-laden territory there is no prior frame to borrow and no
  machine-checkable proxy for right/wrong. This is the human's last un-outsourceable scarce contribution.

Conflate the two and you err in both directions at once: you either guard the checkable branch as
"the last bastion of human dignity" (and stay trapped in work-hours) or surrender the constitutive
branch as "automatable anyway" (and hand value judgment to the generation layer's default bias). The
**verifiability gradient** is continuous — the abundance frontier keeps moving right (today's in-paradigm
question-asking is next year's solved task) — but its **rightmost segment does not move left**, because
its scarcity is structural ("no machine-checkable right/wrong"), not a capability gap. The depth lives in
`references/the-fork-and-the-gradient.md`.

## The redraw-vs-graft gate — open here, before any work

Apply `../../references/_core/redraw-vs-graft.md` to this request. The research-surface tell:

From AI-assisted work to AI-Native work, the question changes from "which tool helps this
step?" to "how should execution, judgment, and context be redistributed?" The gate below is
how you keep that distinction honest.

> If you deleted the AI from this workflow, would it collapse back into "a researcher reading faster
> with an assistant"? **If yes, you are doing AI-enablement** — a six-month review compressed to six
> days, same pipeline, bottleneck still stuck at "who decides which of these to trust and where to
> push." Native research **redraws** the loop around abundant generation gated by a load-bearing
> verifier (replication + credibility), with a traceable evidence base as the spec.

Three misreadings that disguise grafting as native (refuse them by name): **"faster = native"** (only
the execution half sped up); **"more = better"** (output is never the metric — per the 41.3M-paper
bibliometric, individual output rose while topic coverage *contracted*); **"automatic = autonomous"**
(an end-to-end autonomous scientist scores its own ideas by "distance from the existing paradigm," so
the more autonomous it is, the harder it pushes science into the safe in-paradigm zone). Science is a
**resource-allocation problem, not an intelligence problem** — more compute exposes the allocation
bottleneck, it doesn't solve it.

**Boundary (`redraw-vs-graft.md` §boundary):** where a finding feeds a high-stakes irreversible human
decision (clinical, legal, safety) the credibility verdict is *more* reserved for a named human, not
less. Flag it; never let a grade stand in for a sign-off.

## The procedure — the research loop (run in order)

This is the four-step kernel loop (`judgment-execution.md` §the loop) specialized to research. The
**named work product** is a **Research Finding Dossier** (one file) containing: the finding/answer, a
**credibility ledger**, a **knowledge-graph contribution**, and a **blind-spot register**. Write it with
`references/finding-dossier-template.md`.

### Step 1 — Frame: stand up the evidence base *before* generating (③ context as infrastructure, first)
The most common way to misuse a knowledge graph is as a **warehouse** — generate first, file later. That
reverses the load-bearing order. In AI-native research the **traceable evidence base is the spec** (M.03): it
must exist *before* generation and *constrain* it. Write down, up front, **what counts as credible
evidence, what counts as a conflict, and what must trace to raw data.** Then generation has a target to
align to, and the base becomes a live guardrail — unsourced claims get blocked at the door, conflicts get
flagged on arrival, untraceable claims never enter. See `references/knowledge-graph-as-spec.md` for the
four load-bearing properties (agent-readable · traceable · **falsifiable** · integrable) and why
"falsifiable" (conflict surfaces as a real edge, not silence) is the one most often skimped.

### Step 2 — Triage the question into two layers (the worth-knowing call starts here)
Before generating, split the research question: **is this a nearest-neighbour gap inside the existing
paradigm, or does it require changing the variable / the level / the framing?** The in-paradigm half you
hand to agents for batch execution. The paradigm-level half **the human writes first** — the direction
and the falsification conditions. Don't let the system pre-decide this; it defaults to the data-rich,
in-paradigm answer. (This is the kernel ② fork applied at the question level; details in
`references/the-fork-and-the-gradient.md`.)

### Step 3 — Generate abundantly (① abundance: hand the bulk to agents)
Retrieve, traverse the literature/graph, generate candidate hypotheses, run/parallelize standard analyses,
draft synthesis candidates — at scale. This is where AI's leverage is; use it fully. Every generated
claim must enter the base **carrying its evidence edge** (source, measurement basis, traceability link),
or it doesn't enter. Cheap, parallel, many candidates — but candidates, not verdicts.

### Step 4 — Verify: replication + the credibility ledger (the load-bearing gate)
Replication is the **verifier that keeps the loop from being a generator.** Grade every load-bearing
claim on the **two-axis credibility balance** — *evidence strength* (Ⅰ–Ⅴ) **kept separate from**
*distance-from-paradigm*. Do **not** collapse them into one "credibility score": far-from-paradigm is not
the same as wrong (it may be a re-framing), and a single score lets the AI proxy "novelty" by "distance
from the existing distribution," which silently kills the genuinely new. Run the four-quadrant
disposition (not four grades): the **weak-evidence × far-from-paradigm** cell is *suspend + targeted
evidence-seeking*, never *delete* — that cell is where most paradigm shifts are born. When a claim fails
to replicate, **route it, don't delete it**: wrong → refutation base; reveals a blind spot → spawn a new
eval. Errors flow back as guardrails. The disposition matrix, the Ⅰ–Ⅴ register, and the replication
routing live in `references/credibility-ledger.md`.

### Step 5 — Integrate, not retrieve (④ the scarce human act, plus the human verdict)
Retrieval ("find the existing one") is abundified. **Integration** ("stitch claims never before placed
together into a new understanding") is the scarce act — it is a bandwidth problem, not a stock problem,
so producing more summaries makes it *worse*, not better. The human does the cross-frame stitching; the
agent feeds candidate material to hand. Then the human renders the two reserved verdicts:
- **The final credibility verdict** — "this is what I am willing to vouch for, at this grade, in this
  frame." A grade is *drafted*; the verdict is *signed*.
- **The worth-knowing call** — which finding is worth knowing/pursuing, and for whom under which value
  frame. This is constitutive, not a capability ("worth" has no frame-independent right answer; AI learns
  the *community mean* of taste, never the off-mean frontier value). See `references/worth-knowing.md`.
  This is the *worth-knowing* direction call (is this question/finding worth pursuing as research); the
  *worth-betting* direction call (which direction to back as an affordable-loss bet) belongs to
  `ai-native-innovation`.

Both are real gates with teeth: each carries a full disposition set — **{vouch / vouch-with-caveats /
withhold}** — and a non-vouch verdict terminates in a *named* place (a caveated-finding section, a
refutation-base entry, or a re-open-question edge), never a silent stall.

### Step 6 — Write back + future-trajectory
Every step must `feed` something retrievable (`judgment-execution.md` step ③): the ledger rows, the
graph nodes/edges, the conflict edges, the blind-spot register, the replication outcomes. A loop that
lives only in prose does not exist. Close the dossier with 2–3 lines of **future-trajectory**
(`kernel.md` §future-trajectory): how this compounds as the curves advance (the evidence base deepens
into a moat; cheaper models widen the generation/triage layer; the conflict-detection and replication
rules accumulate so the next pass self-corrects) and what must stay un-frozen (a live replication gate,
a human-held worth-knowing node, real human-interaction signal as the anti-homogenization reservoir).

## The collaborator/judge boundary — the line you must draw

AI as **collaborator** (lay out candidates, retrieve, run experiments, draft) is almost always safe — it
sits on the execution side, its output still passes a human judgment. AI as **judge** (let it decide
which is credible / worth publishing / worth funding) is the accountability seat for value and
credibility; hand it over and the structural bias becomes a verdict. Draw the line by three tests:
**can the criterion be machine-checked** (yes → AI may judge), **is the judgment value-laden** (yes →
human), **is a wrong call irreversible** (yes → human). The clean rule: *when "right" can only be
answered as "right for whom, in which value frame," AI is collaborator, never judge.* Don't drop the
line either way — handing over the judgment seat lets the default bias decide direction unowned; clutching
the collaborator seat (refusing to let AI even lay out candidates) keeps you trapped in work-hours.

## Self-check before delivering (the council's lenses, `../../references/_core/council.md`)
- **Kernel fidelity** — Is the scarcity inversion realized *here* (execution abundified, judgment retreated
  to worth-knowing + credibility)? No banned framing (means/ends sloganeering; six surfaces as a pipeline).
- **Domain craft** — Is the evidence handling real research practice (Ⅰ–Ⅴ grading, claims/evidence unmixed,
  replication as verifier, observational ≠ causal), not generic LLM filler? Are cited anchors graded and
  caveated (self-reported / model-predicted / observational — not asserted as law)?
- **Not collapsed to enablement** — Delete the AI: does it fall back to "reading faster"? Is a human
  silently on every edge, or only at the two reserved verdicts? Is "compounding context" a real `feed`
  (ledger rows, graph edges) or just prose?
- **Operable** — Does it produce the dossier (finding + ledger + graph contribution + blind-spot register)?
  Would two different questions yield two genuinely different dossiers, not a template?
- **Human boundary** — Stop-line held: did the human sign the credibility verdict and the worth-knowing
  call, not a tool? Does every non-vouch verdict have a named home? Is the weak-evidence × far-from-paradigm
  cell *suspended*, not auto-killed?

## References (read on demand)
- `../../references/_core/scripts/` — shared tools (stdlib, no install): `council.py` (the 5-role review
  gate) and `essence_lint.py` (sweep the dossier for banned framing / attestation tells). See
  `scripts/README.md`.
- `references/the-fork-and-the-gradient.md` — the kernel ② fork (machine-checkable → abundance vs.
  constitutive → bedrock), the verifiability gradient, the moving frontier, why the cut keeps the thesis
  falsifiable.
- `references/credibility-ledger.md` — the two-axis balance, the Ⅰ–Ⅴ evidence register, claims-unmixed-
  from-evidence discipline, the four-quadrant disposition, replication routing, error-flows-back.
- `references/knowledge-graph-as-spec.md` — the four load-bearing properties, spec-before-generation,
  the integration gap, conflict-as-edge, the same guardrail across surfaces.
- `references/worth-knowing.md` — the epistemology→axiology pivot, "worth" as constitutive not capability,
  taste as a gradient (community mean learnable, off-mean frontier not), hypernormal science & the
  homogenization mechanism, the collaborator/judge boundary, the hand-offs (↑ innovation, ↓ org).
- `references/finding-dossier-template.md` — the copyable deliverable: finding, credibility ledger,
  knowledge-graph contribution, blind-spot register, reserved-verdict block, future-trajectory.
