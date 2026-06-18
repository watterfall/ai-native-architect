# `_core/scripts/` — the kernel, made mechanical

The shared spine of the system describes three workflows that every skill (and
many deliverables) re-derived by hand on every run. These scripts turn the
deterministic half of each into a check the model can *run*, so the prose
contract and the artifact cannot quietly drift. They are **stdlib-only Python 3**
— no install, no dependencies, runnable anywhere `python3` is.

They do **not** replace judgment. Each tool does the mechanical part (parse,
count, gate, lint); the substantive call — is the kernel actually the spine, is
this domain craft sound — stays human / council. That division *is* the kernel:
hand the abundant mechanical work to a tool, keep the scarce judgment.

| Script | What it makes mechanical | Used by |
|---|---|---|
| `validate_workflow_graph.py` | the **graph-executability contract** — typing, explicit joins with wait-sets, `join_policy` on multi-input gates, full verdict sets with named negative paths, real `feeds:` edges | `ai-native-architect` (emits the graph), `ai-native-org` (operates it) |
| `council.py` | the **5-role review gate** — role-prompt scaffold + the PASS/FAIL aggregation (`mean ≥ 8.5 AND no dim < 8.0`) with the binding fixes named | all seven skills, and the gate on the skills themselves (`council.md`) |
| `essence_lint.py` | the **banned house-style sweep** — means/ends sloganeering, six-surfaces-as-pipeline, printed `X/5` essence scorecards, attestation tells, placeholder algebra | any deliverable's self-check (`kernel.md`, `judgment-execution.md`) |

Every script self-verifies — run it with no further setup:

```bash
python3 validate_workflow_graph.py --self-test
python3 council.py --self-test
python3 essence_lint.py --self-test
```

## `validate_workflow_graph.py`

```bash
# validate the graph(s) embedded in a blueprint (or a raw graph file)
python3 references/_core/scripts/validate_workflow_graph.py path/to/blueprint.md
# treat warnings as failures (stricter, e.g. for a publish gate)
python3 references/_core/scripts/validate_workflow_graph.py --strict path/to/blueprint.md
```

It reads every ```` ```yaml ```` block containing a `nodes:` key. Nodes use the
template's readable DSL and/or flow maps; the annotations it enforces (and that
the template now demonstrates):

```yaml
nodes:
  - id: synth     ; type: agent  ; join_inputs: [scan_a, scan_b]      # explicit AND-join wait-set
  - id: judge     ; type: human  ; verdicts: [approve, decline, amend] ; routes: {decline: abort, amend: respec}
  - id: pay_gate  ; type: policy ; join_inputs: [judge] ; join_policy: all   # all | quorum:N | mutually_exclusive_by:<guard>
edges:
  - { from: judge, to: pay_gate, trigger: "approved", on: approve, feeds: "ctx/decision-log" }
  - { from: judge, to: abort,    trigger: "declined", on: decline }
```

`ERROR` blocks (exit 1) — the graph would not run; `WARN` surfaces a likely
design smell (no compounding-context edge, a human on most edges, an
irreversible action with no gate in front of it). Exit 0 = no errors.

## `council.py`

```bash
# 1. print the five reviewer prompts to dispatch as parallel, blind subagents
python3 references/_core/scripts/council.py --scaffold path/to/artifact
# 2. after collecting their scores, aggregate into a verdict
python3 references/_core/scripts/council.py scores.json
```

`scores.json` is a list of `{"dimension","score","top_fix"}` (or a flat
`{dimension: score}` object). On FAIL it names the binding (lowest, gate-blocking)
dimensions and their `top_fix` so the next iteration knows exactly what to fix.

## `essence_lint.py`

```bash
python3 references/_core/scripts/essence_lint.py path/to/deliverable.md
```

Lines that *quote a banned phrase in order to forbid it* (containing "banned",
"don't", "never", "avoid", …) are suppressed, so the canon files themselves lint
clean. Exit 0 = clean.
