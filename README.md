# AI-Native Architect

**A two-tier, seven-skill AI-Native system over one shared kernel.** One skill *designs* a genuinely
AI-Native organization; six skills *do the work* of their surface the AI-native way. It begins from one
premise: **when execution is no longer scarce, the organization must be redesigned** (当执行不再稀缺，组织本身必须被重画).
It is the executable companion to the
[AI Native Organization Methodology](#relationship-to-the-methodology) and runs in
[Claude Code](https://claude.com/claude-code) (and any Claude Agent SDK / claude.ai surface that loads
skills).

> **The thesis in one line:** organization = **distribution of judgment** x **flow of context**.
> Scale is a free variable; management is the engineering of these two structures.

The transition is not from "no AI" to "using AI." It is from **using AI** to **becoming AI-Native**:
the question changes from *which tool helps this step?* to *how should execution, judgment, and context
be redistributed?*

---

## The kernel: why this is a different kind of thing

Pre-AI, **execution was scarce** (you needed people to do the work) and judgment was comparatively
abundant. AI **inverts the scarcity**: execution becomes abundant (agents generate, transform, and
execute at near-zero marginal cost) and **judgment becomes the scarce, value-determining factor.** Every
legacy organizational form is an artifact of the old scarcity. An AI-Native organization is the form
built for the new one, and it has four properties a "company that uses AI" does not:

1. **Judgment is scarce and concentrated** — humans sit at a few irreducible nodes; everything else
   defaults to agents.
2. **Context compounds as the core asset** — knowledge settles into a system and grows, so year two is
   structurally smarter than year one.
3. **Capability decouples from headcount** — output scales with agents and context, not payroll.
4. **The organization improves itself** — instrumented learning loops make decisions better
   automatically.

The decisive test (the **essence test**): **delete the AI. If the design collapses back into a normal org
chart with the same roles and hand-offs, it was AI-enablement, not AI-Native.** Every skill in this
system runs that test on its own work before it starts — the **redraw-vs-graft gate**.

---

## The two tiers (one kernel, six faces)

The whole system is one kernel applied at two altitudes. Both tiers share the same spine in
[`references/_core/`](references/_core/): the scarcity-inversion kernel, the redraw-vs-graft gate, the
judgment-tier / execution-tier split with its **stop-lines** (止步线 — what is *never* offloaded to an
agent), the canon vocabulary (T1, the 16 bottlenecks, the four-layer substrate, M.01–06, the seven
pillars), and the council review gate.

### Architecture / judgment tier — *design* the organization

**`ai-native-architect`** turns a business / startup / org-rebuild intent into a complete **AI-Native
Architecture Blueprint**: the scope gate, T1 applied, a redrawn workflow graph, the four-layer substrate,
conditional depth modules, and the kernel + future-trajectory. This is the judgment-tier skill — it
decides *how the work should be distributed* before any of it is done. (Full detail in
[Architecture tier](#architecture-tier--ai-native-architect) below.)

### Execution tier — *do* the work, the AI-native way

Six skills, **six faces of one kernel — no first, no last**. Each one keeps you at the execution layer
(it produces the actual work product, it does not re-design the org), hands the abundant work to agents,
and holds the few irreducible judgment nodes for a human. Each opens by running the redraw-vs-graft gate
on its own task.

| Skill | Does the work of… | Work product |
|---|---|---|
| **`ai-native-engineering`** | building software — spec-driven, eval suite as the verification spine, judgment gates on irreversible actions, an explicit trust boundary | runnable code + `SPEC` + eval suite + `JUDGMENT.md` + `PERMISSIONS.md` |
| **`ai-native-design`** | producing design — cheap multi-draft generation + human taste as the scarce judgment, design-as-code, anti-homogenization (the 指纹 / fingerprint check) | the artifact + tokens + taste rationale + 指纹 check |
| **`ai-native-research`** | doing research — a credibility ledger (evidence grades Ⅰ–Ⅴ), a knowledge graph, blind-spot scanning, generate-vs-verify split | a Research Finding Dossier |
| **`ai-native-learning`** | building learning that **protects the desirable difficulty** — the sharpest stop-line: keep the cognitively constitutive struggle human | an AI-Native Learning Protocol (scaffold + offload-boundary + reflection store) |
| **`ai-native-innovation`** | running innovation — signal/noise under generative abundance, falsify-before-polish, affordable-loss bets, false-signal guards | an Innovation Portfolio & Bet Sheet |
| **`ai-native-org`** | **operating** an AI-native org — orchestrate the fleet, run the cadence, route exceptions to the human judgment nodes, keep context fresh (distinct from `architect`, which *designs* it) | an Operating Runbook |

The execution tier and the architecture tier are not a pipeline. You can invoke any execution skill on
its own; `architect` is where you go when the question is *how should the work be distributed*, not *do
the work*.

---

## Architecture tier — `ai-native-architect`

Given an intent, the architect produces an **AI-Native Architecture Blueprint**:

1. **A scope gate** that classifies the request honestly into four tracks:
   - **Track A — Greenfield**: a new venture / org / unit built from zero.
   - **Track B — Brownfield carve-out**: an incumbent that builds a new independent unit from zero (the
     only valid AI-Native path for an incumbent).
   - **Out of scope — AI-enablement**: "make our existing teams faster with copilots, keep the org
     chart." The skill says so plainly, explains you cannot graft AI onto a pre-AI architecture, tells
     you that you are **not the target group** of this methodology, and offers the two honest options
     (the adjacent change-management methodology, or a from-zero carve-out).
   - **Boundary — emotional-labor / trust / safety-led domains**: AI assists, but must not lead.
2. **T1 applied** — the distribution of judgment and the flow of context, designed explicitly.
3. **A redrawn workflow graph** — nodes typed `agent` / `human` / `policy`, parallel fan-out, judgment
   anchors, policy gates, and compounding-context writes (YAML + Mermaid).
4. **The four-layer substrate** — model / agent / context / observability, sized to the team.
5. **Conditional depth modules** — only the ones a case demands: computed economics, regulatory
   grounding, residual-harm protocol, human transition and tacit-capture, moat stress-test, beneficiary
   service contract, incentive-compatibility, and a graph-executability contract.
6. **The kernel and future-trajectory** — why the design is future-leading: how it compounds as the
   model curves advance, and what must stay un-frozen to capture it.

**Who the architect is for, and who it is not.** For: founders and operators designing a new venture or
unit from zero, and incumbents willing to carve out an independent new unit and let its output drive
change by contrast. Not for: "roll out copilots across our existing departments and keep the structure."
That is AI-enablement, a difference in **kind**, not degree. The skill will tell you this rather than sell
you a relabeled rollout. Honesty about the boundary is part of the methodology.

---

## No Claude Code? Start with the lite tools (no install)

The skills are the full, rigorous version. If you just want to get your hands on the ideas, the
[`tools/`](tools/) folder holds no-install, low-barrier tools, simplest first:

- **[Self-test](tools/self-test.md)** — Are you AI-Native or AI-enabled? Which track? Pen and paper, ~2 min.
- **[16-Bottleneck Scorecard](tools/bottleneck-scorecard.md)** — score your org 0–16, read the band.
- **[T1 Canvas](tools/t1-canvas.md)** — your judgment distribution × context flow, on one page.
- **[Portable Prompt](tools/portable-prompt.md)** — paste into any chatbot (ChatGPT, Claude, Gemini) for
  an AI-assisted lite blueprint, no install.

---

## Visual entry point

[`site/`](site/) is a lightweight static buffer page / frontispiece, not a replacement for the full
methodology homepage. It states the core premise, waits briefly, routes readers onward to the existing
methodology homepage, and offers a compact seven-skill atlas for people who want the executable layer
first.

Preview it locally:

```bash
python3 -m http.server 8751 -d site
```

---

## Install

### As a Claude Code plugin (recommended) — brings all 7 skills

```text
/plugin marketplace add watterfall/ai-native-architect
/plugin install ai-native-architect@ai-native-architect
```

The repo is itself the marketplace. Installing the plugin auto-discovers and registers **all seven
skills** (the architect plus the six execution skills) from `skills/`.

### Manually (any skill-aware surface)

```bash
git clone https://github.com/watterfall/ai-native-architect.git
# install every skill…
cp -r ai-native-architect/skills/* ~/.claude/skills/
# …or just the architect
cp -r ai-native-architect/skills/ai-native-architect ~/.claude/skills/
```

## Use

Invoke any skill in Claude Code by name, or just describe the task and the right skill triggers.

**Do the work (execution tier):**

```text
/skill ai-native-engineering
> Build the refund-approval handler for our store, with evals and a permissions boundary ...
```

```text
/skill ai-native-research
> Synthesize these 40 longevity papers and tell me which claim is actually credible ...
```

(Same pattern for `ai-native-design`, `ai-native-learning`, `ai-native-innovation`, `ai-native-org`.)

**Design the organization (architecture tier):**

```text
/skill ai-native-architect
> I run a 40-person specialty insurer and want to rebuild claims around AI from zero ...
```

Or just describe the task ("design my startup around agents", "用 AI 把这个功能做出来",
"我想做一个 AI 原生的公司怎么设计") and the matching skill triggers. Each writes its work product to a file
and returns the path plus a short summary.

---

## What's inside

```
references/_core/                       # the shared kernel — written once, referenced by both tiers
├── kernel.md                           # scarcity inversion + the essence test
├── redraw-vs-graft.md                  # the gate every skill runs on its own task first
├── judgment-execution.md               # judgment-tier vs execution-tier split + the stop-lines (止步线)
├── canon-vocab.md                      # T1, 16 bottlenecks, four-layer substrate, M.01–06, seven pillars
└── council.md                          # the 5-role adversarial review gate

skills/
├── ai-native-architect/                # ARCHITECTURE TIER — designs the org → Architecture Blueprint
│   ├── SKILL.md                        #   the procedure, the scope gate, the output contract
│   ├── references/                     #   kernel, methodology canon, bottleneck diagnostic, scope gate, depth modules
│   ├── templates/                      #   workflow-graph + architecture-blueprint scaffolds
│   └── evals/evals.json
├── ai-native-engineering/              # EXECUTION TIER — build software → code + SPEC + evals + JUDGMENT + PERMISSIONS
├── ai-native-design/                   #   produce design → artifact + tokens + taste rationale + 指纹 check
├── ai-native-research/                 #   do research → Research Finding Dossier (credibility ledger Ⅰ–Ⅴ)
├── ai-native-learning/                 #   build learning → Learning Protocol (protects the desirable difficulty)
├── ai-native-innovation/               #   run innovation → Innovation Portfolio & Bet Sheet
└── ai-native-org/                      #   operate the org → Operating Runbook
        (each: SKILL.md + references/ + templates/ + evals/evals.json)

tools/                                  # no-install lite tools, simplest first (start here without Claude Code)
├── self-test.md                        # AI-Native or AI-enabled? which track? (pen + paper, ~2 min)
├── bottleneck-scorecard.md             # the 16-bottleneck diagnostic, 0–16 (pen + paper)
├── t1-canvas.md                        # judgment x context, on one page (fill-in)
└── portable-prompt.md                  # paste into any chatbot for a lite blueprint (no install)

docs/
├── SYSTEM-DESIGN.md                    # how the canon, the two-tier skill layer, and distribution form one system
└── VALIDATION.md                       # the adversarial council track record (architecture + execution tiers)
```

## How it was validated

Both tiers were hardened against an **adversarial multi-role "council" review** — independent expert
lenses score work under strict, no-inflation calibration, each told to name the single biggest weakness
even when scoring high.

- **Architecture tier:** a panel of up to ten lenses scored fresh random design cases. Latest run:
  **mean 9.00 / 10** across three cases (offshore-wind decommissioning, CME accreditation, an Andean
  seed-bank nonprofit).
- **Execution tier (v2.0.0):** a 5-role council (kernel-fidelity · domain-expertise ·
  skeptic/collapse-to-enablement · operability · human-boundary), bar = mean ≥ 8.5 **and** no dimension
  below 8.0. All six skills pass: engineering 9.00, design 8.80, research 8.80, learning 9.00,
  innovation 9.00, org 9.00 — no dimension below 8.0. A lightweight quantitative eval (with-skill vs
  baseline) corroborates the result.

See [`docs/VALIDATION.md`](docs/VALIDATION.md).

## Relationship to the methodology

This system is the **executable "how"** of a larger work, the **AI Native Organization Methodology** (the
"why" and the "what should be"). The methodology is a single-file canon (a drawing set, SHEET 00 to 18);
this system is its operator's toolkit made executable, and shares its exact vocabulary (T1, the 16
bottlenecks, the four-layer substrate, the seven pillars, the kernel). See
[`docs/SYSTEM-DESIGN.md`](docs/SYSTEM-DESIGN.md) for how the two stay in sync.

## Contributing

Issues and pull requests are welcome, especially: new validated example work products, additional depth
modules and execution references (with their trigger), and fidelity fixes that keep the skills faithful
to the canon and to the shared `_core` kernel. Keep the canon vocabulary exact, and prefer "explain the
why" over rigid rules.

## License

[MIT](LICENSE) (c) 2026 Ji Li. Use it, fork it, build on it.

---

## 中文简介

**AI-Native Architect** 是一个**两层、七 skill、共享一个内核**的 AI-Native 系统，是《AI Native 组织方法论》的可执行配套件，
运行于 Claude Code。

内核命题：**组织 = 判断的分布 × 上下文的流动**。当执行变得近乎免费、判断成为稀缺，工作就应当围绕"稀缺的判断"与"复利的
上下文"重新设计——而不是把 AI 嫁接到前 AI 的结构上。每个 skill 开场都先过一道**原生 vs 赋能的判定门**（把 AI 拿掉，活会不会
塌回旧流程？）。

七个 skill 共享 [`references/_core/`](references/_core/) 这同一个内核（稀缺性反转 + 本质判定、判定门、判断层/执行层之分
与**止步线**、术语正典、5 角色评审门）：

- **架构 / 判断层（1 个）：`ai-native-architect`** —— *设计*一个 AI-Native 组织，产出**架构蓝图**（范围闸分四轨：绿地新建 /
  增量"从零切出" / 仅"AI 赋能"诚实判定为不属于目标群体 / 情感劳动边界；T1、工作流图、四层底座、按需深度模块、内核与未来轨迹）。
- **执行层（6 个，六个面·同一内核·无先后）：** 每个都*真的把活做出来*（停在执行层、不回去重设计组织），把充裕的执行交给
  agent、把少数不可让渡的判断节点留给人——
  - `ai-native-engineering` 造软件（规格 + eval 套件 + 判断节点 + 信任边界）；
  - `ai-native-design` 出设计（多稿 + 品味判断 + 设计即码 + 指纹/抗同质化）；
  - `ai-native-research` 做研究（可信度账本 Ⅰ–Ⅴ + 知识图谱 + 盲区）；
  - `ai-native-learning` 搭学习并**守住该有的认知难度**（最硬的一条止步线）；
  - `ai-native-innovation` 跑创新（信噪比 + 先证伪后打磨 + 可承受损失下注）；
  - `ai-native-org` **运营** AI-native 组织（调度 agent 队、跑节奏、异常路由到判断节点、保上下文新鲜——区别于 architect 的"设计"）。

两层经议会式多角色对抗评审验证：架构层 10 角色 × 随机案例均分 9.0/10；执行层 6 个 skill 5 角色评审均分 8.8–9.0、且无单维 < 8.0，
全部通过。开源协议 MIT。安装与用法见上文 [Install](#install)。
