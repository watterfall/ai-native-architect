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
