# Financial Model — Changelog

_Last updated: 2026-06-03_0019_

Newest first. Dates use the project `YYYY-MM-DD_HHMM` stamp.

## 2026-06-03_0019 — v0.5 "Working capital & recurring"

- Added a **consumables subscription** to the LTV build (attach rate × $/month × avg life ×
  margin). Lifts customer LTV ~$81 → LTV:CAC moves **1.6x → ~2.1x**. An "implied steady-state
  MRR" memo shows the recurring upside, deliberately **excluded** from the P&L (conservative).
- Added **wholesale + marketplace channel fees** as a variable cost (fee % applied to the
  wholesale + marketplace share of gross revenue).
- Added **inventory / working-capital timing** to the Seasonality tab: inventory investment
  (months of COGS held) + a **total peak-funding** line = operating cash trough + inventory.
  Dashboard now shows total funding incl. working capital.
- Raised **returns 3% → 6%** (furniture-class durables run 5–15%; 3% was optimistic).
- Benchmarks "bottom line" updated — items previously flagged as missing are now modeled.
- Validation: 400 formulas, 0 self-references, 0 bad references. Still 11 tabs (folded in,
  no new sheet).

## 2026-06-02_1441 — v0.4 "Reality check"

- Added **BOM Landed Cost** tab (P0): per-SKU product + freight + duty + packaging →
  landed cost → COGS %, flowing up into Per Unit → SKU Mix → P&L. COGS is no longer a
  free-floating guess; it's built from components you can replace with supplier data.
- Added **promo / discount allowance** → P&L now runs gross revenue → discounts → net revenue.
- Raised **CAC $45 → $150** (premium-durable realism) and **owner pay $48k → $72k/yr** (market wage).
- Added **LTV:CAC** block (customer LTV incl. consumable repeat, CAC payback, marketing % of revenue).
- Added **Benchmarks** tab — model ratios vs. premium-DTC / VC targets with auto verdicts.
- Net effect: the base case now shows a **realistic year-1 loss** (~−7% net) instead of an
  implausible 23% profit — which is what a savvy investor would expect while acquiring customers.
- Dashboard gains LTV:CAC and marketing-% KPIs. Validation: 394 formulas, 0 bad references.

## 2026-06-02_1441 — v0.3 "Accuracy pass"

- Added **bottom-up Census demand** tab (7 non-overlapping OC buckets) — removes the
  persona overlap fudge; each household counted once. Now the default demand basis.
- Added a **demand-basis switch** (`Assumptions!B5`, CHOOSE) between Profiles and Bottom-up.
- Added **Low/Base/High funnel band** to the Profiles tab.
- Added **SKU Mix** tab — blended COGS now computed from order-share × price × cost
  (was a flat 45% guess).
- **Marketing** switched to CAC × new buyers (was a fixed budget).
- Added variable costs: **per-transaction fees, refunds, chargebacks, live-goods spoilage**.
- Added **owner salary** line — net profit is now after owner pay.
- Added **sales-tax pass-through memo**, **EPA ceiling check**, **break-even** + contribution margin.
- Added **Seasonality & 12-Month** tab — monthly ramp × seasonality, cumulative cash,
  break-even month, peak funding need.
- Added a front **Dashboard** tab — quarter + annualized KPIs and year-1 cash, all linked.
- Added **data validation**: demand-basis cell (1–2) and SKU shares (0–100%) with a 100%-total check.
- Added internal docs (README / ROADMAP / CHANGELOG / ASSUMPTIONS) under `financials/`.
- Fixed a variable-shadowing bug where the Sources loop clobbered the demand-basis
  row, corrupting the Dashboard basis formula (`B<text>` → `B5`).
- Validation: 327 formulas, 0 self-references, 0 bad references, all cross-tab links resolve.

## 2026-06-02 — v0.2 "Profile-driven + sensitivity"

- Rewired demand to pull from `mockups/profiles/profile_market_estimates.xlsx` (20 personas).
- Flipped cost base to **owner-operated** (no salaried staff, home/garage fulfillment, lower marketing).
- Added an **overlap & ramp** haircut on the over-counting persona total.
- Added a **Sources & Method** tab and a 30/45/55/70% overlap **sensitivity table**.
- Fixed a circular reference in the sensitivity net-profit row (`=B24+B26` → `=B24+B25`).

## 2026-06-02 — v0.1 "First estimate"

- Initial per-unit + per-quarter P&L from `products.json` prices.
- Placeholder volumes and a staffed-warehouse cost base (later replaced).
