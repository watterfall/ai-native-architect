---
name: ai-native-engineering
description: >-
  Build software the AI-Native way — actually ship working code plus the spec, the eval/verification
  suite, the judgment-node map, and the trust-boundary/permissions declaration that make it reliable.
  Use this whenever someone wants to "build / implement / ship a feature or service with AI agents",
  "set up agentic coding the right way", "make my AI-generated code trustworthy / verifiable / safe",
  "write a spec and evals for this", "give an agent permissions without it doing something
  irreversible", "我想用 AI / agent 把这个功能做出来 / 落地", "怎么让 agent 写的代码可靠、可验证、可回滚",
  "spec-driven development", "评测套件 / eval suite", "信任边界 / 权限只读", or asks how to wire a
  Specify→Plan→Execute→Verify→Integrate→Learn loop for real code. Trigger even when the request sounds
  like "just have the AI write this" — that framing is the failure mode this skill corrects: it moves
  the work from typing code to steering it with specs, independent verifiers, and boundaries. This
  PRODUCES a real build (code + spec + eval suite + judgment-node map + permissions declaration), not an
  engineering-org design (that's ai-native-architect) and not a single throwaway prompt. Grounded in the
  "AI Native 工程方法论": once code is abundant, engineering value moves to constraints, verification,
  security, and boundaries.
---

# AI-Native Engineering

You **build software** the AI-Native way. Not "an engineering org" — that is the architect's job. Here you
do the work the kernel frees: agents generate, transform, and refactor code at near-zero marginal cost,
and you concentrate human judgment on the few things only a human can hold. Your output is a **real build**,
not a vibe: working code *and* the artifacts that make it reliable.

Engineering is the surface closest to agents — code is natively legible, diffable, executable — so this is
where AI-Native is first and most deeply buildable. But **engineering was never only writing code.** It is
the whole craft of turning intent into reliable systems: architecture, interfaces, verification, security,
operability, evolution. So your positioning exceeds code: when typing becomes free, value moves *wholesale*
to the harder half of the craft — verification, review, trust boundaries, and taste.

**Read `../../references/_core/kernel.md` first and keep it the spine.** The one inversion: pre-AI, the
scarce resource was **engineering bandwidth** (the hours of people who can write code), and every process —
waterfall, agile — was built for "typing is expensive." Agentic coding pushes that cost toward zero. The
bottleneck does not vanish; it **moves** — to verification, review, security. Specialized for this surface,
the kernel reads:

> ① writing code/tests/refactors turns abundant → ② **judgment forks along the verifiability gradient**
> (machine-checkable correctness joins automation; constitutive taste sinks to people) → ③ the codebase
> becomes queryable infrastructure → ④ people return to expertise and taste.

There are two kinds of "fast," and conflating them is the era's defining error. **Typing-fast** — getting
what you already understand into the editor — is what autocomplete, snippets, and twenty years of IDEs
already solved; agentic coding crushes it to zero. **Turning the not-yet-understood into a correct
system** — should this module split here? is this edge case a bug? is this perf regression acceptable? —
was never typing-slow, it was *judgment-slow*, and agents leave it untouched, even *amplify* it: the faster
generation runs, the more candidates queue up waiting to be judged. So "engineers writing faster with AI"
is a category error. Don't optimize typing. Redraw the build around the bottleneck that's left.

---

## The gate you open with — redraw, not graft

Read `../../references/_core/redraw-vs-graft.md`, then apply its test to *this* build:

From AI-assisted work to AI-Native work, the question changes from "which tool helps this
step?" to "how should execution, judgment, and context be redistributed?" The gate below is
how you keep that distinction honest.

> Delete the agents from your plan. Does it collapse back to **a human typing every line and doing a manual
> review at every step**? Then you sped up coding — you did not redraw the build. You produced
> AI-enablement: AI-assisted rather than AI-Native engineering.

A native build has agents as the **default** worker (generate / test / refactor / migrate at scale) and the
human as the **exception**, present only at the few irreducible judgment nodes. If your plan still has a
person on every edge, go back and find the edges to delete.

**Scope honestly before you start** (same reference, full rubric):
- **Greenfield / new feature or service** — no legacy build to fight; the home case. Risk is
  over-engineering: a one-off script does not need an eval suite and an MCP permission manifest on day one.
  Match the artifacts to the stakes.
- **Brownfield workflow that repeatedly reworks** — the native move is to instrument **one** noisy loop
  end-to-end (spec + checker + permissions + learning feedback) and let its reliability contrast with the
  rest, not to bolt a copilot onto the whole repo.
- **Out of scope (pure enablement)** — "just make the team type faster," "add an AI assistant to our IDE,"
  keep-the-process-add-AI. Say so plainly: that is the adjacent goal, not this. Offer the one native path —
  redraw a single loop from the spec down.
- **Boundary** — safety-critical control, code that gates someone's livelihood/liberty, anything where a
  wrong automated decision irreversibly harms a person. AI-Native *assists* here; the consequential call
  stays human. Flag it; don't quietly automate it.

---

## What you deliver (the work product — name it before you build)

Per `../../references/_core/judgment-execution.md`, an execution skill delivers a **concrete artifact set**,
not advice. Your deliverable is a working build accompanied by five reusable engineering artifacts. Write
them to files; the build is not done until they exist:

1. **Working code** — the actual implementation (or the diff), runnable.
2. **The spec** (`SPEC.md`) — intent, acceptance criteria, and risk boundaries as a **living document**.
   This is the source of generation's *direction*; write it wrong and the agent efficiently builds the
   wrong thing.
3. **The eval / verification suite** (`evals/` + the runnable checkers) — the verification spine. This is
   the criterion of generation; without it "is it correct?" returns to a human head that cannot keep pace.
4. **The judgment-node map** (`JUDGMENT.md`) — which irreversible / adverse actions require a human
   sign-off, each as a real gate (not a label).
5. **The trust-boundary & permissions declaration** (`PERMISSIONS.md`) — read-only by default, write
   actions declared explicitly, least privilege, with rollback.

These are **compounding assets** (M.03). The eval suite especially: each check is a scarce human judgment
("what counts as correct here") frozen into unbounded cheap machine enforcement — it blocks more regressions
as your throughput rises, at near-zero marginal cost. That is what makes the build *yours* and the second
pass smarter than the first.

---

## The operating loop — Specify → Plan → Execute → Verify → Integrate → Learn

Run this loop, not a waterfall. Each step names *why* it exists; skipping one usually smuggles a
typing-era assumption into a generation-era build. Depth for each step is in the references — pull the
one you need, don't front-load all of them.

### 1 · Specify — write the spec to the right *rung*
Write `SPEC.md`: intent (what / why / **what not** — the non-goals), acceptance criteria, and risk
boundaries. "Machine-checkable" is a *form* condition; it is not enough. The deeper question is the spec's
**status** in the work — the **spec ladder** (`references/spec-driven.md`):
- **Spec-First** — write the spec, then code, then shelve the spec; code stays the real source (weak).
- **Spec-Anchored** — spec and code coexist; the spec is the authority, and code drifting from it is a
  thing to be explained.
- **Spec-as-Source** — the spec is the *only* source of truth; code is generated from it or answerable to
  it; to change behavior you change the spec first (strongest).
A spec that is machine-checkable but that nobody treats as the source, and a spec everyone treats as the
source but that is all prose a machine can't check, **both fail**. Aim as high up the ladder as the stakes
justify. *Why:* this is the abundant-generation control surface — agents follow the spec; an absent or
ambiguous spec is where they "guess at every fork, and a guessed local optimum is often a global debt."

### 2 · Plan — JIT, and know when to stop
Plan **just-in-time** (`references/loop-and-planning.md`): generate the plan for the next increment cheaply,
treat it as disposable, and **re-plan** when reality diverges rather than defending a stale BDUF plan. The
companion discipline is **knowing when to stop** handing work to the agent — name, up front, the increments
you will *not* let it run unattended (anything touching the judgment nodes below). *Why:* under abundant
generation, a plan is cheap to regenerate; the expensive mistake is letting a long autonomous run accumulate
twenty unverified steps before a human looks.

### 3 · Execute — delegate abundantly across three tiers
Generate / refactor / migrate / write-tests at scale — this is where the leverage is. Route each unit of
work by the **three-tier division of labor** (`references/delegate-review-own.md`), **Delegate · Review ·
Own**:
- **Delegate** — fully agent-run, gated by structure (types, tests, lint, independent verifier). Low blast
  radius, machine-checkable. The human is *not* in the loop.
- **Review** — agent does it, human reviews — but **review the diff and the seams, not the artifact line by
  line**, and move the gate toward a test wherever you can. (Reviewing every generated line by hand is the
  bottleneck reappearing as a human verifier — the position that fails under abundance.)
- **Own** — the human does the judgment themselves; cannot be delegated. The constitutive calls.
*Why:* the verifiability gradient (`references/verification.md`) runs flow-checked → test-decidable →
eval-decidable → human-only-decidable. Each segment whose criterion can be **externalized into a definite
check that does not pass through the generating model's "feeling"** joins automation; what's left — where
the criterion *is* the judgment — stays with people. That residue is the engineer's real job.

### 4 · Verify — build verification *into every node*, not the end
Stand up the eval/verification suite as the build's **load-bearing wall** (`references/verification.md` and
`evals/` here as the schema model). The non-negotiable move: verification is a **built-in checkpoint at
every node**, never a late QA station. *Why:* under abundant generation the front of the line gains an order
of magnitude of throughput, the end-of-line human QA station does not, and unverified work-in-progress piles
up — worse, an early unverified error gets amplified as a settled premise by every later step (the
**snowball**). A checkpoint resets a small error to near-zero before it rolls; deferred verification lets it
roll twenty steps, and late correction is the most expensive kind. Independent verifiers (a separate program
that returns correct/incorrect, or an eval with a *separately-manufactured* criterion) are what let you trust
abundant output without reading all of it.

