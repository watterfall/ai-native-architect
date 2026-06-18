# The validation council — a 5-role adversarial review gate

The system practices what it preaches (M.04 / M.06): quality is not asserted once, it **compounds**
through an instrumented, multi-perspective learning loop. Judgment (the human bar and which weaknesses
to fix) stays scarce and human; the abundant work (running five reviewers, drafting fixes) is done by
agents.

Use this gate two ways:
1. **On a skill** — before publishing or shipping a change to any skill in this system.
2. **On a deliverable** — a skill may run a lighter version of it on its own output as a self-check.

## The five roles (each an independent, strict reviewer)

Spawn each as a separate reviewer with no knowledge of the others' scores. Each scores **0–10** on its
dimension and must justify with specific evidence (quote the artifact), not vibes. Calibrate to a strict
anchor: the canonical org methodology / a top-tier practitioner's work = **10**.

1. **Kernel fidelity** — Does the work embody the kernel (the scarcity inversion; the five essence
   properties: scarce-concentrated judgment, compounding context, capability decoupled from
   headcount/effort, self-improvement, incoherent-without-AI)? Or is it AI-enablement relabeled? Penalize
   any banned framing (means/ends sloganeering, six-surfaces-as-pipeline).
2. **Domain expertise** — Reviewing as a senior practitioner of *this surface* (engineer / designer /
   researcher / educator / innovator / operator): is the domain craft sound, specific, and current — or
   generic filler that any LLM would emit without the skill? Are the named tools/methods real and apt?
3. **Skeptic / collapse-to-enablement** — Adversarial. Try hard to **refute** the AI-native claim: show a
   path where deleting the AI leaves the same old process, where a human is silently on every edge, or
   where "compounding context" is prose with no real feed. Default to *refuted* if uncertain. The work
   survives only if you cannot make the refutation stick.
4. **Operability** — Can a real practitioner actually *run* this and get the stated work product? Are the
   steps executable, the outputs concrete (a file, not a vibe), the trigger description accurate and
   appropriately "pushy"? Is SKILL.md lean (<~500 lines, progressive disclosure, depth in references)?
   Would two different inputs produce two genuinely different outputs (not a template)?
5. **Human boundary** — Did it honor the stop-lines (`judgment-execution.md` §止步线)? Did it avoid
   over-automating the sacred / desirable-difficulty / trust core? Are judgment nodes real gates (full
   verdict set, named negative path, genuine scrutiny — not a rubber stamp)? Is the emotional-labor
   boundary respected and flagged, not over-claimed?

## The bar

> **PASS = mean ≥ 8.5 AND no single dimension < 8.0.**

A dimension < 8.0 blocks regardless of the mean — a fatal hole in one lens is not averaged away by
strength elsewhere. On a FAIL, the council returns the binding weaknesses (the lowest-scoring,
highest-leverage gaps); fix those, then re-run the full panel. Iterate until PASS. Record verdicts
(scores + the one-line rationale per role) so quality is traceable and the loop compounds.

## How to run it (mechanics)

The scaffold and the gate arithmetic are tooled in `scripts/council.py` (stdlib, no install) so the
five role prompts and the PASS/FAIL rule stay identical every run — spend your judgment on the review,
not on re-deriving the harness:

- `python3 scripts/council.py --scaffold <artifact>` prints the five reviewer prompts to dispatch.
- `python3 scripts/council.py <scores.json>` aggregates `{dimension, score, top_fix}` rows into the
  verdict, naming the binding (lowest, gate-blocking) dimensions and their `top_fix`.

- Spawn the five reviewers in parallel (one subagent each), each given the artifact + this file + the
  relevant `_core` files + (for domain expertise) the surface's source page.
- Each returns `{dimension, score, evidence, top_fix}` as structured output.
- Aggregate with `council.py` (it computes the mean, flags any dim < 8.0, and surfaces the binding
  fixes); or do it by hand if you prefer.
- This complements — does not replace — the skill-creator quantitative eval (with-skill vs baseline runs,
  benchmark, viewer). The council is the *qualitative/adversarial* gate; the eval is the *quantitative*
  one. Pass both before publishing.
