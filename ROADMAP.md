# OmniCompost Website — Roadmap

_Updated 2026-05-29. Premium site now at v1.0 with a working storefront. This
document covers two tracks: (A) the **commerce build** for the Premium site, and
(B) the **Mainstream Family and Kids siblings**._

---

## Track A — Commerce build (Premium site)

### Done (v1.0, 2026-05-29)
- Full storefront on `index.html`: 9 SKUs, digester featured, filter chips, cart drawer.
- **Cart persistence** — `localStorage` key `oc_cart`, shared across pages + synced
  across tabs (`storage` event). Extracted to a single shared `cart.js`.
- **Dedicated pages** — `shop.html` (full catalog) and `newsletter.html` (Field Notes
  sign-up with archive teaser). Both reuse `cart.js`; cart count carries across all pages.
- **products.json single source** (v1.2) + per-product pages and Field Notes archive
  issues under `notes/` (v1.3). Cart drawer accessibility pass (v1.3).
- Nav + footer link the new pages. Verified in preview: persistence, filters, form,
  no console errors.

### Next — checkout & backend (the v1.0 → v1.1 gap)
These are backend/integration, not design. Priority order:

1. **Checkout — Snipcart.** Best fit for this static site and already proven on the
   earlier TomCo build (`tomco-site/` uses `snipcart-add-item` / `snipcart-items-count`).
   Plan: add the Snipcart JS + CSS + public API key, convert each `.add` button to
   `class="snipcart-add-item"` with `data-item-id/name/price/url/image/description`,
   and add the `#snipcart` container. Decide whether to keep the custom drawer as the
   "mini-cart" or hand the whole cart over to Snipcart (recommended: hand it over to
   avoid maintaining two carts). Alternative if Snipcart's fee model doesn't fit:
   **Shopify Buy Button** (hosted checkout) or **Stripe Payment Links** (simplest, but
   no real cart).
2. **Per-product detail pages** — DONE (v1.3). `product/<slug>.html` per SKU, generated
   by `build.py` from `products.json` (Premium PDP: image, rating, price, description,
   specs, add-to-cart). Card titles link to them. Still to add when Snipcart lands: a
   crawlable `data-item-url` per product and a small image gallery.
3. **Newsletter handler** — wire the `newsletter.html` form to an ESP. Options:
   Buttondown or Mailchimp (forms-friendly), or Formspree if you just want delivery.
   Currently client-side confirmation only.
4. **Live inventory / sold-out states** — model stock once a backend exists (Snipcart
   has inventory management; otherwise track in `products.json`).
5. **Order/delivery logic** — the "complimentary Orange County delivery" promise needs
   a postal-code gate at checkout (Snipcart shipping rules or a custom validation).
6. **Accessibility pass** — cart drawer DONE (v1.3): `role="dialog" aria-modal`,
   focus-trap, Esc-to-close, `aria-expanded` on the cart button, `aria-live` region on
   the count. Still to do: visible focus states on chips/buttons, a full keyboard +
   screen-reader audit of the long-form pages.

### Single source of truth
The shop catalog is currently duplicated across `index.html`, `shop.html`, and the
mockups. Before adding more SKUs, move products into **`products.json`** and render
both the homepage grid and `shop.html` from it (build step or fetch). This is the
prerequisite that makes items 1, 2, and 4 above tractable.

---

The three audience systems must never blend within one artifact (per the
OmniCompost design system). Each site is its own build with its own paper
color, type stack, logo lockup, voice, and structural devices. They share
one thing only: the content architecture (Tools / Operations / Tips) and the
section skeleton already proven in the Premium build.

---

## Track B — Mainstream Family & Kids siblings

The three audience systems must never blend within one artifact (per the OmniCompost
design system). Each sibling is its own build with its own paper color, type stack,
logo lockup, voice, and structural devices. When these are built, give each its own
copy of the commerce layer from Track A (shared `cart.js` works as-is; only the skin
changes).

### Shared foundation (already built in Premium v0.9)

Reuse the **structure**, rebuild the **skin**:

- Section skeleton: announcement strip → sticky header → hero → ticker →
  product (I) → how it works (II) → zones (III) → gallery (IV) → featured
  band → quote → testimonials (V) → FAQ (VI) → closing/reserve → footer.
- IntersectionObserver scroll-reveal, mobile hamburger, line-art digester SVG.
- Per-tier asset folders already exist under `Kitchen 1 Sheet Guide/` and
  `omnicompost_brand/assets/` (logos, lockups).

