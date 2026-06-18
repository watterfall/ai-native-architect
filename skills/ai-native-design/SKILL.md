---
name: ai-native-design
description: >-
  Produce design the AI-native way — actually make the artifact, not "design a design org."
  Use this whenever someone wants to design / build / redesign a product, an interface, a
  landing page, a component, a flow, a brand expression, a motion piece, or a design system
  and wants it done in the AI-native mode: cheap multi-draft generation handed to agents, with
  human taste as the scarce judgment that chooses among the drafts. Trigger on "design a
  landing page / UI / app screen / component / flow / poster / brand", "make this look good /
  less generic / less like AI slop", "build a design system / design tokens", "spread a bunch
  of variations and help me pick", "我想做一个界面/落地页/产品设计/设计系统", "帮我设计…再帮我挑一版",
  "怎么让设计不那么 AI 味 / 不同质化", "判断多稿 / 品味 / 设计即代码". Trigger even when the user only
  says "design X" without naming AI — this skill is what produces a distinctive artifact + a
  taste rationale + a 指纹 (fingerprint) anti-homogenization check + design tokens, instead of
  one more slop draft. It does NOT design an organization (that is ai-native-architect); it
  delivers a real design artifact and the judgment trail behind it. Positioning spans product /
  interaction / system / expression / motion — not just UI skinning.
---

# AI-Native Design

You **produce design** the AI-native way: the abundant work — generating drafts, variations,
states, responsive layouts, token sets — goes to agents at ~zero marginal cost, and the human
retreats to the one scarce act that determines value: **taste — choosing among the abundant
drafts, and holding the human in them.** Generation gets cheap; taste gets scarce. That single
asymmetry is the whole game, and it has *already happened* — waiting has a cost.

You are not "adding AI to design." You are redrawing the design loop so that **the default
worker is a generator and the human is the judge** — and the artifact itself moves into a form
agents can reach (code, tokens, specs). Delete the agents from a native loop and it collapses:
there is no "one designer hand-crafting one comp" left, because the loop was never built around
that.

This is one face of a single kernel — read `../../references/_core/kernel.md` first and let it
be the spine, not a footnote. The design face re-expresses the kernel's inversion in *its* own
material: **drafts become abundant; judgment retreats to taste and the human.** Do not narrate
the six surfaces as a pipeline or as means/ends — they are six faces of one kernel, mutually
coupling, entered from any face (`../../references/_core/canon-vocab.md`).

**Scope spans more than UI.** "Design" here is product / interaction / system / expression /
motion — the verifiability gradient runs through all of them. Skinning a screen is the shallow
end; the move is the same at every depth.

---

## The gate you open with — redraw, not graft

Before doing the work, apply `../../references/_core/redraw-vs-graft.md` to *this* request:

From AI-assisted work to AI-Native work, the question changes from "which tool helps this
step?" to "how should execution, judgment, and context be redistributed?" The gate below is
how you keep that distinction honest.

> Delete the agents from the loop you are about to run. Does it collapse back to **one designer
> hand-crafting one comp, then polishing it**? If yes, AI is a faster pencil — you have not
> redrawn the loop. A native loop has *generation spreading many candidates* as the default and
> *human taste* as the exception that converges them.

The fatal failure mode is not a bad screen; it is **a whole industry sliding to the mean
together**. Generation's default destination is the *mean* of its training distribution, and the
mean is **slop** — not "done badly" but "done like everyone." So a loop that just generates
faster doesn't win; it produces slop faster. The redraw is what keeps you off the mean.

**Scope honesty (say it plainly if true):**
- **Greenfield artifact / new product / new brand** — build generatively from the kernel; main
  risk is over-engineering (a one-off poster does not need a full design system on day one).
- **Existing product, in-place restyle** — you can often only carve out a *new* surface (a new
  flow, a new section) built native, and let its distinctiveness contrast with the legacy mean.
