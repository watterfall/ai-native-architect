# Research Finding Dossier — the deliverable template

The named work product of this skill (SKILL Step 1). Copy this structure, fill it for the actual
question, write it to a file, return the path + a 2–3 line summary. **Do not** dump the whole dossier
inline. Two different questions must yield two genuinely different dossiers — this is a scaffold, not a
fill-in-the-blank that produces interchangeable output.

Keep claims and evidence unmixed throughout (`../../../references/_core/canon-vocab.md` §evidence
discipline). Demonstrate rigor; don't narrate your own conformance ("here I place the stop-line, per the
kernel") — let the artifact hold together and the rigor be inferred.

---

## 0. Question & framing
- **The research question**, in one line.
- **Triage (the worth-knowing call starts here):** is this an **in-paradigm nearest-neighbour gap** (→
  batch to agents) or **paradigm-level** (change variable/level/framing → human writes direction +
  falsification conditions first)? State which, and for the paradigm-level part, the direction and the
  falsification condition you set.
- **Redraw-vs-graft line:** one honest sentence — would deleting the AI collapse this into "reading
  faster"? (If yes, you're grafting; fix the loop before proceeding.)
- **Boundary flag** (if any): does the finding feed a high-stakes irreversible human decision (clinical /
  legal / safety)? If so, note that the credibility verdict is reserved to a named human, harder.

## 1. The finding / answer
The actual answer to the question, stated plainly, **at the credibility it has earned** — not louder.
If the honest answer is "the evidence is mixed and here is the disposition," say that. Lead with the
finding; the ledger backs it.

## 2. Credibility ledger
A table; **claim and evidence in separate columns, never fused.** One row per load-bearing claim.

| # | Claim (unmixed) | Evidence + measurement basis | Evidence grade Ⅰ–Ⅴ | Paradigm distance (near/far) | Disposition | Replication routing | Signed verdict |
|---|---|---|---|---|---|---|---|
| 1 | … | … (note register: primary / observational / model-predicted / self-reported) | Ⅱ | near | vouch · integrate | replicates | **vouch** (human) |
| 2 | … | … | Ⅴ | far | ★ suspend + targeted evidence-seeking | n/a | **withhold → re-open-question edge** |

Disposition rules (`credibility-ledger.md`): strong×near → vouch·integrate; weak×near → doubt·noise;
strong×far → human looks hard (likely re-framing); **weak×far → suspend + targeted evidence-seeking,
never delete.** Every non-vouch verdict ends in a **named** home (caveated-finding §4 / refutation-base /
re-open-question edge), never a silent stall. The final **vouch / vouch-with-caveats / withhold** verdict
is **signed by the human**, not drafted by the score — this is the stop-line.

## 3. Knowledge-graph contribution (what was written back — ③ feed)
Concrete nodes/edges, not prose:
- **New nodes:** claims / sources added (with IDs).
- **Evidence edges:** claim → source/raw-data, by row.
- **Conflict edges:** any claim raised as contradicting an existing node (the falsifiable property — a
  real edge, not silence).
- **Touched/updated** existing nodes.

## 4. Blind-spot register
What the guardrail/scope locked out, and what to watch — so the next pass inherits the gap:
- **What this finding does not cover** (scope edge, excluded populations/regimes, the description level
  not questioned).
- **Where a claim that failed to replicate revealed a gap** → the **new eval** spawned for it.
- **Candidate-set narrowing risk:** did the generation layer's conservative bias likely under-supply
  paradigm-level candidates? Note what was *not* generated.
- **Leading indicators** to re-check (e.g. does a far-from-paradigm claim gain or lose support next pass).

## 5. The two reserved human verdicts
- **Final credibility verdict** — "what I am willing to vouch for, at this grade, in this frame."
- **Worth-knowing call** — which finding is worth knowing/pursuing, for whom under which value frame, and
  why (this is constitutive, not a score). If it hands off to value-discovery (innovation) or to a
  direction-owner (org governance), name the seam.

> A scaffold cannot *force* genuine scrutiny — a signed verdict can still be a rubber stamp. So the
> observability layer must surface whether the signer actually engaged the evidence (opened the
> conflicting source, overrode a grade, added a caveat); if it can't show that, treat the verdict as
> unearned.

## 6. Future-trajectory (2–3 lines — `../../../references/_core/kernel.md`)
How this compounds as the curves advance — the evidence base deepens into a moat; cheaper models widen the
generation/triage layer; the conflict-detection and replication rules accumulate so the next pass
self-corrects — and what must stay un-frozen: a live replication gate, a human-held worth-knowing node,
real human-interaction signal as the anti-homogenization reservoir.