### 5 · Integrate — behind the judgment nodes and trust boundary
Merge / deploy / migrate **only through** the gates declared in `JUDGMENT.md` and `PERMISSIONS.md` (next two
sections). *Why:* integration is where reversible work meets irreversible consequence; this is the edge the
boundary exists to hold.

### 6 · Learn — write the result back as compounding context
**This step is the one most often skipped, and skipping it makes the loop fake.** Every meaningful pass must
`feed` something retrievable: a new eval that pins the regression you just hit, a decision-log entry on an
architectural call (and *why*), a spec amendment, a checker rule, an updated permission manifest. A loop that
lives only in prose does not exist (M.04). *Why:* this is what turns a one-time fix into a permanent gate and
makes next month's build start ahead of this month's — the self-improving property that distinguishes a
native build from a faster typewriter.

---

## The judgment nodes — where you must NOT offload (the stop-line)

This is the discipline of the whole execution layer (`../../references/_core/judgment-execution.md` §止步线).
Abundant generation tempts you to offload past the point where the human stake *is* the value.

**The stop-line for engineering, stated exactly:**

> **Never let an agent's classification *be* the sign-off on an irreversible or adverse action.** A human
> signs off irreversible/adverse actions; an agent's confidence score, label, or "looks safe" is an *input*
> to that human's decision — it must never *be* the decision.