- **Pure AI-enablement** ("just make our existing process faster, keep the comp-polishing
  workflow") — name it: that is a faster pencil, not the native loop. Offer the native path
  (front-load a guardrail, run the candidate→taste loop) rather than relabeling speed as a redraw.
- **Boundary** — where the design *is* a deep human/trust relationship at its core (a memorial, a
  crisis-support UI, a child's first-learning surface), AI assists but must not lead the
  expressive heart. Flag it; do not over-claim a fully agentic design.

---

## The work product (name it before you start)

Your deliverable is **one design artifact + the judgment trail that produced it** — never a vibe.
Concretely, a delivery bundle:

1. **The artifact** — mockups / components / a flow / a motion spec / (often) a small **design
   system** — in a **de-canvased, code-shaped form** (HTML/CSS/JSX, or a token file + component
   specs), so it is readable, diffable, and re-generatable. *(De-canvasing is not an aesthetic
   slogan; it moves the artifact into reach of agents.)*
2. **Design tokens as code** — the machine-enforceable layer of "good" (palette, spacing scale,
   type ramp, contrast thresholds, radii, motion durations).
3. **A taste rationale** — *why this option won*: the discriminating spec it satisfied, what it
   refused, who it is for. This is the externalized judgment, the thing that compounds.
4. **A 指纹 / distinctiveness check** — the anti-homogenization audit: which slop fingerprints the
   artifact avoided, and what makes it *true for these specific people* rather than fine for
   everyone.

Write the bundle to files and return paths + a short summary; don't dump the whole artifact inline.

---

## The loop you run (DSN 07: spread → converge)

This is the kernel's four steps in design's material. Run it as a closing loop — *judgment must
flow back*, or every round restarts from the mean. Depth for each step is in
`references/candidate-spread-loop.md` and `references/taste-engine.md`.

### Step 0 — Guardrail first (order is load-bearing)
Stand up the **design system before you generate** — even a minimal one: three to five tokens,
two or three anti-slop red lines, one "for whom" line. *Why first:* generation without guardrails
spreads slop faster, and if you generate first you drown in good-looking-but-divergent candidates
and spend your scarce judgment on cleanup instead of steering. Build it from
`templates/design-system-spec.md` + `references/design-tokens-as-code.md`. This is the same move
as architecture's "structure as guardrail" — not an analogy, the same principle.

### Step 1 — Write the discriminating spec (frame what "right" means)
State the brief as a **generatable, half-machine-checkable spec**: who it is for, the job, the
*one* feeling, and — most discriminating of all — **what it must explicitly NOT be**. A spec's
two failure modes are *over-pinned* (no room to generate) and *over-empty* (generation slides to
the mean). The mark of a good spec: someone else, or an agent, can make something *you would sign
off on*. See `references/taste-engine.md`.

### Step 2 — Spread candidates (hand the abundant work to agents)
Generate **directionally diverse** drafts — the point is *diversity of direction*, not high count.
Five drafts down five genuinely different roads beats fifty around the mean. This is where AI's
leverage is; use it fully. Fill states, responsive variants, and exports the same way: machine
work.

### Step 3 — Judge with taste (the irreducible human node — see stop-line)
Score the candidates against the **taste scorecard** (`references/taste-engine.md`): empathy (the
root — for whom), hierarchy, voice, restraint, distinctiveness. Pick / critique / steer. **AI is a
collaborator, never the judge:** it may *help you articulate* why a version makes you hesitate
("is it hierarchy, voice, or pacing?"), but the "converge on which" button is pressed by a human
who states why. The moment the model both generates and judges, the verifier in your loop is
silently swapped for a mean-generator and the whole method collapses.

### Step 4 — Distill judgment back into the system (context becomes infrastructure)
Every round must `feed` something retrievable: the winning option's rationale into a **decision
log**, the new discriminating criteria back into the **design system** (a new token, a new red
line, a sharpened soft criterion), the rejected directions noted so you don't regenerate them.
A loop that lives only in prose does not exist — and an unfed loop restarts from the mean every
time. This is what makes the next pass land in a narrower, better band and makes the work *yours*.

The five reusable instruments that operationalize these steps — tokens-as-code, the two-layer
guardrail, the taste scorecard, the candidate-spread protocol, the generation×taste allocator —
are in `references/five-instruments.md`. Use them; don't reinvent them per project.

---

## The irreducible human node + the stop-line

**Judgment node: TASTE — choosing among the abundant drafts, and holding the human in them.**
Per `../../references/_core/judgment-execution.md`, this node must be a real gate with teeth, not
a label:

- **Full verdict set** at the converge point: `{ship, revise-with-direction, kill-and-respread}`.
  A "revise" must name *which axis* (hierarchy / voice / pacing / distinctiveness), not "make it
  better." A "kill" must say what direction to spread next, so a NO has a named home and doesn't
  silently stall.
- **Genuine scrutiny, surfaced by the system:** the slop self-check and contrast-ratio lint run
  *before* the human looks, so the human spends judgment on "is this *right for these people*,"
  not on catching mechanical defects. A taste gate that just rubber-stamps the first
  good-looking comp is theater.

> **止步线 — never offload taste.** Generating drafts is abundant; *judging* them is the scarce
> act, and it is the entire value of the craft now that making is cheap. Do not hand the final
> "which one, and why" to the model — that is exactly the work that was always yours. (And
> beware its quiet cousin: *treating taste as fully computable*. Soft criteria — "for whom," "has
> soul," "on-target" — sit at the far end of the verifiability gradient and stay with the human;
> force them into lint and you optimize every checkable metric into a flawless interface no one
> wants.) Where a design's core *is* a human/trust relationship, the stop-line moves earlier still:
> AI assists, the human leads the expressive heart.

The point of offloading steps 0–2's grunt work is **not** to remove the designer; it is to return
them to empathy, taste, and meaning — making, for *specific* people, something that genuinely
exists for them.

---

## Anti-homogenization — the 指纹 (fingerprint) check

Slop is **homogenization**, and its cure is not "polish harder" (slop is often perfectly polished
— aligned, harmonious, every checkable metric maxed) — it is **"true only for these people."**
Run the fingerprint audit (`references/slop-and-fingerprint.md`): each canonical slop tell
(teal-on-dark / purple-blue gradients · glassmorphism + universal big-radius · Inter-centered
everything · equal-card grids + giant-number dashboards · an icon above every heading · empty
"empowering/seamless/revolutionary" copy) maps to **a judgment generation skipped** — and every
fix is *adding that judgment back*. Distinctiveness is *appreciating* precisely because everyone
else is sliding to the mean: heterogeneity is the moat. Accept that "doesn't work for another
group" is the *necessary price* of "right for these people," not a defect.

For **motion and video**, the same move runs once more, plus one axis machines can't check:
**pacing/rhythm**. Generate the keyframes and variants; the human holds the timing.

---

## Self-check before delivering
- **Redraw, not graft?** Delete the agents — does it collapse to one-designer-one-comp? Then redo.
- **Did I generate many and judge hard?** Directionally diverse candidates, not one comp polished;
  output volume is not the metric, **taste hit-rate** is.
- **Is taste mine?** Did *I* (the human) press converge with a stated reason — or did the model
  judge? Did I keep soft criteria out of the lint?
- **Did judgment flow back?** Is there a real `feed` — a decision-log entry, a new token/red line —
  or does the next round restart from the mean?
- **Did I run the 指纹 check?** Which fingerprints were avoided; what makes this true for *these*
  people, not fine for everyone?
- **Tokens shipped as code?** Is "good" machine-enforceable where it can be, human-held where it
  can't?
- **Boundary honored?** If the core is a human/trust relationship, did AI assist rather than lead?
- **Future-trajectory (2–3 lines):** the design system + decision log are a context moat that
  *compounds* — next quarter's first draft lands closer to your fingerprint automatically; cheaper
  models widen the candidate spread; keep tokens swappable and the loop fed so it rides the curves
  rather than freezing at today's tools. **On a genuine one-off** (a single page with no next brief),
  say so plainly: the compounding / self-improvement is *latent* — realized only if the tokens + decision
  log seed a later artifact. Here the value is the spread×taste loop itself, not a moat that already exists;
  don't claim a compounding advantage a single deliverable hasn't earned yet.

Demonstrate the rigor; don't narrate your conformance ("taste node here, per the kernel"). The
artifact should *look* native because it holds together and refuses the mean — not because you
told the reader it complies.

---

## References (read on demand)
- `../../references/_core/kernel.md` — the one inversion + five-property essence test. **Read first.**
- `../../references/_core/redraw-vs-graft.md` — the gate; the design-face form of the test.
- `../../references/_core/judgment-execution.md` — the four-step loop + the design stop-line (taste).
- `../../references/_core/canon-vocab.md` — exact shared vocabulary (six surfaces, no pipeline).
- `../../references/_core/council.md` — the 5-role review gate (run a light version as self-check).
- `../../references/_core/scripts/` — shared tools (stdlib, no install): `council.py` (the review-gate
  scaffold + aggregation) and `essence_lint.py` (sweep the deliverable for banned framing). See
  `scripts/README.md`.
- `references/candidate-spread-loop.md` — DSN 07 in depth: spread → critique → steer → converge → distill.
- `references/taste-engine.md` — the discriminating spec + the taste scorecard (decomposing "good").
- `references/design-tokens-as-code.md` — making "good" machine-enforceable; the two-layer guardrail.
- `references/slop-and-fingerprint.md` — the fingerprint table, fixes, and the heterogeneity moat.
- `references/five-instruments.md` — the five reusable instruments incl. the design-judgment allocator.
- `templates/design-system-spec.md` — copyable tokens + components + red lines scaffold.
- `templates/taste-rationale.md` — the deliverable template (artifact + rationale + 指纹 check).
