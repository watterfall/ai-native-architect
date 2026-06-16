# Failure modes — and the defense each maps to

Two boundary errors frame all of these: **do not mistake throughput for success, and do not mistake
supervision for verification.** A build that ships fast and watches the agent closely can still be wrong on
both counts — fast at producing unverified work, and "supervised" by a human who reads but doesn't actually
*check*. The taxonomy below recurs in agentic builds; each failure maps to a defense already in the loop, so
treat the loop's steps as the antidotes, not as ceremony.

## The taxonomy

- **Hallucination** — the agent invents an API, a fact, a file that doesn't exist.
  *Defense:* flow-checked + test-decidable verification at the node (it won't compile / the test fails);
  read-only-by-default so a hallucinated action can't mutate state.

- **Confident-wrongness (synthetic confidence)** — output that *reads* right, is fluent and plausible, and is
  wrong. The dangerous one, because it slips past a tired reviewer. The empirical gauge: senior open-source
  maintainers measured **~19% slower** with AI while *feeling* **~20% faster** (METR RCT, arXiv:2507.09089 —
  one study, 16 people, do not extrapolate to greenfield). The felt-speed/real-speed gap *is* synthetic
  confidence.
  *Defense:* an **independent** verifier whose criterion does not pass through the generating model's
  "feeling" (`verification.md`); Review the diff + seams, not the fluent prose.

- **Snowball** — an early unverified error is amplified as a settled premise by every later step, so it rolls
  twenty steps before discovery and costs the most to fix late.
  *Defense:* verification as a **built-in checkpoint at every node**, never a late QA station — reset small
  errors to near-zero before they grow.

- **Context-rot** — accuracy is non-monotonic in context length; cramming more in past the peak *lowers*
  accuracy.
  *Defense:* retrieval-style assembly of the **right small subset** into the window (`loop-and-planning.md`);
  a queryable codebase over a dumped one.

- **Hidden assumptions** — the agent silently guesses at an unspecified fork, and the guessed local optimum
  becomes a global debt.
  *Defense:* a spec at the right rung with explicit **non-goals** (`spec-driven.md`); when the agent reaches
  an unspecified fork, treat it as a missing spec clause and amend, don't let it guess.

## The deeper pattern — old structures that invert after abundance

Several "best practices" were correct optimizations for *scarce execution* and become **obstacles** once the
constraint inverts. Recognizing them is half of avoiding the failure:

- **Waterfall / BDUF, per-step approval** → under abundance becomes approval-density that causes **vigilance
  decay** (`judgment-nodes.md`). Fix: JIT planning + tiered gates.
- **Review-as-gatekeeping, QA-at-the-end** → becomes the end-station bottleneck + snowball. Fix: verification
  woven into every node.
- **The "10x developer" myth / ticket factory** → measures *implementation/typing throughput*, the very thing
  agentic coding cheapens; optimizing it optimizes the wrong variable. (The "10x" figure traces to
  Sackman et al. 1968 — coding-time spreads ~20:1 — but in that same data output did **not** correlate with
  experience, and the method was flawed.) Fix: optimize judgment throughput, not typing throughput.

These structures were not stupid — they were right *when execution was scarce*. Their shared failure
mechanism is that an optimization for the old bottleneck becomes a blockage in front of the new one. The point
of naming them is to recognize which of your own habits have passed their expiry.

[Source: this volume's failure-modes sheet (the twin-curve checkpoint figure; the constraint-inversion figure)
and Graziano, AI-Native Engineering (the failure-mode taxonomy: hallucination / confident-wrongness / snowball
/ context-rot / hidden assumptions). METR arXiv:2507.09089 and Sackman et al. (CACM, 1968) are directional
anchors, not laws.]
