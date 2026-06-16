# AI-Native Architect V3 Buffer Home Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the approved bilingual static buffer homepage, generate and wire 12 restrained module images, and harden the skills/evals/docs around the v3 positioning.

**Architecture:** Keep the repository lightweight: static HTML/CSS/JS under `site/`, project-bound image assets under `site/assets/images/`, and validation with small Node scripts that use only built-in modules. The existing README and skill files remain the canonical plugin/docs source; the buffer page is a visual frontispiece that redirects to the existing AI Native Organization Methodology homepage through one configurable constant.

**Tech Stack:** Static HTML, CSS, vanilla JavaScript, built-in Node.js validation scripts, Markdown docs, JSON eval files, built-in `image_gen` for raster assets.

---

## File Structure

- Create `site/index.html`: bilingual buffer page and stay-layer markup.
- Create `site/assets/styles.css`: editorial atlas visual system, responsive layout, countdown, stay-layer, module atlas.
- Create `site/assets/app.js`: redirect timer, language toggle, stay behavior, module tab switching.
- Create `site/assets/images/manifest.json`: canonical list of 12 image assets and alt text.
- Create `site/assets/images/README.md`: saved asset paths and prompts used for image generation.
- Create `site/README.md`: local preview, redirect configuration, deployment notes.
- Create `docs/visual-assets.md`: image plan and final prompts for review.
- Create `scripts/validate-site.mjs`: static checks for page assets, manifest, redirect constant, bilingual copy, and image references.
- Modify `README.md`: add buffer page entry, soften introductory framing, link validation and site.
- Modify `docs/VALIDATION.md`: add v3 evaluation-hardening section and failure conditions.
- Modify `docs/SYSTEM-DESIGN.md`: note buffer page as distribution frontispiece, not canonical methodology.
- Modify all `skills/*/SKILL.md`: soften "not AI-Native" opening language while preserving boundary honesty.
- Modify all `skills/*/evals/evals.json`: normalize pass criteria and add/adjust hard edge coverage.

---

### Task 1: Add Static Site Scaffold And Validation Script

**Files:**
- Create: `site/index.html`
- Create: `site/assets/styles.css`
- Create: `site/assets/app.js`
- Create: `site/assets/images/manifest.json`
- Create: `site/README.md`
- Create: `scripts/validate-site.mjs`

- [ ] **Step 1: Create directories**

Run:

```bash
mkdir -p site/assets/images scripts
```

Expected: directories exist.

- [ ] **Step 2: Create `site/index.html`**

Use this structure and fill only with committed bilingual copy, not temporary draft copy:

