from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation

BLUE = Font(name="Arial", size=10, color="0000FF")
BLACK = Font(name="Arial", size=10, color="000000")
GREEN = Font(name="Arial", size=10, color="008000")
BOLD = Font(name="Arial", size=10, bold=True, color="000000")
BLUEB = Font(name="Arial", size=10, bold=True, color="0000FF")
TITLE = Font(name="Arial", size=14, bold=True, color="000000")
H2F = Font(name="Arial", size=12, bold=True, color="000000")
NOTE = Font(name="Arial", size=9, italic=True, color="555555")
HDR = Font(name="Arial", size=10, bold=True, color="FFFFFF")
HDR_FILL = PatternFill("solid", start_color="2F5233")
YELLOW = PatternFill("solid", start_color="FFFF00")
SUB_FILL = PatternFill("solid", start_color="E8E0D0")
GREENBG = PatternFill("solid", start_color="DDEBD8")
CUR = "$#,##0;($#,##0);-"
CUR2 = "$#,##0.00;($#,##0.00);-"
PCT = "0.0%;(0.0%);-"
PCT2 = "0.00%;(0.00%);-"
NUM = "#,##0;(#,##0);-"
NUM1 = "#,##0.0;(#,##0.0);-"
thin = Side(style="thin", color="BBBBBB")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)


def hdrrow(ws, r, labels, start=1, wrap=True):
    for i, h in enumerate(labels, start):
        c = ws.cell(r, i, h)
        c.font = HDR
        c.fill = HDR_FILL
        c.border = BORDER
        c.alignment = Alignment(horizontal="center", wrap_text=wrap)


def section(ws, r, text, span=2):
    c = ws.cell(r, 1, text)
    c.font = BOLD
    for col in range(1, span + 1):
        ws.cell(r, col).fill = SUB_FILL


products = [
    ("The Digester", 385, 0.45),
    ("The Mini Digester", 245, 0.45),
    ("Red Wigglers", 42, 0.35),
    ("Worm Starter Kit", 58, 0.40),
    ("Bedding Bricks x3", 22, 0.40),
    ("Harvest Trowel", 34, 0.42),
    ("Tea Watering Can", 48, 0.42),
    ("Seedling Pots x6", 28, 0.40),
    ("Tea Concentrate", 19, 0.35),
    ("The Whole Loop", 465, 0.46),
]
# order-share of each SKU (sum = 1.0) - drives blended COGS / implied AOV
sku_share = [0.12, 0.12, 0.14, 0.10, 0.08, 0.07, 0.07, 0.08, 0.07, 0.15]

profiles = [
    ("Personal Chef (Marisol)", 500, 0.20, 0.40, 0.30, 385),
    ("DINK Couple (Devon & Priya)", 120000, 0.12, 0.22, 0.26, 385),
    ("Climate New Grad (Theo)", 80000, 0.15, 0.12, 0.14, 245),
    ("Out-of-Zone Aspirational (Renata)", 200000, 0.05, 0.20, 0.26, 385),
    ("Skeptical Gift-Giver (Bob)", 50000, 0.04, 0.10, 0.14, 465),
    ("HOA / Apartment (Grace)", 150000, 0.10, 0.18, 0.16, 245),
    ("Master Gardener (Hank)", 40000, 0.20, 0.40, 0.14, 465),
    ("Accessibility-Reliant (Dana)", 3000, 0.08, 0.20, 0.26, 385),
    ("Mobile Impulse (Jordan)", 60000, 0.15, 0.12, 0.12, 245),
    ("Comparison Shopper (Aaron)", 50000, 0.12, 0.25, 0.12, 385),
    ("Santa Monica Lawyer (Eleanor)", 30000, 0.05, 0.18, 0.18, 465),
    ("Instagram Bakery (Sana)", 5000, 0.06, 0.30, 0.08, 245),
    ("Food Truck (Marco)", 1500, 0.05, 0.35, 0.03, 385),
    ("Small Cafe (Priya)", 3000, 0.07, 0.35, 0.10, 770),
    ("Retired Gardener Grandparents", 90000, 0.15, 0.42, 0.26, 245),
    ("Snowbird Grandparent (Margaret)", 25000, 0.08, 0.30, 0.22, 465),
    ("Fixed-Income Retiree (Eduardo)", 70000, 0.10, 0.35, 0.08, 245),
    ("Eco-Skeptic Spouse (Greg)", 100000, 0.10, 0.08, 0.08, 385),
    ("Wellness / Clean-Living (Saskia)", 60000, 0.12, 0.22, 0.28, 465),
    ("Gen-Z TikTok Discoverer (Mia)", 150000, 0.15, 0.10, 0.05, 245),
]

# Non-overlapping OC household buckets (sizes sum to ~OC households 1.08M) + B2B + out-of-zone
# name, size, reach, in-market, conv, AOV, anchor-note
buckets = [
    (
        "Affluent owner-occ gardener HH",
        110000,
        0.12,
        0.35,
        0.22,
        465,
        "Top-income owner homes that garden",
    ),
    (
        "Affluent owner-occ non-gardener",
        165000,
        0.10,
        0.15,
        0.16,
        385,
        "Top-income owner homes, no garden focus",
    ),
    (
        "Mid-income owner-occ HH",
        335000,
        0.08,
        0.15,
        0.12,
        385,
        "Remaining owner-occupied households",
    ),
    (
        "Renter / apartment HH (Mini)",
        400000,
        0.08,
        0.12,
        0.10,
        245,
        "OC renters; Mini is the unlock",
    ),
    (
        "Budget / fixed-income HH",
        70000,
        0.06,
        0.20,
        0.05,
        245,
        "Better served on Family tier",
    ),
    (
        "OC small business (B2B)",
        9800,
        0.10,
        0.30,
        0.06,
        770,
        "Cafes/food est.; needs B2B lane",
    ),
    (
        "Out-of-zone LA aspirational",
        3420000,
        0.01,
        0.10,
        0.10,
        385,
        "LA metro HH; very low reach as non-local",
    ),
]

wb = Workbook()

# ============================================================ ASSUMPTIONS
a = wb.active
a.title = "Assumptions"
a.sheet_view.showGridLines = False
a["A1"] = "OmniCompost - Financial Model (Owner-Operated)"
a["A1"].font = TITLE
a["A2"] = (
    "Operating period = 1 fiscal quarter. Demand from mockups/profiles/profile_market_estimates.xlsx "
    "and a bottom-up Census build. Blue/yellow = editable input. Green = pulled from another tab."
)
a["A2"].font = NOTE

inp = {}
r = 4


def put(label, val, fmt, note="", blue=True):
    global r
    a.cell(r, 1, label).font = BLACK
    c = a.cell(r, 2)
    c.value = val
    c.number_format = fmt
    if blue:
        c.font = BLUE
        c.fill = YELLOW
    else:
        c.font = GREEN
    if note:
        a.cell(r, 3, note).font = NOTE
    inp[label] = r
    r += 1


section(a, r, "Demand & scenario", 3)
r += 1
put(
    "Demand basis (1 = Profiles, 2 = Bottom-up Census)",
    2,
    NUM,
    "Drives the P&L; 2 = recommended",
)
put("Periods per year", 4, NUM, "Quarters")
put(
    "Year-1 ramp factor (bottom-up maturity)", 0.60, PCT, "Year 1 < mature-brand demand"
)
put(
    "Overlap & ramp factor (profiles only)",
    0.55,
    PCT,
    "Profiles over-count; not needed for bottom-up",
)
put("Funnel scenario - Low multiplier", 0.55, PCT, "Pessimistic band on funnel rates")
put("Funnel scenario - High multiplier", 1.65, PCT, "Optimistic band on funnel rates")

