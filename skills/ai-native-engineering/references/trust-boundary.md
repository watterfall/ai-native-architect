# Trust boundary — read-only by default

The **tool-attachment surface is the attack surface.** The moment you give an agent tools, you inherit tool
poisoning, prompt injection, and credential leakage as live threats. The trust boundary is the engineering
form of "judgment retreats to a few nodes": the agent acts abundantly *inside* the boundary, and consequence
crosses *out* of it only through a declared gate. Write `PERMISSIONS.md` to make the boundary explicit.

## The four principles

1. **Read-only by default.** Agents read freely (code, docs, data, logs). **Every write/mutating action is
   declared explicitly** in the manifest — nothing changes state implicitly. The default capability of an
   agent is to *observe and propose*, not to *act*. Acting is opt-in, per action, in writing.
2. **Least privilege.** Scope each tool and credential to exactly what its task needs and no more. No ambient
   admin, no shared all-powerful token. An agent that only needs to read one table gets read on one table.
   The blast radius of a compromised or misled agent is bounded by what you scoped, so scope tight.
3. **Independent checks.** The verifier that gates an action is **separate from the model that proposed it**
   (`verification.md`). A model authorizing its own side effects inherits its own blind spots; the check must
   be external — a deterministic guard, a policy engine, a separately-authored rule.
4. **Rollback.** Every action that looks irreversible either has a reversal path (transactional, versioned,
   soft-delete + restore) or it goes behind a human judgment node (`judgment-nodes.md`). "Irreversible and
   ungated" is the one combination the boundary must never allow.

## `PERMISSIONS.md` scaffold

```markdown
# Trust boundary & permissions — <build name>

## Default posture
Read-only. Writes are explicit, per-action, declared below.

## Read scopes (granted by default)
- <resource> : read — <why>

## Write / mutating actions (explicit, least-privilege)
| action | tool/credential | scope (least-privilege) | independent check | rollback |
|--------|-----------------|-------------------------|-------------------|----------|
| <e.g. write to staging DB> | <token X> | <only table Y, staging only> | <schema validator> | <txn / restore> |

## Crosses the boundary → behind a judgment node
- <action> → see JUDGMENT.md gate "<node>"

## Threat notes
- tool poisoning / prompt injection on: <which tools>
- credential exposure path: <where a secret could leak>, mitigation: <…>
```

## Why this is the AI-Native move, not just "security hygiene"

Pre-AI, permissions guarded *people*, who exercise judgment continuously and rarely act at machine speed and
scale. An agent acts fast, at scale, and on the basis of text it was fed — including text an attacker may have
injected. So the boundary stops being a background IT concern and becomes a **first-class engineering
artifact**: it is precisely what lets you give an agent real capability (the leverage you came for) without
giving it the power to do something you cannot take back. Read-only-by-default is the boundary's center of
gravity because it makes the *safe* path the *default* path — the agent has to cross an explicit, gated line
to cause consequence, and that line is where the scarce human judgment sits.

[Source: this volume's security / permissions sheet; the protocol-level basis is MCP's least-privilege
manifest and the "read-only by default, write actions declared explicitly" model (modelcontextprotocol.io;
tool poisoning / prompt injection / credential leakage as the attack surface).]