```html
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AI-Native Architect</title>
  <meta name="description" content="当执行不再稀缺，组织需要重新设计。A bilingual buffer page for the AI-Native Architect seven-skill system.">
  <link rel="stylesheet" href="./assets/styles.css">
</head>
<body>
  <main class="page-shell" data-state="redirecting">
    <section class="cover" aria-labelledby="premise-title">
      <nav class="topline" aria-label="Primary">
        <a class="brand" href="https://github.com/watterfall/ai-native-architect">AI-Native Architect</a>
        <div class="nav-actions">
          <button class="text-button" type="button" data-lang-toggle aria-pressed="false">EN</button>
          <button class="text-button" type="button" data-stay>Stay</button>
          <a class="text-button" data-skip href="#">Skip</a>
        </div>
      </nav>

      <div class="cover-grid">
        <div class="cover-copy">
          <p class="eyebrow">THE PREMISE</p>
          <h1 id="premise-title">
            <span lang="zh">当执行不再稀缺，组织需要重新设计。</span>
            <span lang="en">When execution is no longer scarce, the organization must be redesigned.</span>
          </h1>
          <p class="lede">
            <span lang="zh">AI-Native 的分界不在工具数量，而在执行、判断与上下文是否被重新分配。</span>
            <span lang="en">The boundary is not how many AI tools you use; it is whether execution, judgment, and context are redistributed by design.</span>
          </p>
          <div class="cta-row" aria-label="Actions">
            <a class="primary-action" data-skip href="#">进入方法论首页 · Methodology</a>
            <button class="secondary-action" type="button" data-stay>停留查看 skill 图册 · Skill atlas</button>
            <a class="secondary-action" href="#install">安装 7 个 skills · Install</a>
          </div>
        </div>

        <aside class="premise-map" aria-label="Premise map">
          <div class="map-step"><b>01</b><span>执行不再稀缺<br><em>Execution abundance</em></span></div>
          <div class="map-step"><b>02</b><span>判断成为节点<br><em>Judgment nodes</em></span></div>
          <div class="map-step"><b>03</b><span>上下文成为资产<br><em>Context compounds</em></span></div>
          <div class="map-step"><b>04</b><span>组织重画工作图<br><em>Redraw the graph</em></span></div>
        </aside>
      </div>

      <div class="redirect-strip" role="status" aria-live="polite">
        <span data-countdown>08</span>
        <span lang="zh">秒后进入现有 AI Native 组织方法论首页</span>
        <span lang="en">seconds until the existing methodology homepage opens</span>
      </div>
    </section>

    <section class="atlas" id="atlas" aria-labelledby="atlas-title">
      <div class="section-heading">
        <p class="eyebrow">THE SKILL ATLAS</p>
        <h2 id="atlas-title">一张架构图，六个执行面。</h2>
        <p>One architecture surface designs the organization; six execution surfaces do the work.</p>
      </div>

      <div class="module-tabs" role="tablist" aria-label="Execution modules">
        <button role="tab" aria-selected="true" data-module="engineering">Engineering</button>
        <button role="tab" aria-selected="false" data-module="design">Design</button>
        <button role="tab" aria-selected="false" data-module="research">Research</button>
        <button role="tab" aria-selected="false" data-module="learning">Learning</button>
        <button role="tab" aria-selected="false" data-module="innovation">Innovation</button>
        <button role="tab" aria-selected="false" data-module="org">Org</button>
      </div>

      <div class="module-panel" data-module-panel></div>

      <div class="evidence-strip">
        <a href="../docs/VALIDATION.md">Validation record</a>
        <a href="../skills-eval-workspace/iteration-1/BENCHMARK.md">With-skill benchmark</a>
        <a href="../docs/SYSTEM-DESIGN.md">System design</a>
      </div>
    </section>

    <section class="install" id="install" aria-labelledby="install-title">
      <div>
        <p class="eyebrow">INSTALL</p>
        <h2 id="install-title">安装完整七 skill 系统</h2>
        <p>Install the full seven-skill system in Claude Code.</p>
      </div>
      <pre><code>/plugin marketplace add watterfall/ai-native-architect
/plugin install ai-native-architect@ai-native-architect</code></pre>
    </section>
  </main>

  <script src="./assets/app.js"></script>
</body>
</html>
```

- [ ] **Step 3: Create `site/assets/app.js`**

Use this implementation:

