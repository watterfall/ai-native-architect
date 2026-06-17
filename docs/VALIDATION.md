# Validation — the multi-role council review

Neither tier was vibe-checked into existence. Both were built and hardened against an **adversarial
multi-role "council"**: independent expert lenses score work under strict, no-inflation calibration, and
the skill is iterated until the council clears the bar with margin. This document is the track record for
the whole system — the **architecture tier** (`ai-native-architect`) and the six **execution-tier**
skills added in v2.0.0.

## Why this method

Subjective deliverables (an org design, a research finding, a design artifact) resist a single grader. So
the system uses **perspective diversity** instead: each reviewer judges only from one lens and is told to
find the single biggest weakness even when scoring high. Work that satisfies a methodology purist, a
skeptical operator, a domain expert, and a human-boundary realist *simultaneously* is hard to fool. Cases
and tasks are generated to be blind to the skill internals to prevent overfitting.

Calibration anchor used throughout: **10 = flawless · 9 = excellent · 8.5 = clearly strong, minor gaps ·
7 = solid but real weaknesses · 5 = mediocre.** Reviewers were explicitly told not to inflate and to
reserve 9+ for genuinely exceptional work.

## Architecture tier — `ai-native-architect`

This tier's record stands from the v1 line and is unchanged by the v2 expansion (the architect's function
is unchanged; it now references the shared `_core` kernel).

### Track record

| Milestone | Cases | Panel | Result |
|---|---|---|---|
| 1 · pass the bar | funeral group; seed-potato lab | 5 roles | **8.62 / 8.58** (bar: ≥ 8.5) |
| 2 · depth deficit found and fixed | battery-teardown; commercial laundry; poison-control | 10 roles | 8.42 → added 9 conditional depth modules → weakest case lifted 5.5 → 8.2 on its low lenses |
| 3a · kernel deepened | offshore-wind decommissioning; CME accreditation; Andean seed-bank | 10 roles | 8.42 baseline |
| 3b · de-scaffold + 9 module upgrades | same three | 10 roles | **mean 9.00** (wind 9.10 / CME 8.95 / seed-bank 8.95) |

### The latest architecture run (mean 9.00 / 10, 10 roles)

| Reviewer lens | Wind | CME | Seed-bank |
|---|---|---|---|
| methodology purist | 9.0 | 8.5 | 8.5 |
| skeptical operator | 9.5 | 9.5 | 9.0 |
| organizational economist | 9.0 | 9.5 | 9.0 |
| AI systems architect | 9.5 | 9.5 | 9.5 |
| ethics & safety realist | 9.5 | 9.0 | 9.5 |
| change & adoption realist | 8.0 | 9.0 | 9.0 |
| finance / unit-economics | 9.5 | 8.5 | 8.0 |
| risk / compliance / legal | 9.0 | 8.5 | 9.0 |
| strategy / moat | 9.0 | 9.0 | 8.5 |
| beneficiary advocate | 9.0 | 8.5 | 9.5 |
| **mean** | **9.10** | **8.95** | **8.95** |

### What each iteration taught the architect (the durable lessons)

Every score gain came from a **generalizable** fix folded back into the skill, never a per-case tweak:

- **Economics must compute, not template.** Size the opportunity from the brief's own numbers, no
  placeholder algebra, recompute headlines inline so they tie out, anchor inputs externally, band the
  two most fragile inputs, and name the one input whose error flips the recommendation.
- **The workflow graph must run.** Joins are first-class nodes with wait-sets; multi-input gates declare
  a `join_policy`; and every human / community "no" terminates in a named node instead of silently
  deadlocking an `all`-join.
- **Beyond the prevention gate.** Trace harm to the *last human harmed* (the patient, the crew, the
  household), not the institutional counterparty; name the operative legal *instrument* (the SMTA, the
  engagement-letter reliability cap, the accreditation standard), not just the regime.
- **Adoption is engineered, not assumed.** A real tacit-capture workflow, incentive and political design
  for the people asked to externalize their leverage, and cooperation telemetry that detects
  disengagement *before* the knowledge walks.
- **Demonstrate rigor, don't attest it.** The biggest single lever: stop narrating conformance and let
  the design carry the rigor. This made each blueprint read as bespoke rather than as a filled template.

---

## Execution tier — the six skills (v2.0.0)

The six execution skills were validated against the shared **5-role council** in
[`references/_core/council.md`](../references/_core/council.md). Each skill is scored from five lenses
tuned to the execution layer:

- **kernel-fidelity** — does it honor the scarcity inversion and the shared kernel?
- **domain-expertise** — is the work good *as engineering / design / research / etc.*?
- **skeptic / collapse-to-enablement** — would this collapse back to AI-enablement, or to re-designing
  the org instead of doing the work? (the redraw-vs-graft and altitude test)
