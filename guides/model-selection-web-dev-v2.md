# Model Selection Guide — Web Design & Development (v2)

_Last updated: 2026-05-30_1430. Supersedes `../../model_selection_web_dev.md`._

Which model *and effort level* (Sonnet vs Opus low/medium/high/xhigh/max) to use
per task, ordered easiest → hardest.

**Decision rule:** `difficulty × cost-of-a-quiet-bug`. Difficulty alone doesn't
decide the model — a simple task whose bugs are silent and expensive (auth,
payments) still earns Opus. The question to ask on any task: *"If this is subtly
wrong, how bad is it and how hard is it to catch?"* Cheap-to-catch and forgiving
→ Sonnet. Expensive, subtle, or one-shot → Opus.

> **v2 note — the rule held up.** This site is the proof: the storefront layout,
> gallery, and copy were Sonnet-class visible-failure work, while the two parts
> that bit silently — the **Orange County postcode gate** (wrong ranges = a
> customer is quietly told "no" or quietly let through) and the **cart stock
> clamp** (off-by-one = overselling) — are exactly the "looks fine when I test
> the happy path" failures the rule routes upward. The framing survives.

## The effort ladder (Opus 4.7)

Pricing is flat across effort ($5/M in, $25/M out); higher effort costs more
because it *generates* more thinking tokens at the same rate.

1. **Sonnet** — default for easy / visible-failure tasks.
2. **Opus low/medium** — middle-band close calls; reasoning depth without the
   xhigh thinking-token premium.
3. **Opus xhigh** — practical default for hard or high-stakes coding.
4. **Opus max** — worst-case tasks where xhigh isn't enough *and* the problem
   genuinely requires deeper search.

> **De-dogma — the "3%-for-2×-cost" benchmark.** The v1 guide stated "~71% at
> xhigh vs ~74.5% at max" as fact. Treat these as **Anthropic-reported figures
> on one agentic-coding benchmark, as of mid-2026** — directional, not a law of
> nature. The *shape* of the trade-off (max costs roughly double for a small
> accuracy gain) is the durable lesson; the exact percentages will drift with
> every model release. Re-verify against current docs before quoting a number to
> anyone. Don't let a stale benchmark talk you out of `max` on the one task
> (row 13–14) where the failure mode is catastrophic.

**Reading the Switch column:** what happens if you move *off* the recommended
pick — token cost change (↑/↓) and output quality change (+/−). The pattern is
asymmetric: on easy tasks, switching up to Opus burns tokens for no quality
gain; on hard tasks, switching down to Sonnet saves tokens but the quality drop
is real and the savings are often illusory.

---