```js
const METHODOLOGY_HOME_URL = "../ainative/dist/index.html";
const REDIRECT_SECONDS = 8;

const modules = {
  engineering: {
    title: "Engineering · 工程",
    input: "A software task that must become runnable, verifiable code.",
    product: "Code + SPEC + eval suite + JUDGMENT.md + PERMISSIONS.md.",
    stopLine: "Irreversible or high-blast-radius actions require named human sign-off.",
    context: "Every discovered failure becomes a new eval or boundary rule.",
    images: ["engineering-work-scene.webp", "engineering-mechanism.webp"]
  },
  design: {
    title: "Design · 设计",
    input: "A product, interface, flow, expression, motion piece, or design system.",
    product: "Artifact + tokens + taste rationale + fingerprint check.",
    stopLine: "Taste and final convergence stay human; generation supplies candidates.",
    context: "Winning criteria and rejected directions feed the design system.",
    images: ["design-work-scene.webp", "design-mechanism.webp"]
  },
  research: {
    title: "Research · 研究",
    input: "A question, claim batch, literature set, or direction worth testing.",
    product: "Finding dossier + credibility ledger + graph contribution + blind spots.",
    stopLine: "Final credibility and worth-knowing verdicts stay human.",
    context: "Claims enter with evidence edges, conflict edges, and re-check triggers.",
    images: ["research-work-scene.webp", "research-mechanism.webp"]
  },
  learning: {
    title: "Learning · 学习",
    input: "A capacity someone must actually retain and transfer.",
    product: "Learning protocol + offload boundary + scaffold + reflection store.",
    stopLine: "Desirable difficulty stays with the learner.",
    context: "Reflection entries and removal drills update the next practice cycle.",
    images: ["learning-work-scene.webp", "learning-mechanism.webp"]
  },
  innovation: {
    title: "Innovation · 创新",
    input: "A noisy set of directions, ideas, or bets under generative abundance.",
    product: "Portfolio + falsification log + value compass + bet sheet.",
    stopLine: "The bet and who-bears-cost judgment stay human.",
    context: "Bet retrospectives calibrate future signal recognition.",
    images: ["innovation-work-scene.webp", "innovation-mechanism.webp"]
  },
  org: {
    title: "Org · 组织运营",
    input: "An already-designed AI-Native unit that needs daily operation.",
    product: "Operating runbook + review routing + cadence + context upkeep.",
    stopLine: "Trust, safety, relationship, and irreversible exceptions route to named humans.",
    context: "Decision logs, queue telemetry, and eval drift feed the operating loop.",
    images: ["org-work-scene.webp", "org-mechanism.webp"]
  }
};

const root = document.querySelector(".page-shell");
const countdown = document.querySelector("[data-countdown]");
const skipLinks = document.querySelectorAll("[data-skip]");
const stayButtons = document.querySelectorAll("[data-stay]");
const langToggle = document.querySelector("[data-lang-toggle]");
const modulePanel = document.querySelector("[data-module-panel]");
const moduleTabs = document.querySelectorAll("[data-module]");

let remaining = REDIRECT_SECONDS;
let redirectTimer = null;
let redirectCancelled = false;

function setSkipTargets() {
  skipLinks.forEach((link) => {
    link.setAttribute("href", METHODOLOGY_HOME_URL);
  });
}

function cancelRedirect() {
  redirectCancelled = true;
  root.dataset.state = "staying";
  if (redirectTimer) window.clearInterval(redirectTimer);
}

function startRedirect() {
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  redirectTimer = window.setInterval(() => {
    remaining -= 1;
    countdown.textContent = String(Math.max(remaining, 0)).padStart(2, "0");
    if (remaining <= 0 && !redirectCancelled) {
      window.location.href = METHODOLOGY_HOME_URL;
    }
  }, 1000);
}

function renderModule(key) {
  const item = modules[key];
  modulePanel.innerHTML = `
    <article class="module-card">
      <div class="module-copy">
        <p class="eyebrow">${item.title}</p>
        <dl>
          <dt>Input</dt><dd>${item.input}</dd>
          <dt>Work product</dt><dd>${item.product}</dd>
          <dt>Human stop-line</dt><dd>${item.stopLine}</dd>
          <dt>Context write-back</dt><dd>${item.context}</dd>
        </dl>
      </div>
      <div class="module-images">
        <img src="./assets/images/${item.images[0]}" alt="${item.title} work scene">
        <img src="./assets/images/${item.images[1]}" alt="${item.title} mechanism diagram">
      </div>
    </article>
  `;
}

function setLanguage(nextLang) {
  document.documentElement.lang = nextLang === "en" ? "en" : "zh-CN";
  document.body.dataset.lang = nextLang;
  langToggle.textContent = nextLang === "en" ? "中文" : "EN";
  langToggle.setAttribute("aria-pressed", String(nextLang === "en"));
}

setSkipTargets();
renderModule("engineering");
startRedirect();

stayButtons.forEach((button) => {
  button.addEventListener("click", () => {
    cancelRedirect();
    document.querySelector("#atlas").scrollIntoView({ behavior: "smooth", block: "start" });
  });
});

moduleTabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    cancelRedirect();
    moduleTabs.forEach((item) => item.setAttribute("aria-selected", "false"));
    tab.setAttribute("aria-selected", "true");
    renderModule(tab.dataset.module);
  });
});

langToggle.addEventListener("click", () => {
  cancelRedirect();
  setLanguage(document.body.dataset.lang === "en" ? "zh" : "en");
});
```

- [ ] **Step 4: Create `site/assets/images/manifest.json`**

Use this exact manifest shape:

```json
{
  "version": 1,
  "style": "restrained editorial atlas, no generic AI sci-fi, no embedded text",
  "assets": [
    {"module": "engineering", "kind": "work-scene", "file": "engineering-work-scene.webp", "alt": "Engineering work scene with spec, eval suite, permission boundary, and human sign-off."},
    {"module": "engineering", "kind": "mechanism", "file": "engineering-mechanism.webp", "alt": "Engineering mechanism showing a verifiability spine from spec to tests and judgment gate."},
    {"module": "design", "kind": "work-scene", "file": "design-work-scene.webp", "alt": "Design work scene with divergent candidates converging through human taste."},
    {"module": "design", "kind": "mechanism", "file": "design-mechanism.webp", "alt": "Design mechanism showing tokens, fingerprint check, and decision log."},
    {"module": "research", "kind": "work-scene", "file": "research-work-scene.webp", "alt": "Research work scene with evidence ledger and knowledge graph around competing claims."},
    {"module": "research", "kind": "mechanism", "file": "research-mechanism.webp", "alt": "Research mechanism showing credibility ledger, conflict edges, and blind-spot register."},
    {"module": "learning", "kind": "work-scene", "file": "learning-work-scene.webp", "alt": "Learning work scene with self-answer-first practice and a reflection store."},
    {"module": "learning", "kind": "mechanism", "file": "learning-mechanism.webp", "alt": "Learning mechanism showing desirable difficulty boundary and scaffold-crutch line."},
    {"module": "innovation", "kind": "work-scene", "file": "innovation-work-scene.webp", "alt": "Innovation work scene with many polished ideas being falsified before polish."},
    {"module": "innovation", "kind": "mechanism", "file": "innovation-mechanism.webp", "alt": "Innovation mechanism showing value compass, affordable-loss bet sheet, and who-pays row."},
    {"module": "org", "kind": "work-scene", "file": "org-work-scene.webp", "alt": "Organization operations work scene with an agent fleet and named human exception nodes."},
    {"module": "org", "kind": "mechanism", "file": "org-mechanism.webp", "alt": "Organization operations mechanism showing review queue, context upkeep, and observability loop."}
  ]
}
```