r += 1
section(a, r, "Unit economics", 3)
r += 1
a.cell(r, 1, "Blended COGS % (computed from SKU mix)").font = BLACK
a.cell(r, 2).value = "='SKU Mix'!E14"
a.cell(r, 2).font = GREEN
a.cell(r, 2).number_format = PCT
a.cell(r, 3, "Revenue-weighted; edit shares on SKU Mix").font = NOTE
inp["Blended COGS %"] = r
r += 1

r += 1
section(a, r, "Variable cost rates", 3)
r += 1
put("Payment processing % of revenue", 0.029, PCT2)
put("Payment fee per order ($)", 0.30, CUR2)
put(
    "Refunds & returns % of revenue",
    0.06,
    PCT,
    "Furniture-class durable returns run 5-15%; was an optimistic 3%",
)
put("Chargebacks % of revenue", 0.005, PCT2)
put(
    "Live-goods spoilage % of revenue",
    0.010,
    PCT,
    "Worm/concentrate mortality in transit",
)
put(
    "CAC - marketing $ per new customer",
    150,
    CUR,
    "Premium durable; $45 was unrealistically low",
)
put("New-customer share of orders %", 0.70, PCT, "Rest are repeat buyers (no CAC)")
put(
    "Promo / discount allowance % of gross rev",
    0.08,
    PCT,
    "Coupons, sales; real DTC discounts 8-15%",
)
put(
    "Avg shipping absorbed per order ($)",
    9,
    CUR,
    "Free ship >$150; mostly OC self-deliver gas",
)

r += 1
section(a, r, "Fixed operating expenses - per quarter", 3)
r += 1
fx_first = r
put("Part-time / seasonal help", 6000, CUR, "No salaried staff")
put("Home / garage fulfillment & storage", 1500, CUR, "vs leased warehouse")
put("Software, hosting, tools", 1500, CUR)
put("Insurance, admin, misc.", 2500, CUR)
fx_last = r - 1
a.cell(r, 1, "Total fixed opex / quarter").font = BOLD
a.cell(r, 2, f"=SUM(B{fx_first}:B{fx_last})").font = BOLD
a.cell(r, 2).number_format = CUR
total_fixed_row = r
r += 1

r += 1
section(a, r, "Owner pay & tax", 3)
r += 1
put(
    "Owner salary / draw per quarter",
    18000,
    CUR,
    "Market-rate operator wage (~$72k/yr); was $48k",
)
put(
    "Sales tax rate (collected & remitted)",
    0.0775,
    PCT2,
    "Pass-through; excluded from P&L",
)

r += 1
section(a, r, "Customer lifetime value (for LTV:CAC)", 3)
r += 1
put(
    "Repeat consumable orders / customer / yr",
    0.8,
    NUM1,
    "Worms, bedding, concentrate reorders",
)
put("Avg repeat order value ($)", 35, CUR, "Consumable basket")
put("Retention (years)", 3, NUM1, "How long a customer keeps reordering")
put("Repeat-order gross margin %", 0.60, PCT, "Consumables margin")

r += 1
section(a, r, "Subscription (consumables auto-ship)", 3)
r += 1
put(
    "Subscription attach rate % of new customers",
    0.30,
    PCT,
    "Share who start an auto-ship plan",
)
put("Subscription value $/month", 26, CUR, "Worms/bedding/concentrate auto-ship")
put("Subscription gross margin %", 0.65, PCT, "Consumables margin")
put("Subscription avg life (months)", 16, NUM1, "Months before churn")

r += 1
section(a, r, "Sales channels & fees", 3)
r += 1
put("Wholesale % of revenue", 0.10, PCT, "Cafes/retailers at wholesale terms")
put("Marketplace % of revenue", 0.08, PCT, "Amazon/Etsy/etc.")
put(
    "Marketplace/wholesale fee % on those sales",
    0.15,
    PCT,
    "Referral fees / wholesale margin give-up",
)

r += 1
section(a, r, "Working capital", 3)
r += 1
put(
    "Inventory coverage (months of COGS held)",
    2.0,
    NUM1,
    "Stock paid for ahead of the sale",
)

a.column_dimensions["A"].width = 44
a.column_dimensions["B"].width = 13
a.column_dimensions["C"].width = 42

# ============================================================ PER UNIT
pu = wb.create_sheet("Per Unit")
pu.sheet_view.showGridLines = False
pu["A1"] = "Per-Unit Economics"
pu["A1"].font = TITLE
hdrrow(
    pu, 3, ["Product", "Price", "COGS %", "Unit COGS", "Gross Profit", "Gross Margin %"]
)
s = 4
for i, (name, price, cogs) in enumerate(products):
    rr = s + i
    pu.cell(rr, 1, name).font = BLACK
    c = pu.cell(rr, 2, price)
    c.font = BLUE
    c.fill = YELLOW
    c.number_format = CUR
    c = pu.cell(rr, 3, f"='BOM Landed Cost'!H{4 + i}")  # computed landed COGS %
    c.font = GREEN
    c.number_format = PCT
    pu.cell(rr, 4, f"=B{rr}*C{rr}").number_format = CUR2
    pu.cell(rr, 5, f"=B{rr}-D{rr}").number_format = CUR2
    pu.cell(rr, 6, f"=E{rr}/B{rr}").number_format = PCT
    for col in range(1, 7):
        pu.cell(rr, col).border = BORDER
e = s + len(products) - 1
tr = e + 1
pu.cell(tr, 1, "Blended").font = BOLD
pu.cell(tr, 2, f"=AVERAGE(B{s}:B{e})").number_format = CUR
pu.cell(tr, 4, f"=AVERAGE(D{s}:D{e})").number_format = CUR2
pu.cell(tr, 5, f"=AVERAGE(E{s}:E{e})").number_format = CUR2
pu.cell(tr, 6, f"=SUM(E{s}:E{e})/SUM(B{s}:B{e})").number_format = PCT
for col in range(1, 7):
    pu.cell(tr, col).font = BOLD
    pu.cell(tr, col).fill = SUB_FILL
    pu.cell(tr, col).border = BORDER
pu.column_dimensions["A"].width = 22
for col in "BCDEF":
    pu.column_dimensions[col].width = 13

# ============================================================ BOM / LANDED COST
bm = wb.create_sheet("BOM Landed Cost")
bm.sheet_view.showGridLines = False
bm["A1"] = "BOM / Landed Cost - per SKU (drives COGS)"
bm["A1"].font = TITLE
bm["A2"] = (
    "Replace these placeholder splits with real supplier numbers. Landed unit cost = product + "
    "inbound freight + duty + packaging. COGS % = landed / price flows up into Per Unit -> SKU Mix -> P&L."
)
bm["A2"].font = NOTE
hdrrow(
    bm,
    3,
    [
        "Product",
        "Price",
        "Product cost",
        "Inbound freight",
        "Duty / tariff",
        "Packaging",
        "Landed unit cost",
        "COGS %",
    ],
)
# placeholder split of the prior target landed cost (product/freight/duty/packaging)
bom_split = (0.68, 0.14, 0.06, 0.12)
bs0 = 4
for i, (name, price, cogs) in enumerate(products):
    rr = bs0 + i
    pu_row = s + i
    target = round(price * cogs, 2)
    bm.cell(rr, 1, name).font = BLACK
    bm.cell(rr, 2, f"='Per Unit'!B{pu_row}").font = GREEN
    bm.cell(rr, 2).number_format = CUR
    for col, frac in zip((3, 4, 5, 6), bom_split):
        c = bm.cell(rr, col, round(target * frac, 2))
        c.font = BLUE
        c.fill = YELLOW
        c.number_format = CUR2
    bm.cell(rr, 7, f"=SUM(C{rr}:F{rr})").number_format = CUR2
    bm.cell(rr, 8, f"=G{rr}/B{rr}").number_format = PCT
    for col in range(1, 9):
        bm.cell(rr, col).border = BORDER
