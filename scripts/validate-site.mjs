import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const site = path.join(root, "site");
const index = fs.readFileSync(path.join(site, "index.html"), "utf8");
const app = fs.readFileSync(path.join(site, "assets/app.js"), "utf8");
const manifestPath = path.join(site, "assets/images/manifest.json");
const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));

const failures = [];
const githubBase = "https://github.com/watterfall/ai-native-architect/blob/main/";

function assert(condition, message) {
  if (!condition) failures.push(message);
}

function getEvalFiles() {
  const skillsDir = path.join(root, "skills");
  if (!fs.existsSync(skillsDir)) return [];

  return fs.readdirSync(skillsDir, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => path.join(skillsDir, entry.name, "evals", "evals.json"))
    .filter((file) => fs.existsSync(file))
    .map((file) => path.relative(root, file));
}

assert(index.includes("当执行不再稀缺，组织需要重新设计。"), "missing approved Chinese headline");
assert(index.includes("When execution is no longer scarce"), "missing approved English headline");
assert(
  app.includes('const METHODOLOGY_HOME_URL = "../ainative/dist/index.html"'),
  "redirect constant must target ../ainative/dist/index.html"
);
assert(
  /\bconst\s+REDIRECT_SECONDS\s*=\s*8\s*;?(?:\r?\n|$)/.test(app),
  "redirect duration must be exactly numeric 8"
);
assert(!index.includes('href="../docs/'), "evidence links must not use relative docs paths");
assert(!index.includes('href="../skills-eval-workspace/'), "evidence links must not use relative benchmark paths");
assert(
  index.includes(`${githubBase}docs/VALIDATION.md`) &&
    index.includes(`${githubBase}skills-eval-workspace/iteration-1/BENCHMARK.md`) &&
    index.includes(`${githubBase}docs/SYSTEM-DESIGN.md`),
  "evidence links must use absolute GitHub URLs"
);
assert(Array.isArray(manifest.assets), "manifest.assets must be an array");
assert(manifest.assets.length === 12, "manifest must list exactly 12 assets");

for (const asset of manifest.assets) {
  const filePath = path.join(site, "assets/images", asset.file);
  assert(asset.file.endsWith(".webp"), `${asset.file} should be a WebP asset`);
  assert(index.includes(asset.file) || app.includes(asset.file), `${asset.file} is not referenced by page code`);
  assert(fs.existsSync(filePath), `${asset.file} missing from site/assets/images`);
  assert(asset.alt && asset.alt.length >= 24, `${asset.file} needs useful alt text`);
}

const evalFiles = getEvalFiles();
for (const file of evalFiles) {
  try {
    JSON.parse(fs.readFileSync(path.join(root, file), "utf8"));
  } catch (error) {
    failures.push(`${file} contains malformed JSON: ${error.message}`);
  }
}

if (failures.length) {
  console.error(failures.map((failure) => `- ${failure}`).join("\n"));
  process.exit(1);
}

console.log("Site validation passed.");