- [ ] **Step 5: Create `scripts/validate-site.mjs`**

Use this script:

```js
import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const site = path.join(root, "site");
const index = fs.readFileSync(path.join(site, "index.html"), "utf8");
const app = fs.readFileSync(path.join(site, "assets/app.js"), "utf8");
const manifestPath = path.join(site, "assets/images/manifest.json");
const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));

const failures = [];

function assert(condition, message) {
  if (!condition) failures.push(message);
}

assert(index.includes("当执行不再稀缺，组织需要重新设计。"), "missing approved Chinese headline");
assert(index.includes("When execution is no longer scarce"), "missing approved English headline");
assert(app.includes("const METHODOLOGY_HOME_URL"), "missing single redirect constant");
assert(app.includes("REDIRECT_SECONDS = 8"), "redirect duration must remain explicit");
assert(Array.isArray(manifest.assets), "manifest.assets must be an array");
assert(manifest.assets.length === 12, "manifest must list exactly 12 assets");

for (const asset of manifest.assets) {
  const filePath = path.join(site, "assets/images", asset.file);
  assert(asset.file.endsWith(".webp"), `${asset.file} should be a WebP asset`);
  assert(index.includes(asset.file) || app.includes(asset.file), `${asset.file} is not referenced by page code`);
  assert(fs.existsSync(filePath), `${asset.file} missing from site/assets/images`);
  assert(asset.alt && asset.alt.length >= 24, `${asset.file} needs useful alt text`);
}

const evalFiles = fs.globSync ? fs.globSync("skills/*/evals/evals.json") : [];
for (const file of evalFiles) {
  JSON.parse(fs.readFileSync(file, "utf8"));
}

if (failures.length) {
  console.error(failures.map((failure) => `- ${failure}`).join("\n"));
  process.exit(1);
}

console.log("Site validation passed.");
```

- [ ] **Step 6: Run validation and confirm expected image failures**

Run:

```bash
node scripts/validate-site.mjs
```

Expected before image generation: FAIL with 12 missing image files. No syntax errors.

- [ ] **Step 7: Commit scaffold**

Run:

```bash
git add site scripts/validate-site.mjs
git commit -m "feat(site): add buffer homepage scaffold"
```

Expected: commit succeeds.

---

### Task 2: Implement Editorial Atlas Styling

**Files:**
- Modify: `site/assets/styles.css`
- Test: `node scripts/validate-site.mjs`

- [ ] **Step 1: Create `site/assets/styles.css`**

Use CSS variables and stable dimensions:

