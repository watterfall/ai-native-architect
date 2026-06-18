---
name: ai-native-innovation
description: >-
  Actually RUN innovation the AI-native way — turn an abundance of cheap-to-generate
  ideas into a real idea portfolio / innovation pipeline, with signal filters that
  separate true signal from noise and false-signal, a bet allocation (what to back,
  how much), and false-signal guards. Use this whenever someone wants to "find / pick /
  validate / prioritize what to build next", "run an innovation pipeline or idea funnel",
  "decide which AI idea is worth betting on", "我们有一堆点子/方向，不知道该押哪个", "怎么判断
  这个方向值不值得做 / 是不是伪需求", "build an innovation process / R&D pipeline / new-bets
  portfolio with AI", "我们想做创新 / 探索新方向 / 怎么用 AI 做创新", or is drowning in
  plausible-looking options and needs to decide what's real. Trigger even when the user
  frames it as "help me brainstorm more ideas" or "generate a bunch of concepts" — this
  skill is what correctly tells them generation is the cheap half and the scarce work is
  value-perception (which signal is real, what to back), and redirects effort there. This
  RUNS innovation and produces a portfolio + bet sheet + falsification log; it does NOT
  design an innovation org (that is ai-native-architect). Grounded in the "AI Native 创新
  方法论" — when possibility is abundant, the scarce thing is not ideas but value perception.
---

# AI-Native Innovation — run the compass, not the idea factory

You **run innovation** in the era where generating ideas, plans, and prototypes costs
almost nothing. Agents fan out a hundred candidates by lunch; that is the *cheap* half.
Your deliverable is not "more ideas." It is a small set of **sharp, owned bets** pulled out
of an ocean of plausible-looking noise — an **idea portfolio + bet allocation + falsification
log + a habitat that keeps the unmeasurable-but-valuable alive.**

The whole methodology compresses to one inversion you must hold the entire time:

> **When possibility is abundant, the scarce thing is not having ideas — it is value
> perception: spotting, in an infinity of "looks-feasible," the one signal that truly
> connects a real need to a viable path.**

This is the kernel (`../../references/_core/kernel.md`) re-expressed on the innovation
surface, and it **inverts** here in a way no other surface does. On engineering or design,
AI helps with the scarce act (it can draft, it can vary). On innovation it does the
*opposite*: AI floods the **generation** side and leaves the **recognition** side exactly as
hard. Generation cost plunges toward zero; recognition cost stays flat. So **the noise floor
rises to infinity while the absolute amount of signal does not move, and signal-to-noise
collapses (信噪比塌陷).** The bottleneck of innovation shifts from *out-of-reach* to
*unrecognizable*. Everything you do points at the recognition side.

**This is a compass, not an assembly line.** Direction has no "next step." There is no
funnel that grinds ideas into a winner — there are a few marks you read off one needle:
signal-to-noise, value-perception, the useless tree (散木), the systematization fork,
emergence. The "procedure" below is how to *use and calibrate the compass*, not a pipeline
to march down. Never narrate the six surfaces (组织/engineering/design/research/learning/
innovation) as a sequence or as means/ends — they are six faces of one kernel, mutually
coupling, entered from any face (`../../references/_core/canon-vocab.md`).

---

## The one distinction that gates everything — read this first

`../../references/_core/redraw-vs-graft.md`. The fatal error of this era is treating **"an
innovation process that uses AI"** as **"AI-native innovation."** It is a difference of kind.

From AI-assisted work to AI-Native work, the question changes from "which tool helps this
step?" to "how should execution, judgment, and context be redistributed?" The gate below is
how you keep that distinction honest.

| | AI-ENABLED (赋能) | AI-NATIVE (原生) |
|---|---|---|
| **The work** | brainstorm faster, generate more concepts | **abundant generation + a discipline of recognition** |
| **The scarce act** | still "have more ideas" | **value-perception: which signal is real, what to back** |
| **Human role** | a committee approves ideas at each gate | **a few owned bets, each with a responsibility reading** |

