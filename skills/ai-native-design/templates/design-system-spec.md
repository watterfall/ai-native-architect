# Design-system spec — copyable guardrail scaffold

Stand this up *before* generating (Step 0). Start minimal — a one-off poster needs only the
red lines and a "for whom" line; a product needs the full token file. Don't over-build a tiny job.

---

## 0 · For whom (the empathy anchor — one line)
> These are `<specific group>`, doing `<job-to-be-done>`, in `<real context / device / constraint>`.
> The one feeling on arrival: `<single dominant impression>`.

## 1 · Hard rules — design tokens (machine-enforceable, lint fails the build)

```jsonc
{
  "color": {
    "brand.primary": "#______",   // one reasoned color — NOT teal/purple-blue default
    "brand.ink":     "#______",
    "surface":       "#______",
    "surface.alt":   "#______",
    "accent":        "#______",
    "danger":        "#______"
  },
  "type": {
    "family.display": "______",   // a face with character, not Inter/Roboto by default
    "family.text":    "______",
    "scale":  { "sm": "", "base": "", "lg": "", "xl": "", "2xl": "" },
    "weight": { "normal": 400, "bold": 700 }
  },
  "space":  { "scale": [4, 8, 12, 16, 24, 32, 48] },   // one ratio, not ad-hoc px
  "radius": { "none": 0, "card": "__", "pill": 999 },  // radius is a voice choice — don't default round
  "contrast": { "body.min": 4.5, "large.min": 3.0 },   // ← lint red line (WCAG-aligned)
  "motion": { "duration": { "fast": "", "base": "", "slow": "" },
              "ease":     { "standard": "", "entrance": "", "exit": "" } }
}
```

**Lint red lines (fail the build):** off-token color · sub-threshold contrast · off-scale spacing ·
gradient text · more than `<N>` font families.

## 2 · Anti-slop red lines (the fingerprint guard — 2–3 minimum to start)
Pick from `references/slop-and-fingerprint.md`; the most discriminating are usually the **NOTs**:
- [ ] No teal-on-dark / purple-blue gradient text.
- [ ] No glassmorphism / universal big-radius + soft shadow as decoration.
- [ ] No equal-card grid / giant-number dashboard template.
- [ ] No icon-above-every-heading.
- [ ] No empty "empowering / seamless / revolutionary" copy.
- [ ] **Explicit NOT for this brief:** `<the one thing this must not become>`.

## 3 · Soft criteria (stay with the human — the taste scorecard axes)
Do **not** lint these. Held at the converge node:
- **Empathy / fit** — right for *these* people, not everyone.
- **Hierarchy** — the one important thing dominates.
- **Voice** — specific character, not defaults.
- **Restraint** — every element earns its place.
- **Distinctiveness** — recognizable as *yours*.
- *(motion only)* **Pacing** — rhythm is intended, not default-eased.

## 4 · Components (as code specs, de-canvased)
List the components the artifact needs, each as a code-shaped spec (props, states, token usage),
so an agent can generate and a reviewer can diff. Example row:
> `Button` — variants {primary, ghost}; states {default, hover, focus, disabled, loading};
> uses `color.brand.primary`, `radius.pill`, `motion.duration.fast`; min-target 44px.