```css
:root {
  --ink: #11130f;
  --paper: #f5efe3;
  --paper-2: #e7dfcf;
  --muted: #b8ad9e;
  --line: #514b41;
  --accent: #c7a15b;
  --panel: #191b16;
  --max: 1180px;
}

* { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  margin: 0;
  font-family: ui-serif, Georgia, "Times New Roman", serif;
  color: var(--paper);
  background: var(--ink);
}

a { color: inherit; }

button, a {
  -webkit-tap-highlight-color: transparent;
}

.page-shell {
  min-height: 100vh;
  background:
    radial-gradient(circle at 82% 18%, rgba(199, 161, 91, 0.14), transparent 28rem),
    linear-gradient(180deg, #11130f 0%, #171912 52%, #f5efe3 52%, #f5efe3 100%);
}

.cover {
  min-height: 100svh;
  width: min(100%, var(--max));
  margin: 0 auto;
  padding: clamp(20px, 3vw, 34px);
  display: flex;
  flex-direction: column;
}

.topline {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--line);
  font-size: 12px;
  letter-spacing: 0.11em;
  text-transform: uppercase;
}

.brand {
  text-decoration: none;
  font-weight: 800;
}

.nav-actions,
.cta-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
}

.text-button,
.primary-action,
.secondary-action {
  min-height: 42px;
  border: 1px solid color-mix(in srgb, var(--paper) 42%, transparent);
  background: transparent;
  color: inherit;
  text-decoration: none;
  padding: 11px 14px;
  font: inherit;
  cursor: pointer;
}

.primary-action {
  background: var(--paper);
  color: var(--ink);
  border-color: var(--paper);
  font-weight: 750;
}

.cover-grid {
  flex: 1;
  display: grid;
  grid-template-columns: minmax(0, 1.24fr) minmax(280px, 0.76fr);
  gap: clamp(28px, 6vw, 72px);
  align-items: center;
}

.eyebrow {
  margin: 0 0 14px;
  color: var(--accent);
  font-size: 12px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  font-weight: 800;
}

h1, h2 {
  margin: 0;
  line-height: 0.98;
  letter-spacing: 0;
}

h1 {
  max-width: 780px;
  font-size: clamp(44px, 7.2vw, 92px);
}

h2 {
  color: var(--ink);
  font-size: clamp(34px, 5vw, 68px);
}

.lede {
  max-width: 640px;
  margin: 26px 0 0;
  color: #d8cdbd;
  font-size: clamp(16px, 2vw, 20px);
  line-height: 1.62;
}

.premise-map {
  border: 1px solid var(--line);
  background: color-mix(in srgb, var(--panel) 86%, transparent);
  padding: 18px;
  display: grid;
  gap: 12px;
}

.map-step {
  min-height: 84px;
  border-top: 1px solid var(--line);
  padding-top: 12px;
  display: grid;
  grid-template-columns: 44px 1fr;
  gap: 12px;
  align-items: start;
}

.map-step b {
  color: var(--accent);
  font-size: 13px;
}

.map-step span {
  line-height: 1.35;
}

.map-step em {
  color: var(--muted);
  font-style: normal;
  font-size: 13px;
}

.redirect-strip {
  display: flex;
  gap: 8px;
  align-items: center;
  justify-content: flex-end;
  min-height: 40px;
  color: var(--muted);
  font-size: 13px;
}

.redirect-strip [data-countdown] {
  color: var(--paper);
  font-size: 22px;
  font-weight: 850;
}

.atlas,
.install {
  width: min(100%, var(--max));
  margin: 0 auto;
  padding: clamp(44px, 8vw, 96px) clamp(20px, 3vw, 34px);
  color: var(--ink);
}

.section-heading {
  max-width: 760px;
}

.section-heading p:not(.eyebrow) {
  color: #514b41;
  font-size: 18px;
  line-height: 1.55;
}

.module-tabs {
  margin-top: 34px;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.module-tabs button {
  border: 1px solid #c4b9a6;
  background: transparent;
  min-height: 42px;
  padding: 10px 13px;
  color: var(--ink);
  cursor: pointer;
}

.module-tabs button[aria-selected="true"] {
  background: var(--ink);
  color: var(--paper);
}

.module-panel {
  margin-top: 24px;
}

.module-card {
  display: grid;
  grid-template-columns: minmax(0, 0.86fr) minmax(320px, 1.14fr);
  gap: 24px;
  border-top: 1px solid #c4b9a6;
  padding-top: 24px;
}

dl {
  margin: 0;
  display: grid;
  gap: 14px;
}

dt {
  font-weight: 850;
}

dd {
  margin: 4px 0 0;
  color: #4f493f;
  line-height: 1.5;
}

.module-images {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.module-images img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
  border: 1px solid #c4b9a6;
  background: var(--paper-2);
}

.evidence-strip {
  margin-top: 30px;
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.evidence-strip a {
  color: var(--ink);
  border-bottom: 1px solid currentColor;
  text-decoration: none;
}

.install {
  display: grid;
  grid-template-columns: minmax(0, 0.8fr) minmax(320px, 1.2fr);
  gap: 24px;
}

pre {
  margin: 0;
  overflow-x: auto;
  border: 1px solid #c4b9a6;
  padding: 18px;
  background: #eee6d7;
  color: #181a14;
}

body[data-lang="en"] [lang="zh"],
body:not([data-lang="en"]) [lang="en"] {
  display: none;
}

@media (max-width: 820px) {
  .cover-grid,
  .module-card,
  .install {
    grid-template-columns: 1fr;
  }

  .cover {
    min-height: auto;
  }

  .cover-grid {
    padding: 68px 0 38px;
  }

  .module-images {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
}
```

