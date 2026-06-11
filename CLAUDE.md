# OmniCompost Premium Site — Project Memory

_Last updated: 2026-06-10_2016_

A static storefront (HTML/CSS/JS, no framework) for the Premium tier of
OmniCompost, a worm-composting digester. Coastal Orange County buyer; editorial
restraint, not a sales pitch.

## What this site is

- **Plain static files.** No Node, no bundler, no framework. One Python build
  script regenerates the shop from data; everything else is hand-written HTML.
- **Single source of truth:** `products.json` → `build.py` → shop grids +
  `product/<slug>.html`. Never hand-edit a product into the HTML — edit the JSON
  and rebuild (`C:\anaconda\python.exe build.py`).
- **One shared `cart.js`** drives the cart drawer, live inventory clamp, and the
  regional **tiered shipping** estimate (one ZIP field → flat cost by region: OC /
  metro SoCal / rest-of-CA & nationwide, free over $150) on every page. The same
  file ships in the Family site, no logic fork. It's not generated — edit it
  directly. (This replaced the old Orange-County-only delivery gate on 2026-06-01.)

## Layout

```
products.json        catalog (source of truth)
build.py             regenerates shop grids + product/ pages from products.json
index.html           homepage (#shop grid lives between BUILD:SHOP markers)
shop.html            full catalog (same markers)
learn.html           "How it works" — method, one-page-guide/QR scaffold, big FAQ
can-i-compost.html   /can-i-compost — searchable "Can I Compost This?" page.
                     GENERATED — do not hand-edit. Source: field-guides/items.json
                     + field-guides/scripts/build_mobile.py (writes here + the
                     editable prototype). Linked from the learn.html guides row
                     and the homepage "How it works" dropdown. QR short link:
                     /g/compost → /can-i-compost.
gallery.html         editorial photo gallery (harvest / garden / pollinators)
404.html             branded not-found page (host should map 404s here)
product/<slug>.html  generated detail pages — DO NOT hand-edit
                     (optional image2/alt2 in products.json adds a swap thumbnail)
cart.js              shared cart + inventory clamp + tiered regional shipping
                     (OC $7 / metro SoCal $12 / rest-of-CA & nationwide $20, free
                     over $150 — replaced the OC ZIP gate 2026-06-01)
newsletter.html      ESP-wired signup (hand-written)
notes/*.html         Field Notes editorial issues (hand-written)
assets/img|logo/     local images only — never hotlink
guides/              reviewed v2 working guides + README (start here)
scraps/              advisory reference only — NOT authoritative
ROADMAP / CHANGELOG / REVIEW / SUMMARY .md   living docs (keep timestamped)
CONTENT-GUIDE.md     how to add/edit each part of the site
```

## How to work here

- **Editing the shop?** Use the `omnicompost-commerce` skill. Edit
  `products.json`, run `build.py`, done. Stock: set `stock` (0 = sold out).
- **Verifying a change?** Use the `static-site-preview` skill. Preview root is
  **this folder**, so routes are `/index.html`, `/shop.html`,
  `/product/<slug>.html` — not `/omnicompost-premium-site/...`.
- **Writing any customer-facing copy or picking colors/type?** The
  `omnicompost-design-system` skill is authoritative — Premium voice only here
  (cream `#F4EDE0`, sage/terracotta/ochre/teal, Fraunces + Inter, sharp corners,
  Roman numerals, **zero exclamation points**, noun-first titles, exact numbers).
- **Sourcing photos?** `omnicompost-image-sourcing` skill; host locally under
  `assets/img/`, never hotlink.
- **Adding content (a product, a Field Notes issue, an image)?** Step-by-step in
  `CONTENT-GUIDE.md`.

## Conventions

- Living docs (ROADMAP/CHANGELOG/REVIEW/SUMMARY + every guide) carry a
  `_Last updated: YYYY-MM-DD_HHMM_` line under the title. Stamp it on every edit.
- `scraps/` is advisory, not authoritative (per project memory) — useful
  reference, overrulable with reason. Don't treat it as the source of truth.
- Show a visible numeric rating on product/comparison deliverables by default
  (standing user preference).
- No secrets in the repo: `ESP_ENDPOINT` is a form URL, Snipcart's public key is
  publishable; anything secret goes in a serverless function, never committed.

## Not built yet (see ROADMAP.md)

Checkout (Snipcart), coupons (`FIELDNOTES`/`WHOLELOOP`/`EDITIONONE`/`SPRINGWAKE`/
`REFER25`), payments (Stripe cards/Apple Pay/Google Pay/Link + PayPal — **not**
Zelle/Venmo), and the Family/Kids storefront tiers. The shipping tiers are a
client-side estimate only — compute the authoritative charge server-side when a
backend lands.

## Don't

- Don't hand-edit `product/*.html` or the `BUILD:SHOP` regions — `build.py` owns
  them and will overwrite.
- Don't mix another tier's voice/palette into Premium (design-system rule #1).
- Don't run pip/python through Git Bash — it mangles `C:\anaconda\python.exe`
  and leading-slash paths. Use PowerShell.
