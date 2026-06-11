"""Build the 'Inferred Media, Diet & Social Tastes' Word deliverable.

Emits a .docx into scraps/reviews archive/. Standalone; run with Anaconda python via
PowerShell:  C:\\anaconda\\python.exe notes\\build_media_taste_docx.py
"""

import os

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor

# ---- palette (Premium tier) -------------------------------------------------
INK = RGBColor(0x23, 0x21, 0x1C)
TEAL = RGBColor(0x3E, 0x6B, 0x66)
TERRA = RGBColor(0xB5, 0x65, 0x4A)
MUTED = RGBColor(0x6E, 0x66, 0x5A)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(
    HERE,
    "..",
    "scraps",
    "reviews archive",
    "Inferred Media, Diet & Social Tastes — Founders, Author, Customers_2026-06-04.docx",
)


def set_cell(cell, text, bold=False, color=None, size=9):
    """Write a single paragraph into a table cell with light styling."""
    cell.text = ""
    p = cell.paragraphs[0]
    run = p.add_run(text)
    run.bold = bold
    run.font.size = Pt(size)
    if color is not None:
        run.font.color.rgb = color


def heading(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = TEAL if level == 1 else TERRA
    return h


def para(doc, text, italic=False, size=10.5, color=None):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.italic = italic
    run.font.size = Pt(size)
    if color is not None:
        run.font.color.rgb = color
    return p


doc = Document()

# normal style
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(10.5)
normal.font.color.rgb = INK

# ---- title ------------------------------------------------------------------
title = doc.add_heading("Inferred Media, Diet & Social Tastes", level=0)
for run in title.runs:
    run.font.color.rgb = INK
sub = doc.add_paragraph()
r = sub.add_run(
    "Founders · Inferred Author (v5) · Customer Profiles — overlap and contrasts"
)
r.italic = True
r.font.size = Pt(12)
r.font.color.rgb = MUTED
stamp = doc.add_paragraph()
rs = stamp.add_run("Last updated: 2026-06-04")
rs.italic = True
rs.font.size = Pt(9)
rs.font.color.rgb = MUTED

# ---- caveat -----------------------------------------------------------------
heading(doc, "Read this first — confidence is LOW", level=1)
para(
    doc,
    "Profile v5 explicitly flags media/reading taste as unsupported — v1's Kinfolk / "
    "New Yorker tags were deleted for inventing exactly this. The per-founder guesses below "
    "are casting fiction built from each persona's written temperament; useful for voice and "
    "amplification work, not a claim about any real person. The one inference with even "
    "medium footing is restraint — the anti-hype, low-volume disposition five invented "
    "founders couldn't stop repeating (v5's invariance method).",
)

# ---- shared signal ----------------------------------------------------------
heading(doc, "The shared signal", level=1)
para(
    doc,
    "Across all eight founders the constants are: steel + beechwood + brass over plastic; "
    "under-promise in plain words; lone maker controlling the whole chain; ships slowly on "
    "purpose; foregrounds what the product can't do; persuasion anchored to exact numbers "
    "(5 gal/day, 14 prototypes, household of 4), never adjectives; zero exclamation points. "
    "That restrained, craft-first, anti-hype, materials-literate temperament is the only "
    "honest basis for projecting taste.",
)

# ---- per-founder table ------------------------------------------------------
heading(doc, "Per-founder inference (8 About-page personas)", level=1)
founders = [
    (
        "Daniel Mercer — Costa Mesa, ex-industrial designer",
        "Dieter Rams, Monocle, Aeon / Long Now, Kevin Kelly; design podcasts",
        "Cooks from scratch; low-waste 'use the wilted greens'; flexitarian",
        "Lurker; tidy rarely-posted Instagram of objects, not face; no TikTok",
    ),
    (
        "Claire Whitaker — Laguna Beach, editorial voice",
        "The New Yorker, Kinfolk, NYT Cooking, literary nonfiction",
        "Farmers-market seasonal; natural-wine-curious; mostly plant-forward",
        "Curated Instagram, occasional Substack; quietly aesthetic",
    ),
    (
        "Theo Brandt — San Clemente, cabinetmaker",
        "YouTube woodworking (Ishitani, Rex Krueger), Fine Woodworking",
        "Big shared meals, sourdough, fermenting/pickling; omnivore",
        "YouTube/Instagram build clips; process over selfies",
    ),
    (
        "Sam Calloway — Encinitas, 'best-of' composite",
        "Mixed/mainstream-eco: Outside, NPR, a few design newsletters",
        "Surf-town healthy: bowls, tacos, smoothies; flexitarian",
        "Light, friendly Instagram; most 'normal' poster of the eight",
    ),
    (
        "Nora Vance — Oceanside, ex-biology teacher",
        "Scientific American, Radiolab, iNaturalist, Robin Wall Kimmerer",
        "Garden-to-table, big veg, composts everything; vegetarian-leaning",
        "Education-mode: posts to teach, not to perform",
    ),
    (
        "Mateo Salas — Long Beach, 'same promise' creed",
        "Values/essay reading; community radio; documentary over feed",
        "Family cooking, beans-and-rice abundance, low-waste; omnivore",
        "Believes the work speaks; minimal, principle-driven presence",
    ),
    (
        "Ruth Delgado — Carlsbad, 'what it can't do' ledger",
        "Consumer Reports, Wirecutter, repair / right-to-repair forums",
        "Practical, plan-the-week, zero-waste pantry; pragmatic omnivore",
        "Anti-hype; reads reviews before posting one",
    ),
    (
        "Wes Holloway — Long Beach, B2B operator's note",
        "Trade/ops: spec sheets, SB 1383 compliance, LinkedIn, industry email",
        "Functional fuel; coffee; no performance about it",
        "LinkedIn only; numbers and record, no lifestyle feed",
    ),
]
table = doc.add_table(rows=1, cols=4)
table.style = "Light Grid Accent 1"
table.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr = table.rows[0].cells
for c, t in zip(
    hdr,
    [
        "Founder / place",
        "Likely media diet",
        "Likely diet / food",
        "Likely social behavior",
    ],
):
    set_cell(c, t, bold=True, color=TEAL, size=9)
for row in founders:
    cells = table.add_row().cells
    set_cell(cells[0], row[0], bold=True, size=9)
    set_cell(cells[1], row[1], size=9)
    set_cell(cells[2], row[2], size=9)
    set_cell(cells[3], row[3], size=9)

# ---- inferred author --------------------------------------------------------
heading(doc, "The inferred author (distinct from the characters)", level=1)
para(
    doc,
    "Media: systems- and craft-literate, doctrine-driven (note the human-writing rule, "
    "the 'design out the later mistake' instinct). Plausibly reads design/strategy and "
    "build-in-public material — a guess one notch above the personas, not a finding.",
)
para(
    doc,
    "Diet: the whole repo is about composting kitchen scraps for a household of four — a "
    "low-waste, cook-at-home, produce-heavy kitchen is consistent, but it describes the "
    "target customer as much as the author. Coastal-SoCal identity is Low confidence in v5.",
)
para(
    doc,
    "Social media: the strongest cross-persona tell is restraint — every founder distrusts "
    "marketing and lets numbers talk. If that's the author leaking through, they are far more "
    "a low-volume, high-craft poster than an influencer. This is the one inference with "
    "even medium-ish footing.",
)

# ---- NEW: media overlap -----------------------------------------------------
heading(doc, "Media overlap — where the eight converge", level=1)
para(doc, "Stripping the surface variety, the eight cluster on a single media spine:")
for b in [
    "Channel: long-form and owned media (essays, YouTube how-to, newsletters, LinkedIn) over "
    "algorithmic short-form. Not one founder is a TikTok-native.",
    "Mode: process- and proof-driven — build logs, spec sheets, teaching, reviews — rather "
    "than lifestyle/aspiration performance.",
    "Posture: low frequency, high craft; 'show the work, withhold the hype.' The product's "
    "under-promise ethos is also its media ethos.",
    "Diet overlap: every founder is some flavor of cook-at-home, low-waste, produce-heavy "
    "(flexitarian to vegetarian) — the composting worldview made personal.",
]:
    p = doc.add_paragraph(style="List Bullet")
    p.add_run(b).font.size = Pt(10)
para(
    doc,
    "Wes (B2B) is the lone register outlier — LinkedIn/trade media, functional diet — but "
    "even he keeps the proof-over-hype mode. The overlap is the author's invariant temperament "
    "showing through eight masks; the variety is set dressing.",
    italic=True,
)

# ---- NEW: founders vs customers --------------------------------------------
heading(doc, "Founders vs. customer profiles — compare & contrast", level=1)
para(
    doc,
    "The 22 customer profiles in mockups/profiles/ carry their own media/social signals. "
    "Mapping founders to customers exposes a deliberate gap.",
)

cmp = doc.add_table(rows=1, cols=3)
cmp.style = "Light Grid Accent 1"
cmp.alignment = WD_TABLE_ALIGNMENT.CENTER
for c, t in zip(
    cmp.rows[0].cells,
    ["Founder", "Best-matched customer profile(s)", "What the match/mismatch shows"],
):
    set_cell(c, t, bold=True, color=TEAL, size=9)
rows = [
    (
        "Nora Vance (bio teacher)",
        "01 Personal Chef (9.2), 19 Wellness/Clean-Living (8.6), 22 Schoolteacher",
        "Teach-don't-sell media mode lands the highest-fit, advocacy-heavy buyers.",
    ),
    (
        "Daniel Mercer / Claire Whitaker (design)",
        "21 Stager-Designer, 11 Santa Monica Lawyer, 19 Wellness",
        "Curatorial taste mirrors the aesthetic buyer — perfect object, friction is workflow not voice.",
    ),
    (
        "Ruth Delgado (limits ledger)",
        "10 Comparison Shopper (6.2), 18 Eco-Skeptic Spouse (4.5)",
        "Anti-hype, proof-first register is exactly what converts skeptics — strongest persuasion fit.",
    ),
    (
        "Wes Holloway (B2B operator)",
        "12 Bakery, 13 Food Truck, 14 Small Café (B2B-routed)",
        "Trade media + numbers diet matches the business buyer the Premium voice can't serve.",
    ),
    (
        "(none of the eight)",
        "20 Gen-Z TikTok (3.8), 17 Fixed-Income Retiree (5.0)",
        "The blind spot: no founder speaks short-form/values-loud or budget-plain — these route to Family/Kids.",
    ),
]
for r0 in rows:
    cells = cmp.add_row().cells
    set_cell(cells[0], r0[0], bold=True, size=9)
    set_cell(cells[1], r0[1], size=9)
    set_cell(cells[2], r0[2], size=9)

heading(doc, "The decisive contrast", level=2)
para(
    doc,
    "Founders and core customers share one media diet — long-form, proof-driven, low-waste, "
    "restraint as a value. That alignment is why the highest-fit profiles (Personal Chef, DINK "
    "couple, Wellness, Retired Gardeners) convert: the maker's voice is their voice.",
)
para(
    doc,
    "The mismatch is just as revealing. The lowest-fit profiles — Mia (Gen-Z TikTok, "
    "values-loud, short-form, financing-dependent) and the fixed-income retiree — fail on the "
    "exact axis where every founder is silent: none of the eight is a loud, short-form, "
    "stat-forward communicator. The Premium founder cast is, by construction, the temperament of "
    "the Premium customer; reaching the amplifier (Mia) or the budget buyer requires the Family / "
    "Kids voice, not another founder.",
)

# ---- bottom line ------------------------------------------------------------
heading(doc, "Bottom line", level=1)
para(
    doc,
    "Eight founders, one media temperament: long-form, proof-over-hype, low-waste, restrained. "
    "That temperament is the author leaking through the masks — and it is the same temperament "
    "as the Premium core customer, which is why voice and audience align so cleanly. The cast's "
    "single weakness is its single strength inverted: it cannot speak to the loud, short-form, "
    "budget-first audience, which is precisely the audience the other tiers exist to serve. "
    "Everything above the 'restraint' line is casting fiction — use it for voice and reach "
    "strategy, not as fact about anyone real.",
)

doc.save(OUT)
print("Wrote:", os.path.abspath(OUT))
print("Paragraphs:", len(doc.paragraphs), "| Tables:", len(doc.tables))