| # | Task | Difficulty | Best pick | Switch effect | Why |
|---|---|---|---|---|---|
| 1 | Static marketing / landing page | 2 | **Sonnet** | → Opus: tokens ↑↑, quality ≈flat | Markup + styling, no branching logic. Judged by looking at the page; mistakes cost seconds. Opus's reasoning has nothing to bite on. |
| 2 | Responsive layout / CSS theming | 3 | **Sonnet** | → Opus: tokens ↑↑, quality ≈flat | Flexbox/grid/breakpoints are well-represented; failures are visible in the viewport and cheap to iterate. |
| 3 | Forms + client-side validation | 3 | **Sonnet** | → Opus: tokens ↑↑, quality +tiny | Canonical patterns; edge cases are an enumerable list. A miss is low-cost and caught on first test. |
| 4 | Component library / design system | 4 | **Sonnet** (Opus **medium** for the API-design pass) | → all-Opus: tokens ↑, quality + on API only | Component bodies are volume work; the *public API* (prop shapes, naming) rewards one Opus pass because it's costly to change later. |
| 5 | Blog / CMS-driven content site | 4 | **Sonnet** | → Opus: tokens ↑↑, quality ≈flat | Routes, templates, pagination — plumbing, not problem-solving. |
| 6 | REST/GraphQL integration & data fetching | 5 | **Sonnet** (Opus **low/medium** if data flow is tangled) | → Opus xhigh: tokens ↑↑, quality +small | Shallow logic, real surface area in loading/error/empty + cache. Sonnet covers the common path. |
| 7 | Client-side state management | 6 | **Opus medium**, **xhigh** if optimistic/async-heavy | → Sonnet: tokens ↓↓, quality − | Stale closures, effect ordering, derived-state drift surface late and are painful to reproduce. |
| 8 | SEO / accessibility / performance | 6 | **Sonnet** for fixes; **Opus xhigh** for strategy | → other: depends on phase | Mechanical fixes are Sonnet; diagnosing *which* bottleneck matters is Opus. Split the pass. |
| 9 | Database schema & data modeling | 7 | **Opus xhigh** | → Sonnet: tokens ↓↓, quality −− | Foundational; a bad model taxes every downstream query and migration. |
| 10 | Auth / sessions / access control | 8 | **Opus xhigh** | → Sonnet: tokens ↓↓, quality −− | Cheap to write, catastrophic and silent to get wrong. No "looks fine when I test it" safety net. |
| 11 | Payments / checkout / billing | 8 | **Opus xhigh**, **max** for novel reconciliation | → Sonnet: tokens ↓↓, quality −− | Correctness + real money + compliance (PCI, tax, idempotency). Errors surface late, in reconciliation. |
| 12 | SSR / hydration / caching / edge | 8 | **Opus xhigh** | → Sonnet: tokens ↓↓, quality − | Hydration/cache bugs are invisible — the page *looks* right while subtly broken. |
| 13 | Real-time / collaborative (websockets, CRDTs) | 9 | **Opus max** | → xhigh/Sonnet: quality −−− on hardest paths | Race conditions and conflict resolution fail nondeterministically under concurrency you can't reproduce locally. |
| 14 | Large-scale refactor / framework migration | 9 | **Opus max** | → xhigh: tokens ↓, quality − on cross-file invariants | Holding many cross-file constraints at once; a missed dependency cascades. |
| 15 | Aesthetic value analysis / design critique | 4 | **Sonnet** for routine critique; **Opus medium/xhigh** when the verdict is foundational | → Opus on routine critique: tokens ↑, quality +small | Judging hierarchy, balance, type pairing, colour harmony, "does this read Premium." Visible *and* cheap to override — the human is the final arbiter — so the cost-of-a-quiet-bug term is low and Sonnet usually suffices. It climbs only when the critique *sets direction* that's expensive to walk back (see row 16 and the reversibility axis). |
| 16 | Original design creation (new visual language) | 7 | **Sonnet** to execute within an established system; **Opus xhigh** to define a new one | → Sonnet on a from-scratch identity: tokens ↓↓, quality −− on coherence | Two very different jobs hide under "design." *Executing* an existing system (build the business cards from the OmniCompost palette + type) is volume work Sonnet does well — output is visible, iteration is cheap. *Defining* a new visual language from nothing (the brand's first identity, a design system's core grammar) is high-taste, foundational, and expensive to reverse — it behaves like row 4 (API design) or row 9 (schema): one strong pass on the direction, then Sonnet for the rest. |

---

## The reversibility axis (why design work resists the naive rule)

The base rule — `difficulty × cost-of-a-quiet-bug` — leans on bugs being
*silent*. Visual work breaks that assumption: a bad design is **loud** (you see
it instantly) and usually **cheap to redo** (regenerate, nudge, iterate). By the
naive reading every aesthetic task is therefore Sonnet — failure is visible, so
Opus's deep search has nothing hidden to catch.

That's right for **execution** and wrong for **direction**. The thing that flips
it is a third axis the code rows rarely surface: **reversibility.**

- **Low cost to reverse → Sonnet.** Critiquing a layout, restyling a section,
  laying out cards in an existing system, picking between two type sizes. Wrong
  calls are visible and a regeneration away. Paying Opus rates buys little.
- **High cost to reverse → Opus (one direction pass).** A brand's core palette,
  its primary type pairing, the visual grammar a whole product line inherits.
  These aren't loud-and-cheap; a weak choice here is *quietly* expensive because
  everything downstream commits to it and re-deciding means redoing the line.
  That's the same "foundational, hard to migrate later" profile that puts schema
  design (row 9) and public API design (row 4) on Opus despite modest raw
  difficulty.

