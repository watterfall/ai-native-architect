# AI-Native Tool Registry — curated

> The tool layer of the seven-skill system, hand-curated. **"Tool" is meant broadly** — three tiers per surface: **thinking tools / frameworks** (the lenses you think *with* — the methodology's own plus the classics it builds on), **simple tools** we author (no install — checklists, scorecards, canvases, portable prompts), and **open-source tools** that are genuinely AI-native by design.

> **What earns a place (software tier):** the tool would be *incoherent before LLM agents* — the agent IS the worker, not an AI feature bolted onto a pre-existing system. **Excluded:** generic pre-AI infra; **grafts** (AI layered onto an existing app/workflow); nascent/unproven (<500★); redundant near-duplicates. The **thinking-tools tier** has no such bar — a pre-AI framework (Coase, Bjork, OODA) counts when the methodology repurposes it for the AI-native era.

> **Verification:** every software repo confirmed real via `gh api`; ★ gh-measured. **Honest coverage:** learning and innovation have almost no AI-native-by-design OSS yet — those surfaces lean on the thinking tools + authored simple tools, and that gap is itself a signal.


---


## Organization (operate) · `ai-native-org`

**Thinking tools / frameworks:**
- **T1** _(this)_ — org = distribution of judgment × flow of context
- **Redraw-vs-graft test** _(this)_ — native vs enablement gate
- **The 16 bottlenecks** B.01–16 _(this)_ — structural-defect diagnostic
- **The Coase dial** _(Coase 1937 / Williamson)_ — make-vs-buy as a dial + asset-specificity caveat
- **VSM / cybernetics** _(Beer, Brain of the Firm)_ — the org as a steered S1–S5 system
- **OODA loop** _(Boyd)_ — judgment cadence

**Simple tools (author — no install):** **The Named-Human Stop-Line Checklist** _(checklist)_ · **Agent-Fleet Operability Scorecard (0-16)** _(scorecard)_ · **Live-Org Judgment-Flow Canvas** _(canvas)_ · **Incident Triage Worksheet — Hold-for-Human** _(worksheet)_ · **Run-the-Loop Portable Prompt** _(portable-prompt)_

**Open-source — representative AI-native designs:**

| tool | repo | ★ | why AI-native (pointless pre-agents) | serves |
|---|---|---|---|---|
| HumanLayer | [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | 10,995 | Incoherent before LLM agents: its entire reason to exist is that an autonomous worker now executes by default and must reach back  | stop-line / human judgment node — the named-human approval gate where exceptions |
| LangGraph | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 34,935 | Borderline but passes: a generic DAG/workflow engine is pre-AI infra (Temporal/Airflow), which the brief excludes. What clears the | the org's AI-native loop — parallel agent fan-out with explicit human judgment-n |
| Langfuse | [langfuse/langfuse](https://github.com/langfuse/langfuse) | 29,201 | No referent before LLM agents: its primitives are trace=LLM call and eval=judge-an-LLM-output. No LLM traces, no LLM-as-judge, no  | the eval/observability spine — full-traffic telemetry by default so the few huma |
| NeMo Guardrails | [NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 6,451 | Meaningless before LLM agents: programmable guardrails for LLM-based conversational systems are policy-as-code wrapping a generati | the stop-line as automated policy gate — codifiable judgment written as rails so |
| Promptfoo | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 22,276 | No pre-agent referent: a test runner whose units-under-test are prompts and agent behaviors and whose failures are jailbreaks, hal | the verification spine as automated gate — pre-deployment adversarial/quality ch |

## Engineering · `ai-native-engineering`

**Thinking tools / frameworks:**
- **Reversibility × blast-radius** _(this)_ — where to place the human gate
- **Verifiability gradient** _(this)_ — flow → test → eval → human-only
- **Delegate / Review / Own** _(this)_ — agent-output trust tiering
- **Evals are frozen judgment** _(this)_ — the verification-spine principle
- **Spec-as-source-of-truth** _(spec-driven dev)_ — the spec, not the chat, is canonical
- **Conway’s law** _(Conway)_ — the system mirrors its communication structure

**Simple tools (author — no install):** **Reversibility x Blast-Radius Tiering Card** _(worksheet)_ · **JUDGMENT.md Canvas** _(canvas)_ · **Agent-Output Trust Scorecard (0-16)** _(scorecard)_ · **Loop Driver Portable Prompt** _(portable-prompt)_ · **Pre-Merge Gate Checklist** _(checklist)_

**Open-source — representative AI-native designs:**

| tool | repo | ★ | why AI-native (pointless pre-agents) | serves |
|---|---|---|---|---|
| Spec Kit | [github/spec-kit](https://github.com/github/spec-kit) | 112,574 | Pre-agents there was no actor that consumed a natural-language spec and produced working code — specs were human-read design docs. | node |
| OpenHands | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 77,345 | It is a runtime whose only purpose is to host an autonomous software engineer. Without an LLM agent there is no worker to run — th | loop |
| SWE-agent | [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) | 19,529 | Its central contribution — an Agent-Computer Interface engineered specifically so a language model can navigate and edit a codebas | loop |
| SWE-bench | [SWE-bench/SWE-bench](https://github.com/SWE-bench/SWE-bench) | 5,187 | The task formulation — 'resolve this real-world issue end-to-end and pass the hidden test suite' — is only a meaningful, hard benc | loop |
| BMAD-METHOD | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | 49,214 | The method's core move — encoding agile roles AS distinct AI agents that pass structured story/context files to a coding agent — i | node |
| container-use | [dagger/container-use](https://github.com/dagger/container-use) | 3,868 | Per-agent ephemeral, revertable dev environments are a non-sequitur in a pre-agent world: human developers don't need disposable s | stop-line |

## Design · `ai-native-design`

**Thinking tools / frameworks:**
- **Taste = the scarce judgment** _(this)_ — the core lens
- **Spread → converge** _(this)_ — generate many cheaply, judge with taste
- **Fingerprint vs the mean** _(this)_ — anti-homogenization
- **The slop checklist** _(this)_ — the tells of the AI mean
- **Generation × taste allocation** _(this)_ — where to spend the human
- **Don’t lint the soft criteria** _(this)_ — the stop-line principle

**Simple tools (author — no install):** **The Taste Fork (parallel-variant judgment checklist)** _(checklist)_ · **0-16 Design-as-Code Readiness Scorecard** _(scorecard)_ · **Variant-and-Stop-Line Canvas** _(canvas)_ · **Portable Parallel-Critique Prompt** _(portable-prompt)_ · **Token Source-of-Truth Worksheet** _(worksheet)_

**Open-source — representative AI-native designs:**

| tool | repo | ★ | why AI-native (pointless pre-agents) | serves |
|---|---|---|---|---|
| Onlook | [onlook-dev/onlook](https://github.com/onlook-dev/onlook) | 25,940 | Pointless before LLM agents: its reason to exist is that an agent translates visual/NL intent into correct mutations of real produ | loop — the AI-native design-to-code edit loop where the human steers visually an |
| screenshot-to-code | [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) | 72,927 | Incoherent before multimodal LLMs: the core operation is a vision-language model looking at a pixel image and emitting correct, st | loop — the image-to-code generation-and-visual-verification loop |
| OpenUI | [wandb/openui](https://github.com/wandb/openui) | 22,403 | Incoherent before LLM agents: the whole interaction is 'imagine UI in words, see it rendered' — a natural-language-to-interface co | loop — the natural-language-to-rendered-UI generation/iteration loop |
| Superdesign | [superdesigndev/superdesign](https://github.com/superdesigndev/superdesign) | 6,575 | Pointless pre-agents: its defining move is generating N divergent full design candidates at once for the human to choose from. Pro | node — taste/selection is the explicit human judgment node; the agent only suppl |

## Research · `ai-native-research`

**Thinking tools / frameworks:**
- **Two-axis credibility ledger** _(this)_ — evidence strength × distance-from-paradigm, never one score
- **Claims vs evidence, unmixed** _(this)_ — keep the two columns separate
- **The worth-knowing fork** _(this)_ — machine-checkable vs constitutive
- **Replication is the verifier** _(Open Science Collab. 2015)_ — reproduce, don’t trust
- **Evidence grades Ⅰ–Ⅴ** _(this)_ — the graded register
- **Organized skepticism** _(Merton, CUDOS norms)_ — the norm of doubt

**Simple tools (author — no install):** **Believability Ledger Card (two-axis, never one score)** _(worksheet)_ · **Worth-Knowing Self-Test (the stop-line you cannot outsource)** _(checklist)_ · **0-16 Research-Loop Fidelity Scorecard** _(scorecard)_ · **Evidence-Base-First Canvas (the knowledge graph is the spec)** _(canvas)_ · **Portable Research-Triage Prompt (runs the loop in any chatbot)** _(portable-prompt)_

**Open-source — representative AI-native designs:**

| tool | repo | ★ | why AI-native (pointless pre-agents) | serves |
|---|---|---|---|---|
| PaperQA2 | [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 8,713 | Not a search index or a RAG library you query — it runs a multi-step gather/read/cite/verify loop and refuses unsupported claims.  | loop + stop-line — runs the literature loop, leaves the final credibility verdic |
| STORM | [stanford-oval/storm](https://github.com/stanford-oval/storm) | 28,378 | Its core mechanism is LLM agents role-playing distinct expert personas and interrogating each other to surface questions a single  | loop — drives research breadth; the human still signs off on the synthesized rep |
| The AI Scientist | [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 13,980 | The whole artifact is 'the agent IS the scientist': it only makes sense if an LLM can autonomously hold the ideate-to-paper loop.  | loop + stop-line — automates the full research loop while making the automated r |
| GPT Researcher | [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 27,740 | Borderline but passes: pre-agents this looks like a search engine plus a human writing the report. The defining feature — an agent | loop — the research/grounding loop feeding innovation; it is also the retrieval  |
| Tongyi DeepResearch | [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | 19,418 | A model trained specifically to be a research agent (long-horizon tool-use trajectories are the training objective). The entire pr | loop — the autonomous long-horizon research loop; human retains the final credib |

## Learning · `ai-native-learning`

**Thinking tools / frameworks:**
- **Desirable difficulty** _(Bjork)_ — the difficulty worth keeping with the human (the stop-line)
- **The offload-boundary** _(this)_ — constitutiveness × outsourceability decides what to hand over
- **Retrieval practice / testing effect** _(Roediger–Karpicke)_ — recall, don’t reread
- **Spacing & interleaving** _(Bjork)_ — as a thinking frame, not the Anki app
- **ZPD / scaffolding** _(Vygotsky)_ — scaffold vs crutch
- **The generation effect** _(Slamecka–Graf)_ — answer first, then check

**Simple tools (author — no install):** **Self-Answer-First Retrieval Card** _(portable-prompt)_ · **Cognitive Outsourcing Audit (0-16)** _(scorecard)_ · **Desirable-Difficulty Canvas** _(canvas)_ · **Error & Reflection Log Worksheet** _(worksheet)_ · **Socratic-Guardrail Tutor Prompt** _(portable-prompt)_

**Open-source — representative AI-native designs:**

| tool | repo | ★ | why AI-native (pointless pre-agents) | serves |
|---|---|---|---|---|
| PocketFlow Codebase-Knowledge Tutorial Generator | [The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge) | 12,390 | Incoherent before LLM agents: not an indexer or doc-site generator. Its value is an agent doing the comprehension labor a senior e | loop — the source-to-study-artifact loop: arbitrary codebase in, a teachable sur |

_Sparsest surface — one OSS tool clears the bar; the thinking tools + five simple tools carry it._

## Innovation · `ai-native-innovation`

**Thinking tools / frameworks:**
- **Effectuation** _(Sarasvathy)_ — bird-in-hand · affordable loss · crazy-quilt
- **Signal-to-noise under abundance** _(this)_ — the core problem when generation is free
- **Falsify before polish** _(this; Popper)_ — break it before you dress it up
- **Value-perception compass** _(this)_ — who-pays and who-defines-value on the same row
- **The useless-tree / divergence 散木** _(this; Zhuangzi)_ — an exploration reserve
- **Goodhart’s law** _(Goodhart)_ — the metric-gaming guard
- **NK fitness landscapes** _(Kauffman)_ — explore vs exploit

**Simple tools (author — no install):** **Looks-Feasible Trap Self-Test (pen & paper)** _(checklist)_ · **Worth-It Value Compass Scorecard (0-16)** _(scorecard)_ · **Bet & Falsification Canvas (one page)** _(canvas)_ · **Portable Signal-vs-Noise Prompt (paste into any chatbot)** _(portable-prompt)_ · **Useless-Tree Retention Check (worksheet)** _(worksheet)_

**Open-source — representative AI-native designs:**

| tool | repo | ★ | why AI-native (pointless pre-agents) | serves |
|---|---|---|---|---|
| AI Scientist v2 | [SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | 6,589 | Pointless before LLM agents: there is no non-agent reading of 'a program that conceives a research idea, codes the experiment, int | loop — the discover→experiment→analyze→write autonomous innovation loop; the hum |
| AI-Researcher | [HKUDS/AI-Researcher](https://github.com/HKUDS/AI-Researcher) | 5,480 | Incoherent pre-agents: its reason to exist is 'autonomous scientific innovation' — generating *novel* research directions and exec | loop — the ideation→build→validate innovation loop, with value-perception (is th |

_AI-native OSS here is mostly autonomous AI-scientist agents (shared with research); pure ideation/bet tooling barely exists yet._

---

## Cross-cutting AI-native platforms (≥2 surfaces)

| platform | repo | surfaces | why AI-native |
|---|---|---|---|
| Model Context Protocol (MCP) | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | org, engineering, design, research, learning, innovation | MCP exists only to give an autonomous model a standardized way to reach for tools and context at runtime. |
| Agent2Agent (A2A) | [a2aproject/A2A](https://github.com/a2aproject/A2A) | org, engineering, research | A2A standardizes one autonomous agent delegating a task to another autonomous agent it did not build. Wit |
| AG-UI Protocol | [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) | design, engineering, learning | AG-UI defines the wire format for an agent rendering and mutating interface state mid-conversation, inclu |
| LangGraph | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | — | Borderline but passes: a generic DAG/workflow engine is pre-AI infra (Temporal/Airflow), which the brief  |
| CrewAI | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | org, engineering, research, innovation | The entire abstraction — agents with roles delegating to each other toward a shared goal — is incoherent  |
| Graphiti | [getzep/graphiti](https://github.com/getzep/graphiti) | org, research, learning, engineering | Graphiti's reason to exist is giving an agent a continuously-updated, time-aware memory it can query mid- |
| Langfuse | [langfuse/langfuse](https://github.com/langfuse/langfuse) | — | No referent before LLM agents: its primitives are trace=LLM call and eval=judge-an-LLM-output. No LLM tra |
| Promptfoo | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | — | No pre-agent referent: a test runner whose units-under-test are prompts and agent behaviors and whose fai |
| NeMo Guardrails | [NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | — | Meaningless before LLM agents: programmable guardrails for LLM-based conversational systems are policy-as |

---

## Deliberately cut (software tier — transparency)

- **Generic / pre-AI infra:** Style Dictionary · Tokens Studio · axe-core · shadcn/ui · Penpot · Storybook · GROBID · scispaCy · Snakemake · Anki/FSRS · PostHog · GrowthBook · Flipt · Metaforecast · LiteLLM · Chroma · pyalex · LitStudy.
- **Grafts onto existing systems:** CopilotKit · Tambo · Qodo Cover · SurfSense · Podcastfy · PR-Agent.
- **Nascent (<500★):** Invariant · Aviary · Arbor · open-coscientist · Vibe-learning · autoresearch-novelty-bench (★3).
- **Redundant:** OpenSpec≈spec-kit · EvalPlus/Terminal-Bench≈SWE-bench · Opik/Phoenix≈Langfuse · DeepEval/Inspect AI≈promptfoo · mem0 · ToolUniverse.
