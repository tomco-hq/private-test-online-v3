# Token-Saving Levers (v2)

_Last updated: 2026-05-30_1430. Supersedes `../../token_levers.md`._

Levers for reducing token spend in Claude Code, split into **universal** (any
session) and **specific** (a scoped build, e.g. this storefront). Principles are
stable; verify model names, prices, and flags against current docs before acting.

> **The one rule that governs the rest:** cut tokens by removing *waste*
> (re-sent context, dead files, rework), never by capping *reasoning*. This is
> the same line the project `CLAUDE.md` draws ("Context is RAM, not a log… don't
> sandbag your own thinking"). Every lever below is a waste-cutter. None of them
> is "think less."

---

## Universal levers

| Lever | Why it works |
|---|---|
| **Pick the cheaper model** | Sonnet handles routine coding at a fraction of Opus's cost. See `model-selection-web-dev-v2.md` for the per-task call. Reserve Opus for deep or high-stakes reasoning. |
| **Scope sessions short** | Context is re-sent every turn — long threads re-pay for the whole history each message. The single biggest silent drain. |
| **`/compact` at breakpoints** | Summarizes the thread into a compact baseline. Run at ~60% usage / logical breakpoints, not at the auto-compact trigger. |
| **`/clear` on topic change** | Starting fresh beats dragging dead context into unrelated work. |
| **CLAUDE.md for standing context** | Loaded once per session instead of re-explained; keeps repeated instructions out of the chat body. |
| **`@file` references** | Pull reusable info in on demand instead of pasting it inline and re-sending every turn. |
| **Subagents for read-heavy work** | Isolate file-reading in a subagent's own context so it doesn't bloat the main thread. (Costs a fixed startup tax — see exception.) |
| **Skills over CLAUDE.md bloat** | Skills load only name+description at startup; the body loads only when triggered. Right home for repeated workflows. |
| **Match `/effort` to the task** | Drop to low for genuinely trivial work; don't reflexively lower it for real work. |
| **Filter verbose tool output (hook)** | A PreToolUse hook that greps a 10K-line log for `ERROR` before it hits context can turn thousands of tokens into dozens. |

> **De-dogma — the "suppress explanations cuts 40–60%" claim.** The v1 guide
> listed a CLAUDE.md line like *"implement without lengthy explanations"* as a
> 40–60% saver. **Demoted.** That figure is unsourced and the lever is
> double-edged: terse-mode instructions bleed into *hard word caps*, which
> Anthropic's documented April-2026 postmortem says measurably hurt reasoning —
> the project CLAUDE.md bans them for exactly this reason. **Keep:** "skip
> preambles, skip restating the prompt." **Drop:** any self-imposed
> `≤N words` cap. Brevity comes from cutting filler, not truncating thought.

---

## Specific levers (a scoped build)

These control *iteration churn*, where most tokens go on a from-scratch app.

| Lever | Why it works |
|---|---|
| **Lock the feature list up front** | Scope creep is the #1 token sink. Pin what's in/out before generating. |
| **Single source of truth for data** | One `products.json` feeding a `build.py` meant adding `stock`, `desc`, and `details` touched **one file**, not nine product pages by hand. This is the highest-leverage specific lever this build found. |
| **Minimize file count** | Fewer files = less re-reading as the codebase grows across turns. |
| **Centralize cross-cutting UI in one place** | The OC delivery gate and cart a11y live in one shared `cart.js` and inject themselves into all 15 pages. The alternative — editing 15 drawers — would have been 15× the read/write churn. |
| **Accept the first working version** | Pixel-by-pixel polishing rounds are pure iteration cost. Stop at "works," then polish only what a real look flags. |
| **Batch testing/debugging** | Group fixes instead of one round-trip per bug. Verify several states in one `preview_eval`. |

---

## Rule of thumb

Universal levers (model choice + scope) move the number most. Specific levers
keep a single build from ballooning via rework. For a one-app build: cheap model
+ locked scope, then **single-source data + few files + centralized
cross-cutting code**, then accept-first-version.

## Exceptions

- **Exception (subagent tax):** "subagents for read-heavy work" is net-negative
  for *small* jobs. Each teammate re-loads CLAUDE.md + MCP + skill descriptions
  (~50K tokens of fixed startup). Below ~8 heavy reads, do it inline; above it,
  the isolation pays for the tax. (The image-sourcing guide draws the same ~8
  line.)
- **Exception (don't compact mid-debug):** the "compact at 60%" default is wrong
  when you're inside a live debugging chain — a compaction can drop the exact
  tool output you're reasoning from. Finish the thread or `/clear` deliberately
  instead.
- **Exception (effort floor on silent-bug work):** "match effort to the task"
  does **not** mean dropping effort on short-but-dangerous code. The OC gate and
  stock clamp are a few lines each; both warranted full effort because a quiet
  bug is expensive. Length is not difficulty.
- **Exception (skills aren't always cheaper):** a skill triggered on every single
  turn is just CLAUDE.md with extra indirection. Skills win for *occasionally*
  needed workflows; for always-on rules, inline them.

> **Adding a brand-new exception here?** Run the three-part minting test in
> `README.md` (recurring, named-justifiable-reason, would-otherwise-mislead).
> One instance is an exception; three is a pattern — promote it into the rule.
