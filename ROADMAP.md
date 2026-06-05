# OmniCompost Website — Roadmap

_Last updated: 2026-06-03_0333. Premium site now at v1.8 — working storefront
plus live inventory, **tiered regional shipping** (OC $7 / metro SoCal $12 /
rest-of-CA & nationwide $20, free over $150 — replaced the Orange-County-only
delivery gate 2026-06-01), an ESP-ready newsletter, a
Mini Digester ($245) entry SKU, a homepage copy refinement (AI-tell pass), a full
`learn.html` (How it works + one-page-guide/QR scaffold + large FAQ), open-graph
social cards, PDP second images, and American-English copy site-wide. **v1.8 risk-reversal
& proof pass (2026-06-03):** a `guarantee.html` policy page + 30-day hardware return
and six-week living-worm guarantee, a PDP **Specifications expander** (from
`products.json` `specs`), the **vermicompost-vs-dehydrated-scraps** distinction stated
once, small-space/Mini and cost-to-run FAQ lines, a quiet Kids-tier bridge line, and
site-wide shipping-reassurance copy. This document covers: (A) the **commerce build**
for the Premium site, (B) the **Mainstream Family and Kids siblings**, then
cross-cutting tracks for **coupons** (C), **payment methods** (D), **tooling**
(E), and **fulfillment / delivery-zone / risk-reversal** (F, from the persona
analysis in `mockups/profiles/`, now incl. a small-business/micro-commercial
lane from the profile 12–14 batch)._

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

### Done (v1.4, 2026-05-30)
- **Live inventory** (`stock` in `products.json` → states + sold-out buttons +
  cart clamp), **Orange County delivery gate** (postcode lock in the cart drawer
  across all pages), **ESP-ready newsletter** (configurable endpoint, honeypot,
  states), and **Field Notes expanded ~2.5×** with photography. See items 3–5 below.
- **Guides consolidated** — `guides/` folder holds reviewed v2 rewrites of the
  process/dev guides, print-proofing standard, and skill review layers.

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
3. **Newsletter handler** — DONE (v1.4). `newsletter.html` form wired to a
   configurable `ESP_ENDPOINT` constant (honeypot + loading/success/error states,
   graceful demo fallback when unset, no API keys in-file). **To go live:** paste
   your provider's public form endpoint (Buttondown / Mailchimp / Formspree) into
   `ESP_ENDPOINT`. Currently in demo mode (endpoint empty).
4. **Live inventory / sold-out states** — DONE (v1.4). `stock` per product in
   `products.json`; `build.py` renders In stock / "Low stock — N left" / Sold out
   and disables sold-out buttons; `cart.js` clamps quantity to `data-s`. Bedding
   Bricks ships sold-out as the demo case. **To extend:** when Snipcart lands, sync
   stock to its inventory management instead of the static `stock` field.
5. **Order/delivery logic** — SUPERSEDED (v1.8, 2026-06-01). The original
   Orange-County-only postcode *gate* was replaced by **tiered regional shipping**:
   `cart.js` takes one ZIP and returns a flat cost by region (OC $7 / metro SoCal
   $12 / rest-of-CA & nationwide $20, free over $150), remembered across pages.
   Checkout is no longer locked outside OC — the site ships statewide and
   nationwide. **To harden:** this is a client-side *estimate* only; compute the
   authoritative charge server-side / via Snipcart shipping rules at checkout so it
   can't be bypassed by editing the DOM.
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

---

## Track C — Coupon / promo codes

Gated on a real checkout (Track A item 1). A static site can *collect* a code,
but only the checkout backend can validate and apply a discount safely — never
trust a client-side price reduction. Sequence accordingly.

**Mechanism:** Snipcart has native discounts (Dashboard → Discounts), applied by
code at checkout — percentage, fixed amount, or free shipping, with usage caps,
expiry dates, and product/category targeting. This is the right home; do **not**
hand-roll discount math in `cart.js`.

**Candidate codes (popular, on-brand for the Premium voice — keep it restrained,
no "BLOWOUT50"):**

| Code | Offer | Use / trigger | Notes |
|---|---|---|---|
| `FIELDNOTES` | 10% first order | Reward newsletter sign-up; email it on subscribe | Ties the ESP work to a conversion. Low % keeps Premium feel. |
| `WHOLELOOP` | Free delivery on The Whole Loop | Nudge the bundle | OC delivery is already "complimentary" in copy — make it a literal line item the code zeroes. |
| `EDITIONONE` | $25 off the Digester | Launch / founding-customer window | Matches the "Edition One" seal already on the digester. |
| `SPRINGWAKE` | 15% seasonal | Time to the April Field Notes issue | Seasonal, expires — reinforces the "one letter a month" cadence. |
| `REFER25` | $25 off, both parties | Referral | Needs unique-code generation; later, once volume justifies it. |

