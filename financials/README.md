# OmniCompost — Financial Model

_Last updated: 2026-06-03_0019_

A profit / revenue / expense estimate for the Premium storefront, modeled both
**per unit** and **per operating period** (one fiscal quarter), with a 12-month
ramp + cash-flow view. Owner-operated cost structure.

## Files

| File | What it is |
|------|------------|
| `../OmniCompost_Financial_Estimate.xlsx` | The deliverable workbook (8 tabs). |
| `../build_financials.py` | The generator. Edit this, not the xlsx, for structural changes. |
| `FINANCIALS-ROADMAP.md` | Planned accuracy upgrades, prioritized. |
| `FINANCIALS-CHANGELOG.md` | Version history of the model. |
| `FINANCIALS-ASSUMPTIONS.md` | Register of every input: value, source, status. |

## How to regenerate

```powershell
C:\anaconda\python.exe build_financials.py
```

Run from the `omnicompost-premium-site/` folder. **Close the xlsx in Excel first**
— an open file locks it and the save fails with `PermissionError`.

The script writes formulas, not cached values. Excel recalculates on open, so the
numbers populate automatically. (LibreOffice isn't installed here, so the skill's
`recalc.py` can't pre-bake values — not a problem for Excel users.)

## The 11 tabs

1. **Dashboard** — front-page KPI snapshot (quarter + annualized + year-1 cash + LTV:CAC), all linked.
2. **Assumptions** — every editable input (blue/yellow = edit; green = pulled from another tab).
   The demand-basis cell has 1–2 data validation; out-of-range entry is rejected.
3. **Per Unit** — price, COGS, gross profit/margin for all 10 SKUs (COGS pulled from BOM).
4. **BOM Landed Cost** — per-SKU product + freight + duty + packaging → landed cost → COGS %.
   **Drop real supplier numbers here**; they flow up into everything.
5. **SKU Mix** — order-share per SKU → computes the blended COGS % used downstream.
   Shares are validated 0–100% with a visible "total = 100%" check.
6. **Demand (Profiles)** — 20 personas from `mockups/profiles/`, with a Low/Base/High funnel band.
7. **Demand (Bottom-Up)** — non-overlapping OC Census buckets + EPA plausibility check. **Default driver.**
8. **Per Period (Quarter)** — the P&L (gross→discount→net revenue, incl. channel fees), break-even,
   LTV:CAC (now incl. subscription), subscription-MRR memo, sensitivity.
9. **Seasonality & 12-Month** — monthly ramp × seasonality, cumulative cash, break-even month,
   inventory/working-capital + total peak funding need.
10. **Sources & Method** — provenance of every number (REPO / PROFILES / CENSUS / ESTIMATE).
11. **Benchmarks** — savvy-operator/investor read: model ratios vs. premium-DTC targets, with verdicts.

## Switching demand basis

`Assumptions!B5`: **1** = profiles (sum-of-personas, over-counts, uses an overlap
haircut), **2** = bottom-up Census (each household counted once — recommended).
The whole P&L and 12-month view follow the switch via `CHOOSE`.

## Trust level

The **demand math rests on real repo + Census data**; the **cost structure and
funnel rates are estimates**. The two highest-value real numbers to drop in are
**per-SKU landed COGS** (no BOM exists yet) and **real checkout conversion** (Snipcart
is still a demo stub). See `FINANCIALS-ASSUMPTIONS.md` for the full status table.