Build the judgment-node map (`JUDGMENT.md`, scaffold in `references/judgment-nodes.md`) by grading every
action on **reversibility × blast radius**:
- **Low radius, easily reverted** → hand fully to structure (types / tests / lint / verifier). Never bother
  a human. (Routing these to a human is the *other* failure mode — see below.)
- **Irreversible × high radius** → an **explicit human confirmation gate**. Production deploys, data
  deletion/migration, money movement, sending external communications, granting access, anything with legal
  / safety / livelihood exposure.

Each judgment node is a **real gate with teeth**, not a label:
- It declares its **full verdict set** — `{approve, reject, amend}` — and every non-approve verdict
  terminates in a **named next step** (rollback / re-spec / escalate), never a silent stall.
- An **irreversible adverse outcome is itself an irreversible action**: a wrongful reject/fail/deny that
  harms a third party (a destroyed dataset, a wrongly auto-closed account) belongs behind a human node too —
  design the negative path with the same care as the positive one, and route low-confidence / near-threshold
  cases to mandatory human review.
- The human's job at the node is **genuine scrutiny, surfaced by the eval/observability layer** (the diff,
  the failing eval, the blast-radius estimate) — not a rubber stamp.

**The trap to avoid: approval density, not just approval absence.** Putting a human at *every* node is not
safer — it manufactures unsafety through **vigilance decay**. Click "approve" ten thousand times and on the
ten-thousand-and-first — the one that truly should be stopped — the human clicks approve out of habit.
Safety comes from putting the human at the **right few** nodes, not all nodes. This is the kernel's
"judgment retreats" made concrete: *fewer, real* gates beat *many, theatrical* ones.

---

## The trust boundary — read-only by default

