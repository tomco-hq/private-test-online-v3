# OmniCompost — Master Roadmap

_Last updated: 2026-06-03_0340_

The single top-level map of the OmniCompost build. This document does **not** duplicate
the detailed plans — it indexes the authoritative per-area roadmaps and carries the
cross-cutting to-do list. When in doubt, the linked documents win on detail; this one
wins on priority and "what's the state of the whole thing."

## Tier / surface status at a glance

| Surface | State | Authoritative doc |
|---|---|---|
| **Premium site** (production) | v1.8 — live storefront, cart, inventory, tiered regional shipping (ships statewide/nationwide), newsletter, learn.html, guarantee page, PDP specs expander, comparison/small-space FAQ | [ROADMAP.md](ROADMAP.md) |
| **B2B site** | v0.4 — build-complete, on-register, 9.0/10; blocked on launch deps | [mockups/omnicompost-b2b-site/REVIEW.md](mockups/omnicompost-b2b-site/REVIEW.md) · [README](mockups/omnicompost-b2b-site/README.md) |
| **Mainstream Family** | v0.7 — built sibling site (family-c bento `index` + `start` LP + shop/learn/gallery/newsletter/404 + 10 PDPs), shared cart.js + build.py wired, AA a11y pass, reviewed 9.1/10. Blocked only on real product photography (brand shoot) + checkout backend. | [mockups/omnicompost-family-site/REVIEW.md](mockups/omnicompost-family-site/REVIEW.md) · [SCAFFOLD-NOTES](mockups/omnicompost-family-site/SCAFFOLD-NOTES.md) · [MAINSTREAM-PLAN.md](MAINSTREAM-PLAN.md) |
| **Kids** | v0.5 — 4-page site + sort game + printable PDFs, AA-clean text, reviewed 9.2/10 | [mockups/omnicompost-kids-site/REVIEW.md](mockups/omnicompost-kids-site/REVIEW.md) · [PLAN](mockups/omnicompost-kids-site/PLAN.md) |
| **Financial model** | Active; replacing invented inputs with measured data | [financials/FINANCIALS-ROADMAP.md](financials/FINANCIALS-ROADMAP.md) |
| **Personas / segments** | Reference for fulfillment, delivery zones, B2B lane | [mockups/profiles/](mockups/profiles/) |

## Referenced individual roadmaps

- [ROADMAP.md](ROADMAP.md) — Premium commerce build + cross-cutting tracks (checkout,
  coupons, payments, tooling, fulfillment). The deepest single doc.
- [financials/FINANCIALS-ROADMAP.md](financials/FINANCIALS-ROADMAP.md) — financial model,
  prioritized P0→P1 by uncertainty removed.
- [MAINSTREAM-PLAN.md](MAINSTREAM-PLAN.md) — Mainstream Family tier plan.
- [mockups/omnicompost-kids-site/PLAN.md](mockups/omnicompost-kids-site/PLAN.md) — Kids tier.
- [mockups/profiles/B2B-REVIEW-AND-PLAN.md](mockups/profiles/B2B-REVIEW-AND-PLAN.md) — B2B plan.
- READMEs: [mockups/omnicompost-b2b-site/README.md](mockups/omnicompost-b2b-site/README.md) ·
  [mockups/website ideas/README.md](mockups/website%20ideas/README.md)

---

## Master to-do list

Ordered by what unblocks the most. Checkbox state reflects this document's last-updated
date — confirm against each area's own roadmap before acting.

### P0 — blocks launch / revenue

- [ ] **Wire live checkout (Snipcart).** Premium checkout is still a demo stub. Add
      Snipcart JS/CSS + public key, convert `.add` buttons to `snipcart-add-item`, hand
      the cart over to Snipcart. _Unblocks the Premium store **and** the financial model's
      conversion input._ → [ROADMAP.md](ROADMAP.md) Track A.1
- [ ] **Go-live the newsletter endpoint.** Paste the ESP public form endpoint into
      `ESP_ENDPOINT` (currently empty / demo mode). → [ROADMAP.md](ROADMAP.md) Track A.3
- [ ] **Stand up a live B2B quote endpoint.** The quote pipeline works in the mockup but
      posts nowhere. → [mockups/omnicompost-b2b-site/REVIEW.md](mockups/omnicompost-b2b-site/REVIEW.md)
- [ ] **Real per-SKU landed COGS.** Replace the 35–46% guess with a true BOM/landed-cost
      sheet; wire into `Per Unit!C`. _Biggest single swing in the model._
      → [financials/FINANCIALS-ROADMAP.md](financials/FINANCIALS-ROADMAP.md) P0

### P1 — structural / decisions to make

- [x] **Promote a Family homepage.** DONE — family-c "The Marketplace" bento is now the
      built site's `index.html`, with `cart.js` + `build.py` wired and a full page set
      (v0.7, 9.1/10). What remains for the Family tier is **not build work**: real product
      photography (brand-shoot-blocked) and the shared checkout backend (the P0 Snipcart
      item below). → [mockups/omnicompost-family-site/REVIEW.md](mockups/omnicompost-family-site/REVIEW.md) · [SCAFFOLD-NOTES](mockups/omnicompost-family-site/SCAFFOLD-NOTES.md)
- [ ] **B2B launch dependencies.** Real diversion/ROI data, business imagery, legal
      sign-off. Build is done; these gate going live.
      → [mockups/omnicompost-b2b-site/REVIEW.md](mockups/omnicompost-b2b-site/REVIEW.md)
- [ ] **Target-CAC marketing tied to channels.** Break the flat $45 CAC into per-channel.
      → [financials/FINANCIALS-ROADMAP.md](financials/FINANCIALS-ROADMAP.md) P1
- [ ] **Premium PDP polish for checkout.** Add crawlable `data-item-url` per product and a
      small image gallery once Snipcart lands. → [ROADMAP.md](ROADMAP.md) Track A.2

### P2 — polish / housekeeping

- [ ] Replace measured checkout conversion into the model once Snipcart is live.
      → [financials/FINANCIALS-ROADMAP.md](financials/FINANCIALS-ROADMAP.md) P0 (2nd item)
- [ ] Coupons / payment-method tracks (Premium). → [ROADMAP.md](ROADMAP.md) Tracks C, D
- [ ] Tooling track (build pipeline). → [ROADMAP.md](ROADMAP.md) Track E
- [~] Fulfillment / delivery-zone / risk-reversal from the persona analysis —
      _largely shipped (v1.8):_ tiered shipping replaced the OC gate (so the
      out-of-zone dead-end is gone), the 30-day + six-week guarantee is live, and
      the comparison/small-space/spec content landed. _Still open:_ third-party
      cert/social proof, two fulfillment tiers (ship vs. white-glove) + gift/
      deliver-to-second-address — both ride the Snipcart build.
      → [ROADMAP.md](ROADMAP.md) Track F · [mockups/profiles/](mockups/profiles/)

---

_Maintenance: when any linked roadmap changes priority or an item ships, update the
status table and the relevant checkbox here, and bump the timestamp above._
