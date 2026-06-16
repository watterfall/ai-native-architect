# Worth-knowing — the pivot from "what is true" to "what is worth knowing"

This is the deepest move of the research surface and the second reserved human verdict (SKILL Step 5).
The depth behind why "what is worth knowing" is the scarce node, why it is *constitutive* rather than a
capability, and where it hands off. Read it before signing a worth-knowing call.

## The pivot: a coordinate-system switch, not another bottleneck move
Bottleneck-moves (execution → verification) all slide along **one** axis — they keep asking "对不对
(right/wrong)," so automation eventually catches up. The worth-knowing step is different: the
load-bearing question **drops vertically onto a second axis.**

- **Epistemology axis — "what is true":** right/wrong, machine-checkable, frontier moves right, will be
  automated.
- **Axiology axis — "what is worth knowing":** no right/wrong, only *belonging* — worth to whom, under
  which value frame. Not machine-checkable → a human holds it.

A machine can push the first axis's frontier all the way to the right end; it cannot reach the second
axis, because there is no machine-checkable criterion there. Research's most defensible ground is this
**axis-switch itself.** A judgment going from "is this true" to "is this worth knowing" changes the
coordinate system — and the new system has no checkable right/wrong. That is the layer research has that
engineering does not.

## "Worth" is a constitutive规定, not a capability
The most common and most dangerous misreading: "humans are *better at judging value*, a capability." If
"judging worth" were a capability, a strong enough model eventually does it better and the human case is
temporary. The thesis claims something else: **"worth" is not a capability, it is a constitutive
규정.** Capability asks "who judges more accurately"; constitutive asks "who gets to *define* whether this
counts at all." "This truth is worth knowing to us" has no external correct answer a more-accurate
judge approaches — its truth value is **constituted by the value frame that poses it.** For a group that
holds extended healthspan as the first good, "the molecular mechanism of aging" is worth knowing; for a
group that holds ecological integrity first, the same budget perhaps belongs elsewhere. Neither
"judged wrong," because worth is *relative to a frame, constituted not discovered.* AI cannot step past
this constitutive fact to a "worth" correct for all frames — that thing does not logically exist.

**Why AI learns the mean but not the off-mean.** Anything learnable needs many inducible samples. The
*average* "worth" — a value orientation expressed repeatedly across a field — has abundant samples and is
externalizable (RLCF has shown the community mean of scientific taste is learnable, rewardable). The
load-bearing "worth" is the kind that holds **only for a specific individual/group under a specific value
frame** — its sample size is essentially one, constitutively bound to a unique standpoint, so it has no
inducible training set. This is the mirror of the homogenization mechanism below: AI defaults to the mean
(regression to a domain prototype); heterogeneous value judgment is by definition the off-mean part.
So this is **not** "AI can't yet, but will" — in the statistical-learning frame heterogeneous worth has
no learnable object, because learnable means inducible and this is precisely not inducible.

## Taste is a gradient — AI learns the band, not the off-mean frontier
Problem-selection taste runs low→high: pick a benchmarked, steady-paper topic (low; AI already does it) →
chase a neglected anomaly → pose what the old frame cannot even state (high; outside training
distribution). RLCF can learn the **community mean** band; the rightmost **off-mean frontier value** sits
outside it. The danger: an organization that mistakes "learnable mean taste" for "all taste" and
systematizes it is **systematizing homogenization itself.** This resolves the apparent paradox that
scientific taste is *both* learnable *and* the human's last redoubt — the learnable part is the mean,
the redoubt is the off-mean frontier. (Open question, the hand-off to innovation: can RLCF learn
*anti-consensus* frontier value? Evidence that it learns community preference is grade Ⅱ–Ⅲ; that it learns
the anti-consensus frontier has no direct experiment — grade Ⅴ inference.)

## Hypernormal science and the homogenization mechanism (why "worth" must be guarded actively)
The generation layer has a **conservative bias**: it defaults to "safe, data-rich, consistent with the
existing paradigm." This produces *hypernormal science* — output explodes, exploration space narrows.
Three things to hold:

- **Predict-accurate ≠ understand-correct.** A model trained on simulated solar systems predicts orbits
  to high precision yet never grows the concept "gravity" internally — its objective rewards prediction
  error only, never "is this the right description level." Rising predictive power is not deepening
  understanding; this is the first cognitive defense against being fooled by hypernormal science.