- **operability** — can someone actually run this and get the work product?
- **human-boundary** — is the stop-line — what is never offloaded — named and held?

**Bar: mean ≥ 8.5 AND no dimension below 8.0.** All six skills pass.

| Skill | Council mean | Lowest dimension | Verdict |
|---|---|---|---|
| `ai-native-engineering` | **9.00** | ≥ 8.0 | PASS |
| `ai-native-design` | **8.80** | ≥ 8.0 | PASS |
| `ai-native-research` | **8.80** | ≥ 8.0 | PASS |
| `ai-native-learning` | **9.00** | ≥ 8.0 | PASS |
| `ai-native-innovation` | **9.00** | ≥ 8.0 | PASS |
| `ai-native-org` | **9.00** | ≥ 8.0 | PASS |

No skill fell below 8.0 on any dimension — the council's secondary floor, which catches a high mean that
hides one weak lens.

### Lightweight quantitative eval (with-skill vs baseline)

Alongside the qualitative council, each execution skill ran one lightweight quantitative eval — the same
real task done **with the skill** and as a **baseline** (no skill). See
[`skills-eval-workspace/iteration-1/BENCHMARK.md`](../skills-eval-workspace/iteration-1/BENCHMARK.md) for
the per-surface detail. Four deltas showed up in **6/6** with-skill runs and were largely **absent** in
the baselines:

1. **Stays at the execution layer.** The skill produces the actual work product. Baseline engineering
   (and partly org) drifted to a *design / blueprint* — the architect's altitude, not the builder's. The
   skill keeps you *doing*, not re-designing.
2. **The adverse / negative path designed with equal care.** The single most common "the skill made me do
   this" across all six: gate the wrongful *no* (the denied refund, the denied customer, the suspended
   weak-but-real claim), not just the positive action. Baselines secured the happy path only.
3. **Compounding context as *real artifacts*.** Named decision logs, conflict edges, reflection stores
   with a named read-back edge — not implicit prose. Baselines left the compounding implicit.
4. **The scarce judgment node + stop-line named explicitly.** With-skill always named the one human node
   and what is *never* offloaded; baselines diffused it.

Per-surface highlights of what the skill forced over an already-strong baseline:

- **engineering** — kept it a *build* (runnable handler + SPEC + eval suite + JUDGMENT + PERMISSIONS) and
  froze the recurring bug as a new eval, rather than drifting into an architecture blueprint.
- **research** — split the paradigm *before* grading (human-lifespan vs mouse/biomarker) so abundant
  evidence can't answer the wrong question; a weak × far claim is **suspended, not deleted**.
- **learning** — reframed abundant execution as the *temptation* and applied the *constitutiveness*
  criterion to keep the borrow-checker struggle human; a reflection store with a named read-back.
- **org** — gated the adverse "no" as its own irreversible action and held the stop-line **under SLA
  pressure** (escalate up, never auto-resolve); context-rot split into three named feeds.
- **design** — a genuinely divergent 5-spread (including the SaaS-mean generated only to reject as a
  foil), a 指纹 fingerprint check, and soft axes kept *out* of the lint.
- **innovation** — **falsify before polish**: flagged inflated ideas on the *viable-path* axis rather
  than ranking polished one-pagers; the bet stays human, with who-pays on the same row.

**Conclusion of the lightweight pass:** over a strong baseline, the skills add consistent, real
discipline — most decisively by keeping work at the execution layer and designing the adverse path +
compounding context. No skill regressed below baseline on any task. The lightweight pass **supports** the
adversarial council PASS (means 8.8–9.0).

---

## Honest limits

A high council mean means strict lenses found the work strong, not that any given real-world build will
succeed. That is why every architecture blueprint ships its own **falsifiable risks** and a **Phase-1
test** of the assumption most likely to be wrong, and every execution work product ships its own
verification — the eval suite, the credibility ledger Ⅰ–Ⅴ, the 指纹 check, the reflection read-back. The
work must be tested against reality, not against reviewers. The lightweight quantitative eval is
**iteration 1, one eval per skill** — a corroborating signal, not a saturated benchmark; deeper coverage
is on the roadmap.

## Reproducing it

The validation harness is a council of subagents (one per lens), each handed the case brief / task and
the skill's output and asked for a calibrated score plus the single biggest weakness. Aggregate the
means, read the systemic weaknesses, fold the generalizable ones back into the skill (or into shared
`_core` when the lesson is kernel-level), regenerate fresh cases / tasks, and repeat until the means clear
the bar with margin. The execution-tier lightweight eval re-runs each task with and without the skill and
diffs the result. Contributions that add validated example work products (with their council scores) to
`examples/` are especially welcome.
