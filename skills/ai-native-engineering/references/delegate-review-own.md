# Delegate · Review · Own — the three-tier division of labor

Route every unit of work into one of three tiers. The tier is set by *where the work sits on the
verifiability gradient* (`verification.md`) and *its blast radius* (`judgment-nodes.md`) — not by how
important it feels. Getting the routing right is what keeps judgment scarce instead of diffuse.

## The three tiers

### Delegate — fully agent-run, gated by structure
The agent does it end-to-end; the **human is not in the loop.** Trust comes from *structure*, not
supervision: types, tests, lint, an independent verifier return correct/incorrect automatically. Use for
machine-checkable, low-blast-radius work: boilerplate, mechanical refactors, codegen from a spec, test
scaffolding, format/style, dependency bumps behind a green test suite.
*Routing a human into this tier is a failure mode* — it reintroduces the bottleneck and burns the scarce
attention you need for the Own tier (vigilance decay).

### Review — agent does it, human reviews the *diff and the seams*
The agent produces the work; a human checks it — but **not line by line.** Reviewing every generated line by
hand *is the bottleneck reappearing as a human verifier*, the position that fails under abundance. Instead:
- **Review the diff, not the artifact** — what changed and why, against the spec.
- **Review the seams** — interfaces, contracts, the boundaries between modules, where a local-optimal guess
  becomes a global debt.
- **Move the gate toward a test** — every time review catches something, encode it as a check so next time
  it's Delegate-tier (this is the Learn write-back; it *moves work down a tier* permanently).
- The human **takes over only where the structure flags red** — a failing eval, a risky seam, a
  near-threshold case.

### Own — the human does the judgment; cannot be delegated
The constitutive calls where no external criterion exists — the human *is* the criterion. Architecture and
module boundaries, the "does this count as correct at all" calls, naming that encodes a domain model, the
spec's intent and non-goals, and **sign-off on every irreversible/adverse action** (`judgment-nodes.md`).
This tier is the engineer's real job in 2030: not implementing, but **holding intent, constraints, and
verification.**

## From implementer to orchestrator — the three the human keeps

The role shift this formalizes: the engineer goes from **implementer** (writes every line) to **orchestrator**
— and an orchestrator is *not* "a manager of agents." It is the person who holds the three things an agent
cannot hold for you:

1. **Intent** — what you want, why, and what you *don't* want. This is the direction of generation; write it
   wrong and the agent efficiently builds the wrong thing.
2. **Constraints** — architecture, standards, non-goals. This is the boundary of generation; absent it, the
   agent guesses at every fork, and a guessed local optimum is often a global debt.
3. **Verification** — tests, review, quality gates. This is the criterion of generation; absent it, "is it
   correct?" returns to the human head that cannot keep pace.

These map precisely onto the kernel's ② judgment and ④ people: the orchestrator lifts judgment *up* from
implementation detail to the three constitutive nodes. Everything below those nodes Delegates.

## How to decide the tier (quick test)

- Can a definite check (that doesn't consult the generating model) decide it? → **Delegate**.
- Needs a human eye but the criterion is mostly externalizable to a diff/seam review? → **Review** (and try
  to push it to Delegate over time).
- Is the criterion itself a judgment only a human can set, *or* is the action irreversible/high-radius? →
  **Own**.

[Source: this volume's delegation + boundaries sheets and Graziano, AI-Native Engineering (Delegate/Review/Own;
implementer→orchestrator).]