- **The bias acts *before* judgment is handed back.** The generation layer does not neutrally lay out all
  candidates and wait for a human to pick — it preferentially generates in-paradigm candidates and buries
  the change-the-frame ones. So when the human arrives to judge, **the candidate set is already
  narrowed.** Guarding worth must therefore move *upstream*: actively require the candidate set to include
  paradigm-level options, or the human is choosing from a menu already tampered with.
- **Homogenization is written into the weights, not recoverable at inference.** Causal anchors: LLM-seeded
  writing makes individual stories *more* creative but *more similar to each other* (a "social dilemma":
  individually better, collectively narrower); cross-model similarity exceeds human-to-human similarity
  (swapping models doesn't save you); post-training diversity collapse is in the weights; recursive
  training on synthetic data causes model collapse (distribution tails vanish). This makes **real human-
  interaction data an increasingly precious anti-homogenization reservoir** — the distribution tail, the
  last reservoir of heterogeneity. *Honest counter-evidence:* homogenization varies by task/prompt/exposure
  and in high-exposure dynamic setups collective diversity can *rise*; open-ended / quality-diversity
  algorithms (novelty-search, MAP-Elites, POET) show machines *can* produce heterogeneity once you drop a
  single objective. So the correct, tighter claim is **"AI defaults to the mean; deliberate force is
  required to deviate"** — the enemy of heterogeneity is single-objective over-optimization, not the
  machine itself; the human defines "what is worth being different about," the machine diversifies under
  that definition. (Doshi & Hauser grade Ⅱ causal; weights-level diversity collapse grade Ⅲ.)

## The collaborator/judge boundary — the line you must draw at the verdict
AI as **collaborator** (lay candidates, retrieve, run experiments, draft) sits on the execution side and
is almost always safe. AI as **judge** (decides which is credible / worth publishing / worth funding) is
the **accountability seat for value and credibility** — hand it over and the structural bias upgrades
from "suggestion" to "verdict." Draw the line by three tests: criterion machine-checkable (yes → AI may
judge) · judgment value-laden (yes → human) · wrong call irreversible (yes → human). Clean rule: **when
"right" can only be answered as "right for whom, under which value frame," AI is collaborator, never
judge.** Two failure symptoms: *quietly ceding the judge seat* (the team uses "AI scored it high" instead
of "I read it, I vouch" — nobody owns credibility, bias compounds unnoticed); *clutching even the
collaborator seat* (distrust so deep you won't even let AI lay out candidates — execution never
abundified). Position the two seats by *kind*: hand over the execution seat freely, hold the judge seat
warily — and warily is decided case-by-case by the three tests.

## Why a value judgment must have a named owner (the org hand-off)
A value judgment does not sit in a vacuum: it is **either owned by a named person and consciously
exercised, or silently filled by the generation layer's default bias.** No middle state. When an
organization leaves "who judges whether this direction is worth chasing" unspecified, the judgment does
not disappear — it defaults to "whichever direction has data, a benchmark, steady results," i.e. the
conservative bias. The org *thinks* it is "neutrally following the data" while an unowned structural bias
chooses its direction. Governance's whole point is to wrest that judgment back to a **named person
accountable for long-term consequences.** Related: saved capacity does **not** auto-become slack — freed
hours get reallocated to *more of the same* (more volume), because slack is unmeasurable and "+X% papers"
is measurable; protecting exploration must be an explicit, owned, deliberately-budgeted decision.

## Hand-offs (the coupling)
- **↑ Innovation (value-discovery):** research identifies the gap on the knowledge frontier; innovation
  judges the *value* the gap points to. The seam is the moment "worth" passes from epistemology to
  axiology — the open question "who has the right to say *this* is worth knowing, and can that judgment be
  losslessly systematized" is innovation's fork.
- **↓ Org (governance):** once the value judgment has a named owner, it is a power/governance question —
  who decides direction, who vouches, who is accountable. This is also the **人本主线 (human-centered
  through-line)** on the research surface: AI-native research is not stacking papers faster, it is
  **returning the researcher to the questions worth asking** — the time spent on asking/judging/integrating
  should *rise*, not the time spent racing output. (See the org surface for the governance design; this
  skill *respects* that node, it does not design it.)