- [ ] **Step 2: Verify CSS loads**

Run:

```bash
python3 -m http.server 8751 -d site
```

Expected: server starts at `http://localhost:8751`. Open or curl `http://localhost:8751/index.html`; CSS file returns HTTP 200.

- [ ] **Step 3: Stop preview server**

Run:

```bash
pkill -f "http.server 8751"
```

Expected: preview server exits.

- [ ] **Step 4: Commit styling**

Run:

```bash
git add site/assets/styles.css
git commit -m "feat(site): add editorial atlas styling"
```

Expected: commit succeeds.

---

### Task 3: Generate And Wire Twelve Image Assets

**Files:**
- Create: `site/assets/images/*.webp`
- Create: `site/assets/images/README.md`
- Create: `docs/visual-assets.md`
- Test: `node scripts/validate-site.mjs`

- [ ] **Step 1: Generate each image with built-in `image_gen`**

Use one `image_gen` call per asset. Every prompt must follow this common style block:

```text
Use case: productivity-visual
Asset type: static website module image for AI-Native Architect
Style/medium: restrained editorial atlas illustration, sober and precise, high-quality methodology plate, tactile paper and ink, subtle dimensionality
Composition/framing: landscape, 4:3, single clear focal structure, enough negative space for surrounding UI
Lighting/mood: calm, serious, analytical
Color palette: charcoal, warm paper, muted brass, muted moss, small red only for gates or warnings
Constraints: no embedded text, no logos, no generic robots, no glowing hands, no neon gradients, no floating chat bubbles, no decorative orbs, no watermark
```

Generate these 12 prompts:

```text
engineering-work-scene.webp: a software engineering worktable with a spec document, eval suite cards, a permissions boundary line, and a named human approval gate around an irreversible refund action; agents appear only as abstract worker lanes, not robots.
engineering-mechanism.webp: a clean mechanism diagram made of physical plates and lines showing spec -> deterministic tests -> evals -> human judgment gate -> learn write-back, no words rendered in the image.
design-work-scene.webp: five divergent interface drafts spread across an editorial table, converging toward a single human taste decision point, with a small token palette and rejected directions visible as muted sheets.
design-mechanism.webp: a design system mechanism with tokens, fingerprint check, candidate spread, decision log, and context feed represented as organized plates and fine connecting lines, no text.
research-work-scene.webp: a research desk with competing claim cards, evidence ledger columns, source fragments, and a knowledge graph with conflict edges, restrained and serious.
research-mechanism.webp: a two-axis credibility mechanism with evidence strength and paradigm-distance implied by a grid, conflict edges and blind-spot register represented visually, no labels.
learning-work-scene.webp: a learner writing a self-answer before opening AI help, with a reflection store and delayed scaffold visible as layered notebooks and a quiet terminal.
learning-mechanism.webp: a desirable-difficulty boundary diagram showing a learner path, scaffold zone, crutch danger zone, and reflection write-back as calm editorial geometry, no text.
innovation-work-scene.webp: many polished idea sheets on a table being deliberately punctured by falsification checks before any polish race, with only a few sharp bet cards surviving.
innovation-mechanism.webp: a value-perception compass, affordable-loss bet sheet, who-bears-cost row, and retrospective loop rendered as abstract editorial instruments, no readable words.
org-work-scene.webp: an AI-native operating room with an agent fleet shown as worker lanes, named human exception nodes, review queue, and context upkeep feed, no humanoid robots.
org-mechanism.webp: an organization operations loop showing review routing, context freshness, observability signals, and escalation upward for trust/safety exceptions, restrained diagrammatic style, no text.
```

- [ ] **Step 2: Copy generated images into the repo**

After each generated asset is selected, copy or move it from `$CODEX_HOME/generated_images/...` into
`site/assets/images/<filename>.webp`. Do not reference files outside this repository.

Run after copying:

```bash
ls site/assets/images/*.webp | wc -l
```

Expected: `12`.

- [ ] **Step 3: Document final prompts**

Create `site/assets/images/README.md`:

```markdown
# Visual Assets

These images are project-bound assets for the static buffer homepage. They were generated with the
built-in `image_gen` tool and saved into this repository so the site never references external temporary
paths.

See `docs/visual-assets.md` for the prompt set, style constraints, and asset roles.
```

Create `docs/visual-assets.md` with the common style block and 12 final prompts from Step 1, plus the
final saved file paths.

- [ ] **Step 4: Run site validation**

Run:

```bash
node scripts/validate-site.mjs
```

Expected: `Site validation passed.`

- [ ] **Step 5: Commit images**

Run:

