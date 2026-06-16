# AI-Native Architect Buffer Site

This directory contains the static bilingual buffer homepage for the AI-Native Architect seven-skill system.

## Local Preview

From the repository root:

```bash
python3 -m http.server 8742 -d site
```

Then open `http://localhost:8742/`.

## Redirect Config

The redirect target is controlled by the single constant in `site/assets/app.js`:

```js
const METHODOLOGY_HOME_URL = "../ainative/dist/index.html";
```

The public deployment URL should replace that one constant when the methodology homepage is deployed.

## Validation

Run the static validation script from the repository root:

```bash
node scripts/validate-site.mjs
```

Before Task 3 generates images, validation is expected to fail only because the 12 WebP files listed in `site/assets/images/manifest.json` do not exist yet.