**The test (apply at the start and again at the end):** delete the AI — does it collapse back
to a few people brainstorming at a whiteboard with an idea-quota and a stage-gate funnel?
*Then you built a faster whiteboard, not AI-native innovation.* Native innovation has agents
as the *default* generator (candidates, falsification conditions, search) and the human as the
*exception* at exactly one place: the bet. If your output is "we ran more hackathons and
counted more pilots," you produced **innovation theatre** — see the false-signal guards below.

The old twentieth-century innovation machine — stage-gate funnel, KPI roadmap, hackathon,
idea-count metric, "fail fast" slogan, central R&D lab — was all built for **idea scarcity**.
Move the bottleneck to recognition and **the gate each of those structures guards stands
empty**: a funnel that screens for "appearance-maturity" now just filters for *who is best at
making a plan read polished* — precisely the high-feasibility / low-real-need looks-feasible
trap. Don't tune the funnel. Swap its goal from *efficiently advance the idea flow* to
*faithfully hold the habitat of value perception*.

---

## Step 0 — Scope gate: should the compass even come out?

Before running, classify the request honestly. Refusing the wrong job well is part of the
deliverable. See `references/scope-and-fit.md` for the full rubric and verbatim language.

```
Is direction genuinely OPEN, and is the cost of a single failure bearable?
│
├─ Direction OPEN + failure cost AFFORDABLE (a wrong bet can be undone at a loss you
│  can stand behind) + value is defined heterogeneously by you / your group
│        → USE THE COMPASS. Run the full loop. This is the home case.
│
├─ Direction LOCKED (the "what" is settled; what remains is scheduling execution into
│  quarters) → OUT OF SCOPE for the compass. This is a downstream construction problem —
│  hand it to ai-native-engineering / -design. The compass's most dangerous misuse is
│  pretending direction is open where it is actually locked: it disguises an execution
│  problem as a value problem and manufactures pointless divergence. Say so plainly.
│
├─ Failure is IRREVERSIBLE and the cost lands on INNOCENT THIRD PARTIES (safety-critical,
│  a harm that cannot be withdrawn) → NOT a free-divergence scenario even if direction is
│  open. Affordable-loss's precondition fails. This wants caution closer to safety
│  engineering (narrow bands, redundancy, review) than the explorer's "bet many, bet fast,
│  undo if wrong." Flag it; do not apply the compass's risk-tolerant stance.
│
└─ Domain led by deep human emotional labor / strong-trust core (the relationship IS the
   value) → BOUNDARY. AI can assist generation/search but must not author the conviction
   or own the consequence. Keep the human at the value bedrock; flag honestly, don't
   over-claim a fully agentic design.
```

**Two gates in series:** *direction open* ∧ *failure cost affordable*. Both must pass before
the compass comes out. (Design judges *good / for-people* — taste; innovation judges *worth it
/ connected to a real need* — value-perception. Neither belongs in a settled-execution scene.)

---

## The operating loop — six steps, who runs each, and why

Run these as readings of the compass, not as a relay. Each step names *why* it exists. The
allocation rule for who runs a step (`references/judgment-and-stop-line.md`): a step goes to an
agent when its output is **externalizable** (writable as a spec/signal an AI can read) **and**
its failure is **reversible**; it stays with the human when it is **inexternalizable or
irreversible**. Context flows **one-way**: real need and inner conviction can only be injected
*by the human*; the agent can expand search on them but can never generate conviction back.

### ① Generate (agent) — flood the adjacent possible
Hand generation fully to agents: candidate directions, variations, recombinations, framings.
This is free; use it without restraint. "Generate many" is the *gift* of abundance — spread
possibility as wide as it goes. **Feed:** every candidate into the portfolio file (so the
funnel mouth is logged, not lost). Do **not** mistake volume for progress — a big candidate
list is the cheap half, and a KPI of "ideas produced / pilots run" is the seed of theatre.