be0 = bs0 + len(products) - 1
bt0 = be0 + 1
bm.cell(bt0, 1, "Blended").font = BOLD
bm.cell(bt0, 7, f"=AVERAGE(G{bs0}:G{be0})").number_format = CUR2
bm.cell(bt0, 8, f"=SUM(G{bs0}:G{be0})/SUM(B{bs0}:B{be0})").number_format = PCT
for col in range(1, 9):
    bm.cell(bt0, col).font = BOLD
    bm.cell(bt0, col).fill = SUB_FILL
    bm.cell(bt0, col).border = BORDER
bm.column_dimensions["A"].width = 22
for col in "BCDEFGH":
    bm.column_dimensions[col].width = 13

# ============================================================ SKU MIX
sk = wb.create_sheet("SKU Mix")
sk.sheet_view.showGridLines = False
sk["A1"] = "SKU Mix - blended COGS & implied basket"
sk["A1"].font = TITLE
sk[
    "A2"
] = "Order share by SKU drives the revenue-weighted blended COGS used in the P&L. Shares must sum to 100%."
sk["A2"].font = NOTE
hdrrow(
    sk, 3, ["Product", "Price", "COGS %", "Order share %", "Rev weight", "COGS weight"]
)
ss = 4
for i, (name, price, cogs) in enumerate(products):
    rr = ss + i
    pu_row = s + i
    sk.cell(rr, 1, name).font = BLACK
    sk.cell(rr, 2, f"='Per Unit'!B{pu_row}").font = GREEN
    sk.cell(rr, 2).number_format = CUR
    sk.cell(rr, 3, f"='Per Unit'!C{pu_row}").font = GREEN
    sk.cell(rr, 3).number_format = PCT
    c = sk.cell(rr, 4, sku_share[i])
    c.font = BLUE
    c.fill = YELLOW
    c.number_format = PCT
    sk.cell(rr, 5, f"=B{rr}*D{rr}").number_format = CUR2
    sk.cell(rr, 6, f"=B{rr}*C{rr}*D{rr}").number_format = CUR2
    for col in range(1, 7):
        sk.cell(rr, col).border = BORDER
se = ss + len(products) - 1  # = 13
# row 14: blended
sk.cell(14, 1, "Blended / total").font = BOLD
sk.cell(14, 4, f"=SUM(D{ss}:D{se})").number_format = PCT  # share check (should = 100%)
sk.cell(14, 5, f"=SUM(E{ss}:E{se})")
sk.cell(14, 5).number_format = CUR2
sk.cell(
    14, 6, f"=SUM(F{ss}:F{se})/SUM(E{ss}:E{se})"
)  # blended COGS %  (E14 referenced by Assumptions)
# NOTE: Assumptions links 'SKU Mix'!E14 as blended COGS%; place it in E14:
sk.cell(14, 5).value = f"=SUM(F{ss}:F{se})/SUM(E{ss}:E{se})"  # blended COGS% in E14
sk.cell(14, 5).number_format = PCT
sk.cell(14, 6).value = f"=SUM(E{ss}:E{se})"  # implied AOV/basket in F14
sk.cell(14, 6).number_format = CUR2
for col in range(1, 7):
    sk.cell(14, col).font = BOLD
    sk.cell(14, col).fill = SUB_FILL
    sk.cell(14, col).border = BORDER
sk.cell(15, 4, "<- must total 100%").font = NOTE
sk.cell(15, 5, "<- blended COGS %").font = NOTE
sk.cell(15, 6, "<- implied basket $").font = NOTE
sk.column_dimensions["A"].width = 22
for col in "BCDEF":
    sk.column_dimensions[col].width = 13
sk.column_dimensions["F"].width = 14

# ============================================================ DEMAND (PROFILES)
dm = wb.create_sheet("Demand (Profiles)")
dm.sheet_view.showGridLines = False
dm["A1"] = "Annual Demand - Reception Profiles (with funnel band)"
dm["A1"].font = TITLE
dm["A2"] = (
    "Source: profile_market_estimates.xlsx. Purchase % = Reach x In-market x Conv-fit. "
    "Raw total over-counts (segments overlap) -> overlap factor. Low/High = funnel scenario band."
)
dm["A2"].font = NOTE
hdrrow(
    dm,
    4,
    [
        "Persona",
        "Segment",
        "Reach %",
        "In-mkt %",
        "Conv %",
        "Purchase %",
        "Buyers/yr",
        "AOV",
        "Revenue/yr",
    ],
)
ds = 5
for i, (name, size, reach, inm, conv, aov) in enumerate(profiles):
    rr = ds + i
    dm.cell(rr, 1, name).font = BLACK
    for col, val, fmt in [
        (2, size, NUM),
        (3, reach, PCT),
        (4, inm, PCT),
        (5, conv, PCT),
        (8, aov, CUR),
    ]:
        c = dm.cell(rr, col, val)
        c.font = BLUE
        c.fill = YELLOW
        c.number_format = fmt
    dm.cell(rr, 6, f"=C{rr}*D{rr}*E{rr}").number_format = PCT2
    dm.cell(rr, 7, f"=B{rr}*F{rr}").number_format = NUM1
    dm.cell(rr, 9, f"=G{rr}*H{rr}").number_format = CUR
    for col in range(1, 10):
        dm.cell(rr, col).border = BORDER
de = ds + len(profiles) - 1
dt = de + 1
dm.cell(dt, 1, "TOTAL (raw - over-counts)").font = BOLD
dm.cell(dt, 7, f"=SUM(G{ds}:G{de})").number_format = NUM
dm.cell(dt, 9, f"=SUM(I{ds}:I{de})").number_format = CUR
for col in range(1, 10):
    dm.cell(dt, col).font = BOLD
    dm.cell(dt, col).fill = SUB_FILL
    dm.cell(dt, col).border = BORDER
ov = inp["Overlap & ramp factor (profiles only)"]
lo = inp["Funnel scenario - Low multiplier"]
hi = inp["Funnel scenario - High multiplier"]
adj = dt + 1
dm.cell(adj, 1, "Realized (x overlap)  [BASE]").font = BOLD
dm.cell(adj, 7, f"=G{dt}*Assumptions!B{ov}").font = BOLD
dm.cell(adj, 7).number_format = NUM
dm.cell(adj, 9, f"=I{dt}*Assumptions!B{ov}").font = BOLD
dm.cell(adj, 9).number_format = CUR
for col in range(1, 10):
    dm.cell(adj, col).fill = GREENBG
prof_buyers, prof_rev = adj, adj
band = adj + 1
dm.cell(band, 1, "Realized - Low funnel").font = BLACK
dm.cell(band, 7, f"=G{adj}*Assumptions!B{lo}").number_format = NUM
dm.cell(band, 9, f"=I{adj}*Assumptions!B{lo}").number_format = CUR
dm.cell(band + 1, 1, "Realized - High funnel").font = BLACK
dm.cell(band + 1, 7, f"=G{adj}*Assumptions!B{hi}").number_format = NUM
dm.cell(band + 1, 9, f"=I{adj}*Assumptions!B{hi}").number_format = CUR
dm.column_dimensions["A"].width = 32
for col in "BCDEFGHI":
    dm.column_dimensions[col].width = 11

