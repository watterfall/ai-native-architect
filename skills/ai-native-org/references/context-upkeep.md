# Context-upkeep — operate against rot, compound the asset

Context is the org's compounding core asset (essence property 2; T1's second structure: *the flow of
context*). It is what makes the agents *yours* rather than generic. But context behaves the opposite
of a tool: a tool degrades when unused, context degrades when **un-maintained** — and a native org
runs *on* its context, so rot is a production incident, not a tidiness issue. Context-upkeep is the
operating practice that keeps context compounding instead of decaying.

The canon's pillar: **context engineering as a system practice** (M.03 + Pillar 03). Knowledge only
*exists* once it's in a machine-readable store; decisions are stored with their rationale; processes
self-document as code (Pillar 02, workflow-as-code); agent execution traces deposit automatically
into organizational memory. The payoff: onboarding for new humans *and new agents* drops from months
to days. The operating job is to keep that true under daily pressure.

## 1. Write-back is part of "done" (not a separate chore)

The single most important habit. A work item is **not done when the artifact ships** — it's done
when:

- the **decision + its rationale** is in the decision log (not just the *what*, the *why* — so a
  future agent or human can tell whether the decision still applies);
- the **eval result** is recorded (did it pass the suite? which evals?);
- any **lesson** (a failure, a near-miss, a better approach) is written where the next pass reads it
  (knowledge-graph edge, postmortem note, updated prompt/scope).

If write-back is optional, it doesn't happen — throughput pressure always wins. So wire it into the
definition of done: an item the orchestrator can't see written-back isn't cleared. The monitoring
agents can draft the write-back; the human confirms it's true. (This is itself the four-step loop:
abundant drafting by agents, the scarce *is-this-actually-true* judgment by the human.)

## 2. The context-debt test (M.03) — the early-warning instrument

Run this on a cadence (tight or deliberate band):

> **Which single person leaving would paralyze some piece of work for more than a week?**

Whatever is in that person's head is **context-engineering debt** — and the canon's discipline is
that *every item of it can be named and listed*. Each named item is a capture task: elicit it,
write it to the store, verify an agent can act on it. A growing debt list is the clearest signal an
org is **silently de-nativizing** — knowledge re-accumulating in heads (the old form), agents
becoming generic again. Watch the trend, not just the snapshot.

## 3. Freshness — accumulation is not upkeep

Stale context is *worse* than missing context: an agent acts on it with full confidence. So upkeep
is not "write more," it's "keep it true":

- **Prune / flag the outdated.** When a decision is superseded, mark it — don't leave two
  contradictory entries for an agent to pick from. A store that only grows eventually poisons the
  fleet.
- **Re-run evals when the substrate changes.** Treat a model-layer swap as a **regression test the
  eval suite must pass** (Multi-Model pillar: switching models is a regression test, not a rewrite —
  and not a silent quality cliff). The proprietary eval suite is what makes the swap safe; if you
  can't swap models without flying blind, you have *algorithmic-feudalism* exposure (the deepest
  single risk: one provider becomes your landlord).
- **Tie freshness to the cadence.** The tight loop checks the debt test and eval drift; the
  deliberate band reviews whether the context *model* (what's worth storing) still fits the org.

## 4. Where context lives (operate all of it)

The context layer of the substrate: **knowledge graph / decision log / organizational memory** (the
machine-readable store the agents retrieve from). Operating it means:

- every store has a **writer** (who/what deposits) and a **reader** (who/what retrieves) named — a
  store nothing reads back is dead weight; a store nothing writes to is already stale;
- traces deposit automatically (don't rely on humans to log what the agent layer can emit);
- the store is versioned alongside the workflow code, so context and process evolve together.

## Feeds (the upkeep loop itself compounds)
- The debt list `feeds:` the capture backlog; closing a debt item `feeds:` the store and *removes a
  single point of failure* — the org gets structurally more resilient each cycle.
- Eval-on-swap results `feed:` the model-layer decision (which provider, when to switch) and the
  observability layer (quality baselines).
- This is the loop that makes the org's *second year structurally smarter than its first*: context
  compounds, onboarding shrinks, the fleet gets more *yours* — none of which a graft can do, because
  a graft keeps its knowledge in heads and chat.
