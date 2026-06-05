# OmniCompost Premium — Site Structure & Content Review

_Last updated: 2026-05-31_

A whole-site pass on **structure** (page inventory, homepage section order) and
**content** (voice, coverage, consistency). Companion to `REVIEW.md` (which scores
the overall build). Scope: the live Premium storefront only — `mockups/`, `scraps/`,
and `archive/` are out of scope.

---

## 1. Page inventory

| Page | Role | Generated? | Status |
|---|---|---|---|
| `index.html` | Homepage / landing + teaser shop | partial (`BUILD:SHOP` grid) | Live |
| `shop.html` | Full catalog + filters | partial (`BUILD:SHOP` grid) | Live |
| `learn.html` | "How it works" — full method, feeding table, QR scaffold, FAQ | hand | Live |
| `gallery.html` | Editorial photo gallery (harvest / garden / pollinators) | hand | Live (v1.8) |
| `newsletter.html` | ESP-wired Field Notes signup + archive teaser | hand | Live |
| `404.html` | Branded not-found | hand | Live |
| `product/<slug>.html` ×10 | Per-SKU detail pages | **generated** (`build.py`) | Live |
| `notes/*.html` ×3 | Field Notes editorial issues | hand | Live |

Nav + footer wiring is consistent site-wide after v1.8 (Gallery added everywhere,
homepage footer "Gallery" link fixed). No orphaned routes found.

---

## 2. Homepage section order

Current flow (Roman numerals are the on-page section numbers):

| # | Section | Anchor | Numbered | Role |
|---|---|---|---|---|
| 1 | Announcement strip | — | — | Edition / delivery banner |
| 2 | Hero — "Scraps in. Garden out." | `#top` | — | Promise + primary CTA |
| 3 | Ticker | — | — | Keyword rhythm |
| 4 | **I. The digester** | `#product` | I | Hero-product spec + add-to-cart |
| 5 | **II. The shop** | `#shop` | II | 10-SKU teaser grid |
| 6 | **III. How it works** | `#how` | III | 4-step method |
| 7 | Featured — "The quiet partner" | — | — | The worms / trust block |
| 8 | **IV. What it gives back** | `#garden` | IV | Gallery payoff grid |
| 9 | Quote — Margaret H. | — | — | Single pull-quote |
| 10 | **V. Voices from the kitchen** | `#voices` | V | 3 testimonial cards |
| 11 | **VI. Questions** | `#faq` | VI | 5-item FAQ |
| 12 | Closing — "Bring one home" | `#order` | — | Reserve + newsletter cap |
| 13 | Footer | — | — | Site map |

**Overall: the order is logical and reads as a coherent editorial landing flow.**
Lead with the object, show the catalog, explain the method, show the payoff, prove it,
answer objections, close. Two genuine flags below.

### Flag A — "Featured / The quiet partner" placement ✅ RESOLVED (2026-05-31)
The block previously sat *after* the gallery, separated from the method it elaborates,
reading as a late repeat. **Moved** to immediately follow §III "How it works" — the new
beat is method → quiet-partner trust block → gallery payoff. Unnumbered, no Roman-numeral
churn, tighter education arc.

### Flag B — Shop (§II) precedes the case for buying
For a $385 considered purchase, the full 10-SKU catalog appears as section II, before
"How it works," the trust block, and any social proof. This is a valid "commerce-early"
pattern (and §I already sells the hero object), so it is **a judgment call, not a
defect.** If conversion data later shows drop-off, the alternative flow is:
I. Digester → How it works → Quiet partner → Gallery → **Shop** → Voices → FAQ → Reserve.
Note this reorder shifts the Roman numerals and the `#shop`/`#how` nav anchors, so it is
a deliberate change, not a quick edit — left for your call.

### Minor — back-to-back social proof
Section 9 (single pull-quote) immediately precedes section 10 (three testimonial cards):
two social-proof blocks in a row. Optional: float the pull-quote up as the emotional
payoff right after the gallery (§IV), leaving the card grid to stand alone later.

---

## 3. Content & voice

- **Premium voice holds site-wide:** noun-first titles, Roman numerals, exact numbers
  (8 weeks, 5 gallons, 312 reviews), zero exclamation points. American English
  (converted in v1.7). No tier bleed.
- **Ratings present** on the hero product, every shop card, and PDPs (standing
  preference satisfied).
- **CTAs are layered correctly:** header dropdowns (jump vs full page), in-body teaser
  buttons at the end of Shop and How-it-works, and footer — no dead ends.
- **AI-tell pass** already applied to the hero/featured copy (v1.6); the rest reads
  clean.

---

## 4. Image coverage (carried from `target_coverage_2026-05-31.md`)

- **Over-covered:** gallery, Field Notes, learn heroes, produce PDP seconds.
- **Newly added (batch 5):** a "what goes in" scrap-still bench (`garlic-cloves-slate`,
  `eggshell-pail`, `walnut-shells-slats`) — promoted, not yet placed.
- **Still un-sourceable from free stock (brand-shoot items):**
  1. the digester photographed in-register (blocks hero alts, living-goods PDPs, packaging);
  2. the feeding/pouring **action** (scraps going in — stills exist, the action doesn't);
  3. the Kids commission set;
  4. the "Whole Loop" bundle composite.
- Mainstream→Premium **batch tone-filtering ruled out** — fixes colour only, not faces /
  flash / busy framing.

---

## 5. Issues found & fixed this pass

- **Flag A fixed** — "quiet partner" block moved to follow §III (see above).
- **Dead CSS removed** — the `.zones` / `.zone--tools|ops|tips` rule block (orphaned when
  homepage §IV "From counter to garden" was removed in 1.7.1) plus its mobile override.
- **Footer version policy set** — the public footer now reads a single fixed `v0.9` on all
  six customer-facing pages (index, shop, learn, gallery, newsletter, 404). The internal
  release numbers (v1.x in CHANGELOG / ROADMAP / this doc) are **not** shown to visitors;
  the live site stays on a stable public-facing `v0.9` until launch.

## 6. Open recommendations (prioritized)

1. **Place or shelve the 3 new scrap stills** — best home is a future "What goes in"
   Field Note, not the already-full gallery.
2. **Confirm the Unsplash+ seat** before using any `premium_photo-*` pick. (Note: the two
   `premium_photo-*` scrap files tested this pass are watermarked comps — a licensed
   download is required even to evaluate them properly.)
3. Consider the Shop-position A/B (Flag B) only if/when you have conversion data.

**Structure & content rating: 9.6 / 10** — coherent flow, consistent voice, no broken
wiring; Flag A and the footer drift are now resolved. Remaining headroom is the optional
Shop-position experiment, which needs real conversion data to justify.