**Design constraints (so codes don't break the voice):** no exclamation points or
urgency banners in the Premium tier; surface a single quiet "Have a code?" link in
the cart drawer, not a flashing field. Restraint is the brand.

**Effort:** trivial once Snipcart is live (dashboard config + one cart link).
Blocked entirely until then.

---

## Track D — Payment methods (via Snipcart)

Snipcart doesn't process payments itself — it connects to a **payment gateway**,
and the gateway determines which methods appear at checkout. Pick the gateway
first; the methods follow.

**Supported natively (gateway-dependent, but standard):**

| Method | How | Notes |
|---|---|---|
| **Credit / debit cards** | Any Snipcart gateway (Stripe, Square, Paymill, Mollie, etc.) | The baseline. Stripe is the most common pairing and is already familiar from the TomCo build. |
| **Apple Pay** | Via Stripe (or other supporting gateway) on Snipcart | Works on Safari/iOS; needs domain verification with the gateway. High-value for the iPhone-heavy Premium OC audience. |
| **Google Pay** | Via supporting gateway | Android/Chrome counterpart to Apple Pay. |
| **Link / saved cards** | Stripe Link | Faster repeat checkout. |

**Wallet / P2P methods that are NOT Snipcart-native — flagged for honesty:**

| Method | Reality | Path if required |
|---|---|---|
| **Venmo** | Not a Snipcart payment method. Venmo for business is delivered via **PayPal/Braintree**. | Snipcart's PayPal support can surface PayPal; Venmo specifically would need Braintree integration, which is **not** a first-class Snipcart gateway. Likely out of scope unless you leave Snipcart. |
| **Zelle** | Bank-to-bank transfer with **no merchant/e-commerce API** and no buyer protection. | Cannot be wired into Snipcart checkout. Only viable as a manual, off-site "pay by bank transfer" arrangement — not recommended for a storefront. |
| **PayPal** | Supported by Snipcart as an alternative gateway alongside a card gateway. | Realistic to add; covers a meaningful slice of buyers. |
| **Buy-now-pay-later (Affirm/Klarna/Afterpay)** | Via Stripe's BNPL surface. | Optional; weigh against the Premium positioning (BNPL can read down-market). |

**Recommended stack:** **Stripe** as the gateway (cards + Apple Pay + Google Pay +
Link + optional BNPL) and **PayPal** added as a second gateway for wallet
coverage. That combination covers everything realistic; **drop Zelle and Venmo
from the requirements** as incompatible with a hosted-checkout static site.

**Effort:** part of Track A item 1 (Snipcart). Apple Pay adds a domain-
verification step; otherwise gateway config is dashboard work, not code.

---

## Track E — Tooling: skills & CLAUDE.md changes

Improvements to how *this project* is built, surfaced by the work so far. Cheap,
compounding, and independent of the site itself.

### New skills worth extracting

1. **`omnicompost-commerce` skill** — the storefront has hardened into a
   repeatable system (single-source `products.json` → `build.py`, shared
   `cart.js` with localStorage + cross-tab sync + a11y drawer, the stock-state +
   delivery-gate patterns). The Family and Kids shops will rebuild the *skin* but
   reuse this *machinery*. That's textbook skill material: a multi-step,
   reused-across-artifacts workflow that shouldn't reload into every session.
   Pull the build/cart conventions out of `build.py` comments and `CHANGELOG`
   into one skill body.
2. **`static-site-preview` skill** — codify the Claude-Preview-MCP workflow from
   `guides/serving-sites-locally-v2.md` (start/list/eval/screenshot, the
   document-root gotcha, "servers die between sessions"). Repeated every build.
3. **`snipcart-integration` skill** — once Track A item 1 is done, capture the
   button-conversion recipe (`.add` → `snipcart-add-item` with `data-item-*`),
   the discount/gateway dashboard steps, and the delivery-gate hardening, so the
   three sibling sites don't re-derive it.

### CLAUDE.md changes

- **Fill the empty `## Project specifics` section.** It currently ships with
  placeholder comments. Populate:
  - **Stack:** static HTML/CSS/JS, `build.py` (Python 3.9 / Anaconda) as the
    generator, `products.json` single source, shared `cart.js`.
  - **Conventions:** never hand-edit the `<!-- BUILD:SHOP -->` regions (regenerate
    via `build.py`); cross-cutting cart UI lives only in `cart.js`; serve via the
    Claude Preview MCP server (root = site folder).
  - **Skills used by this project:** `omnicompost-design-system`,
    `omnicompost-image-sourcing` (+ the three proposed above as they land).
- **Add a "guides" pointer** — note that `guides/` holds the reviewed v2 process
  guides so future sessions reference them on demand instead of re-deriving
  model-selection / token / serving advice.
- **Add the spec-sync rule** — the temperature/moisture/feeding numbers must stay
  consistent across print pieces *and* the website Field Notes (see
  `guides/print-proofing-standard-v2.md`). Worth a one-line standing rule so a
  future copy edit on one surface doesn't silently desync the others.

**Effort:** skills are ~1 short session each, best done when their domain is next
touched (commerce skill alongside the Family build; Snipcart skill alongside the
checkout). The CLAUDE.md edits are minutes and worth doing now.

> **Update 2026-05-30:** items 1 (`omnicompost-commerce`) and 2
> (`static-site-preview`) are **done** — both skills now live under
> `.claude/skills/`. The project `CLAUDE.md` and a content guide
> (`CONTENT-GUIDE.md`) were also written. `snipcart-integration` (item 3) remains
> pending the checkout build.
>
> **Update 2026-05-30 (v1.6):** a 4th skill, **`human-writing`**, was added — a
> final-pass checklist for removing AI-writing tells from human-facing copy. It
> carries a "don't over-correct" rule and an explicit audience caveat: the
> Premium calibration (em dashes welcome, restrained voice) does NOT transfer to
> the Family/Kids tiers (Track B), where triplets/exclamation/simple parallelism
> are features, not faults. **Re-tune the skill's trade-offs before applying it to
> a non-Premium tier.** First use: the homepage copy refinement logged in
> `CHANGELOG.md` [1.6], with the effectiveness review in the site's `AI testing/`
> folder.

---

## Track F — Fulfillment, delivery-zone & risk-reversal

Surfaced by the `mockups/profiles/` reception analysis (2026-05-30). These move
conversion for specific personas; see `mockups/profiles/README.md` for the buyer
evidence behind each.

### 1. Two fulfillment tiers — ship-only vs. white-glove

Offer at checkout:
- **Ship it (assembly required)** — flat/free national or regional shipping, buyer
  assembles. Available wherever we ship; unlocks out-of-zone buyers (profiles 04,
  11) who currently hit a dead end.
- **White-glove delivery + setup** — the current OC promise, expandable to
  counties *near* OC (LA / Riverside / San Bernardino / San Diego ZIP bands) **for
  a fee and/or above a minimum order** (e.g. setup free over $400, else $X; or
  only within N miles).

**Site-specific vs. Snipcart-automatic (important):**
- **Snipcart handles the offer + charge.** Multiple **shipping methods/rates** are
  Snipcart config — it displays them, adds the fee, collects it. Country/region
  gating and simple rate rules are built in. *Not custom code.*
- **The ZIP-radius eligibility + minimum-order rule is site-specific / custom.**
  Snipcart does not natively know "this ZIP is within 25 mi of OC" or "offer setup
  only above $400." That logic lives in **Snipcart's shipping webhook**: Snipcart
  POSTs the cart + address to *our* endpoint, which returns the allowed
  methods/rates (e.g. "white-glove $75" for a qualifying LA ZIP over the minimum,
  else "ship-only"). Same logic as today's client-side `inOC()` gate, moved
  server-side so it can actually enforce and price.

So: **two-tier offer = Snipcart config; near-OC paid-assembly-with-minimum =
custom shipping webhook.** (The current OC gate is client-side courtesy only;
real eligibility must be enforced server-side once money is involved.)

### 2. Out-of-zone waitlist capture — SUPERSEDED (2026-06-01)

Originally the highest-ROI fix: the OC gate's "outside OC" branch was a hard dead
end that disabled checkout and captured nothing, losing out-of-zone buyers
(profile 04, Renata). **This was resolved by removing the gate entirely** — the
site now ships statewide and nationwide via tiered shipping (see Track A item 5),
so there is no dead-end branch left to convert into a waitlist. Renata is a buyer,
not a leak. (If a future product is ever genuinely OC-only again, restore a
waitlist branch then.)

### 3. Money-back guarantee / trial — DONE (v1.8, 2026-06-03)

Shipped as a **two-part guarantee** rather than the originally-proposed flat
60-day, after a category review: 30-day money-back on the hardware is the *premium
electric-composter* norm (Lomi, Vitamix FoodCycler), while worms take ~4–6 weeks to
establish — so a single 60-day cash window over-exposed the biological half. The
split de-risks establishment without the liability:
- **Thirty-day hardware return** — full refund on the digester, Mini, bundle, and
  every garden tool; OC pickup, prepaid label elsewhere; usable condition.
- **Six-week living guarantee on the worms** — free replacement if they arrive
  other than alive or fail to establish in the first six weeks.
Both windows start the day the order arrives. Lives on a dedicated
**`guarantee.html`** policy page (Premium voice), linked from `index.html` #order,
the footer, and the `learn.html` FAQ. Addresses profiles 02, 05, 06, 10 and the
eco-skeptic veto (18).

### 4. Gift / deliver-to-another-address flow

Buyer ≠ recipient for profiles 01 (chef buying for a client), 05 (gift-giver), and
11 (lawyer routing to a second home). The single-postcode gate trips all three.
Add a separate shipping address (and gift receipt / note). Note this interacts
with the zone gate — eligibility should key off the *delivery* ZIP, not the
billing one.

### 5. Trust + reason-to-choose content (no backend) — MOSTLY DONE (v1.8, 2026-06-03)

Cheap content fixes the profiles asked for:
- **Third-party social proof** — _still open._ Verified-purchase marks, an
  independent review/rating badge, or a certification seal (OMRI / B-Corp). One or
  two, quiet. Wanted most by the wellness buyer (profile 19), who will only
  amplify once she can cite a cert. Note the on-page star ratings/review counts
  already render from `products.json` — this item is specifically *third-party*
  proof, not the existing self-reported scores.
- **"How this differs from countertop units"** — DONE. The vermicompost (finished,
  living castings) vs. dehydrated-scraps "pre-compost" distinction is now stated
  once, plainly, in the `learn.html` FAQ and the homepage FAQ (profile 10).
- **Apartment / small-space FAQ** — DONE. `learn.html` adds small-apartment/Mini
  fit, odor failure mode, fruit-fly/pest, and cost-to-run lines (profiles 06, 03).
- **Quiet Premium spec expander** — DONE. PDPs render a `<details>` Specifications
  table from a `specs` object in `products.json` (exact numbers; profile 07). The
  loud comparison grid still belongs to the Mainstream Family tier, not Premium.

### 6. Small-business / micro-commercial lane

Surfaced by the small-business profile batch (profiles 12 Instagram bakery, 13 food
truck, 14 small café, added 2026-05-30). A cluster of in-zone, brand-aligned,
scrap-rich micro-businesses currently can't tell whether the product is for them,
can't transact as a business, and find the household sizing + single-address
delivery model don't fit. This is **scope-definition first, build second** — decide
how far down-market the consumer SKU reaches before building anything.

**a. Throughput-based sizing guidance (content, cheap).** Replace/augment
"household of four" with a litres-per-week answer keyed to use, including a
small-maker/small-café line ("for a small café, plan on ~N units"). Lives on the
PDP next to the quiet spec expander (item 5). Directly unblocks profiles 12 and 14,
whose only real blocker is "will it keep up with my scraps?"

**b. Honest scope-setting (content, cheap, on-brand).** State plainly where the
consumer product *stops* — that it's not sized for full restaurant/truck volume
(profile 13) and that for a regulated business it **supplements, not replaces,**
mandated organics hauling (SB 1383; profile 14). Premium voice is already
declarative and honest; saying "not for this" builds more trust than silence and
stops the wrong buyer from churning. No backend.

**c. Business checkout / receipt (backend, gated on Snipcart — Track A).** A proper
itemised receipt, an optional business name / tax-ID field, and "buy as a business."
Profiles 12 and 14 would expense the purchase today if a real receipt existed;
profile 13 expects an invoice. Snipcart supports custom checkout fields and order
receipts — most of this is config once checkout lands; net-terms invoicing is out
of scope for a hosted static checkout (flag, don't build).

**d. Multi-unit / B2B tier (scope decision, likely deferred).** The honest answer
to a food truck or busy café may be "two or three units" or "not yet." Whether to
open a genuine B2B/volume path (multi-unit pricing, deliver-to-commissary, recurring
service framing) is a **positioning decision above the Premium tier**, not a quick
build — adjacent to the Mainstream Family / future commercial sibling, not this
storefront. Decide intent before committing; for now items (a) and (b) serve this
group at near-zero cost.

**Sequence:** (a) and (b) are content-only and shippable now alongside item 5; (c)
rides the Snipcart build (Track A item 1); (d) is a deliberate positioning call to
make, not a task to schedule yet.