```bash
git add site/assets/images docs/visual-assets.md
git commit -m "feat(site): add execution module visual assets"
```

Expected: commit succeeds.

---

### Task 4: Harden README And System Docs

**Files:**
- Modify: `README.md`
- Modify: `docs/SYSTEM-DESIGN.md`
- Modify: `docs/VALIDATION.md`
- Test: `node scripts/validate-site.mjs`

- [ ] **Step 1: Update README opening**

Replace the brittle negative lead with a transition paragraph near the top:

```markdown
**A two-tier, seven-skill AI-Native system over one shared kernel.** One skill designs a genuinely
AI-Native organization; six skills do the work of their surface the AI-native way. It is the executable
companion to the AI Native Organization Methodology.

> **The premise:** when execution is no longer scarce, the organization must be redesigned.
> From using AI to becoming AI-Native, the question changes from "which tool helps this step?" to
> "how should execution, judgment, and context be redistributed?"
```

- [ ] **Step 2: Add buffer page section to README**

Add after the install or use section:

```markdown
## Visual entry point

The repository includes a lightweight static buffer page in [`site/`](site/). It is not a replacement for
the full methodology homepage. It is a short bilingual frontispiece: it states the premise, waits briefly,
and routes readers to the existing AI Native Organization Methodology homepage, while offering a compact
seven-skill atlas for readers who stay.

Preview locally:

```bash
python3 -m http.server 8751 -d site
```
```

- [ ] **Step 3: Update `docs/SYSTEM-DESIGN.md` distribution layer**

Add this bullet under Layer 3:

```markdown
- **The buffer homepage in `site/`**: a static bilingual frontispiece that caches and orients readers
  before sending them to the existing methodology homepage. It is a distribution surface, not a new source
  of truth.
```

- [ ] **Step 4: Update `docs/VALIDATION.md` with v3 hardening**

Add a section:

```markdown
## V3 hardening target

The next validation pass treats each skill as failing if it cannot show three things at once:

1. **Artifact reality** — it produces the named work product, not advice about the work.
2. **Boundary honesty** — it preserves the human stop-line, including adverse and negative paths.
3. **Context compounding** — it writes a decision, eval, ledger, reflection, or routing rule back into a
   retrievable artifact.

This is the evaluation lens for the v3 docs and buffer homepage work: the public surface must make the
system feel executable because the underlying skill files and evals are executable.
```

- [ ] **Step 5: Run validation**

Run:

```bash
node scripts/validate-site.mjs
```

Expected: pass.

- [ ] **Step 6: Commit docs**

Run:

```bash
git add README.md docs/SYSTEM-DESIGN.md docs/VALIDATION.md
git commit -m "docs: clarify v3 buffer page and validation target"
```

Expected: commit succeeds.

---

### Task 5: Soften Skill Boundary Language Without Weakening Gates

**Files:**
- Modify: `skills/ai-native-architect/SKILL.md`
- Modify: `skills/ai-native-engineering/SKILL.md`
- Modify: `skills/ai-native-design/SKILL.md`
- Modify: `skills/ai-native-research/SKILL.md`
- Modify: `skills/ai-native-learning/SKILL.md`
- Modify: `skills/ai-native-innovation/SKILL.md`
- Modify: `skills/ai-native-org/SKILL.md`
- Test: `rg -n "not AI-Native|不是 AI-Native|你不是|not the target group" skills README.md docs`

- [ ] **Step 1: Apply common framing**

In each skill's gate section, preserve the gate but introduce it with this pattern:

```markdown
From AI-assisted work to AI-Native work, the question changes from "which tool helps this step?" to
"how should execution, judgment, and context be redistributed?" The gate below is how you keep that
distinction honest.
```

For Chinese-facing sections, use:

```markdown
从 AI 辅助到 AI-Native，问题不再是"哪个工具能帮这一步"，而是"执行、判断与上下文应该如何重新分配"。下面这道门用于保持这个分界诚实。
```

- [ ] **Step 2: Replace abrupt phrases**

Use these replacements where they preserve meaning:

```text
"not AI-Native" -> "AI-assisted rather than AI-Native"
"不是 AI-Native" -> "仍是 AI 辅助，而不是 AI-Native"
"you are not the target group" -> "this methodology is not the right fit for the request as framed"
"你不是本方法论的目标群体" -> "按当前请求表述，这套方法论并不是最合适的入口"
```

Keep phrases that are part of eval assertions when exact boundary language is necessary; do not weaken
the scope gate in `fit-and-scope.md`.

- [ ] **Step 3: Verify no accidental dilution**

Run:

