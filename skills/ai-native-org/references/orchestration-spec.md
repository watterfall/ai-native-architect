# Orchestration spec — running the fleet

The architect drew the workflow graph (nodes, edges, joins, gates). The orchestration spec is how
that graph *runs* — the agent fleet that does the abundant execution, and the thin human layer that
steers it. The shift the canon insists on: the operator is an **orchestrator of agents**, not a
**manager of people**. This is not a vibe; it is structural. Coordination overhead grows as
headcount² (B.05) — adding human coordinators makes the org slower, not faster — so a native org
scales capability by adding *agents and context*, not by adding people to coordinate (essence
property 3: capability decoupled from headcount).

## 1. Name the fleet by role (what each agent class is *a worker for*)

List the agent classes operating the core loop. Name each as a **worker doing a slice of the
graph**, not as a tool in a stack. For each: what it consumes, what it produces, where its output
goes (next agent / a join / a human gate / a context store). Typical classes (adapt to the org):

| class | does the abundant work of | output goes to |
|---|---|---|
| **generation** | drafting / producing candidates / first-pass artifacts | a transform agent or a join |
| **transformation** | reformatting, translating, enriching, normalizing | next stage or context store |
| **traversal / retrieval** | sweeping a corpus, gathering, cross-referencing | a synthesis agent |
| **synthesis** | merging parallel outputs into one coherent result | a join → delivery or a human gate |
| **monitoring** | watching runs, flagging anomalies, scoring against evals | the observability layer / review queue |

The monitoring class matters most for safe operation: it is the agent layer feeding the
observability layer, which in turn feeds the human gates. An org with generation agents but no
monitoring agents is flying blind.

## 2. Dispatch and reconverge — make the graph's joins actually run

The graph's parallel fan-outs are where AI's leverage lives (break the serial chain B.01). But
**every fan-out must reconverge at an explicit join** before any delivery or irreversible step.
Operating discipline:

- **Dispatch** is scoped, not open-ended: each agent gets a bounded task, the context it needs, and
  a definition of done. An agent dispatched with the whole problem and no scope is how you get drift.
- **Reconvergence is a real join node with a wait-set** — the orchestrator (or an orchestration
  runtime) holds the item until *all required* branches return, then advances. You do not invent
  joins the architecture lacks; you make the architecture's joins *fire correctly at runtime*. A
  join that releases on the first branch to finish lets a case complete with half its work floating.
- **Judgment fan-outs join too:** when an item needs more than one human ruling (e.g. two
  reviewers), the join waits for *all* required verdicts before the gate fires — don't trigger on
  the first verdict to arrive.

If you find a fan-out in operation with **no** join in the graph, that's a design defect — surface
it to the architect; don't paper over it with a manual "I'll just check it myself" step (that
silently puts a human on the edge and re-grows the approval chain).

## 3. The orchestrator's own operating loop

What the human (or lead) orchestrator actually does each cycle — this *is* the human role in a
native org, and it is deliberately *not* "approve every step":

1. **Scope & dispatch** — frame the cycle's work, dispatch it to the fleet with context + done-defs.
2. **Watch the queue** — monitor the review queue and observability signals; the default is *no
   touch* (most items never escalate). Attention goes to what surfaced, not to every item.
3. **Clear escalations** — rule on the items that escalated to your node (per the review-queue
   routing). This is the scarce judgment work; protect time for it.
4. **Write context back** — ensure the cycle's decisions, evals, and lessons landed in the context
   stores (this is part of "done", not a separate chore — see `context-upkeep.md`).
5. **Tune the fleet** — adjust scopes, prompts, evals, and dispatch rules based on what the cycle
   taught. This is where the org *improves itself* (essence property 4).

## 4. Size to the org — don't over-build the control plane

The orchestration spec must match the org's real capability and size (the canon's over-engineering
trap):

- **N=1 / tiny:** the fleet is a handful of agents driven from a terminal or a light orchestration
  runtime; "joins" may be the operator's own checklist; the context store may be a structured repo
  of decision logs. Don't specify a multi-agent control plane a solo operator can't run.
- **Larger:** an orchestration runtime, explicit join/queue infrastructure, dedicated monitoring
  agents, an on-call rotation for the human nodes.

The test is the same at every size: *could you switch off the agents and have the same org?* If yes,
the fleet isn't the default worker and you have a graft, not a native org to orchestrate.

## Feeds (what this step writes back)
- The **fleet roster + dispatch rules** are themselves versioned context (workflow-as-code, Pillar
  02) — they live in the repo, not in the operator's head, so a new operator or a new agent onboards
  in days, not months.
- Each cycle's scope/dispatch decisions `feed:` the decision log; tuning changes `feed:` the eval
  suite and the prompt/scope definitions.