What changes per tier: paper color, hero color, fonts, corner radius, logo
lockup, illustration style, voice, and the imagery set.

---

## Phase 1 — Mainstream Family site (next)

**Audience:** –150K suburban parent, Costco/Home Depot, warm but un-arty.
~3–4× the Premium market by household count — the volume play.

| Token | Value |
|---|---|
| Paper | Warm cream `#FCF7EE` |
| Hero color | One per page — Apple red `#D94F3E` or Garden green `#5AAE3F` |
| Display font | Recoleta (slab serif) |
| Body font | Nunito Sans |
| Accent | Caveat (sparingly — "Grandma's tip") |
| Corner radius | 12–16px soft |
| Logo | Cider hero / cider lockup |
| Rules | Solid 2–3px brand green or red (not dashed) |
| Illustration | Flat-color with modest shading (Bob's Red Mill register) |

**Voice shifts:** second person, contractions, allowed enthusiasm
("Great for your tomatoes!"), specific-but-plain measurements ("about the
size of a softball," "about half water, half liquid"). Max one folk-wisdom
line and two ornamental badges per page.

**Imagery:** the Mainstream Family library is the deepest (36 keepers) —
chopping/prep, peelings & scraps, hands in the kitchen, planting & seedlings,
casual garden tools, watering cans. Plenty to fill hero + gallery + featured.

**Effort:** ~1 build session. Largest risk is voice drift toward Premium —
keep the three-voice reference table open while writing copy.

**Open gap:** the digester in a real kitchen/garden setting (brand-specific,
needs own shoot). Use the line-art SVG as Premium does until a render exists.

---

## Phase 2 — Kids site (after Family; partially blocked)

**Audience:** the ~10-year-old who helps with the bin. Sticker-book confidence.

| Token | Value |
|---|---|
| Paper | Cream `#FFFBF0` on peach `#FFE8CC` margin |
| Zone colors | Sky `#5BC3E8` (Tools), Grass `#4AB85C` (Ops), Sun `#FFC93C` (Tips) |
| Display font | Fredoka (rounded) |
| Body font | Nunito 600 |
| Accent | Patrick Hand (only inside dashed NOTE callouts) |
| Corner radius | 12–20px chunky |
| Logo | Meadow worm / meadow lockup |
| Structure | 3px black outline on every element; offset drop-shadows |
| Illustration | Emoji-in-outlined-bubble; pink worm mascot once per page |

**Voice shifts:** verb-first titles ("Scoop out the compost"), two sentences
per card max, concrete comparisons ("as tall as your hand"), allowed
anthropomorphism ("the worms get grumpy"), one exclamation per card max.

**Why it's blocked:** the image-coverage audit (2026-05-27) concluded Kids
**cannot be completed from stock**. It needs a commissioned illustration set:
pink worm mascot + digester drawn in Kids style + 4–6 action stickers
(kid feeding scraps, worms "eating," before/after compost) in one consistent
hand. This is the single biggest open gap in the whole image program.

**Plan:**
1. Commission the Kids illustration set (mascot + product + action stickers).
2. Build the site skin (can proceed in parallel with placeholders).
3. Drop in commissioned art once delivered.

**Effort:** ~1 build session for the skin; **gated on the commission** for
final art.

---

## Phase 3 — cross-tier finishing (all three)

These items recur in every tier and are best handled once at the end:

1. **Real digester product photography/render** in all three registers —
   brand-specific, needs its own shoot. Currently substituted by line-art SVG.
2. **Premium feeding/pouring action shot** — could not be sourced free at
   register; candidate for the same shoot as the product.
3. **Wire real commerce + forms** — the Reserve CTA and newsletter are
   currently mailto/no-op stubs. Pick a checkout (Snipcart was used on the
   earlier TomCo build) and a form handler (Formspree) per tier.
4. **Hosting** — deploy each tier to its own path/subdomain, mirror the
   v1/v2 GitHub Pages pattern already documented in `DIFFERENCES.md`.

---

## Suggested sequence

```
v0.9  Premium site            ✓ shipped
v1.0  + Mainstream Family      Phase 1   (deepest imagery, biggest market)
v1.1  + Kids skin              Phase 2   (build now, art on commission)
v1.2  commission digester +    Phase 3   (closes the last shared gaps)
      Kids action set, wire
      commerce, deploy
```

Family first: it has the most usable imagery on disk and the largest market.
Kids last because it is gated on commissioned illustration regardless of how
fast the skin is built.
