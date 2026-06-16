# Skills 系统 v2 — 执行层重设计分析

> 系统分析（skill-creator 的 "Capture Intent" 阶段产物）。回答："6 个 skill 对应 6 个模块，但是执行层" 该怎么落地。

## 0. 结论先行

当前 `ai-native-architect` 是**架构/判断层**的单一 skill——它*设计*一个 AI-native 组织（产出蓝图）。方法论现在是"六个面、同一内核"，但 skill 只覆盖 1/6，且停在"设计"，没有"执行"。

**提议：升级为两层系统，共享一个内核。**

```
ai-native-architect/                      ← plugin = 整个系统（保名，文档外链不破）
  references/_core/                       ← 同一内核（只写一次，两层都引用）
    kernel.md            执行充裕→判断退守→上下文成基设→人回归意义 / 稀缺性反转
    redraw-vs-graft.md   原生 vs 赋能的判定门（每个 skill 开场自检）
    judgment-execution.md 判断层/执行层之分 + 何时把活交给 agent、何时不交
    canon-vocab.md       T1·16 瓶颈·四层基设·六面·七柱（精确术语，双语）
    council.md           5 角色对抗评审门（发布前质量闸）
  skills/
    ai-native-architect/   ← 架构/判断层（既有，升级为引用 _core + 可编排执行层）
    ai-native-engineering/ ┐
    ai-native-design/      │
    ai-native-research/    ├ 执行层（6 个新 skill，对应 6 个模块页面）
    ai-native-learning/    │
    ai-native-innovation/  │
    ai-native-org/         ┘ 运营/编排（"运行"组织，区别于 architect 的"设计"组织）
  tools/                                  ← 共享（文档 /tools 链接指此）
```

## 1. 架构层 vs 执行层 —— 这正是内核里的那条分界

内核："**执行充裕** → 判断退守 → 上下文成基设 → 人回归意义"。

- **架构/判断层（`ai-native-architect`）** = 人做的那部分稀缺判断：判断哪里值得做、把判断节点放在哪、上下文怎么流。产出 = **蓝图**，一次性。
- **执行层（6 个新 skill）** = agent 干的那部分充裕执行：被调用时**真的去做**该域的工作，按方法论的方式。产出 = **真实工作产物**，持续使用。

architect 设计"判断节点放在哪"；执行层 skill 就是"在节点之间被 agent 反复执行的那段工"。两层咬合，不是替代。

## 2. 六个执行层 skill 的 Capture-Intent 规格

| skill | 做什么（执行层动作） | 何时触发 | 输出（真实产物，非设计文档） | 区别于架构层 |
|---|---|---|---|---|
| **ai-native-engineering** | 规格驱动地造软件：JIT 规划→规格阶梯→自改进环→评测套件做验证脊柱→只读默认权限→不可逆动作设判断节点 | "用 AI 把这个功能/系统做出来"、写规格、搭 agent 编码环、评测套件 | 可运行代码 + 规格 + eval 套件 + 判断节点图 + 信任边界 | architect 设计工程组织；这个**真的写**并自我验证 |
| **ai-native-design** | 多稿廉价生成 + 以品味做稀缺判断 + 设计即码 + 抗同质化(守指纹) + 设计系统 + 人本护栏 | "设计这个产品/界面/系统/表达"、要多方案、品味评估、建设计系统 | 设计产物(mock/组件/系统) + 品味依据 + 指纹/差异化检查 + tokens | architect 不出设计；这个**真的产出设计** |
| **ai-native-research** | 担保可信(证据分级) + 知识图谱整合 + 判定值得知 + 生成/验证两层 + 盲区扫描 + 元科学 | "研究/查证这个问题"、要可信度担保、文献整合、找盲区 | 研究结论 + 可信度账本(证据级 Ⅰ–Ⅴ) + 知识图谱贡献 + 盲区登记 | architect 设计研究组织；这个**真的做研究** |
| **ai-native-learning** | 学习者即提问者 + 主动抵抗(守住该有的认知难度) + 脚手架 + 止步线(哪里不该卸载) + 慢的价值 | "帮我/团队学会 X"、设计学习路径、防 AI 把脑子掏空 | 学习脚手架/协议(保留 desirable difficulty) + 卸载边界 + 反思库 | 不是"设计教育机构"；这个**真的搭学习过程** |
| **ai-native-innovation** | 生成充裕下管信噪比 + 价值感知 + 分叉 + 涌现 + 栖息地 + 伪信号识别 + 资源分配 | "找新方向/做创新"、点子组合管理、押注分配、辨真假信号 | 想法组合/管线 + 信号过滤器 + 押注分配 + 伪信号护栏 | architect 设计创新组织；这个**真的跑创新管线** |
| **ai-native-org** | 运营/编排 AI-native 组织：调度 agent 队、跑运营节奏、异常路由到判断节点、保上下文新鲜、跑可观测/复审队列 | "运行/运营我的 AI-native 组织"、编排 agent 团队、建复审队列 | 运营 runbook/编排 + 复审队列路由 + 节奏 | architect **设计**组织；这个**运行**组织（设计 vs 运营之分） |

每个执行层 skill 开场都先过 `_core/redraw-vs-graft.md` 自检：若把 AI 拿掉这活会塌回旧流程 → 那是赋能不是原生，先纠偏。

## 3. 用 skill-creator 的施工流程（每个 skill 走一遍）

1. **Capture Intent**（本文件即此阶段产物）。
2. **写 SKILL.md** — 渐进披露，<500 行；域深度入 `references/`，引用共享 `_core`。
3. **evals/evals.json** — 每 skill 2–3 个真实任务 prompt。
4. **跑测** — 每个 eval 同回合并行 spawn `with_skill` + `baseline`（新建 skill 的 baseline = 无 skill）。
5. **量化** — `aggregate_benchmark` 出 benchmark.json + `generate_review.py` 出评审器（headless 用 `--static`）。
6. **质量闸** — 叠加 `_core/council.md` 的 5 角色对抗评审（域专属定性门）。
7. **迭代** — 据 feedback 改 → 进 `iteration-N+1/` 重跑。
8. **description 优化** — `run_loop.py` 跑触发优化（用本会话 model id）。
9. **打包/发布** — 更新 `.claude-plugin/{plugin.json,marketplace.json}` 收 7 个 skill → 建公开仓库 → push。

## 4. 待确认的一处承重决策

`architect` 与 6 个执行层 skill 的关系（见 §5 问题）。其余（命名保 `ai-native-architect`、公开发布、整套一次到位）已定。
