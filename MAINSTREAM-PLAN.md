# MAINSTREAM-PLAN — the Family-tier OmniCompost site

_Last updated: 2026-06-01_2115_

A plan for the **mainstream / Family-tier** version of the OmniCompost storefront —
the counterpart to this Premium site, aimed at value-minded households rather than the
coastal-OC editorial buyer. Grounded in the existing mockup
`mockups/website ideas/family/index.html` (rated **9.0/10** in `mockups/website ideas/RATINGS.md`)
and the Family voice in the `omnicompost-design-system` skill.

> **Scope of this doc:** a plan, not an implementation. Nothing is built yet.

---

## 1. The one-paragraph thesis

The Family site sells the **same digester and the same consumables** as Premium, but to
a different person: a budget- and family-conscious buyer who shops the way they'd shop
Amazon or Home Depot. The job is not editorial restraint — it's **clarity, savings,
reassurance, and momentum**. The same commerce *engine* runs underneath; the **skin and
the voice change completely**.

## 2. What's REUSABLE (the key insight)

The commerce core ports almost unchanged — this is a **restyle + re-voice over the same
pipeline**, not a rewrite:

- **`build.py` + `products.json`** — same schema (id, slug, category, price, image,
  image2, stock, blurb, desc, details, stars/score/count). The catalog data is largely
  shared; only copy tone and possibly price framing differ.
