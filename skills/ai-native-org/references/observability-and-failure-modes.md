# Observability & the documented failure modes

In operation, observability is not a reporting layer bolted on at the end — it is the org's **nervous
system**, and it is the precondition for everything else in the runbook. Without it you scale failure
faster than humans can correct it; the human gates degrade into rubber stamps because no one can see
*what to challenge*; and the documented failure modes go unnoticed until they're expensive.

## The four-layer substrate, operated (not just specified)

The architect specified the substrate; you run it. From bottom (most foundational) to top (closest
to the work):

1. **Model layer** — multi-vendor / open-weights / **switchable abstraction**. Operating duty: keep
   the swap abstraction real (a model change is a regression-test run, not a rewrite) and keep ≥2
   provider relationships live. The risk you operate against is *algorithmic feudalism* — one
   provider becomes your landlord and prices you hostage.
2. **Agent layer** — orchestration / runtime / tool integrations. Operating duty: dispatch, scope,
   reconverge (see `orchestration-spec.md`); keep guardrails live (these are S3 real-time control).
3. **Context layer** — knowledge graph / decision log / org memory. Operating duty: write-back-as-
   done, freshness, the context-debt test (see `context-upkeep.md`).
4. **Observability layer** — **logs / traces / evals / review queue**. The nervous system. Operating
   duty: be able to answer, from a trace, *what did the agent do and why*; score runs against evals;
   surface to the human gates *what to scrutinize*; route exceptions to the queue.

The layers are a dependency order: observability is closest to the pillars because it's what makes
the pillars *true* rather than slogans. **Stand observability up first** — before scaling the fleet.
An org that scaled agents before it could trace them is the observability-last failure, below.

## The signals worth watching (each consumed by a routing rule)

A dashboard metric that no decision reads is theater — cut it. Every signal here feeds a rule:

| signal | what it tells you | the rule it drives |
|---|---|---|
| **per-class escalation rate** | is judgment still scarce-but-real? | →0 on a should-escalate class = over-automation; flooding = bar too low |
| **gate approve-rate + dwell time** | is the human gate genuine scrutiny? | ~100% approve at near-zero dwell = rubber stamp |
| **eval scores / drift** | is fleet quality holding? | drift = re-tune / re-train / investigate before it reaches output |
| **rework rate** | is context fresh and scope right? | rising = context rot or mis-scoped dispatch |
| **context-debt list size/trend** | is the org staying native? | growing = knowledge re-accumulating in heads |
| **trace completeness** | can you explain any agent action? | gaps = observability-last; fix first |

## The documented failure modes (foreseeable, therefore avoidable — SHEET 11)

These are on record from real native orgs and failed transformations. The runbook actively guards
each:

### Over-automating judgment
The queue gets quietly auto-resolved; a node the architecture reserved for a human becomes an agent
classification. This is the inverse of the kernel ("essence is not maximalism") and the most
seductive failure under throughput pressure. **Early signal:** escalation rate trending to zero on a
class that *should* escalate (especially adverse/irreversible classes). **Guard:** the org stop-line,
a floor on escalation for sacred classes, and the rule that an un-actioned trust/safety item
escalates *up the human chain*, never auto-resolves.

### Context rot
Write-back lapses under deadline; the store goes stale; agents run confidently on outdated context.
Because a native org runs *on* its context, this is a slow-motion production outage. **Early signal:**
rising rework, the context-debt test lighting up, evals drifting un-noticed. **Guard:** write-back-as-
done, freshness rituals, debt test on a cadence (see `context-upkeep.md`).

### Observability-last
The org scaled the fleet *before* instrumenting it — now it can't answer "what did the agent do and
why," so it can't correct failures and can't make the human gates genuine. **Early signal:** trace
gaps; incidents you can't reconstruct. **Guard:** stand observability up *first*; it's the
precondition for the queue, the gates, and every other control. This is the one to fix before any
other.

### Pointless-graph / dashboard theater
Dashboards and metrics that look like control but drive no decision. **Early signal:** a metric no
routing rule consumes; a graph drawn but never read. **Guard:** every signal must name the rule it
feeds (the table above); if it feeds none, cut it.

### (Org-specific) the approval-chain ghost
A native-looking queue that has quietly re-grown into multi-tier sign-off — every item touched by
several humans "to be safe," accountability diffusing across all of them (B.08). **Guard:** one
named owner per gate; count human touches per item; if most items see >1 human, you rebuilt the
chain.

## Feeds (observability is itself a compounding loop)
- Eval results + traces `feed:` the context layer (quality baselines, failure cases become test
  cases) — failures *teach the suite*, so the same failure is caught automatically next time
  (self-improvement, essence property 4).
- Gate-health metrics `feed:` the review-queue design (a rubber-stamp gate gets re-cut or removed).
- Recurring incident classes `feed:` a design-change request to `ai-native-architect` when the fix
  is structural, not operational.

## Future-trajectory (why an instrumented org rides the curves)
An observable, eval-anchored org *improves automatically as the substrate improves*: cheaper/better
models drop in through the swap abstraction and the eval suite proves the upgrade safe; longer
context and A2A protocols widen what the fleet handles without redrawing the org; the context moat
deepens every cycle. The two things that must stay un-frozen to capture it: a **swappable model
layer** and a **live learning loop** (evals + write-back). A grafted org freezes at today's node-
speed; an operated native org gets structurally stronger the longer it runs.
