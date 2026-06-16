# Review-queue routing — the exception path, with teeth

This is the operating runbook's load-bearing artifact. The architecture *named* the human judgment
nodes; the review queue is the **operating mechanism that gets the right exception to the right
human at the right moment, and refuses to let an agent silently take that human's place.**

The principle (judgment-execution four-step loop, step 2 判断退守): the agent fleet handles the vast
majority of work with **no human touch** — that's the leverage. A human is summoned only at the few
irreducible nodes: deciding what's worth doing, choosing among options, owning consequences, signing
off irreversible/adverse actions. If your queue routes most items to a human, judgment isn't scarce
and you've rebuilt the approval chain — concentrate the nodes and raise the auto-handle bar.

## The routing table (one row per exception class)

For *this* org, fill a table. Every column is mandatory — a missing column is how exceptions
silently fail.

| column | what it specifies | failure if omitted |
|---|---|---|
| **Trigger** | the precise condition that queues an item | items either flood the queue or slip past it |
| **Named human node** | *which human, by role* — not "the team" | escalates to no one; B.06 becomes an ownerless queue |
| **Wait-set** | exactly what the human must rule on before the item moves | the human rules on the wrong thing or guesses |
| **Join policy** (multi-input) | `all` / `quorum:n` / `mutually_exclusive_by:<guard>` | gate fires on first verdict; half the judgment is skipped |
| **Verdict set** | `{approve, decline, amend}` (+ domain variants) | only "approve" is wired; a "no" deadlocks |
| **Each verdict's next step** | a *named* node per verdict | a non-approve verdict silently stalls |
| **SLA / fallback** | how long the human has, what happens if they don't act | items rot in queue, or auto-resolve unsafely |

### Trigger classes that must escalate (don't auto-handle these)
- **Low confidence** — the agent's confidence (or the monitoring agent's eval) is below the class
  threshold. Near-threshold cases go to a human, not to the agent's own coin-flip.
- **Irreversible action pending** — anything that can't be undone (a payment, a publish, a deletion,
  a filing, a physical/real-world commitment).
- **Irreversible *adverse* outcome pending** — a reject / deny / fail that *harms a third party* (a
  denied claim, a destroyed lot, a wrong rejection). This is itself an irreversible action: design
  the negative path with the same care as the positive one. A wrongful "no" belongs behind a human
  judgment node, **never** behind an agent's classification.
- **Out-of-policy / regulated / safety-critical** — legal, licensure, or safety exposure → a
  **named accountable human**, and (if regulated) name the governing regime, not just the person.
- **Trust / relationship / safety touch** — anything at the human-reserved core (see stop-line).

## Make the gate a real node, not a label

A named human node has teeth only if all three hold (judgment-execution.md §"a judgment node is a
real node"):

1. **Full verdict set, every verdict homed.** `{approve, decline, amend}` — and each non-approve
   verdict terminates in a *named* next step: a rework/renegotiate loop, an abort node, a
   caveated-release node, or a named re-entry edge. A "decline" wired only into an `all`-join doesn't
   fail loudly; it **silently deadlocks** the very node the org built the gate to protect (a
   reviewer refusing to sign, a community withholding consent). Define what the join does on a
   negative verdict: route-to-named-abort, not wait-forever.
2. **Genuine scrutiny, fed by observability.** The human's job is to *challenge*, and the
   observability layer must hand them what to challenge — the drifting eval, the anomalous trace,
   the low-confidence span — not a green checkmark. A gate the human waves through unread is theater,
   and theater is *worse than no gate*: it launders the risk and diffuses accountability (B.08 —
   "the AI pre-approved it" is the new "I assumed the tier above checked it"). If the queue's
   approve-rate is ~100% with near-zero dwell time, the gate is a rubber stamp — fix it or remove it.
3. **One accountable owner per node.** Not "the team." A single-threaded *named* owner with a backup
   in the on-call rotation. Ownership that diffuses across a group is no ownership (B.06).

## The org stop-line (止步线) — in operation

> **Never put an agent at the center of a trust / safety / relationship node the architecture
> reserved for a human.**

You operate *around* that node: agents can brief the human, draft options, gather context, monitor
for the trigger. The agent does not *become* the node. The pressure that breaks this line is
operational, not architectural — a backed-up queue, an SLA breach, a throughput target. The runbook
must make the line hold *under that pressure*: the fallback for an un-actioned trust/safety item is
**escalate further up the human chain**, never **auto-resolve**. Crossing the line to clear the
queue is precisely how an org hollows out the human and calls it efficiency. Essence is not
maximalism: the scarce-and-sacred core is *elevated and protected*, not automated into.

If operating reality keeps forcing items past a human node faster than the human can rule, that's a
**design signal**, not an operating fix: the node may be mis-scoped or the upstream auto-handle bar
mis-set. Surface it to the architect; don't lower the bar silently.

## Feeds (what the queue writes back)
- Every escalation + its verdict + rationale `feeds:` the **decision log** — so the next similar
  case can be auto-handled (the queue *teaches the fleet its own thresholds*; this is self-
  improvement, essence property 4).
- Recurring escalation patterns `feed:` the **eval suite** (a class that escalates often needs a
  better eval or a tuned threshold) and, when structural, a **design-change request** to the
  architect.
- Rubber-stamp signals (approve-rate, dwell time per gate) `feed:` the observability layer as a
  first-class metric — the gate's *health* is monitored, not assumed.
