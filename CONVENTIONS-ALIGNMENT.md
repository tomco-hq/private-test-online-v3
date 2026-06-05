# OmniCompost — How Both Sites Match Current Web Conventions

_Last updated: 2026-06-01_2000_

A short audit of the two storefronts against 2026 e-commerce design conventions, with the
research they're checked against. The short version: the **tier split is the strategy**.
Premium follows the *premium-minimalist / editorial* playbook; Family follows the *mainstream
information-density / trust-signal* playbook. Each is the right convention for its buyer, and
they deliberately don't converge.

## The conventions (2026 baseline)
From current industry guidance (sources below):
1. **One hero, one strongest message, one primary CTA**; remove anything that dilutes it.
2. **Trust signals surfaced early** — "free shipping over $X", guarantees, ratings.
3. **Best-sellers / featured grid with visible prices** (3–8 items).
4. **Social proof woven into the layout**, not buried — stars in the hero, review counts, UGC.
5. **Value-prop / brand-story block**; **email capture with an incentive**.
6. **Mobile-first**, clear hierarchy, tight palette.
7. **Performance**: sub-2s load is the baseline (a 100 ms delay can cost ~7% conversion).
8. **Two diverging aesthetic tracks**: premium-minimalist editorial (whitespace, strong
   editorial voice, "destination" content) *vs.* a mainstream counter-trend toward
   **information density** and modular **bento grids** for fast scanning.

## Premium site — the editorial / minimalist track
| Convention | How the Premium site meets it |
|---|---|
| One quiet hero, restrained CTA | Single-product feature hero; editorial restraint, exact numbers, zero exclamation points. |
| Destination content (premium signal) | `learn.html` — method essay, one-page guides + QR/PDF loop, deep FAQ. The site reads as a resource, not just a catalogue. |
| Tight, calm palette + serif/grotesque type | Cream `#F4EDE0` + muted sage/terracotta/ochre/teal; Fraunces + Inter; sharp corners. |
| Restrained social proof | A "Voices" testimonials section — present but quiet, matching the register. |
| Trust signal | Drawer note + tiered free-shipping line ("Free shipping over $150"). |
| Email capture | ESP-wired `newsletter.html`. |
| Performance | Plain static HTML/CSS/JS, no framework → fast by construction. |

This matches the documented premium pattern: soft palette, generous whitespace, editorial
voice, and educational resources that position the brand as a *destination*. (Adobe's figure
that shoppers spend ~40% longer on minimalist designs is the upside being chased here.)

## Family site — the mainstream density / trust track
| Convention | How the Family site meets it |
|---|---|
| Benefit-led hero + strong CTA | "Turn today's scraps into tomorrow's garden" + "Start composting — $389". |
| Trust signals early | Star badge in the hero, "🚚 Free shipping over $150", "🛡️ 90-day money-back". |
| Best-sellers grid w/ prices | "Stock up your bin" consumables grid with prices and Add buttons. |
| Social proof woven in | Stars in the hero, "loved by 40,000+ families", review cards/wall. |
| Information density / bento | `family-c` "The Marketplace" — a bento hero showing product + deal + stat + review + eco all above the fold. |
| One-primary-action variant | `family-b` "The Quick Start" — a focused single-CTA conversion landing page. |
| Replenishment / channel reality | Subscribe-and-save framing + "also at Amazon / Home Depot". |
| Mobile-first | Responsive breakpoints collapse grids to 1–2 columns on small screens. |
| Performance | Same static stack → fast. |

This matches the mainstream counter-trend: customers rewired by high-density feeds (TikTok,
Instagram) want to see options without scrolling, and **bento grids** are replacing long
lists. Emoji as functional icons and louder, numeric social proof are on-convention for the
big-box register.

## Shared, both tiers
- **Accessibility basics**: focus-trapped cart drawer, `aria-live` status regions, alt text.
- **Trust via shipping clarity**: one shared `cart.js` with a regional **tiered-shipping**
  estimate (OC / metro SoCal / nationwide, free over $150) — surfaces cost honestly instead
  of hiding it to checkout, which is the conversion-positive move.
- **Single source of truth** for the catalogue (`products.json` → `build.py`).

## Where they intentionally diverge (and should stay divergent)
Whitespace-and-restraint vs. density-and-energy is **not** an inconsistency to fix — it's two
audiences. Premium's buyer rewards calm and editorial depth; Family's buyer rewards seeing
everything, fast, with the deal and the rating in view. Forcing one convention on both would
weaken whichever tier it didn't fit. Design-system rule #1 (never mix tiers) is what keeps
each site matching *its own* convention.

## Gaps / next moves
- Family `family-c` / `family-b` are mockups: wire the shared cart and swap lifestyle
  placeholders for real product photography before they ship.
- Premium: stand up the `/g/*` guide redirects on the host so the QR-loop "destination"
  content fully works.
- Both: real checkout (Snipcart/Stripe) is the remaining non-design work.

## Sources
- [10 Essential Ecommerce Homepage Design Best Practices for 2026 — ecorn.agency](https://www.ecorn.agency/blog/ecommerce-homepage-design-best-practices)
- [Ecommerce Website Design in 2026 — BigCommerce](https://www.bigcommerce.com/articles/ecommerce/best-ecommerce-website-design/)
- [5 eCommerce Homepages Thriving After Google's Feb 2026 Update — ConvertCart](https://www.convertcart.com/blog/high-converting-ecommerce-homepage)
- [Brands Are Ditching Minimalism: Why Busy Design Is Winning — Inc.](https://www.inc.com/ryan-vanni/brands-are-ditching-minimalism-why-busy-design-is-suddenly-winning-in-e-commerce/91310763)
- [eCommerce Design Trends 2026 (bento grids, density) — Code Theorem](https://codetheorem.co/blogs/ecommerce-design-trends/)
