# Financial Model — Roadmap

_Last updated: 2026-06-03_0019_

Prioritized by how much uncertainty each item removes. Top items replace the
largest *invented* inputs with measured data.

## P0 — replaces the biggest guesses

- [x] **BOM/landed-cost sheet scaffolded** (v0.4). Per-SKU product + freight + duty +
      packaging → COGS, wired into Per Unit → SKU Mix → P&L. **Still TODO:** replace the
      placeholder component splits with real supplier invoices.
- [ ] **Real checkout conversion.** Once Snipcart is live (it's a demo stub per the
      site ROADMAP), replace the per-bucket Conv-given-fit % with measured
      `sessions → add-to-cart → purchase`. This is the single softest demand input.
- [ ] **Tune CAC to real ad data.** Now $150 placeholder; replace with actual blended
      acquisition cost once any paid channel runs. Drives the LTV:CAC verdict.

## P1 — structural realism

- [ ] **Target-CAC marketing tied to channels.** Break the flat $45 CAC into
      paid-social / referral / organic with per-channel CAC and volume.
- [~] **Repeat-purchase / LTV.** Subscription added in v0.5 (attach × $/mo × life × margin),
      lifting LTV:CAC ~1.6x → ~2.1x. **TODO:** replace the single attach/life pair with real
      cohort churn curves; push attach/value to clear 3.0x.
- [ ] **B2B lane.** Cafes/food trucks need invoicing + multi-unit pricing before the
      B2B bucket converts. Currently modeled at near-floor conversion.
- [~] **Inventory & working capital.** v0.5 adds an inventory-coverage (months of COGS held)
      working-capital line + total peak-funding. **TODO:** real per-SKU lead times and reorder
      points instead of a flat coverage factor.
- [~] **Channels & fees.** v0.5 adds wholesale + marketplace fee drag. **TODO:** split channel
      revenue/AOV/conversion rather than a flat fee on a revenue share.

## P2 — refinement

- [ ] **Per-bucket funnel band** (not just a global Low/High multiplier).
- [ ] **Tax handling beyond pass-through** — nexus, filing cadence.
- [ ] **Scenario manager** — save named cases (Conservative / Base / Aggressive).
- [ ] **Multi-year build** — years 2–3 with maturing conversion and churn.

## Data hooks to add when available

| Source | Replaces | Tab |
|--------|----------|-----|
| Snipcart order export | Conv %, SKU mix, AOV, repeat rate | Demand, SKU Mix |
| Supplier invoices / BOM | Per-SKU COGS | Per Unit |
| Ad platform reports | CAC, Reach % | Assumptions, Demand |
| ESP analytics | Newsletter → buyer rate | Demand |
| Bookkeeping actuals | Fixed opex lines | Assumptions |