# ============================================================ DEMAND (BOTTOM-UP)
bu = wb.create_sheet("Demand (Bottom-Up)")
bu.sheet_view.showGridLines = False
bu["A1"] = "Annual Demand - Bottom-Up (non-overlapping Census buckets)"
bu["A1"].font = TITLE
bu["A2"] = (
    "Each OC household counted once. No overlap haircut needed - only the Year-1 ramp factor. "
    "Anchors web-verified 2026-06-01 (US Census/ACS). EPA composting-rate ceiling check below."
)
bu["A2"].font = NOTE
hdrrow(
    bu,
    4,
    [
        "Bucket",
        "Size (HH/biz)",
        "Reach %",
        "In-mkt %",
        "Conv %",
        "Purchase %",
        "Buyers/yr",
        "AOV",
        "Revenue/yr",
        "Basis / anchor",
    ],
)
bs = 5
for i, (name, size, reach, inm, conv, aov, note) in enumerate(buckets):
    rr = bs + i
    bu.cell(rr, 1, name).font = BLACK
    for col, val, fmt in [
        (2, size, NUM),
        (3, reach, PCT),
        (4, inm, PCT),
        (5, conv, PCT),
        (8, aov, CUR),
    ]:
        c = bu.cell(rr, col, val)
        c.font = BLUE
        c.fill = YELLOW
        c.number_format = fmt
    bu.cell(rr, 6, f"=C{rr}*D{rr}*E{rr}").number_format = PCT2
    bu.cell(rr, 7, f"=B{rr}*F{rr}").number_format = NUM1
    bu.cell(rr, 9, f"=G{rr}*H{rr}").number_format = CUR
    bu.cell(rr, 10, note).font = NOTE
    for col in range(1, 10):
        bu.cell(rr, col).border = BORDER
be = bs + len(buckets) - 1
bt = be + 1
bu.cell(bt, 1, "TOTAL (no overlap)").font = BOLD
bu.cell(bt, 2, f"=SUM(B{bs}:B{be})").number_format = NUM
bu.cell(bt, 7, f"=SUM(G{bs}:G{be})").number_format = NUM
bu.cell(bt, 9, f"=SUM(I{bs}:I{be})").number_format = CUR
for col in range(1, 10):
    bu.cell(bt, col).font = BOLD
    bu.cell(bt, col).fill = SUB_FILL
    bu.cell(bt, col).border = BORDER
ramp = inp["Year-1 ramp factor (bottom-up maturity)"]
badj = bt + 1
bu.cell(badj, 1, "Realized Year-1 (x ramp)  [BASE]").font = BOLD
bu.cell(badj, 7, f"=G{bt}*Assumptions!B{ramp}").font = BOLD
bu.cell(badj, 7).number_format = NUM
bu.cell(badj, 9, f"=I{bt}*Assumptions!B{ramp}").font = BOLD
bu.cell(badj, 9).number_format = CUR
for col in range(1, 10):
    bu.cell(badj, col).fill = GREENBG
bu_buyers, bu_rev = badj, badj
# EPA ceiling check
ck = badj + 2
bu.cell(ck, 1, "Plausibility ceiling check").font = BOLD
oc_hh_row = bs + 2  # mid-income owner row not ideal; compute OC HH directly
bu.cell(ck + 1, 1, "OC households (residential buckets)").font = BLACK
bu.cell(ck + 1, 2, f"=SUM(B{bs}:B{bs+4})").number_format = NUM
bu.cell(ck + 2, 1, "Composting-household rate (EPA proxy)").font = BLACK
cc = bu.cell(ck + 2, 2, 0.04)
cc.font = BLUE
cc.fill = YELLOW
cc.number_format = PCT
bu.cell(ck + 3, 1, "=> Ceiling: composting HH in OC").font = BLACK
bu.cell(ck + 3, 2, f"=B{ck+1}*B{ck+2}").number_format = NUM
bu.cell(ck + 4, 1, "Model residential buyers/yr (realized)").font = BLACK
bu.cell(
    ck + 4,
    2,
    f"=G{badj}-B{bs+5}*F{bs+5}*Assumptions!B{ramp}-B{bs+6}*F{bs+6}*Assumptions!B{ramp}",
).number_format = NUM
bu.cell(ck + 5, 1, "Within ceiling?").font = BOLD
bu.cell(
    ck + 5, 2, f'=IF(B{ck+4}<=B{ck+3},"YES - plausible","NO - too high")'
).font = BOLD
bu.cell(
    ck + 5,
    3,
    "Vermicompost is a subset of all composting, so staying well under is expected.",
).font = NOTE
bu.column_dimensions["A"].width = 34
for col in "BCDEFGHI":
    bu.column_dimensions[col].width = 11
bu.column_dimensions["J"].width = 32

# ============================================================ PER PERIOD P&L
pp = wb.create_sheet("Per Period (Quarter)")
pp.sheet_view.showGridLines = False
pp["A1"] = "Per-Period P&L - One Operating Quarter (Owner-Operated)"
pp["A1"].font = TITLE
pp[
    "A2"
] = "Revenue/orders pulled from the chosen demand basis / periods-per-year. Marketing is CAC-driven."
pp["A2"].font = NOTE

basis = inp["Demand basis (1 = Profiles, 2 = Bottom-up Census)"]
ppy = inp["Periods per year"]
cogs_r = inp["Blended COGS %"]
proc_r = inp["Payment processing % of revenue"]
fee_r = inp["Payment fee per order ($)"]
ref_r = inp["Refunds & returns % of revenue"]
cb_r = inp["Chargebacks % of revenue"]
sp_r = inp["Live-goods spoilage % of revenue"]
cac_r = inp["CAC - marketing $ per new customer"]
ncs_r = inp["New-customer share of orders %"]
ship_r = inp["Avg shipping absorbed per order ($)"]
own_r = inp["Owner salary / draw per quarter"]
tax_r = inp["Sales tax rate (collected & remitted)"]
disc_r = inp["Promo / discount allowance % of gross rev"]
rep_n = inp["Repeat consumable orders / customer / yr"]
rep_v = inp["Avg repeat order value ($)"]
rep_y = inp["Retention (years)"]
rep_m = inp["Repeat-order gross margin %"]
sub_a = inp["Subscription attach rate % of new customers"]
sub_v = inp["Subscription value $/month"]
sub_m = inp["Subscription gross margin %"]
sub_l = inp["Subscription avg life (months)"]
wh_r = inp["Wholesale % of revenue"]
mp_r = inp["Marketplace % of revenue"]
mpfee_r = inp["Marketplace/wholesale fee % on those sales"]
invcov_r = inp["Inventory coverage (months of COGS held)"]

PB = f"'Demand (Profiles)'!G{prof_buyers}"
PR = f"'Demand (Profiles)'!I{prof_rev}"
BB = f"'Demand (Bottom-Up)'!G{bu_buyers}"
BR = f"'Demand (Bottom-Up)'!I{bu_rev}"

pr = {}
b = 4


def L(lbl, formula, fmt=CUR, bold=False, fill=None, note=None, key=None):
    global b
    lc = pp.cell(b, 1, lbl)
    lc.font = BOLD if bold else BLACK
    vc = pp.cell(b, 2, formula)
    vc.number_format = fmt
    vc.font = BOLD if bold else BLACK
    if fill:
        lc.fill = fill
        vc.fill = fill
    if note:
        pp.cell(b, 3, note).font = NOTE
    if key:
        pr[key] = b
    b += 1


