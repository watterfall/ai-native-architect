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
