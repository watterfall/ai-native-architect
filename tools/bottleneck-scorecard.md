# The 16-Bottleneck Scorecard · 十六瓶颈诊断表

> A one-page, fill-in diagnostic. Pen and paper, no AI. For each of the sixteen structural bottlenecks,
> mark **hit / partial / clear** and jot one line of evidence. Sum the hits; read the band. This is
> SHEET 04 of the methodology made fillable.
>
> 一页纸、随手填的诊断。纸笔、不用 AI。对十六个结构瓶颈逐一标 **命中 / 部分 / 无**,各写一行证据,数出命中
> 数、对照区段读结论。这是方法论 SHEET 04 的可填写版。

**Why these and not "where can we add AI":** these bottlenecks live in the **shape of the graph**, not in
the speed of any node. Tools cannot reach them; "transformation" cannot route around them. Adding AI to a
node leaves the graph untouched, which is why end-to-end throughput barely moves. The diagnostic's job is
to convert "we should add AI" into the right question: **"what would this look like if we redrew the graph
from zero?"**

---

## Score it · 打分

For each row: **H** = hit (clearly true of us), **P** = partial, **C** = clear (not a problem). Evidence =
one concrete line. · 每行:**H** 命中、**P** 部分、**C** 无问题;证据写一行。

| # | Bottleneck · 瓶颈 | The tell · 识别信号 | H/P/C | Evidence · 证据 |
|---|---|---|---|---|
| B.01 | Serial dependency chain · 串行依赖链 | work moves as a relay; total time = sum of stages | | |
| B.02 | Quadratic coordination tax · 协调成本平方律 | every added head taxes everyone (~n²) | | |
| B.03 | Executive bandwidth ceiling · 决策带宽天花板 | all decisions route through a few overloaded people | | |
| B.04 | Hierarchical signal decay · 层级信息衰减 | information degrades as it climbs or descends layers | | |
| B.05 | Functional silos & local optima · 部门墙与局部最优 | departments optimize locally; the whole suffers | | |
| B.06 | Synchronous coordination tax · 会议同步税 | calendars are the bottleneck; meetings to sync | | |
| B.07 | Tacit knowledge lock-in · 知识私有化 | key knowledge lives in heads; lost when people leave | | |
| B.08 | Approval chains & diffused accountability · 审批链与责任稀释 | long approval chains; no one owns the outcome | | |
| B.09 | Headcount-as-capacity · 人头即产能 | more output means hiring more people | | |
| B.10 | Planning cadence mismatch · 规划节奏失配 | annual/quarterly plans vs. a fast-moving world | | |
| B.11 | Experiment cost & risk aversion · 试错成本与风险规避 | each experiment is costly, so few are run | | |
| B.12 | Metric theater · 指标剧场 | proxies get gamed; activity measured, not value | | |
| B.13 | Trust-radius collapse · 信任半径坍缩 | trust doesn't scale; control replaces it | | |
| B.14 | Power gradient & agenda capture · 权力梯度与议程垄断 | ideas filtered by status, not merit | | |
| B.15 | Motivation crowding-out · 动机抽干 | extrinsic controls crush intrinsic motivation | | |
| B.16 | Niche lock-in · 生态位锁定 | captured by the current position; cannot move | | |

**Hit count · 命中数 = ____ / 16**

---

## Read the band · 读区段 (brownfield / existing org · 既有组织)

- **0–3 hits** — unusually healthy. Confirm you weren't gentle. Note: AI-Native is about *kind*, not
  degree; even a healthy org cannot be *grafted* into native form. · 异常健康(先确认没手软)。
- **4–9 hits** — a typical incumbent. The bottlenecks are structural; adding AI will not move throughput.
  The path is a **from-zero carve-out** (Track B), not a graft. · 典型既有组织。路径是**从零切出**,不是嫁接。
- **10–16 hits** — the structure *is* the problem. Any in-place "transformation" is theater. The only
  AI-Native move is a new unit built from zero. · 结构本身就是问题;原地"转型"是表演,唯一原生动作是从零另起一个单元。

Whatever the count, the diagnostic does **not** become a to-do list for fixing the old org. A high count is
the **argument** that the old graph cannot be fixed in place. · 无论几分,它都**不是**修旧组织的待办清单——高分恰是
"旧图无法原地修复"的论据。

## Greenfield? Invert it · 绿地?反过来用

Building from zero? You have no legacy to diagnose. Instead, for each row write the **design rule that
keeps you from building the bottleneck in** (e.g. B.01 → no default serial hand-off; B.09 → never equate
headcount with capacity). Greenfield's whole advantage is the freedom *not* to import these. · 从零开始就
没有"旧"可诊断——把每行反过来,写下"如何不把它建进去"的设计规则。绿地的全部优势,就是不进口它们的自由。

---

Next: the [T1 Canvas](t1-canvas.md), then a full blueprint via the [portable prompt](portable-prompt.md)
or the skill.
