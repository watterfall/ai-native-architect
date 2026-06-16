# AI-Native Architect v3 Design

Date: 2026-06-17
Status: approved direction, pre-implementation spec

## Purpose

This iteration upgrades `ai-native-architect` from a strong plugin/docs repository into a sharper public
entry point for founders, operators, and team leads. The repository should still be a seven-skill system
over one shared kernel, but it needs a better first-contact layer:

- system evaluation and testing docs that make the skills feel verified, not merely asserted;
- a lightweight static buffer homepage that quickly frames the core AI-Native problem;
- restrained visual assets for the six execution modules;
- softer, more precise copy around the "not AI-Native" distinction.

The buffer page is not the canonical methodology site. It is a high-quality frontispiece that caches,
orients, and then sends users to the existing AI Native Organization Methodology homepage.

## Target User

Primary users are founders, operators, and team leads. They are not primarily browsing for a developer
tool; they are trying to decide whether their company, venture, or unit needs a structural redraw rather
than more AI tools. The page must help them confront that question quickly, then give them the next path:
read the full methodology, stay for the skill atlas, or install the skills.

Secondary users are Claude Code / agent-tool users and methodology readers. They matter, but they should
not pull the first screen into a developer dashboard or academic table of contents.

## Design Direction

Visual direction: **editorial atlas / methodology frontispiece**.

The page should feel like the opening plate of a serious method: minimal, high-contrast, exact, bilingual,
and intentionally paced. Avoid product-marketing hero clutter. Avoid sensational copy. Avoid generic AI
visual language such as purple-blue gradients, glowing network spheres, oversized chat bubbles, and
uniform SaaS card grids.

The approved headline is:

> 当执行不再稀缺，组织需要重新设计。
> When execution is no longer scarce, the organization must be redesigned.

This replaces harsher or clickbait-like framing. It is sharp because it is structurally precise, not
because it attacks the reader.

## Static Buffer Homepage

Add a lightweight static entry surface in this repository. Recommended shape:

- `site/index.html`
- `site/assets/styles.css`
- `site/assets/app.js`
- `site/assets/images/*`
- optional `site/README.md` explaining preview and deployment

No heavy framework is needed unless implementation discovers a strong reason. A static page keeps the
repo easy to browse, deploy, and cache.

### Behavior

The buffer page should:

- show the approved core premise immediately;
- display a visible countdown, around 8 seconds by default;
- automatically redirect to the existing AI Native Organization Methodology homepage;
- expose three actions:
  - `Skip to methodology`;
  - `Stay for skill atlas`;
  - `Install the 7 skills`;
- pause or cancel redirect when the user chooses to stay, interacts with the page, or has reduced-motion
  preferences that make the countdown disruptive;
- keep the redirect target in one config value, for example `METHODOLOGY_HOME_URL`, so the final URL can
  be replaced without editing multiple files.

The redirect target is the current AI Native Organization Methodology homepage from the existing
`ainative` site, corresponding to the AI-Native organization page / `dist/index.html`. Implementation
should keep this as a single constant. For local verification, the default may point to the sibling
workspace's built homepage (`/Users/jili/AIAI/ainative/dist/index.html` or an equivalent local preview
URL). For deployment, replace that single value with the canonical public methodology URL.

### First Screen

First screen content should be sparse:

- small product mark: `AI-Native Architect`;
- label: `THE PREMISE`;
- headline:
  - `当执行不再稀缺，组织需要重新设计。`
  - `When execution is no longer scarce, the organization must be redesigned.`
- one supporting sentence:
  - Chinese: "AI-Native 的分界不在工具数量，而在执行、判断与上下文是否被重新分配。"
  - English: "The boundary is not how many AI tools you use; it is whether execution, judgment, and context are redistributed by design."
- countdown / redirect status;
- the three actions.

### Stay Layer

If the user chooses `Stay for skill atlas`, reveal a second layer rather than navigating away. This layer
should stay compact and support the buffer page's role:

- a seven-skill atlas: one architecture-tier skill plus six execution-tier skills;
- six execution modules with bilingual labels;
- for each execution module:
  - input;
  - work product;
  - human stop-line;
  - context write-back;
  - two images;
- a small eval evidence strip linking to `docs/VALIDATION.md` and skill eval files;
- install block with Claude Code plugin commands.

The stay layer should not become a full website. It is a compressed atlas that persuades the user the
system is executable, then routes them onward.

## Image Assets

Generate 12 images with image-2: 2 images for each execution module.

Style constraints for all images:

- restrained editorial atlas style;
- no generic AI sci-fi;
- no neon gradients, glowing robot hands, floating chat bubbles, or decorative orbs;
- no embedded text unless required by the image prompt, because text rendering will be unreliable;
- useful as visual anchors on a serious methodology page;
- consistent aspect ratio, preferably landscape or wide card-friendly.

Per module:

1. Engineering
   - work scene: spec, eval suite, permission boundary, human sign-off around irreversible action;
   - mechanism image: verifiability spine from spec to tests/evals to judgment gate.