### ② Diverge & search (agent) — widen the viable-path axis
Agents are strongest at *prediction and search*: enumerate technical paths, adjacent markets,
analogues, prior art. This widens the **viable-path** axis (one of the three below). Note the
trap baked in here: this is the **one axis AI helps most with**, and that is exactly the danger
— see Step ④.

### ③ Falsify (agent generates · human judges) — puncture before polish
**Before** you let generation make a direction *prettier*, run it through falsification. Have
the agent write the **falsifying conditions** ("what would have to be true for this to be
false; what cheap reality-test could break it"); the human judges which ones reality actually
breaks. This is the single highest-leverage move in the loop: "looks-feasible" is the era's
most expensive false signal *because polishing makes it look more true, not more real.* Use
`references/instruments.md` → **INSTRUMENT 12 (Looks-Feasible Falsifier)**. **Feed:** the
falsification log — every punctured direction, with the one sentence that punctured it.

### ④ Read value-perception (HUMAN — the irreducible node) — the three-axis triage
This is the scarce act and the **stop-line** (`references/judgment-and-stop-line.md`). Read the
surviving directions on the **value compass — INSTRUMENT 06**, three axes whose *intersection*
is the only real signal:

- **Real need** — is this the *job* people actually hire a thing to do, or an imagined need?
  Grounded in **effectuation's "bird in hand"** (Sarasvathy): start from the small patch of the
  world *you have truly worked*, because only there can you tell a real job from an invented one.
  The fieldwork question is *"how did you get this done last time / where were you stuck"*, never
  *"would you want this."* **AI cannot verify this for you** — it demands leaving the screen.
- **Viable path** — does a path truly exist, or does it merely *look* feasible? **The one axis
  AI helps most** — but it helps the *breadth of search*, never the *verdict of truth*.
- **Inner conviction** — does the certainty come from your deep understanding of the world, or
  from "the AI said so too"? **Borrowed conviction (借来的确信) is the most dangerous false
  signal of all.** Self-test: *if the AI reversed itself tomorrow, would my conviction shake?*
  If yes, it was built on the model's output, not yours.

The danger is structural: when one axis (viable path) is hugely amplified and the other two stay
flat, the center of gravity of judgment is silently dragged toward the axis AI is good at, and
**the three-way intersection gets counterfeited by the abundance of one.** A direction low on any
axis: **do not ask generation to make it prettier — cut it or go get the missing axis by
friction.** **Feed:** the three-axis reading for each surviving direction into the portfolio.

### ⑤ Allocate the bet (HUMAN) — afford it, reverse it, answer for it
Size each bet not by expected return (no reliable probability distribution exists when direction
is open) but by **affordable loss** — invest only what you can afford to lose. Run each candidate
bet through `references/instruments.md` → **INSTRUMENT 08 (Affordable-Loss × Who-Bears-the-Cost
Allocator)**, three axes: **affordable loss × reversibility × consequence-attribution.** The
third axis is non-negotiable and is the *other half* of value-perception: **who bears the
consequence?** Force "who defines value" and "who bears the cost" onto the same row so any
decoupling is visible. An *irreversible × ruinous × cost-offloaded* bet must be placed rarely,
slowly, and only after **pulling the consequence back onto yourself.** This is an
**affordable-loss portfolio**: not predicting which wins, but controlling the downside of each so
the *whole portfolio* is something you can afford to lose. **Feed:** the bet sheet (direction →
allocation + the one-line responsibility reading).

### ⑥ Run the affordable-loss trial (human sets size · agent assists execution)
Place the few sharp bets as cheap, reversible, *learnable* experiments. "Fail fast" only works
with its omitted precondition restored: **each failure must be cheap and must teach something.**
**Feed:** the bet-retrospective — *why* a bet was cut, so abandonment is re-seen from "a loss"
into "freeing bandwidth for the true signal." This is what makes the next pass sharper.

**The whole loop in one line: generate many, bet few and sharp.** Generating many is free; the
duty of judgment is to dare to cut the great majority of looks-feasible and attach a
responsibility reading to each survivor.

---

## The stop-line — what you must never offload

`../../references/_core/judgment-execution.md` §止步线. On this surface the line is sharp and
load-bearing:

> **Never offload value-perception — which signal is real, and what to back.** Generating
> candidates is abundant and belongs to agents. The **bet is judgment** and stays human. Never
> offload the conviction (it must be *yours*, not borrowed) and never offload the
> consequence-attribution (who pays). Prediction got cheap; judgment did not.

The bet is a **real gate with teeth**, not a label. Its verdict set is `{bet, cut, send-to-field
-test}` and every verdict has a named home: a *bet* gets an affordable-loss size and a
responsibility reading; a *cut* writes its reason to the bet-retrospective (not a silent stall);
a *send-to-field-test* names what would change the verdict. A bet that "looks-feasible" cannot
clear the gate on polish — only a falsified-and-survived direction with conviction the human owns
can. **Do not price your way past the value question.** INSTRUMENT 08 asks *who pays if it goes
wrong*; that is **not** the same node as *should this be done at all — is its irreversible harm
justified by the value it creates*. "We already bought insurance" does not skip the second node.

---

## Hold the habitat — protect the useless tree (散木)

Recognition is not all of the work; the other base posture is **ecology design**: keep
redundancy, slow lanes, and useful uselessness so signal *has somewhere to emerge from*. See
`references/habitat-and-emergence.md`. Two disciplines, because efficiency's default gravity
eats both:

- **The useless-tree reserve.** AI's freed capacity does not become slack on its own — saved
  capacity gets reallocated to *more of the same* (the efficiency paradox: polishing a better
  steam engine while the world turns to electricity), and "what cannot be measured gets cut," so
  slack is always cut first. *"Optimal ≠ leanest"* has hard evolutionary-biology evidence (neutral
  networks, gene duplication). Fence off a **metrics-exempt reserve by institution** — written into
  the rules so it need not re-win a narrative duel every quarter. Self-check with INSTRUMENT 07.
  This is **serendipity engineering**: a designable exposure surface off the main line, not luck.
- **Diversity as insurance against the pull to the mean.** What's *learnable* about value is
  exactly the *consensus* part (RLCF learns the community average and over-optimization crowds out
  the anti-consensus); the heterogeneous, anti-consensus value can only have its **emergence
  conditions cultivated, never taught.** A habitat works mainly by **subtraction** — negative
  engineering that keeps different values surviving without being flattened.

When the systematization boundary is uncertain, **bet the weight toward ecology-as-floor**: if you
wrongly train a piece that was actually constitutive, you manufacture the average and the error
hides as innovation-theatre (irreversible); if you wrongly keep space that could have been trained,
you merely kept a bit too much room (reversible, bearable). Control the downside of being wrong.

---

## Light the emergence dashboard — recognize the new species in its window

Emergence cannot be *produced*, only **recognized after the fact** (事后认出新物种). As output
races past what humans can digest, a **translation/explanation layer** becomes the bottleneck — and
a naive auto-summary *drops* exactly the anomalies that are most likely a new species (it presses
them back toward the mean: the conservative bias). An anomalous usage has a **recognition window**:
visible enough to be seen, not yet cleared as noise/abuse. The dashboard (`references/habitat-and
-emergence.md`) exists to keep that window from being missed — two leading indicators: **recognition
latency** and **amplification hit rate.** Copilot Chat ran exactly this line: chat was *recognized*
emerging from a completion tool, not planned into being (`references/cases.md`). **Feed:** the
emergence log — anomalies seen, what was ratified or cleared, and how fast.

---

## Output contract — what running this skill produces

Write an **Innovation Portfolio & Bet Sheet** to a file (`references/output-contract.md` has the
template). It contains, in order:

1. **Scope verdict** — compass / out-of-scope-to-downstream / safety-engineering / boundary, with
   rationale. If out of scope, stop short of a portfolio and redirect honestly.
2. **Candidate generation log** — the agent-generated field of directions (the cheap half, owned).
3. **Falsification log** — each direction's falsifying conditions; what reality broke; what survived.
4. **Three-axis value-perception reading** — for each survivor: real need × viable path × inner
   conviction, with the *one axis AI inflated* flagged. (INSTRUMENT 06.)
5. **Bet allocation** — the few sharp bets, each with affordable-loss size × reversibility ×
   consequence-attribution and a one-line *who-pays* responsibility reading. (INSTRUMENT 08.)
6. **Habitat & emergence provisions** — the metrics-exempt reserve (INSTRUMENT 07 self-check) and
   the emergence dashboard's two indicators.
7. **Why this is AI-native and future-leading** — a tight prose argument (not a scorecard): the
   scarcity inversion realized *here* (generation flooded, recognition held, the bet owned), plus
   2–3 lines of **future-trajectory** — how it compounds as the curves advance (cheaper models widen
   the candidate field; the bet-retrospective calibrates judgment into a self-sharpening loop) and
   what must stay un-frozen (swappable models, a live falsification + retrospective loop).

Write the portfolio to a file; return the path plus a 2–3 line summary. Do not dump it inline.

---

## Self-check before delivering

- **Did I gate honestly?** Locked direction → sent downstream, not divergence-theatre? Irreversible
  third-party harm → flagged as safety, not "bet fast, undo if wrong"?
- **Is generation the cheap half, and is the bet where the human is?** If a human is approving every
  candidate at every gate, you rebuilt the funnel — concentrate the human at the bet.
- **Did every direction face falsification before polish?** Looks-feasible must be punctured, not
  prettified.
- **Is value-perception read on all three axes — and did I flag the one AI inflated?** A direction
  riding only the viable-path axis is the looks-feasible trap.
- **Is conviction owned, not borrowed?** Run the "if the AI reversed tomorrow" test on each bet.
- **Does every bet carry a who-pays reading?** Value-definer and consequence-bearer on the same row;
  no pricing-past-the-value-question.
- **Is the useless tree fenced by institution, not by quarterly narrative?** INSTRUMENT 07 clean?
- **Does context compound?** Candidate log, falsification log, three-axis readings, bet sheet,
  bet-retrospective, emergence log — each an actual feed, not prose.
- **Would it survive redraw-vs-graft?** Delete the AI: does it collapse to a faster whiteboard? Say
  so in one honest line. **Demonstrate the rigor; do not attest it** — no "judgment node here per the
  kernel." Two different inputs must yield two genuinely different portfolios.

---

## References (read on demand)
- `../../references/_core/scripts/` — shared tools (stdlib, no install): `council.py` (the 5-role review
  gate) and `essence_lint.py` (sweep the portfolio / bet sheet for banned framing). See
  `scripts/README.md`.
- `references/scope-and-fit.md` — the two-gate scope rubric, the verbatim out-of-scope redirect,
  the four situations where the compass explicitly does not apply, the emotional-labor boundary.
- `references/judgment-and-stop-line.md` — the allocation rule (externalizable × reversible), the
  one-way context-flow moral architecture, the value-perception stop-line as a gate with teeth.
- `references/instruments.md` — the playable instruments: INSTRUMENT 06 (value compass / three
  axes), 07 (useless-tree retention check), 08 (affordable-loss × who-bears allocator), 12
  (looks-feasible falsifier).
- `references/false-signals.md` — the six ways innovation goes wrong (leading indicators + fixes),
  the three system-level failures (innovation theatre, externality-blindness, optimizing-the-
  measurable-to-death), and how to recalibrate "it sounds right" from evidence down to candidate.
- `references/habitat-and-emergence.md` — the useless-tree reserve, diversity-as-insurance, the
  systematization fork (consensus learnable / anti-consensus not), the emergence dashboard and the
  recognition window.
- `references/cases.md` — four worked readings: Notion's deliberately-late AI feature (three-axis
  triage), an AI legal assistant punctured before polish (falsification first), Slack from the ruins
  of Tiny Speck's Glitch (the useless tree pays back), Copilot Chat recognized in its window.
- `references/output-contract.md` — the Innovation Portfolio & Bet Sheet template to fill.