```bash
rg -n "redraw-vs-graft|stop-line|止步线|human judgment|named human" skills/*/SKILL.md
```

Expected: every skill still names the gate or stop-line.

- [ ] **Step 4: Commit skill copy update**

Run:

```bash
git add skills/*/SKILL.md
git commit -m "polish(skills): soften boundary framing"
```

Expected: commit succeeds.

---

### Task 6: Normalize Eval Coverage And Pass Criteria

**Files:**
- Modify: `skills/*/evals/evals.json`
- Test: `node -e 'for (const f of require("fs").readdirSync("skills")) JSON.parse(require("fs").readFileSync(`skills/${f}/evals/evals.json`, "utf8")); console.log("eval json ok")'`

- [ ] **Step 1: Add or normalize `pass_criterion`**

Each eval file should include:

```json
"pass_criterion": "A strict 5-lens council review scores the skill output at mean >= 8.5/10 with no lens below 8.0, and the output produces the named work product, holds the human stop-line, covers adverse/negative paths, and writes context back into a retrievable artifact."
```

Keep skill-specific details after that sentence when already present.

- [ ] **Step 2: Ensure every skill has three evals**

Run:

```bash
node -e 'const fs=require("fs"); for (const d of fs.readdirSync("skills")) { const f=`skills/${d}/evals/evals.json`; const j=JSON.parse(fs.readFileSync(f,"utf8")); console.log(d, j.evals.length); }'
```

Expected: every skill prints `3` or more.

- [ ] **Step 3: Add missing assertion fields where useful**

For eval files that already use `assertions`, keep that pattern. For files without assertions, add concise
assertions only when the expected output is too long to scan. Example assertion set:

```json
"assertions": [
  "Produces the named work product rather than advice.",
  "Names the scarce human judgment node and stop-line.",
  "Designs the adverse or negative path with equal care.",
  "Writes context back into a retrievable artifact.",
  "Does not drift to the architect tier."
]
```

- [ ] **Step 4: Validate JSON**

Run:

```bash
node -e 'const fs=require("fs"); for (const d of fs.readdirSync("skills")) { const f=`skills/${d}/evals/evals.json`; JSON.parse(fs.readFileSync(f,"utf8")); } console.log("eval json ok")'
```

Expected: `eval json ok`.

- [ ] **Step 5: Commit eval updates**

Run:

```bash
git add skills/*/evals/evals.json
git commit -m "test(skills): normalize eval pass criteria"
```

Expected: commit succeeds.

---

### Task 7: Final Verification And Preview

**Files:**
- Modify only if verification finds defects.
- Test: static site, JSON, docs links.

- [ ] **Step 1: Run site validation**

Run:

```bash
node scripts/validate-site.mjs
```

Expected: `Site validation passed.`

- [ ] **Step 2: Validate eval JSON**

Run:

```bash
node -e 'const fs=require("fs"); for (const d of fs.readdirSync("skills")) { const f=`skills/${d}/evals/evals.json`; JSON.parse(fs.readFileSync(f,"utf8")); } console.log("eval json ok")'
```

Expected: `eval json ok`.

- [ ] **Step 3: Preview static page locally**

Run:

```bash
python3 -m http.server 8751 -d site
```

Expected: server starts at `http://localhost:8751`.

- [ ] **Step 4: Browser QA**

Open `http://localhost:8751` and verify:

```text
Desktop width:
- headline fits without overlap;
- countdown changes once per second;
- Stay cancels redirect and scrolls to atlas;
- EN toggle switches visible language;
- all six module tabs change content;
- images render.

Mobile width:
- no horizontal scroll;
- headline wraps cleanly;
- premise map stacks below copy;
- module images stack.
```

- [ ] **Step 5: Stop preview server**

Run:

```bash
pkill -f "http.server 8751"
```

Expected: no server remains on port 8751.

- [ ] **Step 6: Check worktree**

Run:

```bash
git status --short --branch
```

Expected: clean worktree on `main`, ahead of `origin/main` by the implementation commits.

---

## Self-Review

Spec coverage:

- Static buffer page: Tasks 1, 2, 7.
- Redirect behavior and single config constant: Tasks 1, 7.
- Stay layer and skill atlas: Tasks 1, 2, 7.
- Twelve image assets: Task 3.
- Skills/evals/docs improvement: Tasks 4, 5, 6.
- Softer "not AI-Native" framing: Tasks 4, 5.
- Organization premise map: Tasks 1, 2.
- Verification: Tasks 1, 3, 4, 6, 7.

No task should add a heavy frontend framework. No task should make generated images a source of evidence.
The methodology homepage remains the canonical destination.
