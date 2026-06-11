"""Build the 'Founder Cast — Stay the Course or Branch' strategy memo (.docx).

Standalone; run with Anaconda python via PowerShell:
    C:\\anaconda\\python.exe notes\\build_founder_strategy_docx.py
"""

import os

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.shared import Pt, RGBColor

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
    "Founder Cast Strategy — Stay the Course vs Branch_2026-06-04.docx",
)


def heading(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = TEAL if level == 1 else TERRA
    return h


def para(doc, text, italic=False, size=10.5, color=None, style=None):
    p = doc.add_paragraph(style=style)
    run = p.add_run(text)
    run.italic = italic
    run.font.size = Pt(size)
    if color is not None:
        run.font.color.rgb = color
    return p


def set_cell(cell, text, bold=False, color=None, size=9):
    cell.text = ""
    p = cell.paragraphs[0]
    run = p.add_run(text)
    run.bold = bold
    run.font.size = Pt(size)
    if color is not None:
        run.font.color.rgb = color


doc = Document()
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(10.5)
normal.font.color.rgb = INK

title = doc.add_heading("Founder Cast — Strategy Memo", level=0)
for run in title.runs:
    run.font.color.rgb = INK
sub = doc.add_paragraph()
r = sub.add_run(
    "Should the founder profiles branch out or stay the course? Demographics, character, and tier."
)
r.italic = True
r.font.size = Pt(12)
r.font.color.rgb = MUTED
stamp = doc.add_paragraph()
rs = stamp.add_run("Last updated: 2026-06-04")
rs.italic = True
rs.font.size = Pt(9)
rs.font.color.rgb = MUTED

# ---- recommendation ---------------------------------------------------------
heading(doc, "Recommendation", level=1)
para(
    doc,
    "Stay the course on demographics and on Premium character. Branch only at the tier "
    "line. The eight founders already cover the demographic and geographic ground; their "
    "shared temperament is a brand asset, not a limitation; and every real audience gap the "
    "customer-profile work exposed is a voice/tier gap, not a demographic one.",
    size=11,
)

# ---- demographics: hold -----------------------------------------------------
heading(doc, "1. Demographics — hold steady", level=1)
para(doc, "The cast is already balanced where it counts:")
for b in [
    "Gender: four men (Daniel, Theo, Mateo, Wes), three women (Claire, Nora, Ruth) — near-even, "
    "deliberately so, since home-garden purchase skews female while 'engineered hardware' framing skews male.",
    "Geography: a single affluent coastal corridor — Costa Mesa, Laguna, San Clemente, Encinitas, "
    "Oceanside, Carlsbad, Long Beach x2 — the exact OmniCompost target strip (coastal OC into North San Diego).",
    "Occupation/age: designer, materials maker, cabinetmaker, teacher, community figure, B2B operator — "
    "a wide credibility range across one buyer class.",
]:
    para(doc, b, style="List Bullet", size=10)
para(
    doc,
    "Adding more demographic variety would re-prove a point the cast already makes. Hold it.",
    italic=True,
)

# ---- character: deepen, don't diversify ------------------------------------
heading(doc, "2. Premium character — deepen, do not diversify", level=1)
para(
    doc,
    "Profile v5's central finding: five invented founders preached an identical creed — measured "
    "honesty, under-promise, the solo maker who controls the whole chain. v5's own note reframes "
    "this as the most flattering thing in the analysis: 'the same promise no matter who's making "
    "it' is a brand line, not a criticism.",
)
para(
    doc,
    "Branching Premium founders into genuinely different temperaments (a hype-driven scaler, a "
    "lifestyle influencer) would destroy the one thing that makes the cast read as honest rather "
    "than as marketing. Eight restrained makers is a coherent brand; eight personalities is a "
    "focus group. Inside Premium: pick the 2-3 strongest directions (v7 limits-ledger, v1 letter, "
    "v5 teacher-authority) and make them excellent instead of minting v9-v12 that repeat the point.",
)

# ---- where branching is warranted ------------------------------------------
heading(doc, "3. Where branching IS warranted — the tier line", level=1)
para(
    doc,
    "The customer profiles already named where the cast is silent, and it is never inside Premium:",
)
gap = doc.add_table(rows=1, cols=3)
gap.style = "Light Grid Accent 1"
gap.alignment = WD_TABLE_ALIGNMENT.CENTER
for c, t in zip(
    gap.rows[0].cells,
    ["Unserved audience", "Why no founder reaches them", "Right home"],
):
    set_cell(c, t, bold=True, color=TEAL, size=9)
for r0 in [
    (
        "Gen-Z / values-loud (Mia, fit 3.8)",
        "Needs loud, short-form, stat-forward voice; every founder is quiet/long-form",
        "Family voice",
    ),
    (
        "Fixed-income (Eduardo, fit 5.0)",
        "Premium restraint-as-luxury talks past a budget buyer",
        "Family voice",
    ),
    (
        "Business buyers (cafe/bakery/food-truck)",
        "Premium 'imply, never state' can't quote tonnage/ROI",
        "B2B (extend Wes/v8)",
    ),
]:
    cells = gap.add_row().cells
    set_cell(cells[0], r0[0], bold=True, size=9)
    set_cell(cells[1], r0[1], size=9)
    set_cell(cells[2], r0[2], size=9)
para(
    doc,
    "The founders should not branch in character; the tiers should branch in voice, each with its "
    "own founder treatment.",
    italic=True,
)

# ---- new ideas --------------------------------------------------------------
heading(doc, "4. New directions worth exploring (ranked by leverage)", level=1)
ideas = [
    (
        "Face-less / collective Premium founder",
        "Lean all the way into the invariance thesis: "
        "'the name may change; the four lines will not.' Most on-brand option; v6-v8 started here before "
        "faces were added. Also sidesteps the synthetic-headshot gate.",
        "High",
    ),
    (
        "Family-tier founder in the Family voice",
        "Same maker, values stated plainly and loudly (impact "
        "number, landfill stat). Directly closes the Mia/Eduardo gap. Highest-leverage branch.",
        "High",
    ),
    (
        "Customer-as-narrator origin",
        "Let a high-fit buyer (e.g. Personal Chef, 9.2) tell the origin "
        "instead of the founder. Removes the synthetic-face need AND the narrow-character tension at once.",
        "High",
    ),
    (
        "B2B founder buildout (extend Wes)",
        "Operator's-note register with a real spec sheet / SB 1383 "
        "compliance framing. Profiles 12/13/14 are waiting on it.",
        "Medium",
    ),
    (
        "Successor / continuity angle",
        "What happens to 'one person checks each unit' when volume grows? "
        "Tests the honesty ethos under stress. Net-new, not a re-skin.",
        "Medium",
    ),
    (
        "'What changed' / errata founder note",
        "A page documenting a past mistake and its fix — the "
        "grading-honestly trait made literal. Risky, maximally on-brand if real.",
        "Medium",
    ),
]
it = doc.add_table(rows=1, cols=3)
it.style = "Light Grid Accent 1"
it.alignment = WD_TABLE_ALIGNMENT.CENTER
for c, t in zip(it.rows[0].cells, ["Idea", "What it does", "Leverage"]):
    set_cell(c, t, bold=True, color=TEAL, size=9)
for r0 in ideas:
    cells = it.add_row().cells
    set_cell(cells[0], r0[0], bold=True, size=9)
    set_cell(cells[1], r0[1], size=9)
    set_cell(cells[2], r0[2], size=9)

# ---- gating caveat ----------------------------------------------------------
heading(doc, "5. Gating caveat", level=1)
para(
    doc,
    "Nothing ships until the synthetic-headshot gate clears (handoff section 6 / constraint #1): "
    "every founder face is an AI non-person right now and cannot front a live named founder without "
    "real photography or an illustration label. Ideas 1 and 3 are attractive partly because they "
    "reduce or remove the need for a fabricated face.",
)

heading(doc, "Bottom line", level=2)
para(
    doc,
    "Demographics: hold. Premium character: deepen, don't diversify — the invariance is the brand. "
    "Branch only at the tier boundary, where Family/Kids/B2B voices reach the loud, budget, and "
    "business audiences the Premium founders are built not to serve. Top three moves: a face-less "
    "Premium founder, a Family-voice founder, and a customer-narrated origin.",
    size=11,
)

doc.save(OUT)
print("Wrote:", os.path.abspath(OUT))
print("Paragraphs:", len(doc.paragraphs), "| Tables:", len(doc.tables))
