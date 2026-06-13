# Validation — the multi-role council review

The skill was not vibe-checked into existence. It was built and hardened against an **adversarial
multi-role "council"**: independent expert lenses score randomly generated design cases under strict,
no-inflation calibration, and the skill is iterated until the council mean clears the bar with margin.
This document is the track record.

## Why this method

Subjective deliverables (an org design) resist a single grader. So the system uses **perspective
diversity** instead: each reviewer judges only from one lens and is told to find the single biggest
weakness even when scoring high. A design that satisfies a methodology purist, a skeptical operator, an
organizational economist, an AI systems architect, an ethics-and-safety realist, a change-and-adoption
realist, a finance analyst, a compliance lawyer, a strategy-and-moat analyst, and a beneficiary advocate
*simultaneously* is hard to fool. The cases are generated randomly (and blind to the skill internals) to
prevent overfitting.

Calibration anchor used throughout: **10 = flawless · 9 = excellent · 8.5 = clearly strong, minor gaps ·
7 = solid but real weaknesses · 5 = mediocre.** Reviewers were explicitly told not to inflate and to
reserve 9+ for genuinely exceptional work.

## Track record

| Milestone | Cases | Panel | Result |
|---|---|---|---|
| 1 · pass the bar | funeral group; seed-potato lab | 5 roles | **8.62 / 8.58** (bar: ≥ 8.5) |
| 2 · depth deficit found and fixed | battery-teardown; commercial laundry; poison-control | 10 roles | 8.42 → added 9 conditional depth modules → weakest case lifted 5.5 → 8.2 on its low lenses |
| 3a · kernel deepened | offshore-wind decommissioning; CME accreditation; Andean seed-bank | 10 roles | 8.42 baseline |
| 3b · de-scaffold + 9 module upgrades | same three | 10 roles | **mean 9.00** (wind 9.10 / CME 8.95 / seed-bank 8.95) |

### The latest run (mean 9.00 / 10)

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

## What each iteration taught the skill (the durable lessons)

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

## Honest limits

A 9.0/10 council mean means ten strict lenses found the work strong, not that any given real-world build
will succeed. That is why every blueprint ships its own **falsifiable risks** and a **Phase-1 test** of
the assumption most likely to be wrong: the design must be tested against reality, not against reviewers.

## Reproducing it

The validation harness is a council of subagents (one per lens), each handed the case brief and the
skill's output and asked for a calibrated score plus the single biggest weakness. Aggregate the means,
read the systemic weaknesses, fold the generalizable ones back into the skill, regenerate fresh cases,
and repeat until the mean clears the bar with margin. Contributions that add validated example blueprints
(with their council scores) to `examples/` are especially welcome.