2. Design
   - work scene: divergent candidate spread converging through human taste;
   - mechanism image: design tokens + fingerprint check + decision log.
3. Research
   - work scene: evidence ledger and knowledge graph around competing claims;
   - mechanism image: two-axis credibility ledger, conflict edges, blind-spot register.
4. Learning
   - work scene: learner self-answering before AI help, reflection store visible;
   - mechanism image: desirable difficulty boundary and scaffold/crutch line.
5. Innovation
   - work scene: many polished ideas being falsified before polish;
   - mechanism image: value-perception compass, affordable-loss bet sheet, who-pays row.
6. Org
   - work scene: agent fleet operating with named human exception nodes;
   - mechanism image: review queue, context upkeep feed, observability loop.

The final prompts and saved paths should be recorded in a project document, likely
`site/assets/images/README.md` or `docs/visual-assets.md`.

## Skills, Evals, And Docs Upgrade

This iteration should harden the system documents and the skills themselves.

### Skill Files

Review all seven `skills/*/SKILL.md` files for:

- trigger clarity;
- altitude discipline: architect designs the org; execution skills do the work;
- output contracts written as real deliverables, not advice;
- human stop-lines stated without overclaiming;
- context write-back as a concrete artifact;
- softer but still honest redraw-vs-graft language.

Do not dilute the boundary. The tone should become less abrupt, not less clear.

Preferred framing pattern:

> From AI-assisted work to AI-Native work, the question changes from "which tool helps this step?" to
> "how should execution, judgment, and context be redistributed?"

Chinese pattern:

> 从 AI 辅助到 AI-Native，问题不再是"哪个工具能帮这一步"，而是"执行、判断与上下文应该如何重新分配"。

### Eval Files

Review all seven `skills/*/evals/evals.json` files for:

- at least three meaningful evals per skill where practical;
- one positive path, one graft/boundary path, and one hard edge case;
- expected outputs that assert concrete artifacts and failure-mode coverage;
- consistency of `pass_criterion` across all skills.

Do not add large synthetic benchmark machinery unless needed. The current repo is lightweight; the eval
upgrade should make review stronger without creating a maintenance burden.

### Validation Docs

Update `docs/VALIDATION.md` and related docs so the reader can answer:

- what was evaluated;
- what changed in this iteration;
- what remains limited;
- how someone can reproduce or extend the evaluation;
- how council review and lightweight quantitative evals relate.

The validation story should be more operational: "what would fail this skill?" should be visible.

### Existing README And Docs

Update README and docs to point to the new buffer page, clarify the two-tier system, and soften the
opening negative framing. Keep the README as the authoritative GitHub entry. The buffer page is a visual
entry, not a replacement.

## Copy Updates

Replace brittle "what is not AI-Native" introductions with transition framing:

- "从使用 AI，到 AI-Native";
- "从加速节点，到重画工作图";
- "从工具辅助，到执行、判断与上下文的重新分配";
- "From AI-assisted work to AI-Native work";
- "From accelerating nodes to redrawing the graph."

Avoid wording that implies the reader is wrong or unsophisticated. The boundary remains firm, but the
entry should invite understanding before correction.

## Organization Premise Update

For the organization section's `THE PREMISE`, use the approved structure:

1. execution is no longer scarce;
2. judgment becomes the scarce node;
3. context becomes the compounding asset;
4. organization must be redesigned around that redistribution.

This should appear visually as a premise map, not as a dense paragraph.

## Acceptance Criteria

- A static buffer page exists and can be opened locally without a build step.
- The page redirects to a single configured methodology-home URL after a visible countdown.
- The page lets users skip, stay, or install without fighting the redirect.
- The stay layer shows the seven-skill atlas and six execution modules.
- Twelve final image assets are saved in the repo and referenced by the page.
- Public-facing new page copy is bilingual.
- Skills/evals/docs are reviewed and materially improved.
- The harsh "what is not AI-Native" framing is softened without weakening scope honesty.
- `THE PREMISE` is redesigned around the scarcity-inversion sequence.
- Verification includes at least local page preview, link/asset checks, and JSON validity for eval files.

## Non-Goals

- Do not build a large multi-page marketing site.
- Do not replace the existing AI Native Organization Methodology homepage.
- Do not introduce a heavy frontend framework unless implementation discovers a concrete need.
- Do not turn the skill repository into a design portfolio.
- Do not weaken the AI-Native vs AI-enabled distinction for the sake of friendliness.
- Do not use generated images as evidence; they are explanatory visual anchors only.

## Redirect Configuration

Use one redirect constant only, for example `METHODOLOGY_HOME_URL`.

Local verification target: the sibling `ainative` repository's built homepage, `dist/index.html`, served
by a local static server.

Deployment target: the canonical public URL for the existing AI Native Organization Methodology homepage.
If that URL is not present in the repository at implementation time, keep the public value in one obvious
configuration line and document it in `site/README.md` so it can be replaced without code search.
