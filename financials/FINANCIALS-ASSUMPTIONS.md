# Financial Model — Assumptions Register

_Last updated: 2026-06-03_0019_

Every input the model rests on, with its source and how much to trust it. Mirrors
the workbook's **Sources & Method** tab in living-doc form. Status key:

- **REPO** — real data from a project file.
- **PROFILES** — from `mockups/profiles/profile_market_estimates.xlsx` (part-verified).
- **CENSUS** — web-verified US Census/ACS anchor (checked 2026-06-01).
- **ESTIMATE** — my assumption; replace with real data.

## Demand

| Input | Value | Source | Status |
|-------|-------|--------|--------|
| SKU list prices | $19–$465 | `products.json` | REPO |
| Persona segment sizes / AOV | per row | profiles workbook | PROFILES |
| Reach / In-market / Conv-fit % | per row | profiles rules-of-thumb | ESTIMATE |
| OC households | 1,080,000 | Census/ACS 2024 | CENSUS |
| OC owner-occupied share | 56–57% | FRED/Data USA ACS | CENSUS |
| OC median household income | ~$116,300 | Census QuickFacts | CENSUS |
| OC food establishments | ~9,800 | Tripadvisor proxy | CENSUS (approx) |
| LA County households | ~3.42M | Census QuickFacts | CENSUS |
| EPA composting rate | ~4% | EPA 2019 est. | CENSUS |
| Bottom-up bucket sizes | see tab | derived from anchors above | ESTIMATE |
| Year-1 ramp / overlap factor | 60% / 55% | maturity & de-dup judgement | ESTIMATE |
| Funnel Low/High multiplier | 0.55 / 1.65 | scenario band | ESTIMATE |

## Unit economics & costs

| Input | Value | Source | Status |
|-------|-------|--------|--------|
| Per-SKU landed COGS | see BOM tab | placeholder product/freight/duty/packaging splits | ESTIMATE |
| SKU order-share mix | see SKU Mix | guessed basket | ESTIMATE |
| Promo / discount allowance | 8% of gross rev | coupons/sales; real DTC 8–15% | ESTIMATE |
| CAC per new customer | $150 | premium-durable realism (was $45) | ESTIMATE |
| Customer LTV inputs | 0.8 reorders × 3 yr × $35 × 60% | consumable repeat | ESTIMATE |
| Payment processing | 2.9% + $0.30/order | Stripe-class | ESTIMATE |
| Refunds & returns | 6.0% of rev | furniture-class durable 5–15%; was 3% | ESTIMATE |
| Subscription attach / value / margin / life | 30% / $26-mo / 65% / 16 mo | consumables auto-ship | ESTIMATE |
| Wholesale / marketplace share | 10% / 8% of rev | channel mix | ESTIMATE |
| Marketplace/wholesale fee | 15% on those sales | referral fee / wholesale give-up | ESTIMATE |
| Inventory coverage | 2.0 months of COGS | stock held ahead of sale | ESTIMATE |
| Chargebacks | 0.5% of rev | industry rule | ESTIMATE |
| Live-goods spoilage | 1.0% of rev | worm/concentrate mortality | ESTIMATE |
| Shipping absorbed / order | $9 | per tiered shipping in `cart.js` | REPO-informed |
| CAC / new-customer share | $45 / 70% | placeholder | ESTIMATE |
| Fixed opex (4 lines) | $11,500/qtr | owner-operated structure | ESTIMATE |
| Owner salary | $18,000/qtr | market-rate operator wage (~$72k/yr) | ESTIMATE |
| Sales tax rate | 7.75% | OC rate; pass-through | REPO-informed |

## Seasonality (Year-1)

| Input | Value | Source | Status |
|-------|-------|--------|--------|
| Monthly ramp index | 0.35 → 1.20 | year-1 growth curve | ESTIMATE |
| Monthly season multiplier | spring/holiday peaks | garden demand pattern | ESTIMATE |

## The honest summary

Revenue is better-grounded than the bottom line. Demand uses real prices and
verified Census anchors; **costs and funnel conversion are estimates**. Treat the
output as a *structured scenario*, not a forecast, until the P0 items in the
roadmap (real COGS + real conversion) are filled in.