L(
    "Annual buyers (chosen basis)",
    f"=CHOOSE(Assumptions!B{basis},{PB},{BB})",
    NUM,
    key="abuy",
    note="1=Profiles, 2=Bottom-up",
)
L(
    "Annual revenue (chosen basis)",
    f"=CHOOSE(Assumptions!B{basis},{PR},{BR})",
    CUR,
    key="arev",
)
L("Orders / quarter", f"=B{pr['abuy']}/Assumptions!B{ppy}", NUM, key="orders")
L("Gross revenue", f"=B{pr['arev']}/Assumptions!B{ppy}", bold=True, key="grev")
L("Promotional discounts", f"=-B{pr['grev']}*Assumptions!B{disc_r}", key="disc")
L("Net revenue", f"=B{pr['grev']}+B{pr['disc']}", bold=True, fill=SUB_FILL, key="rev")
L(
    "Cost of goods sold",
    f"=-B{pr['grev']}*Assumptions!B{cogs_r}",
    key="cogs",
    note="On units (gross), not discounted price",
)
L("Gross profit", f"=B{pr['rev']}+B{pr['cogs']}", bold=True, fill=SUB_FILL, key="gp")
L("Gross margin % (on net rev)", f"=B{pr['gp']}/B{pr['rev']}", PCT)
section(pp, b, "Variable operating costs", 1)
b += 1
L(
    "Payment processing",
    f"=-(B{pr['rev']}*Assumptions!B{proc_r}+B{pr['orders']}*Assumptions!B{fee_r})",
)
vfirst = b - 1
L("Refunds & returns", f"=-B{pr['rev']}*Assumptions!B{ref_r}")
L("Chargebacks", f"=-B{pr['rev']}*Assumptions!B{cb_r}")
L("Live-goods spoilage", f"=-B{pr['rev']}*Assumptions!B{sp_r}")
L("Shipping absorbed", f"=-B{pr['orders']}*Assumptions!B{ship_r}")
L(
    "Marketing (CAC x new buyers)",
    f"=-B{pr['orders']}*Assumptions!B{ncs_r}*Assumptions!B{cac_r}",
    key="mkt",
)
L(
    "Wholesale/marketplace fees",
    f"=-B{pr['grev']}*(Assumptions!B{wh_r}+Assumptions!B{mp_r})*Assumptions!B{mpfee_r}",
    note="Fees only on the wholesale + marketplace share",
)
vlast = b - 1
L("Total variable opex", f"=SUM(B{vfirst}:B{vlast})", bold=True, key="vtot")
section(pp, b, "Fixed operating costs", 1)
b += 1
L(
    "Fixed opex (help/fulfil/software/insur.)",
    f"=-Assumptions!B{total_fixed_row}",
    key="fix",
)
L("Owner salary / draw", f"=-Assumptions!B{own_r}", key="own")
L("Total fixed + owner", f"=B{pr['fix']}+B{pr['own']}", bold=True, key="ftot")
L(
    "Net profit (after owner pay, pre-tax)",
    f"=B{pr['gp']}+B{pr['vtot']}+B{pr['ftot']}",
    bold=True,
    fill=YELLOW,
    key="net",
)
L("Net margin %", f"=B{pr['net']}/B{pr['rev']}", PCT, bold=True)
b += 1
section(pp, b, "Memos & break-even", 1)
b += 1
L(
    "Sales tax collected (pass-through, excl.)",
    f"=B{pr['rev']}*Assumptions!B{tax_r}",
    note="Remitted, not income",
)
L(
    "Contribution margin ratio",
    f"=(B{pr['gp']}+B{pr['vtot']})/B{pr['rev']}",
    PCT,
    key="cm",
)
L("Break-even revenue / quarter", f"=-B{pr['ftot']}/B{pr['cm']}", key="be")
L("Break-even as % of modeled revenue", f"=B{pr['be']}/B{pr['rev']}", PCT)
b += 1
section(pp, b, "Unit economics (LTV:CAC)", 1)
b += 1
L(
    "Gross profit per order (first order)",
    f"=B{pr['gp']}/B{pr['orders']}",
    CUR2,
    key="gppo",
)
L(
    "Repeat-order LTV (consumables)",
    f"=Assumptions!B{rep_n}*Assumptions!B{rep_y}*Assumptions!B{rep_v}*Assumptions!B{rep_m}",
    CUR2,
    key="rltv",
    note="reorders/yr x years x value x margin",
)
L(
    "Subscription LTV (auto-ship GP)",
    f"=Assumptions!B{sub_a}*Assumptions!B{sub_v}*Assumptions!B{sub_l}*Assumptions!B{sub_m}",
    CUR2,
    key="subltv",
    note="attach x $/mo x months x margin",
)
L(
    "Customer LTV (gross profit)",
    f"=B{pr['gppo']}+B{pr['rltv']}+B{pr['subltv']}",
    CUR2,
    key="ltv",
)
L("CAC (per new customer)", f"=Assumptions!B{cac_r}", CUR2, key="cac")
L(
    "LTV : CAC ratio",
    f"=B{pr['ltv']}/B{pr['cac']}",
    '0.0"x"',
    bold=True,
    key="ltvcac",
    note="Savvy target >= 3.0x",
)
L(
    "CAC payback (orders to recoup)",
    f"=B{pr['cac']}/B{pr['gppo']}",
    "0.0",
    key="payback",
    note="< 1 order = recovered on first sale",
)
L(
    "Marketing as % of net revenue",
    f"=-B{pr['mkt']}/B{pr['rev']}",
    PCT,
    key="mktpct",
    note="Year-1 DTC often 20-40%",
)
L(
    "Implied steady-state subscription MRR",
    f"=B{pr['orders']}*Assumptions!B{ncs_r}*Assumptions!B{ppy}/12*Assumptions!B{sub_a}*Assumptions!B{sub_v}*Assumptions!B{sub_l}/12",
    CUR,
    key="mrr",
    note="Memo only - upside NOT in the P&L above (conservative)",
)
b += 1
section(pp, b, "Annualized & monthly feeds", 1)
b += 1
L("Annualized revenue", f"=B{pr['rev']}*Assumptions!B{ppy}", bold=True, key="anrev")
L(
    "Annualized net profit",
    f"=B{pr['net']}*Assumptions!B{ppy}",
    bold=True,
    fill=YELLOW,
    key="annet",
)
L(
    "Variable-cost ratio (incl. COGS)",
    f"=-(B{pr['cogs']}+B{pr['vtot']})/B{pr['rev']}",
    PCT,
    key="vratio",
)
L("Annual fixed + owner", f"=-B{pr['ftot']}*Assumptions!B{ppy}", CUR, key="anfix")

# Sensitivity vs demand-driver factor (overlap for profiles / ramp for bottom-up)
b += 2
pp.cell(b, 1, "Sensitivity - realized-demand factor").font = H2F
b += 1
pp.cell(
    b, 1, "Scales the chosen basis up/down. Yellow = base (1.00x). Re-runs net profit."
).font = NOTE
b += 1
sfactors = [0.5, 0.75, 1.0, 1.25, 1.5]
hrow = b
pp.cell(hrow, 1, "Demand multiplier").font = HDR
pp.cell(hrow, 1).fill = HDR_FILL
pp.cell(hrow, 1).border = BORDER
for j, f in enumerate(sfactors):
    c = pp.cell(hrow, 2 + j, f)
    c.number_format = '0.00"x"'
    c.alignment = Alignment(horizontal="center")
    c.border = BORDER
    if abs(f - 1.0) < 1e-9:
        c.fill = YELLOW
        c.font = BLUEB
    else:
        c.fill = HDR_FILL
        c.font = HDR
rev_q = f"B{pr['rev']}"
ord_q = f"B{pr['orders']}"
rows_def = [
    ("Revenue / quarter", lambda col: f"={rev_q}*{col}{hrow}", CUR),
    (
        "Gross profit / quarter",
        lambda col: f"={rev_q}*{col}{hrow}*B{pr['gp']}/{rev_q}",
        CUR,
    ),
    ("Variable opex / quarter", lambda col: f"=B{pr['vtot']}*{col}{hrow}", CUR),
    ("Fixed + owner / quarter", lambda col: f"=B{pr['ftot']}", CUR),
]
mr = hrow + 1
defrows = {}
for label, fn, fmt in rows_def:
    pp.cell(mr, 1, label).font = BLACK
    pp.cell(mr, 1).border = BORDER
    for j in range(len(sfactors)):
        col = chr(ord("B") + j)
        c = pp.cell(mr, 2 + j, fn(col))
        c.number_format = fmt
        c.border = BORDER
    defrows[label] = mr
    mr += 1