So: **judge design work by how hard the decision is to undo, not by how hard the
pixels are to push.** Loud-and-reversible is Sonnet's home; quiet-because-
foundational earns one Opus pass on the direction, then drops back to Sonnet to
execute it. The business-card mockups in `../scraps/business_card_mockups.html`
are the clean example — executing the *already-decided* Horizon/Meadow/Cider
lockups is Sonnet work; it would only have been Opus work back when those three
identities were first being *defined*.

---

## Where this site landed on the table

A worked example, since the abstract table is easier to trust against a real build:

| This site's task | Row | Pick used | Verdict |
|---|---|---|---|
| Premium landing + gallery + copy | 1–2 | Sonnet-class | Correct — visible, cheap to fix. |
| Shop grid from `products.json` + `build.py` | 5–6 | Sonnet-class | Correct — plumbing. |
| Cart accessibility (focus trap, ARIA, Esc) | 8 | strategy bumps to xhigh | Mechanical ARIA is Sonnet; *getting the focus-trap semantics right* is the bump. |
| Live inventory clamp | 7 | Opus medium-ish | Off-by-one here oversells stock — the silent failure profile justifies the care. |
| OC postcode gate | 3 → **10-adjacent** | treat as access-control-lite | A *form* by difficulty, but it gates who can transact — bugs are silent. Reason about it like row 10, not row 3. |
| Snipcart checkout (roadmapped) | 11 | **Opus xhigh** when built | Real money. Don't let "it's just wiring a button" fool you. |
| Premium look + line-art digester SVG | 15–16 | Sonnet-class | Executing the *already-defined* Premium system (cream/Fraunces/sage, sharp corners). Loud-and-reversible — correct to keep cheap. Defining that system the first time would have warranted an Opus direction pass. |

**The OC-gate row is the whole point of the decision rule.** By line count it's a
regex on a text input — row 3, trivially Sonnet. By *cost-of-a-quiet-bug* it's
access control: a wrong range silently refuses paying customers in-area or
promises delivery you can't honour. Difficulty said Sonnet; the rule correctly
overrode it.

## Where each effort level lives

- **Sonnet:** rows 1–6, mechanical fixes in row 8, routine critique (15) and
  in-system design execution (16).
- **Opus low/medium:** rows 4 (API design), 6 (tangled data flow), 7 (standard
  client state), 15 (foundational/expensive-to-reverse aesthetic verdicts).
- **Opus xhigh:** rows 7 (async-heavy), 8 (strategy), 9–12, 16 (defining a new
  visual language from scratch).
- **Opus max:** rows 11 (novel reconciliation), 13–14.

## Exceptions

- **Exception (drop below the recommendation):** a hard-row task that is *fully
  covered by a mature SDK* can drop a notch. Wiring Stripe's or Snipcart's
  documented happy path (row 11) on xhigh is defensible; you only need `max`
  when you design the reconciliation/refund logic yourself.
- **Exception (climb above):** a row-1/2 task stops being Sonnet the moment it
  carries hidden state — see the OC gate. "It's just a form/landing page" is the
  sentence that precedes most silently-wrong commerce code.
- **Exception (prototype throwaway):** for code you will delete after looking at
  it (a spike to answer one question), drop a full tier. The cost-of-a-quiet-bug
  term goes to ~zero when the artifact has no future.
- **Exception (design — direction vs execution):** a single design task can split
  across tiers. When the *direction* is foundational (a new palette, the primary
  type pairing) do that pass on Opus, then drop to Sonnet to execute it — don't
  pay Opus rates to lay out the hundredth card in a system already decided, and
  don't let Sonnet quietly *invent* a brand identity that a whole product line
  will inherit. (See the reversibility axis above.)

> **Adding a brand-new exception here?** Run the three-part minting test in
> `README.md` first (recurring, named-justifiable-reason, would-otherwise-mislead).
> One instance is an exception; three is a pattern — promote it into the rule.
