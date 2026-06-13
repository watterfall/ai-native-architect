# AI-Native Architect

**An executable skill that designs a genuinely AI-Native organizational architecture** from a business
idea, a startup wedge, a new organization, a new internal unit, or an incumbent's from-zero rebuild. It
is the executable companion to the [AI Native Organization Methodology](#relationship-to-the-methodology)
and runs in [Claude Code](https://claude.com/claude-code) (and any Claude Agent SDK / claude.ai surface
that loads skills).

> **The thesis in one line:** organization = **distribution of judgment** x **flow of context**.
> Scale is a free variable; management is the engineering of these two structures.

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

The decisive test: **delete the AI. If the design collapses back into a normal org chart with the same
roles and hand-offs, it was AI-enablement, not AI-Native.**

---

## What it does

Given an intent, the skill produces an **AI-Native Architecture Blueprint**:

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

## Who this is for, and who it is not

**For:** founders and operators designing a new venture or unit from zero, and incumbents willing to
carve out an independent new unit and let its output drive change by contrast.

**Not for:** "roll out copilots across our existing departments and keep the structure." That is
AI-enablement, a difference in **kind**, not degree. The skill will tell you this rather than sell you a
relabeled rollout. Honesty about the boundary is part of the methodology.

---

## No Claude Code? Start with the lite tools (no install)

The skill is the full, rigorous version. If you just want to get your hands on the ideas, the
[`tools/`](tools/) folder holds no-install, low-barrier tools, simplest first:

- **[Self-test](tools/self-test.md)** — Are you AI-Native or AI-enabled? Which track? Pen and paper, ~2 min.
- **[16-Bottleneck Scorecard](tools/bottleneck-scorecard.md)** — score your org 0–16, read the band.
- **[T1 Canvas](tools/t1-canvas.md)** — your judgment distribution × context flow, on one page.
- **[Portable Prompt](tools/portable-prompt.md)** — paste into any chatbot (ChatGPT, Claude, Gemini) for
  an AI-assisted lite blueprint, no install.

---

## Install

### As a Claude Code plugin (recommended)

```text
/plugin marketplace add watterfall/ai-native-architect
/plugin install ai-native-architect@ai-native-architect
```

### Manually (any skill-aware surface)

```bash
git clone https://github.com/watterfall/ai-native-architect.git
cp -r ai-native-architect/skills/ai-native-architect ~/.claude/skills/
```

## Use

Invoke it in Claude Code:

```text
/skill ai-native-architect
> I run a 40-person specialty insurer and want to rebuild claims around AI from zero ...
```

Or just describe the task ("design my startup around agents", "我想做一个 AI 原生的公司怎么设计") and the
skill triggers. It writes the blueprint to a file and returns the path plus a short summary.

---

## What's inside

```
skills/ai-native-architect/
├── SKILL.md                          # the procedure, the scope gate, the output contract
├── references/
│   ├── ai-native-kernel.md           # the kernel: why AI-Native is the future org form
│   ├── methodology-canon.md          # T1, the 16 bottlenecks, four-layer substrate, worldviews, pillars
│   ├── bottleneck-diagnostic.md      # the 16 structural bottlenecks, score (brownfield) / invert (greenfield)
│   ├── fit-and-scope.md              # the scope gate in full, the AI-enablement redirect, the boundary
│   └── depth-checklists.md           # the 9 conditional depth modules
├── templates/
│   ├── workflow-graph.md             # the agent/human/policy node + annotation scaffold (YAML + Mermaid)
│   └── architecture-blueprint.md     # the deliverable template
└── evals/evals.json                  # test cases + assertions
tools/                                # no-install lite tools, simplest first (start here without Claude Code)
├── self-test.md                      # AI-Native or AI-enabled? which track? (pen + paper, ~2 min)
├── bottleneck-scorecard.md           # the 16-bottleneck diagnostic, 0–16 (pen + paper)
├── t1-canvas.md                      # judgment x context, on one page (fill-in)
└── portable-prompt.md                # paste into any chatbot for a lite blueprint (no install)
docs/
├── SYSTEM-DESIGN.md                  # how the canon, the skill, and this repo form one system
└── VALIDATION.md                     # the multi-role council review track record
```

## How it was validated

The skill was built and hardened against an **adversarial multi-role "council" review**: a panel of up
to ten independent expert lenses (methodology purist, skeptical operator, organizational economist, AI
systems architect, ethics and safety realist, change and adoption realist, finance, legal, strategy and
moat, beneficiary advocate) scores randomly generated design cases, strictly calibrated. The skill was
iterated until the council mean exceeded the bar with margin. Latest run: **mean 9.00 / 10** across three
fresh random cases (offshore-wind decommissioning, CME accreditation, an Andean seed-bank nonprofit). See
[`docs/VALIDATION.md`](docs/VALIDATION.md).

## Relationship to the methodology

This skill is the **executable "how"** of a larger work, the **AI Native Organization Methodology** (the
"why" and the "what should be"). The methodology is a single-file canon (a drawing set, SHEET 00 to 18);
this skill is its SHEET 17 toolkit made executable, and shares its exact vocabulary (T1, the 16
bottlenecks, the four-layer substrate, the seven pillars, the kernel). See
[`docs/SYSTEM-DESIGN.md`](docs/SYSTEM-DESIGN.md) for how the two stay in sync.

## Contributing

Issues and pull requests are welcome, especially: new validated example blueprints, additional depth
modules (with their trigger), and fidelity fixes that keep the skill faithful to the canon. Keep the
canon vocabulary exact, and prefer "explain the why" over rigid rules.

## License

[MIT](LICENSE) (c) 2026 Ji Li. Use it, fork it, build on it.

---

## 中文简介

**AI-Native 架构师** 是一个可执行的 skill：输入一个业务、创业切入点、新组织、或一次"从零重构"的意图，它产出一份完整的
**AI-Native 架构蓝图**。它是《AI Native 组织方法论》的可执行配套件,运行于 Claude Code。

内核命题:**组织 = 判断的分布 × 上下文的流动**。当执行变得近乎免费、判断成为稀缺,组织就应当围绕"稀缺的判断"与"复利的
上下文"重新设计——而不是把 AI 嫁接到前 AI 的结构上。

它先过一道**范围闸**,分流四条轨:绿地新建 / 增量"从零切出" / 仅"AI 赋能"(诚实判定为**不属于目标群体**并说明)/ 情感劳动边界
(AI 辅助、不主导);再落出工作流图、四层底座、按需的九个深度模块,与"内核 + 未来轨迹"。经议会式多角色评审验证(10 角色 ×
随机案例,均分 9.0/10)。开源协议 MIT。安装与用法见上文 [Install](#install)。
