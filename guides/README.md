# Guides — Final Set (v2)

_Last updated: 2026-05-30_1610_

This folder is the consolidated, reviewed home for the working guides that grew
up around the OmniCompost build. Each was re-read against **the finished Premium
site** (live inventory, Orange County delivery gate, ESP-wired newsletter,
per-product pages, accessible cart) and rewritten as a **v2** — corrected where
it was wrong, trimmed where it had hardened into dogma, and reconciled so the
set reads as one voice instead of seven memos written on different days.

## What "v2" means here

Three passes were applied to every guide:

1. **Correctness** — claims checked against what actually shipped. Where a number
   or behaviour couldn't be verified, it's now marked as a claim to verify rather
   than stated as fact.
2. **De-dogma** — rules that were really *defaults dressed as laws* are demoted
   to defaults, each with an **Exception** block naming the case where the
   original rule (or a new one) is the better call. A rule with no stated
   exception is a rule no one has stress-tested.
3. **Cohesion** — shared vocabulary, shared date format, cross-references instead
   of repetition. The site is the reference implementation; guides point at it.

## How this folder is organized (and why flat)

Seven docs. At this size the industry norm — and the most useful layout — is
**flat files plus one strong index**, not a tree of `engineering/`, `brand/`,
`process/` subfolders. Domain subfolders earn their keep at roughly **12+ docs**;
below that they mostly add `../../` link churn and a layer to click through for
no findability gain. So the files stay flat and the *index* does the
categorizing, below. (Revisit if the set grows past ~12 — at that point split by
the two categories already used here: **Engineering / process** vs
**Brand / production**.)

Naming: each file keeps its `-v2` suffix on purpose — the v1 originals still
exist elsewhere in the repo, so the suffix disambiguates "reviewed version" from
"original." If the originals are ever deleted, drop the suffix and let the file
*be* the current version (git holds the history).

## Topic organization within the set — reviewed (and left as-is)

Separate from *folder* layout: do the seven **topics** themselves want
reshuffling — split, merged, or moved between the two categories? Checked; the
answer is no. Each guide covers one non-overlapping domain (model choice, token
spend, local serving, build patterns, print proofing, design review, image
review), so there's nothing to merge and nothing doing two jobs that should be
split. The category split (engineering vs brand) still holds.

The one thing that *did* change is the arrival of two skills —
`omnicompost-commerce` (storefront mechanics) and `static-site-preview` (verify a
change). These overlap two guides: **serving-sites-locally-v2** (preview) and
**build-strategy-v2** (the single-source build pipeline). That overlap is
intentional and handled by the **layer split**, not a reorg: the *skills* are the
operational "do-it" checklist; the *guides* are the "why / durable lessons" layer
and cross-reference the skills. Don't fold one into the other — a guide that
turns into a command list stops being a guide (same rule that keeps the
`*-review-v2` files as a review layer over their skills). Revisit only if a guide
shrinks to nothing but steps the skill already lists, at which point retire the
guide rather than reorganize it.

## The set

**Engineering / process** — how the build runs:

| v2 guide | Supersedes | One-line scope |
|---|---|---|
| [model-selection-web-dev-v2.md](model-selection-web-dev-v2.md) | `../../model_selection_web_dev.md` | Which model + effort per web task (incl. aesthetic judgment + design creation). |
| [token-levers-v2.md](token-levers-v2.md) | `../../token_levers.md` | Cutting token spend without cutting reasoning. |
| [serving-sites-locally-v2.md](serving-sites-locally-v2.md) | `../../HOW-TO-SERVE.md` | Previewing a static site on this machine. |
| [build-strategy-v2.md](build-strategy-v2.md) | `../../DIFFERENCES.md` | Responsive + build-pipeline patterns proven across TomCo v1/v2 and this site. |

**Brand / production** — how OmniCompost artifacts get made:

| v2 guide | Supersedes / reviews | One-line scope |
|---|---|---|
| [print-proofing-standard-v2.md](print-proofing-standard-v2.md) | `../../Kitchen 1 Sheet Guide/Print Proofing Standard.md` | Pre-print checks for physical pieces. |
| [design-system-review-v2.md](design-system-review-v2.md) | the `omnicompost-design-system` skill | Where the three-voice rules held and where the site earned exceptions. |
| [image-sourcing-review-v2.md](image-sourcing-review-v2.md) | the `omnicompost-image-sourcing` skill | Sourcing/vetting notes, updated for the local-preview workflow. |

## Relationship to the live skills and site docs

- The **skills** (`.claude/skills/omnicompost-design-system`,
  `omnicompost-image-sourcing`, and the two new ones —
  `omnicompost-commerce` for the storefront mechanics and `static-site-preview`
  for verifying changes) remain the authoritative, auto-loaded source.
  The two `*-review-v2.md` files here are a **review layer**, not a replacement —
  they record the exceptions the finished product justified. Promote any
  exception into the skill itself only if it proves out across more than one
  artifact.
- The **site docs** (`../ROADMAP.md`, `../CHANGELOG.md`, `../REVIEW.md`,
  `../SUMMARY.md`) are living records, not guides — they stay in place and now
  carry dated timestamps. They are listed here so the set is complete, but they
  are not rewritten as v2.
