# Knowledge graph as spec — the guardrail that keeps generation from collapsing into noise

The traceable evidence base / knowledge graph is the **上下文成基设 (context-as-infrastructure)** of the
research surface. This file is the depth behind SKILL Step 1. The core inversion: it is **not a warehouse
you file results into afterward — it is the spec that must exist before generation and constrain it.**

## Spec-before-generation — the order is load-bearing
The most common way to misuse the graph is to **generate first, file later.** That reverses the
load-bearing order. In AI-native research the base must exist *first* and define what counts as "done
right" — exactly as engineering's "context is the spec, not supplementary material, so it precedes
implementation." Write down, up front: **what counts as credible evidence, what counts as a conflict,
what must trace to raw data.** Then generation has a target to align to.

Reverse the order and the failure shows immediately: let agents batch-produce ten thousand claims and
*then* try to file them, and you get a heap of mismatched formats, broken provenance, and mutually
contradictory claims that nobody catches — **an un-integrable garbage mountain** whose cleanup cost
dwarfs the generation it saved. Stand the base up first and it becomes a live guardrail: unsourced claims
blocked at the door, conflicting claims flagged on arrival, untraceable claims kept out entirely. This is
why the research loop puts "frame the base" *before* "generate" — not process hygiene, the thesis itself.

## The four load-bearing properties (it's the properties that win, not a tool)
Any evidence carrier satisfying these four is amplified in a generation-abundant world; any carrier
missing one (locked in PDF screenshots, private databases, untraceable reviews) is selected against. It
is **not** that some graph product wins — it is that these four properties are the minimum sufficient
condition for "massive generation not collapsing into noise." Same principle as engineering's context
layer and design's design-system.

1. **Agent-readable** — claims, evidence, sources are structured nodes a model can read and write
   directly, not human-only prose.
2. **Traceable** — every claim carries its evidence edge: back to raw data / the paper, trackable by
   independent replication.
3. **Falsifiable** — contradictory claims surface as a **conflict edge** in the graph, not buried across
   two papers that never cite each other.
4. **Integrable** — cross-domain claims can be stitched, compared, synthesized (the substrate for Step 5's
   integration).

## "Falsifiable" is the property most often skimped — and the one that matters most
Vendors love demoing "agent-readable" and "traceable" because they sell well. The load-bearing one that
gets quietly cut is **falsifiable.** A base that chases only "readable + traceable" becomes an efficient
**echo chamber**: it stores and serves ten thousand mutually consistent claims beautifully but never lets
two contradictory claims collide. Its concrete form is making conflict **surface as a conflict edge** —
one paper says X, one says not-X, each "traceable," and the system never reports they contradict. At
thousands of claims/hour this silent contradiction compounds exponentially until you hold not a knowledge
base but a **self-consistent hallucination.** So conflict detection is not a nice-to-have advanced
feature — it is the line that separates a "base" (库) from a "heap" (堆).

## The integration gap — why this base is built for *integration*, not retrieval
Human understanding's bottleneck was never the *amount* of knowledge, it is the *integration* of it. As
generation pushes output toward near-infinite, the scissor-gap between knowledge-production speed and
human-digestion bandwidth blows open — and that is a **bandwidth problem, not a stock problem.** This has
an operating consequence: **retrieval** ("find the relevant existing one" — nearest-neighbour, vector
search, RAG) gets abundified to near-free; **integration** ("stitch claims never before placed together
into a new understanding") stays scarce, because it requires a mind holding several frames at once and
judging which to stitch and whether the stitch holds. Producing more summaries makes the heap grow
*faster* and the bandwidth *tighter* — so the base is designed to feed candidate material to the human
integrator, not to auto-produce more digests. Watch one metric: the ratio of integration products (genuine
new-understanding syntheses) to raw output — is it rising or falling?

## The same guardrail across surfaces
This is one move in four projections, all answering "when generation is near-free, massive, parallel,
what structure keeps it from collapsing into noise?" — engineering: context + spec; design: design system
+ component library; architecture: clear agent-readable boundaries; research: knowledge graph + evidence
base. Seeing this stops you treating "build a knowledge graph" as an isolated research-tech task; it is
the shared substrate principle landing on the research surface.

## What the contribution looks like in the dossier (③ feed)
The dossier's **knowledge-graph contribution** section records, concretely: the new nodes added (claims,
sources), the evidence edges attached, any **conflict edges** raised against existing claims, and which
existing nodes were touched/updated. "Wrote it back" must be these actual nodes/edges — a contribution
that lives only in prose does not exist.

## Evidence discipline (`canon-vocab.md`)
"Integration gap blows open" is currently **thesis-derivation + order-of-magnitude side-evidence**
(literature base ~2.5M papers/yr, doubling ~9 yr, grade Ⅱ; individual output up while topic coverage
−4.63%, grade Ⅱ) — there is **no single primary anchor** quantifying the un-integrated accrual rate, so
mark it "待坐实" (to be grounded), grade Ⅲ for the accrual claim. Falsification condition: if an automated
synthesis system can produce, under expert blind review, integrations judged "genuinely stitched, not
collaged," the human-exclusivity of integration loosens.
