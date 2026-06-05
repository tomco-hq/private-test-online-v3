# OmniCompost — Main Website Review

_Last updated: 2026-05-30_1912._
_File reviewed: [index.html](index.html) · Original review date: 2026-05-29 · v1.0_
**Overall rating: 9.6 / 10** (original v1.0 review; see the v1.4 addendum below.)

> **v1.6 addendum (2026-05-30):** homepage copy given an AI-tell pass via the new
> `human-writing` skill — hero lede de-em-dashed into two clean sentences, the
> "quiet partner" featured block's filler triplet trimmed. Premium voice
> preserved; two over-zealous draft edits were rejected. Full rationale and a
> before/after rating (8.5 → 9.1 on the homepage copy axis) in the site's
> `AI testing/` folder and `CHANGELOG.md` [1.6].

## What this is

The production Premium website. It was built by taking the polished Premium landing page
and folding in the storefront from the premium-c "Boutique" mockup, so it serves as both
the marketing page and the shop in one self-contained file. The OmniCompost digester stays
the featured hero product; the 7–10 consumable SKUs sit in a dedicated shop section below.

Design system: **Premium** only — cream `#F4EDE0`, Fraunces + Inter, sage / terracotta /
ochre / teal zone colors, sharp corners, dashed rules, Roman-numeral sections, noun-first
declarative voice, zero exclamation points. The new sage "A"-monogram favicon is applied.

## Section map

| № | Section | Notes |
|---|---|---|
| I | Hero | Asymmetric, line-art digester, calm intro |
| — | Product feature | The Digester, "Edition One", Add-to-cart ($385) |
| II | Shop | 9 products, digester featured 2×2, filter chips, Add-to-cart |
| III | How it works | Process explainer |
| IV | Garden / zones | Tools / Operations / Tips zone colors by role |
| V | Gallery | Photography grid |
| VI | Voices | Testimonials |
| VII | FAQ | — |
| — | Journal + Newsletter | Editorial cards + sign-up band |
| — | Cart drawer | Slide-in, live count + subtotal, qty +/−, remove |

## Verification (preview, port 8099)

- ✅ 9 product cards render; 10 add-to-cart buttons (1 feature + 9 shop)
- ✅ Cart adds, merges duplicates, updates count + subtotal (3× digester = $1,155)
- ✅ Filter chips work (garden → Trowel / Tea Can / Seedling Pots)
- ✅ 18 images load, none broken
- ✅ No console errors
- ✅ Responsive: shop collapses to 2-up, feature spans 2 on mobile

## Strengths

- **One coherent voice.** No design-system blending — reads as Premium throughout.
- **Featured-product discipline.** The digester keeps prominence (own feature section +
  2×2 grid span) even as consumables are added, exactly as briefed.
- **Real commerce UX.** Functional cart with quantity control and a filterable catalog,
  not a static mockup.
- **Self-contained.** Inline CSS/JS, Google Fonts only — trivial to deploy.

## Gaps / production to-do

These are backend/scope items, not design flaws — they account for the −0.4:

1. **Checkout is a demo.** Wire to Stripe / Shopify / Snipcart for real payment.
2. **No per-product detail pages.** Each SKU needs its own page (specs, gallery, reviews).
3. **No live inventory.** Stock counts and "sold out" states are not modeled.
4. **Cart is session-only.** No persistence (localStorage) or account.
5. **Newsletter form is inert** (`onsubmit="return false"`) — connect to an ESP.
6. **Accessibility pass recommended** — focus trapping in the drawer, ARIA live region on
   the cart count, keyboard-dismiss (Esc) for the drawer.

## Recommendation

Ship this as the production front end. It is the strongest single artifact across all
mockups and satisfies the brief: full shop + gallery + journal/newsletter + working cart,
Premium-consistent, digester featured. Next milestone is backend integration (items 1–5
above), then an accessibility/QA pass before launch.

---

## v1.4 addendum — 2026-05-30

Most of the −0.4 gap list above has since closed (v1.1–v1.4):

| v1.0 gap | Status now |
|---|---|
| 1. Checkout is a demo | **Still open** — roadmapped (Snipcart, Track A item 1). The one remaining true gap. |
| 2. No per-product detail pages | **Closed (v1.3)** — `product/<slug>.html` per SKU from `build.py`. |
| 3. No live inventory | **Closed (v1.4)** — stock states + sold-out + cart clamp. |
| 4. Cart is session-only | **Closed (v1.1)** — `localStorage` + cross-tab sync. |
| 5. Newsletter inert | **Closed (v1.4)** — ESP-ready (endpoint to be filled to go live). |
| 6. Accessibility pass | **Largely closed (v1.3)** — drawer dialog semantics, focus-trap, Esc, `aria-expanded`, live region. Remaining: full keyboard/SR audit of long-form pages. |

Net: of the six v1.0 production to-dos, **five are done** and the sixth (real
checkout) is the gating backend item. The score isn't re-graded here — the
original 9.6 was for the v1.0 artifact — but the path to launch is now just
checkout + a final QA pass. The Field Notes expansion and the OC delivery gate
added since are net positives not reflected in the original number.