- **`cart.js`** — the cart drawer, live inventory clamp, and the OC ZIP delivery gate
  are tier-agnostic. Reuse as-is (restyle the drawer's CSS only).
- **Page architecture** — index / shop / learn / gallery / product / newsletter / 404
  is a sound skeleton; keep it.

The cleanest implementation is a **sibling folder** (`omnicompost-family-site/`) that
forks the HTML/CSS shells but **shares or mirrors `build.py`/`products.json`/`cart.js`**.
Open question (§9): fork the build script vs. parameterize one script by `--theme`.

## 3. What's RADICALLY DIFFERENT

### Design tokens
| | Premium (this site) | Family |
|---|---|---|
| Palette | cream `#F4EDE0`, muted sage/terracotta/ochre/teal | paper `#FCF7EE`, **red `#D94F3E`, green `#5AAE3F`, sun `#F4C430`**, denim/wood |
| Corners | sharp (0–2px) | **rounded** (14–20px) |
| Shadows | flat / hairline | **chunky hard-offset** (`0 3px 0 ink`), pressable buttons |
| Ornament | none | badges, seals, ribbons, emoji icons |
| Type | Fraunces + Inter | **Bitter + Nunito Sans + Caveat** (handwritten accent) |

### Voice
| Premium | Family |
|---|---|
| Noun-first titles, Roman numerals | Verb-first, benefit-led ("Turn today's scraps into tomorrow's garden") |
| **Zero exclamation points** | Exclamation points welcome |
| Exact numbers ("385", "8 weeks") | Round, friendly numbers ("40,000+ households", "4.8/5") |
| Editorial restraint, second-person sparingly | Warm, conversational, heavy second-person, "you/your family" |
| No emoji | Emoji as functional icons (🚚 ⭐ 🏆 ♻️) |

### Content & structure
- **Hero**: big benefit headline + product shot + **trust seal** ("Best seller",
  star rating), value props as stat badges — vs Premium's quiet hero object.
- **How it works**: "Three easy steps. The worms do the rest." emoji **cards** —
  vs Premium's four-step numbered method essay.
- **Eco/value band**: "Great for your garden — and the planet" — explicit
  carbon/diversion + money-saving framing (Premium implies, never pitches).
- **Consumables store front-and-center**: "**Stock up your bin**" add-on grid is a
  headline section, not a sober catalog — recurring-purchase, replenishment framing.
- **Social proof**: review counts, "Loved by N families", third-party badges — louder
  and more numeric than Premium's restrained Voices section.
- **Learn page** skews **tips / recipes / FAQ / deals** ("Kitchen notes"), not a
  method monograph.
- **Guarantee / risk-reversal**: money-back guarantee and free-shipping threshold are
  surfaced prominently (per the profiles' design Q&A).

### Imagery
- Draws from the **60 parked `mainstream/` images** (brighter, people-present, real
  kitchens, market/garden, kids) — **explicitly NOT** the Premium Kodak-Portra register.
- Faces are fine here; lifestyle and family-in-frame is on-brand, the opposite of the
  Premium "partial hands, no faces" rule.

### Channels
- Consumables may also sell through **Amazon / Home Depot / big-box** (per RATINGS note).
  This affects messaging (replenishment, "also available at…"), and may add outbound
  CTAs or a channel-picker the Premium site never needs.

## 4. Page set (proposed)
Same skeleton as Premium, re-voiced:
`index.html` · `shop.html` · `learn.html` (→ "Kitchen notes / tips") · `gallery.html`
(family/lifestyle, not editorial) · `product/<slug>.html` (generated) · `newsletter.html`
(→ "Tips, recipes & deals") · `404.html`. Possible **Kids crossover** tab/section (see §9).
**Plus a campaign landing page** (`start.html`) for paid traffic — see §4a.

## 4a. Homepage direction — DECIDED (2026-06-01)
Settled by the comparative review (`mockups/website ideas/Family Options Review_2026-06-01.md`),
which rated three Family directions and recommended **using two of them for different jobs**:

- **Homepage → family-c "The Marketplace" (9.1/10).** The bento-grid, replenishment-forward
  layout is the best *fit* for the confirmed business model: it leads with the real
  consumables line, **subscribe-and-save**, the **"also at Amazon / Home Depot"** channel
  story, and the regional-shipping line — all above the fold in the 2026 information-density
  style, warmed into the Family register. This becomes the scaffold's `index.html`.
- **Campaign landing page → family-b "The Quick Start" (8.7/10).** The single-CTA conversion
  funnel ("Start composting — $389", trust row, 3 steps, money-back band, reviews, $15-off
  capture). It's a paid-traffic LP for the digester, **not** the storefront — it deliberately
  omits the consumables line, so it can't be the home. Ship it as `start.html`.
- **`family/` shell stays** as the proven, complete fallback homepage (9.0/10) and the source
  of the working `shop.html` / cart wiring already ported in step 3.

**Gates before either goes live** (from the review's −deductions):
1. Wire the shared `cart.js` into the family-c bento (its mockup cart is a static demo).
2. Swap the **lifestyle placeholders** in the bento tiles for real on-register **product**
   shots from `scraps/img-manual-pre-vetting/mainstream/`.
3. Watch density: family-c can read busy once real (longer) copy lands — verify at mobile widths.

## 5. What to learn / read first (before building)
1. The **Family** section of the `omnicompost-design-system` skill (authoritative voice
   + palette + type — do not improvise it).
2. `mockups/website ideas/family/index.html` — the 9.0/10 reference shell (tokens,
   button/badge/seal CSS, section order).
3. `mockups/website ideas/RATINGS.md` — the family note (−1.0 reasons, channel context).
4. The **mainstream image register** in the `omnicompost-image-sourcing` skill, and the
   60 `scraps/img-manual-pre-vetting/mainstream/` images.
5. `mockups/profiles/profiles/README.md` — fit-score ranking + the design Q&A
   (carbon pitch, social proof, money-back guarantee, shipping/assembly, out-of-zone
   waitlist).

## 6. Commerce specifics to mirror
- Reuse `cart.js` wholesale (restyle only). **DONE 2026-06-01:** the OC-only gate was
  replaced by a **regional tiered-shipping** module shared verbatim by both sites — one ZIP
  field → flat cost by region (OC $7 / metro SoCal $12 / rest-of-CA & nationwide $20, free
  over $150). Both sites ship everywhere; OC just gets the cheapest tier.
- Coupons already roadmapped (`FIELDNOTES`/`WHOLELOOP`/etc.) — Family may add
  value-oriented codes (bundle/first-order/subscribe-and-save).
- Subscribe-and-save / replenishment is a natural Family-only feature the Premium site
  deliberately omits.

## 7. Explicit DON'Ts
- **Do not mix tiers.** No cream/sage, no Fraunces, no Roman numerals, no "zero
  exclamation points" rule here — and conversely never let Family's red/sun/emoji bleed
  into the Premium site. (Design-system rule #1.)
- Don't reuse Premium photography in the Family register or vice-versa.
- Don't fork `cart.js` logic — only its styling.

## 8. Suggested build order (when greenlit)
1. ~~Scaffold `omnicompost-family-site/` from the family mockup; extract inline CSS to a
   token stylesheet.~~ **DONE (step 1).**
2. ~~Wire `cart.js` (copy in, restyle).~~ **DONE (step 2)** — now regional tiered shipping.
3. ~~Port `products.json` + `build.py`; re-voice; rebuild `shop.html` + product pages.~~
   **DONE (step 3).**
4. **Adopt the family-c "The Marketplace" bento as `index.html`** (per §4a): port its layout
   into the scaffold, replace the static demo cart with the shared `cart.js` drawer + IDs,
   and convert its product tiles to the `BUILD:SHOP` region so `build.py` owns them. Then build
   out `learn.html` ("Kitchen notes / tips"), `gallery.html`, `newsletter.html`, `404.html`
   in the Family voice. (`shop.html` already done in step 3.)
5. **Add `start.html`** — port family-b "The Quick Start" as the paid-traffic landing page
   (single CTA to the digester PDP/checkout; no consumables grid).
6. Source/place real mainstream **product** photography (replace lifestyle placeholders in the
   bento tiles); verify the whole set with `static-site-preview`.

## 9. Open questions to settle first (not decided here)
- **Repo layout:** ~~sibling folder vs. monorepo~~ — the Family site now lives under
  `omnicompost-premium-site/mockups/omnicompost-family-site/` (moved 2026-06-01).
- **Build script:** ~~fork vs. `--theme`~~ **RESOLVED 2026-06-01: forked** `build.py` into the
  Family folder (simplest, matches layout). Revisit `--theme` only if drift becomes a burden.
- **Catalog:** ~~one shared file vs. two~~ **RESOLVED 2026-06-01: two files** — a separate
  Family `products.json` re-voiced to the Family tone.
- **Kids:** a tab/section of Family, or its own separate surface (the Kids mockup is
  engagement-only, no cart)?
- ~~**Shipping story**~~ **RESOLVED 2026-06-01:** regional tiered shipping replaces the
  OC-only gate in both sites (OC / metro SoCal / nationwide; free over $150). See §6.
