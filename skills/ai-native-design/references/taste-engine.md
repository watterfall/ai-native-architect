# The taste engine — the discriminating spec + the taste scorecard

Taste is the scarce judgment of AI-native design. It is **not mysticism**: it is a set of
decomposable judgments that can be **externalized, taught, and fed back**. This file makes it
operational so a human can wield it fast and an agent can be steered by it — without the agent
ever becoming the judge.

Two facts to hold:
- **Empathy is the root of taste.** Without it, "taste" is just personal preference. Taste is the
  judgment of *what is right for these specific people* — so it is grounded in a real audience,
  their job, their context, their constraints.
- **Taste is subjective — relatively, not arbitrarily.** "Relative" means it is indexed to a
  group and a goal; it is *not* "anything goes." A version can be *wrong* for these people, and
  you can say why. That is what makes taste a verifier and not a vibe.

---

## Part A — the discriminating spec

Before generating, write the spec. A good spec's mark: **someone else (or an agent) can make
something *you would sign off on*.** If their output surprises you in a bad way, your spec wasn't
discriminating enough.

A spec has two failure modes — keep off both:
- **Over-pinned** — so prescriptive there's nothing left to generate; you've hand-built one comp
  in spec form and killed the spread.
- **Over-empty** — so loose that generation has no constraint and slides straight to the mean
  ("clean, modern, professional" produces slop every time).

Minimum viable spec (five lines):
1. **For whom** — the specific group, their job-to-be-done, their real context/device/constraint.
   (This is the empathy anchor; everything else indexes to it.)
2. **The one feeling** — the single dominant impression on arrival (not three; one).
3. **The job** — what the artifact must get the person to do / understand / feel-able-to-do.
4. **The reference frame** — one or two real-world directions to aim at (an aesthetic lineage,
   not a competitor to clone).
5. **The explicit NOT** — *the most discriminating line in the spec.* What this must **not** be
   ("not another teal-gradient SaaS hero," "not a giant-number dashboard," "not warm/playful").
   Naming what to refuse is what pulls generation off the mean, because the mean is exactly the
   set of defaults you didn't forbid.

Mark which lines are **hard** (will become tokens/lint) and which are **soft** (stay human
judgment). See `design-tokens-as-code.md` for the split.

---

## Part B — the taste scorecard (decompose "good")

Score each candidate item-by-item. The scorecard turns "I don't like it" into a *direction* the
generator can act on, and turns intuition into something you can teach and feed back.

| Axis | The question | Machine-checkable? | What a low score steers |
|---|---|---|---|
| **Empathy / fit** | Is this *right for these specific people* and their real job? | No (constitutive) | Re-anchor to the audience; you're designing for "everyone." |
| **Hierarchy** | Does attention land in the intended order; does the one important thing dominate? | Partly | One element should win; cut competition; resize by content weight, not equal cards. |
| **Voice** | Does the copy/type/color carry a *specific* character, or generic defaults? | Partly | Replace Inter-centered defaults & empty adjectives with a real voice. |
| **Restraint** | Is every element earning its place, or is it decoration (gradient text, icon-above-every-heading)? | Partly | Remove the decorative; let material serve hierarchy, not ornament. |
| **Distinctiveness** | Would this be recognizable as *yours*, or could it belong to anyone? | No (the 指纹 axis) | Add back a skipped judgment (see `slop-and-fingerprint.md`). |
| **Pacing** *(motion/video only)* | Does the rhythm feel intended, or default-eased? | No | Re-time; hold beats; the time axis no machine checks. |

**How to use it well:**
- The axes that are "No" on machine-checkable (**empathy** and **distinctiveness**, plus
  **pacing** for motion) are the *taste* axes — they stay with the human and are the reason the
  converge node can't be automated.
- The "Partly" axes can be *pre-screened* by tooling (contrast lint, alignment check) so the human
  doesn't burn judgment catching mechanical defects — then judged on the part tooling can't reach.
- A low score must produce a **named direction** for the steer step, not a redo. "Voice: 3 — too
  generic, push editorial, kill the stock adjectives" is steerable; "I don't love it" is not.

**The most discriminating single question**, if you only have time for one: *"Is this true for
these people, or merely fine for everyone?"* "Fine for everyone" is the signature of the mean.

---

## Why "judging many" is *harder* than "polishing one"

Counterintuitively, the native loop is not the lazy option. Polishing one comp keeps the
judgment *implicit* — you nudge until it feels right. Judging many forces you to make the criteria
**explicit and comparative**: you must say *why A beats B beats C*, on which axes, for whom. That
explicitness is harder — and it is exactly what lets the judgment be externalized, taught to a
teammate, fed to an agent, and compounded across rounds. The difficulty is the point: it is where
the value moved when making got cheap.