- New since the guides set: **`../CLAUDE.md`** (project memory — how to work in
  this folder, which skill for which job) and **`../CONTENT-GUIDE.md`** (a
  plain-language walkthrough for adding products, Field Notes issues, and images).
  Both are living docs and carry the timestamp convention.

## Scraps — what to incorporate, what to leave

The `../scraps/` folder is advisory reference, not authoritative (per project
memory). Two items there look guide-adjacent; the calls:

- **`../scraps/brand_style_guide.html` — partially incorporate (as a reference,
  not a v2).** It is a real brand guide (tier positioning, logo system, palette,
  typography, approved backgrounds, mascot, applications) and **overlaps the
  `omnicompost-design-system` skill**, which is the authoritative source. It does
  *not* need its own v2 here. What it *does* need: a one-time **reconciliation
  check** that its palette hexes, type stack, and tier positioning match the
  skill exactly — if they drift, the skill wins and the HTML guide gets corrected
  or retired. Tracked as a line in `design-system-review-v2.md`. Don't fork brand
  truth across an HTML file and a skill; pick one (the skill) and make the other
  defer.
- **`../scraps/business_card_mockups.html` — do NOT incorporate.** It's a design
  **deliverable** (Horizon / Meadow / Cider lockups + card backs), not guidance.
  Guides describe how to make things; mockups *are* the made thing. It belongs in
  an assets/deliverables location, not the guides folder. (It is, however, a good
  worked example for the new "design creation" criteria in the model-selection
  guide — referenced there, not rewritten here.)

A fuller scan of `../scraps/` turned up four more guide-shaped HTML files. The
calls, by the same logic (does it overlap an authoritative skill? is it guidance
or a deliverable?):

- **`../scraps/web_style_guide.html` — partially incorporate (reference, reconcile).**
  Genuine web-styling guidance across tiers, but it overlaps both the
  `omnicompost-design-system` skill (voice/palette/type) and the new
  `omnicompost-commerce` skill (storefront mechanics). Don't fork it as a v2;
  reconcile any web-specific rules into those skills, skill wins on conflict.
- **`../scraps/image_style_guide.html` — partially incorporate (reference, reconcile).**
  Same ground as the `omnicompost-image-sourcing` skill. Reconciliation check
  only (per-tier visual rules match the skill); skill is authoritative.
- **`../scraps/logo_usage_guide.html` — partially incorporate (reference, reconcile).**
  Real guidance (clearspace, min sizes, knockouts, don'ts) but it's brand-asset
  spec that belongs *with* the design-system skill, not as a standalone v2. Fold
  into the same reconciliation pass as `brand_style_guide.html`.
- **`../scraps/logo_lockups.html` — do NOT incorporate.** A deliverable (rendered
  lockups), not guidance — same call as `business_card_mockups.html`. It's an
  asset.

The point-in-time review files in scraps (`Kitchen Guide v5 Review_…`, `Lawn
Guide v6 Review_…`, `… Sheet Review_…`, `site_review_…`, `tomco-v2-review.html`)
are **frozen artifacts**, not living guides — leave them as-is under the
filename-timestamp convention; don't rewrite them as v2.

Rule of thumb for future scraps: **incorporate it as a guide only if it tells you
how to decide or do something repeatable.** A finished artifact (mockup, export,
lockup render, one-off page, point-in-time review) is a reference or an asset,
never a guide. When a scrap *does* overlap a skill, the skill is authoritative —
the scrap gets a reconciliation check, not a fork.

## Minting a new exception (applies to every guide's Exceptions section)

The Exceptions blocks are not a dumping ground — an exception is a *documented*
deviation, and documenting one has a cost (every reader now has to weigh it).
Before adding a brand-new exception to any guide, it must pass all three:

1. **Recurring, not one-off.** A single weird situation you reason through and
   move on from doesn't need a documented exception — just decide. Document it
   only when you expect to face the same fork again. (One-offs are decisions;
   exceptions are patterns.)
2. **Named, justifiable reason — not a preference.** "I'd rather do X here" is not
   an exception; "the default produces a *worse outcome* here because Y" is. If
   you can't name the property that flips (cost-of-a-quiet-bug, audience,
   artifact lifespan, material constraint), it's taste, not an exception.
3. **A reasonable person would otherwise get it wrong.** If the default rule
   already leads to the right call here, no exception is needed. Add one only when
   following the rule literally would mislead.

Each new exception must state **the rule it bends, the case that triggers it, and
the justification** — the format the existing blocks use.

**Promotion / retirement:** one instance is an exception; **three is a pattern** —
promote a thrice-seen exception into the rule itself (and delete it from
Exceptions). An exception that hasn't fired in a long time, or whose triggering
case no longer exists, gets **retired** so the section stays honest. A stale
exception is as misleading as a stale rule.

## Standing convention (new)

Every guide and every living doc (summary, roadmap, changelog, review) now
carries a `_Last updated: YYYY-MM-DD_HHMM_` line directly under its title.
Stamp it on every edit. The filename-timestamp style used by the older review
docs (`… Review_2026-05-21_1357.md`) is fine for **frozen, point-in-time**
artifacts; the in-file stamp is for **living** ones.
