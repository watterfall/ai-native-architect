# Verification — the load-bearing wall

Once generation is abundant, **verification is the one load-bearing wall** of the build. "Is it correct?" can
no longer return to a human head reading line by line — that head cannot keep pace with generation. So the
verification suite is not QA hygiene; it is the structural member the whole build hangs from.

## The verifiability gradient — where judgment forks

Lay every correctness question on a spectrum by *how externalizable its criterion is*:

| segment | criterion | who decides |
|---|---|---|
| **flow-checked** | a deterministic program returns correct/incorrect on the spot (types, compile, lint) | machine |
| **test-decidable** | behavior checked against fixed assertions, re-run by machine | machine |
| **eval-decidable** | semantic review needing a **separately-manufactured** independent criterion | machine (with a human-built rubric) |
| **human-only-decidable** | architectural trade-offs, naming, "does this even *count* as correct" — no external criterion exists; the criterion *is* the judgment | human |

**The fork rule reads straight off this:** wherever on the spectrum the criterion can be **externalized into a
definite check that does not pass through the generating model's "feeling,"** it joins automation (this is the
*independent verifier*). Wherever the criterion cannot be externalized and must be supplied by a human on the
spot, it stays with people. So "judgment retreats" is a concrete operation, not a slogan: move left-to-right
along the gradient, hand each machine-checkable segment to the machine, until what remains is the residue
where a human must still *set the criterion*. **That residue is the engineer's real job.**

## Independent verifier — why "independent" is the whole point

The verifier that gates an action must be **separate from the model that produced the action.** A model
grading its own output inherits its own blind spots — confident-wrongness passes its own review. Forms:
- a **deterministic program** (a parser, a schema validator, a property test) that returns correct/incorrect
  without consulting the generator;
- an **eval with a separately-manufactured criterion** — a rubric or gold set a *human* authored, run by a
  judge that did not generate the candidate.

This is what lets you trust abundant output **without reading all of it** — the economic precondition for
abundant generation to actually pay off.

## The eval suite is frozen judgment — and it compounds

When a human notices a defect once ("Chinese punctuation leaking into an English UI looks bad") and encodes it
as a check, a **state change** happens: the judgment moves from "living in one QA's head, re-invoked each
time" to "living in the suite, reused automatically." The eval suite is therefore a **compounding asset**:

> regressions blocked = runs-per-day × potential-regressions-caught-per-run

— a number that *rises with team capacity* at near-zero marginal cost. This is the exact inverse of the
patch-by-hand curve, whose cost rises linearly with capacity while its benefit never accrues. The machine
enforces the standard a million times cheaply; it will never *set* the standard for you — the standard is
always a product of human taste and context. So an eval's value is not automation per se but how it
**amplifies one scarce human judgment into unbounded cheap machine enforcement.**

## Build verification into every node, not at the end

The mechanical fix that the whole surface insists on: change verification from a late "end station" to a
**built-in checkpoint at every node.** Under abundant generation the front of the line (generation) gains an
order of magnitude of throughput; an end-of-line human-QA station does not; unverified work-in-progress
explodes between them. Worse, the **snowball**: an early unverified error is amplified as a settled premise by
every later step — deferring verification to the end lets the error roll twenty steps before discovery, and
late correction is the most expensive kind. A checkpointed trajectory resets a small error to near-zero while
it is still small; an un-checkpointed one lets it grow exponentially. QA is not a department at the end of the
line — it is the independent verifier woven into every loop. **Quality is not detected at the end; it is
locked in at every step by locking intent.**

[Source: this volume's verification + failure sheets, with the verifiability-gradient derivation (a grade-Ⅴ
inference) and "eval = accumulated judgment" (grade Ⅳ). The METR RCT (arXiv:2507.09089) is a single study on
16 senior maintainers — directional, do not extrapolate to greenfield.]