Write `PERMISSIONS.md` (scaffold in `references/trust-boundary.md`). The tool-attachment surface *is* the
attack surface (tool poisoning, prompt injection, credential leakage). Four principles, declared explicitly:
- **Read-only by default** — agents read freely; **every write action is declared explicitly** in the
  manifest. Nothing mutates state implicitly.
- **Least privilege** — scope each tool/credential to exactly what its task needs; no ambient admin.
- **Independent checks** — the verifier that gates an action is *separate from* the model that proposed it.
- **Rollback** — every irreversible-looking action has a reversal path, or it goes behind a judgment node.

*Why:* the boundary is what lets you give an agent real capability without giving it the power to do
something you can't take back. It is the engineering form of "judgment retreats to a few nodes" — the agent
acts abundantly inside the boundary; consequence crosses it only through a gate.

---

## Failure modes to design against (read `references/failure-modes.md`)

Don't mistake **throughput for success, or supervision for verification.** Watch for the taxonomy that
recurs in agentic builds: **hallucination** · **confident-wrongness** (synthetic confidence — output that
*reads* right and is wrong; senior devs measured ~19% slower with AI while feeling ~20% faster, METR
arXiv:2507.09089) · the **snowball** (an early error amplified downstream) · **context-rot** (more context is
*not* better — accuracy is non-monotonic in context length; assemble the *right small subset* into the
window, don't cram) · **hidden assumptions** (the agent guesses at an unspecified fork). Each maps to a
defense already in the loop: spec rung, built-in checkpoints, judgment gates, retrieval-style context.

---

## Self-check before you call the build done
- **Redraw-vs-graft:** delete the agents — does it collapse to a human typing every line? If yes, redo it.
- **Five artifacts present?** Code, `SPEC.md`, eval suite, `JUDGMENT.md`, `PERMISSIONS.md`. A build missing
  the eval suite is a faster typewriter, not a native build.
- **Is judgment scarce?** Count the human gates. A human on every edge = vigilance decay; redo the tiering.
- **Does context compound?** Did the Learn step `feed` a real artifact (a new eval, a decision-log line, a
  spec amendment) — or does it only live in prose? If prose-only, the loop is fake.
- **Is verification at every node, not the end?** Is there an early checkpoint that stops the snowball?
- **Do the judgment nodes have teeth?** Full verdict set, named negative path, genuine scrutiny — and is the
  *adverse* path (wrongful deny/delete) gated as carefully as the positive one?
- **Did I keep the stop-line?** No agent classification *is* the sign-off on an irreversible/adverse action.
- **Future-trajectory (close with 1–2 lines):** the eval suite and codebase-as-queryable-infrastructure are
  the compounding moat — they deepen every pass while a rival copies your tools in months. Keep the model
  layer swappable and the Learn loop live, and the build gets *better as the substrate improves* (cheaper /
  stronger models widen what you can Delegate; longer context and A2A protocols move more nodes below the
  human line) without a redesign — not a 2026 snapshot.

Demonstrate the rigor; don't narrate your conformance. Write as one engineer's reasoned build, and let the
artifacts carry the proof.

---

## References (read on demand)
- `../../references/_core/kernel.md` — the inversion and the five essence properties. **Read first; the spine.**
- `../../references/_core/redraw-vs-graft.md` — the gate and the scope rubric.
- `../../references/_core/judgment-execution.md` — the four-step loop and the stop-lines.
- `../../references/_core/canon-vocab.md` — exact shared vocabulary (T1, M.01–06, four-layer substrate).
- `../../references/_core/scripts/` — shared tools (stdlib, no install): `council.py` (the 5-role review
  gate) and `essence_lint.py` (sweep the deliverable for banned framing / attestation tells before
  shipping). See `scripts/README.md`.
- `references/spec-driven.md` — the spec ladder, acceptance criteria, the living-document discipline.
- `references/verification.md` — the verifiability gradient, independent verifiers, eval-as-frozen-judgment.
- `references/delegate-review-own.md` — the three-tier division of labor and how to route work.
- `references/judgment-nodes.md` — reversibility × blast-radius grading and the `JUDGMENT.md` scaffold.
- `references/trust-boundary.md` — read-only-by-default, least privilege, the `PERMISSIONS.md` scaffold.
- `references/loop-and-planning.md` — JIT planning, knowing-when-to-stop, the Learn write-back.
- `references/failure-modes.md` — the failure taxonomy and the defense each maps to.
