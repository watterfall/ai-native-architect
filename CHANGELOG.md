# Changelog

All notable changes to **ai-native-architect** are recorded here. The system is grounded in the
*AI Native Organization Methodology* (organization = distribution of judgment × flow of context).

## [Unreleased] — the skills, made mechanical

Applies the same skill-creator principle the kernel scripts use — *bundle the repeated check into a
script, then hold the artifact to it* — to the **skills themselves**, against the `writing-skills`
authoring bar.

### Added

- **`references/_core/scripts/validate_skills.py`** — a meta-gate over the seven `SKILL.md` interfaces.
  ERROR (publish floor): frontmatter over the 1024-char spec cap, or a `description` that doesn't open
  with "Use when". WARN: body word budget, version drift across manifests, orphaned / unreachable
  references. `--self-test` included; documented in `references/_core/scripts/README.md`.

### Changed

- **All seven `description` fields rewritten to "Use when …" trigger-only form** (was: leading with what
  the skill *does*, the SDO anti-pattern that makes agents follow the summary instead of reading the
  skill body). Frontmatter brought back under the 1024-char spec cap and each description under the
  500-char target, while preserving the bilingual (EN + 中文) trigger phrases. Verified: gate exits 0;
  a 3-rep fresh-context routing micro-test routed 42/42 tasks (including edge framings) to the correct
  skill.

## [2.1.0] — the kernel made mechanical

Applies the skill-creator principle *"bundle the repeated workflow into a script, then tell the skill to
use it"* to the shared kernel. Three disciplines that were judgment-shaped but **deterministic** — and
were re-derived by hand on every run — are now executable checks, while the judgment itself stays human.

### Added — shared executable layer (`references/_core/scripts/`, stdlib Python, no install)

- **`validate_workflow_graph.py`** — the graph-executability contract, mechanized. Checks that a
  blueprint's workflow graph would actually run: every node typed (agent / human / policy); parallel
  branches reconverging at explicit joins with `join_inputs` wait-sets; multi-input gates declaring a
  `join_policy` (`all` / `quorum:N` / `mutually_exclusive_by:<guard>`); every human/community judgment
  node declaring a full verdict set with each non-approve verdict routed to a **named** node (no silent
  `all`-join deadlock); every compounding-context claim a real `feeds:` edge. Supports both inline-node
  and sectioned (`joins:` / `verdict_sets:`) representations. `--self-test` included.
- **`council.py`** — the 5-role review gate (`council.md`) made repeatable: `--scaffold` prints the five
  reviewer prompts; passing a scores file aggregates them into the `mean ≥ 8.5 AND no dimension < 8.0`
  verdict and names the binding (lowest, gate-blocking) fixes.
- **`essence_lint.py`** — sweeps a finished deliverable for the canon's banned house-style: means/ends
  sloganeering, the six-surfaces-as-pipeline framing, printed `X/5` essence scorecards, attestation
  tells ("per the kernel"), and placeholder algebra. Paragraph-level suppression keeps the canon files,
  which *define* the bans, from flagging themselves.
- **`references/_core/scripts/README.md`** — documents the three tools and their contracts.

### Changed

- **`ai-native-architect`** — Step 4 and the self-check now call `validate_workflow_graph.py` instead of
  eyeballing the graph; the workflow-graph template demonstrates the full annotation set (`join_inputs`,
  `join_policy`, `verdicts`, `routes`/`on`, `terminal`) and validates clean.
- **`ai-native-org`** — validates a handed-over workflow graph before building the runbook on it.
- **All seven skills** surface the shared scripts in their reference lists; `_core/council.md` and
  `_core/judgment-execution.md` wire in `council.py` and `essence_lint.py`.
- **Flagship example** (`examples/offshore-wind-decommissioning/blueprint.md`) hardened: the validator
  found four graph-executability gaps a 9.10 council review had missed (an undeclared verdict set, two
  implicit joins, a multi-input gate with no `join_policy`) plus a silently-dropped edge; all fixed, and
  it now validates clean.

### Verified

- All three scripts pass `--self-test`; `essence_lint.py` sweeps the whole repo clean; the template and
  the hardened example pass `validate_workflow_graph.py` with zero errors.
- Canon alignment re-checked against `ai-native.build` (the 16 bottlenecks, the four-layer substrate, the
  MIT NANDA figure, the Coase/Williamson caveat, judgment-scarcity) — no drift.

## [2.0.0] — two-tier, seven-skill system

- Added the **execution tier** — six skills (engineering, design, research, learning, innovation, org)
  over a shared `references/_core/` kernel — alongside the architecture-tier `ai-native-architect`.
- Added the curated tool registry and the no-install lite tools (`tools/`).
- Validated both tiers against the adversarial council (architecture mean 9.00; execution skills 8.8–9.0,
  no dimension below 8.0).

## [1.0.0] — AI-Native Architect

- Initial open-source (MIT) release: the architecture-tier skill that turns an intent into an AI-Native
  Architecture Blueprint.