gpR = defrows["Gross profit / quarter"]
voR = defrows["Variable opex / quarter"]
foR = defrows["Fixed + owner / quarter"]
pp.cell(mr, 1, "Net profit / quarter").font = BOLD
pp.cell(mr, 1).fill = SUB_FILL
pp.cell(mr, 1).border = BORDER
for j in range(len(sfactors)):
    col = chr(ord("B") + j)
    c = pp.cell(mr, 2 + j, f"={col}{gpR}+{col}{voR}+{col}{foR}")
    c.number_format = CUR
    c.font = BOLD
    c.border = BORDER
    c.fill = YELLOW if abs(sfactors[j] - 1.0) < 1e-9 else SUB_FILL
neR = mr
mr += 1
pp.cell(mr, 1, "Annualized net profit").font = BOLD
pp.cell(mr, 1).border = BORDER
for j in range(len(sfactors)):
    col = chr(ord("B") + j)
    c = pp.cell(mr, 2 + j, f"={col}{neR}*Assumptions!B{ppy}")
    c.number_format = CUR
    c.font = BOLD
    c.border = BORDER

pp.column_dimensions["A"].width = 36
for col in "BCDEF":
    pp.column_dimensions[col].width = 13

# ============================================================ SEASONALITY & 12-MONTH
sz = wb.create_sheet("Seasonality & 12-Month")
sz.sheet_view.showGridLines = False
sz["A1"] = "Year-1 Monthly Ramp, Seasonality & Cash Flow"
sz["A1"].font = TITLE
sz["A2"] = (
    "Annual revenue is spread across 12 months by Ramp index (year-1 growth) x Season multiplier, "
    "normalized so the year sums to the modeled annual revenue. Break-even = first month cash turns positive."
)
sz["A2"].font = NOTE

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
ramp_idx = [0.35, 0.45, 0.60, 0.75, 0.90, 1.00, 1.00, 0.95, 1.00, 1.05, 1.20, 1.10]
season = [0.70, 0.75, 1.05, 1.30, 1.35, 1.10, 0.85, 0.80, 1.00, 1.05, 1.25, 1.15]

# layout: row labels in col A, months across B..M
R_MON, R_RAMP, R_SEAS, R_W, R_REV, R_VAR, R_FIX, R_NET, R_CUM = (
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
)
labels = {
    R_MON: "Month",
    R_RAMP: "Ramp index",
    R_SEAS: "Season mult.",
    R_W: "Weight (norm.)",
    R_REV: "Revenue",
    R_VAR: "Variable + COGS",
    R_FIX: "Fixed + owner",
    R_NET: "Net profit",
    R_CUM: "Cumulative cash",
}
for rr, lab in labels.items():
    sz.cell(rr, 1, lab).font = BOLD if rr in (R_REV, R_NET, R_CUM) else BLACK
    if rr == R_MON:
        sz.cell(rr, 1).font = HDR
        sz.cell(rr, 1).fill = HDR_FILL
anrev = f"'Per Period (Quarter)'!B{pr['anrev']}"
vratio = f"'Per Period (Quarter)'!B{pr['vratio']}"
anfix = f"'Per Period (Quarter)'!B{pr['anfix']}"
first_col = 2
last_col = 1 + 12
for i in range(12):
    col = i + 2
    L_ = chr(ord("A") + col - 1)
    c = sz.cell(R_MON, col, months[i])
    c.font = HDR
    c.fill = HDR_FILL
    c.alignment = Alignment(horizontal="center")
    c.border = BORDER
    c = sz.cell(R_RAMP, col, ramp_idx[i])
    c.font = BLUE
    c.fill = YELLOW
    c.number_format = "0.00"
    c = sz.cell(R_SEAS, col, season[i])
    c.font = BLUE
    c.fill = YELLOW
    c.number_format = "0.00"
    # weight normalized by sum of ramp*season across all months
    sz.cell(
        R_W,
        col,
        f"=({L_}{R_RAMP}*{L_}{R_SEAS})/SUMPRODUCT($B{R_RAMP}:$M{R_RAMP},$B{R_SEAS}:$M{R_SEAS})",
    )
    sz.cell(R_W, col).number_format = PCT
    sz.cell(R_REV, col, f"={anrev}*{L_}{R_W}").number_format = CUR
    sz.cell(R_VAR, col, f"=-{L_}{R_REV}*{vratio}").number_format = CUR
    sz.cell(R_FIX, col, f"=-{anfix}/12").number_format = CUR
    sz.cell(R_NET, col, f"={L_}{R_REV}+{L_}{R_VAR}+{L_}{R_FIX}").number_format = CUR
    if i == 0:
        sz.cell(R_CUM, col, f"={L_}{R_NET}").number_format = CUR
    else:
        prev = chr(ord("A") + col - 2)
        sz.cell(R_CUM, col, f"={prev}{R_CUM}+{L_}{R_NET}").number_format = CUR
    for rr in range(R_MON, R_CUM + 1):
        sz.cell(rr, col).border = BORDER
# Year total column
yc = 14
yL = chr(ord("A") + yc - 1)
sz.cell(R_MON, yc, "YEAR").font = HDR
sz.cell(R_MON, yc).fill = HDR_FILL
sz.cell(R_MON, yc).border = BORDER
sz.cell(R_W, yc, "=SUM(B7:M7)").number_format = PCT
sz.cell(R_REV, yc, "=SUM(B8:M8)").number_format = CUR
sz.cell(R_VAR, yc, "=SUM(B9:M9)").number_format = CUR
sz.cell(R_FIX, yc, "=SUM(B10:M10)").number_format = CUR
sz.cell(R_NET, yc, "=SUM(B11:M11)").number_format = CUR
for rr in (R_W, R_REV, R_VAR, R_FIX, R_NET):
    sz.cell(rr, yc).font = BOLD
    sz.cell(rr, yc).fill = SUB_FILL
    sz.cell(rr, yc).border = BORDER

# Break-even month
br = R_CUM + 2
sz.cell(br, 1, "Cumulative-cash break-even month").font = BOLD
sz.cell(
    br,
    2,
    '=IFERROR(INDEX($B$4:$M$4,MATCH(TRUE,INDEX($B$12:$M$12>=0,0),0)),"not within year 1")',
)
sz.cell(br, 2).font = BOLD
sz.cell(br + 1, 1, "Lowest cumulative cash (operating trough)").font = BLACK
sz.cell(br + 1, 2, "=MIN(B12:M12)").number_format = CUR
sz.cell(br + 1, 3, "Cash the P&L alone needs at its trough").font = NOTE
sz.cell(br + 2, 1, "Inventory investment (working capital)").font = BLACK
sz.cell(
    br + 2,
    2,
    f"=-'Per Period (Quarter)'!B{pr['anrev']}*Assumptions!B{cogs_r}/12*Assumptions!B{invcov_r}",
).number_format = CUR
sz.cell(br + 2, 3, "COGS tied up in stock ahead of the sale").font = NOTE
sz.cell(br + 3, 1, "Total peak funding (trough + inventory)").font = BOLD
sz.cell(br + 3, 2, f"=B{br+1}+B{br+2}").number_format = CUR
sz.cell(br + 3, 2).font = BOLD
sz.cell(br + 3, 3, "What you actually have to finance up front").font = NOTE

sz.column_dimensions["A"].width = 26
for i in range(12):
    sz.column_dimensions[chr(ord("B") + i)].width = 9
sz.column_dimensions["N"].width = 11

# ============================================================ SOURCES & METHOD
sm = wb.create_sheet("Sources & Method")
sm.sheet_view.showGridLines = False
sm["A1"] = "Sources & Method - where every number came from"
sm["A1"].font = TITLE
sm["A2"] = (
    "Key: REPO = real project file; PROFILES = reception-profiles workbook (part-verified); "
    "CENSUS = web-verified US Census/ACS anchor; ESTIMATE = my assumption, replace with real data."
)
sm["A2"].font = NOTE
row = 4
section(sm, row, "Files pulled in", 4)
row += 1
hdrrow(sm, row, ["File / document", "What I took from it", "Used in tab", "Status"])
row += 1
files = [
    (
        "products.json",
        "List prices for all 10 SKUs ($19-$465)",
        "Per Unit / SKU Mix",
        "REPO",
    ),
    (
        "mockups/profiles/profile_market_estimates.xlsx -> Market Estimates",
        "20 personas: segment size, Reach/In-market/Conv %, AOV",
        "Demand (Profiles)",
        "PROFILES",
    ),
    (
        "...same file -> Sources & Method",
        "OC Census anchors (1.08M HH, 56-57% owner-occ, ~$116k median income, ~9,800 food est.); "
        "EPA ~4% composting rate; the over-count warning",
        "Demand (Bottom-Up)",
        "CENSUS",
    ),
    (
        "CLAUDE.md + cart.js",
        "Tiered shipping (OC $7 / metro $12 / US $20, free >$150)",
        "Assumptions",
        "REPO",
    ),
]
for f, took, tab, status in files:
    for col, val in [(1, f), (2, took), (3, tab), (4, status)]:
        c = sm.cell(row, col, val)
        c.font = BLACK
        c.border = BORDER
        c.alignment = Alignment(vertical="top", wrap_text=True)
    row += 1
row += 1
section(sm, row, "My estimates (no source file - replace with real data)", 4)
row += 1
hdrrow(sm, row, ["Assumption", "Value", "Basis", "Status"])
row += 1
est = [
    (
        "Per-SKU COGS %",
        "35-46%",
        "Typical landed-cost margin; no BOM in repo",
        "ESTIMATE",
    ),
    (
        "SKU order-share mix",
        "see SKU Mix",
        "Guessed basket; replace w/ order data",
        "ESTIMATE",
    ),
    (
        "Bottom-up funnel rates",
        "per bucket",
        "Reach/In-mkt/Conv rules-of-thumb",
        "ESTIMATE",
    ),
    (
        "Year-1 ramp / overlap factors",
        "60% / 55%",
        "Maturity & de-dup judgement",
        "ESTIMATE",
    ),
    (
        "Payment processing + per-txn",
        "2.9% + $0.30",
        "Stripe-class card rate",
        "ESTIMATE",
    ),
    (
        "Refunds / chargebacks / spoilage",
        "3% / 0.5% / 1%",
        "Industry + live-goods loss",
        "ESTIMATE",
    ),
    (
        "CAC / new-customer share",
        "$45 / 70%",
        "Replace w/ real ad+channel data",
        "ESTIMATE",
    ),
    (
        "Fixed opex + owner salary",
        "$11.5k + $12k /qtr",
        "Owner-operated structure",
        "ESTIMATE",
    ),
    (
        "Monthly ramp & seasonality",
        "see tab",
        "Spring/holiday garden pattern",
        "ESTIMATE",
    ),
]
for label, val, bss, status in est:
    for col, v in [(1, label), (2, val), (3, bss), (4, status)]:
        c = sm.cell(row, col, v)
        c.font = BLACK
        c.border = BORDER
        c.alignment = Alignment(vertical="top", wrap_text=True)
    row += 1
row += 1
section(sm, row, "What changed in this revision (accuracy upgrades)", 4)
row += 1
upg = [
    "Bottom-up Census demand: each OC household counted once -> removes the overlap fudge factor.",
    "Funnel band: Low/Base/High scenarios on the profiles tab show a revenue range, not a point.",
    "SKU Mix tab computes blended COGS from order-share x price x cost (was a flat 45% guess).",
    "Marketing is now CAC x new buyers, so it scales with demand instead of a fixed budget.",
    "Added real variable costs: per-transaction fees, refunds, chargebacks, live-goods spoilage.",
    "Owner salary is a line item -> net profit is now AFTER paying the owner a wage.",
    "Sales tax shown as a pass-through memo (collected & remitted, excluded from profit).",
    "EPA composting-rate ceiling check flags if demand exceeds a plausible OC pool.",
    "Break-even revenue and contribution margin added to the P&L.",
    "12-month tab: ramp + seasonality + cumulative cash, break-even month, and peak funding need.",
]
for u in upg:
    sm.cell(row, 1, u).font = BLACK
    sm.merge_cells(start_row=row, start_column=1, end_row=row, end_column=4)
    row += 1
row += 1
c = sm.cell(
    row,
    1,
    (
        "Still the two biggest unknowns: real per-SKU landed COGS and real checkout "
        "conversion. Drop those in (BOM sheet + live Snipcart data) and most of the "
        "remaining uncertainty disappears. Funnel rates remain rules-of-thumb until "
        "replaced with analytics or a panel survey."
    ),
)
c.font = NOTE
sm.merge_cells(start_row=row, start_column=1, end_row=row, end_column=4)
c.alignment = Alignment(wrap_text=True, vertical="top")
sm.row_dimensions[row].height = 56
sm.column_dimensions["A"].width = 40
sm.column_dimensions["B"].width = 30
sm.column_dimensions["C"].width = 26
sm.column_dimensions["D"].width = 12

# ============================================================ BENCHMARKS / REALITY CHECK
bk = wb.create_sheet("Benchmarks")
bk.sheet_view.showGridLines = False
bk["A1"] = "Benchmarks - what a savvy operator/investor would say"
bk["A1"].font = TITLE
bk["A2"] = (
    "Comparables: premium DTC / consumer-hardware brands (Yeti, Solo Stove-class) and the unit-economics "
    "discipline VCs apply (Bessemer/a16z DTC benchmarks). Verdict compares THIS model to those targets."
)
bk["A2"].font = NOTE
hdrrow(
    bk,
    4,
    ["Metric", "This model", "Savvy target", "Verdict / what they'd say"],
    wrap=True,
)
PPq = "'Per Period (Quarter)'!"
br0 = 5


def bench(metric, cell, fmt, target, verdict_formula, w=False):
    global br0
    bk.cell(br0, 1, metric).font = BLACK
    c = bk.cell(br0, 2, cell)
    c.number_format = fmt
    c.font = BOLD
    bk.cell(br0, 3, target).font = BLACK
    vc = bk.cell(br0, 4, verdict_formula)
    vc.font = BLACK
    vc.alignment = Alignment(wrap_text=True, vertical="top")
    for col in range(1, 5):
        bk.cell(br0, col).border = BORDER
    br0 += 1


bench(
    "Gross margin % (on net rev)",
    f"={PPq}B{pr['gp']}/{PPq}B{pr['rev']}",
    PCT,
    "Premium DTC 60-75%; durables 45-55%",
    f'=IF({PPq}B{pr["gp"]}/{PPq}B{pr["rev"]}>=0.55,"OK for hardware - but caps everything downstream",'
    f'"LOW - little room to absorb CAC & returns")',
)
bench(
    "Contribution margin %",
    f"={PPq}B{pr['cm']}",
    PCT,
    ">= 40%",
    f'=IF({PPq}B{pr["cm"]}>=0.4,"Healthy per-order economics","THIN - fixed costs hard to cover")',
)
bench(
    "LTV : CAC",
    f"={PPq}B{pr['ltvcac']}",
    '0.0"x"',
    ">= 3.0x",
    f'=IF({PPq}B{pr["ltvcac"]}>=3,"Acquisition pays off",'
    f'"FLAG - durable bought once + low repeat; raise AOV/repeat or cut CAC")',
)
bench(
    "CAC payback (orders)",
    f"={PPq}B{pr['payback']}",
    "0.0",
    "<= 1 order",
    f'=IF({PPq}B{pr["payback"]}<=1,"Recovered on first sale - good","Slow payback")',
)
bench(
    "Marketing % of net revenue",
    f"={PPq}B{pr['mktpct']}",
    PCT,
    "Year-1 DTC 20-40%",
    f'=IF({PPq}B{pr["mktpct"]}<0.1,"UNDERFUNDED - cannot reach the demand modeled",'
    f'IF({PPq}B{pr["mktpct"]}>0.45,"Very heavy - growth-at-all-costs","In a realistic band"))',
)
bench(
    "Net margin % (after owner pay)",
    f"={PPq}B{pr['net']}/{PPq}B{pr['rev']}",
    PCT,
    "Year 1 ~0%; mature 10-20%",
    f'=IF({PPq}B{pr["net"]}/{PPq}B{pr["rev"]}>0.2,'
    f'"SKEPTICAL - >20% net in year 1 implies costs/CAC understated",'
    f'IF({PPq}B{pr["net"]}/{PPq}B{pr["rev"]}<0,"Loss - normal for DTC year 1","Credible band"))',
)
bench(
    "Discount allowance %",
    f"=Assumptions!B{disc_r}",
    PCT,
    "8-15%",
    f'=IF(Assumptions!B{disc_r}<0.05,"OPTIMISTIC - few brands sell at full price","Realistic")',
)
br0 += 1
bk.cell(br0, 1, "Bottom line").font = BOLD
br0 += 1
notes_txt = [
    "1. Gross margin (~50-55%) is fine for hardware but LOW for premium DTC - it makes LTV:CAC the whole game.",
    "2. A one-time durable with weak repeat usually can't clear LTV:CAC 3.0x. A consumables subscription is now",
    "   modeled (attach x $/mo x life x margin) - it lifts LTV; push attach/value to clear 3.0x.",
    "3. A >20% net margin in YEAR ONE reads as fantasy to an investor. Realistic year-1 is near break-even",
    "   or a planned loss while you buy customers; profit shows up once CAC efficiency and repeat build.",
    "4. The old $45 CAC + $4k marketing couldn't physically acquire the buyers the demand model assumed -",
    "   demand (reach) and marketing spend must be consistent. CAC is now $150; tune it to real ad data.",
    "5. Owner pay is now a real wage ($72k); 'profit' is what's left AFTER paying the operator a market rate.",
    "6. Now modeled (v0.5): inventory/working-capital timing (Seasonality tab), wholesale/marketplace channel",
    "   fees (P&L), and furniture-class returns at 6% (was 3%). Replace each with your real numbers as they land.",
]
for t in notes_txt:
    bk.cell(br0, 1, t).font = BLACK
    bk.merge_cells(start_row=br0, start_column=1, end_row=br0, end_column=4)
    br0 += 1
bk.column_dimensions["A"].width = 34
bk.column_dimensions["B"].width = 13
bk.column_dimensions["C"].width = 26
bk.column_dimensions["D"].width = 52

# ============================================================ DATA VALIDATION
dv_basis = DataValidation(
    type="whole",
    operator="between",
    formula1=1,
    formula2=2,
    showErrorMessage=True,
    errorTitle="Demand basis",
    error="Enter 1 (Profiles) or 2 (Bottom-up Census).",
)
a.add_data_validation(dv_basis)
dv_basis.add(a.cell(inp["Demand basis (1 = Profiles, 2 = Bottom-up Census)"], 2))
dv_pct = DataValidation(
    type="decimal",
    operator="between",
    formula1=0,
    formula2=1,
    showErrorMessage=True,
    errorTitle="Share",
    error="Order share must be between 0% and 100%.",
)
sk.add_data_validation(dv_pct)
dv_pct.add(f"D{ss}:D{se}")
# visible flag if SKU shares don't total 100%
sk.cell(16, 1, "Share total check").font = BOLD
sk.cell(
    16, 2, f'=IF(ABS(D14-1)<0.0001,"OK = 100%","FIX: total is "&TEXT(D14,"0.0%"))'
).font = BOLD

# ============================================================ DASHBOARD (front)
db = wb.create_sheet("Dashboard")
db.sheet_view.showGridLines = False
db["A1"] = "OmniCompost - Financial Snapshot"
db["A1"].font = TITLE
db["A2"] = (
    "Headline KPIs from the chosen demand basis. Edit inputs on Assumptions / SKU Mix; "
    "everything here recalculates. See Sources & Method for what's real vs. estimated."
)
db["A2"].font = NOTE
db.cell(3, 1, "Demand basis").font = BLACK
db.cell(
    3, 2, f'=IF(Assumptions!B{basis}=1,"Profiles (sum-of-personas)","Bottom-up Census")'
).font = BOLD


def kpi(r, label, formula, fmt, note=""):
    db.cell(r, 1, label).font = BLACK
    c = db.cell(r, 2, formula)
    c.number_format = fmt
    c.font = H2F
    if note:
        db.cell(r, 3, note).font = NOTE
    for col in (1, 2):
        db.cell(r, col).border = BORDER


section(db, 5, "Per operating quarter", 3)
kpi(6, "Revenue", f"='Per Period (Quarter)'!B{pr['rev']}", CUR)
kpi(7, "Gross profit", f"='Per Period (Quarter)'!B{pr['gp']}", CUR)
kpi(8, "Net profit (after owner pay)", f"='Per Period (Quarter)'!B{pr['net']}", CUR)
kpi(
    9,
    "Net margin",
    f"='Per Period (Quarter)'!B{pr['net']}/'Per Period (Quarter)'!B{pr['rev']}",
    PCT,
)
kpi(10, "Break-even revenue / qtr", f"='Per Period (Quarter)'!B{pr['be']}", CUR)
section(db, 12, "Annualized", 3)
kpi(13, "Revenue", f"='Per Period (Quarter)'!B{pr['anrev']}", CUR)
kpi(14, "Net profit (after owner pay)", f"='Per Period (Quarter)'!B{pr['annet']}", CUR)
kpi(
    15,
    "Owner salary already paid",
    f"=Assumptions!B{own_r}*Assumptions!B{ppy}",
    CUR,
    "On top of net above",
)
kpi(16, "Blended COGS %", f"=Assumptions!B{cogs_r}", PCT, "Computed from SKU Mix")
section(db, 18, "Year-1 cash", 3)
kpi(19, "Cumulative break-even month", f"='Seasonality & 12-Month'!B{br}", "General")
kpi(20, "Operating cash trough", f"='Seasonality & 12-Month'!B{br+1}", CUR)
kpi(
    21,
    "Total funding incl. working capital",
    f"='Seasonality & 12-Month'!B{br+3}",
    CUR,
    "Trough + inventory held",
)
section(db, 22, "Unit economics (see Benchmarks)", 3)
kpi(
    23,
    "LTV : CAC",
    f"='Per Period (Quarter)'!B{pr['ltvcac']}",
    '0.0"x"',
    "Target >= 3.0x",
)
kpi(
    24,
    "Marketing % of net revenue",
    f"='Per Period (Quarter)'!B{pr['mktpct']}",
    PCT,
    "Year-1 20-40%",
)
db.cell(
    26,
    1,
    (
        "Reminder: revenue rests on real prices + Census anchors; costs and funnel "
        "conversion are estimates. Not a forecast. See Benchmarks for the savvy-operator read."
    ),
).font = NOTE
db.merge_cells("A26:C26")
db.column_dimensions["A"].width = 32
db.column_dimensions["B"].width = 22
db.column_dimensions["C"].width = 30
# move Dashboard to the front
wb.move_sheet("Dashboard", -(len(wb.sheetnames) - 1))

out = (
    r"C:\Users\Sub Account\Documents\Claude\Projects\claude code test v2.0"
    r"\ccode\chat in code\omnicompost-premium-site\OmniCompost_Financial_Estimate.xlsx"
)
wb.save(out)
print("saved", out)
