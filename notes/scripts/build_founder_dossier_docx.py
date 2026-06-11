"""Build the consolidated 'Founder Cast Dossier' (.docx).

Merges three session artifacts into one document:
  I.   Coverage & Demographics (from the meta-analysis)
  II.  Media, Diet & Social tastes + overlap + founders-vs-customers
  III. Demographic gaps (NEW)
  IV.  Strategy — stay the course vs branch

Standalone; run via PowerShell:
    C:\\anaconda\\python.exe notes\\build_founder_dossier_docx.py
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
    "Founder Cast Dossier — Coverage, Tastes, Gaps, Strategy_2026-06-04.docx",
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


def table(doc, headers, rows):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Light Grid Accent 1"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for c, h in zip(t.rows[0].cells, headers):
        set_cell(c, h, bold=True, color=TEAL, size=9)
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            set_cell(cells[i], val, bold=(i == 0), size=9)
    return t


doc = Document()
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(10.5)
normal.font.color.rgb = INK

# ── title ────────────────────────────────────────────────────────────────
title = doc.add_heading("Founder Cast Dossier", level=0)
for run in title.runs:
    run.font.color.rgb = INK
sub = doc.add_paragraph()
r = sub.add_run(
    "Demographic coverage · media/diet/social tastes · gaps · strategy — for the 10 "
    "About-page founders and the inferred author"
)
r.italic = True
r.font.size = Pt(12)
r.font.color.rgb = MUTED
stamp = doc.add_paragraph()
rs = stamp.add_run(
    "Last updated: 2026-06-04 · Consolidates and supersedes the four 2026-06-04 "
    "session docs (now in archive/). Part IV reconciled with focus-group Panel 9 "
    "(set-dressing / voice-vs-face). Advisory, not authoritative."
)
rs.italic = True
rs.font.size = Pt(9)
rs.font.color.rgb = MUTED

para(
    doc,
    "Scope note: confidence is LOW on all taste inference. Profile v5 flags media/reading "
    "taste as unsupported; the per-founder guesses are casting fiction built from each "
    "persona's written temperament. The one inference with even medium footing is restraint.",
    italic=True,
    size=9.5,
    color=MUTED,
)

# ══ PART I ════════════════════════════════════════════════════════════════
heading(doc, "Part I — Coverage & Demographics", level=1)
para(
    doc,
    "The founders (v1-v8, plus the gap-filling v9-v10) are not eight versions of one pitch. "
    "Each persona is matched to a direction that disarms a specific buyer objection, so the "
    "set spans the full trust spectrum — emotional (the letter) to evidential (the limits "
    "ledger) to commercial (the operator's note). That breadth, not demographic targeting, "
    "is why the cast hits the markets it does.",
)
para(
    doc,
    "Geography is a deliberate corridor — the affluent coast from Costa Mesa down to Carlsbad "
    "plus Long Beach — the exact OmniCompost target strip. Gender is near-even by design "
    "(home-garden purchase skews female; 'engineered hardware' framing skews male).",
)
table(
    doc,
    ["Variant", "Founder / place", "Direction", "Objection disarmed"],
    [
        [
            "v1",
            "Daniel Mercer, Costa Mesa",
            "The Letter",
            "wants intimacy / personal trust",
        ],
        [
            "v2",
            "Claire Whitaker, Laguna Beach",
            "The Profile",
            "wants editorial credibility",
        ],
        ["v3", "Theo Brandt, San Clemente", "The Bench", "wants to see it built"],
        [
            "v4",
            "Sam Calloway, Encinitas",
            "Best-of composite",
            "the safe mainstream default",
        ],
        [
            "v5",
            "Nora Vance, Oceanside",
            "Solid-plate / teacher",
            "wants authority + science",
        ],
        ["v6", "Mateo Salas, Long Beach", "The Same Promise", "values buyer"],
        [
            "v7",
            "Ruth Delgado, Carlsbad",
            "What It Can't Do",
            "the skeptic, won by under-promising",
        ],
        [
            "v8",
            "Wes Holloway, Long Beach",
            "Operator's Note (B2B)",
            "numbers-first commercial buyer",
        ],
        [
            "v9",
            "Linh Tran, Huntington Beach",
            "The Material (NEW)",
            "fills ethnicity gap; craft-as-proof",
        ],
        [
            "v10",
            "Hal Brunner, Dana Point",
            "The Long Wear (NEW)",
            "fills age gap; durability buyer",
        ],
    ],
)

# ══ PART II ═══════════════════════════════════════════════════════════════
heading(doc, "Part II — Media, Diet & Social Tastes", level=1)
para(
    doc,
    "Across the cast the constants are: steel + beechwood + brass over plastic; under-promise "
    "in plain words; lone maker controlling the whole chain; ships slowly; foregrounds what "
    "the product can't do; persuasion anchored to exact numbers, never adjectives. That "
    "restrained, craft-first temperament is the only honest basis for projecting taste.",
)
table(
    doc,
    ["Founder", "Likely media diet", "Likely diet / food", "Likely social behavior"],
    [
        [
            "Daniel Mercer",
            "Rams, Monocle, Aeon/Long Now; design podcasts",
            "Cooks from scratch; low-waste; flexitarian",
            "Lurker; tidy object-Instagram; no TikTok",
        ],
        [
            "Claire Whitaker",
            "New Yorker, Kinfolk, NYT Cooking",
            "Farmers-market seasonal; plant-forward",
            "Curated Instagram; occasional Substack",
        ],
        [
            "Theo Brandt",
            "YouTube woodworking; Fine Woodworking",
            "Big shared meals; sourdough; ferments",
            "Build clips; process over selfies",
        ],
        [
            "Sam Calloway",
            "Mainstream-eco: Outside, NPR",
            "Surf-town healthy; flexitarian",
            "Light friendly Instagram; most 'normal'",
        ],
        [
            "Nora Vance",
            "Scientific American, Radiolab, iNaturalist",
            "Garden-to-table; vegetarian-leaning",
            "Posts to teach, not perform",
        ],
        [
            "Mateo Salas",
            "Essays; community radio; documentary",
            "Family cooking; low-waste; omnivore",
            "Work speaks; minimal presence",
        ],
        [
            "Ruth Delgado",
            "Consumer Reports, Wirecutter, repair forums",
            "Plan-the-week; zero-waste pantry",
            "Anti-hype; reads reviews before posting",
        ],
        [
            "Wes Holloway",
            "Spec sheets, SB 1383, LinkedIn",
            "Functional fuel; coffee",
            "LinkedIn only; numbers, no lifestyle",
        ],
        [
            "Linh Tran",
            "Material/ceramics + food-science reading",
            "Vietnamese home cooking; whole-ingredient, low-waste",
            "Quiet portfolio-style; craft detail shots",
        ],
        [
            "Hal Brunner",
            "Trade journals, public radio, print over feed",
            "Plain home cooking; garden produce",
            "Barely online; values word-of-mouth",
        ],
    ],
)

heading(doc, "Media overlap — where the cast converges", level=2)
for b in [
    "Channel: long-form and owned media (essays, YouTube how-to, newsletters, LinkedIn) over "
    "algorithmic short-form. Not one founder is TikTok-native.",
    "Mode: process- and proof-driven (build logs, spec sheets, teaching, reviews) over "
    "lifestyle/aspiration performance.",
    "Posture: low frequency, high craft — 'show the work, withhold the hype.' The product's "
    "under-promise ethos is also its media ethos.",
    "Diet overlap: every founder is some flavor of cook-at-home, low-waste, produce-heavy — the "
    "composting worldview made personal.",
]:
    para(doc, b, style="List Bullet", size=10)

heading(doc, "Founders vs. customer profiles", level=2)
para(
    doc,
    "Mapping founders to the 22 customer profiles in mockups/profiles/ exposes a deliberate gap.",
)
table(
    doc,
    ["Founder", "Best-matched customer profile(s)", "What the match/mismatch shows"],
    [
        [
            "Nora Vance",
            "01 Personal Chef (9.2), 19 Wellness (8.6), 22 Schoolteacher",
            "Teach-don't-sell mode lands the highest-fit advocates.",
        ],
        [
            "Mercer / Whitaker",
            "21 Stager-Designer, 11 SM Lawyer, 19 Wellness",
            "Curatorial taste mirrors the aesthetic buyer.",
        ],
        [
            "Ruth Delgado",
            "10 Comparison Shopper (6.2), 18 Eco-Skeptic (4.5)",
            "Proof-first register converts skeptics best.",
        ],
        [
            "Wes Holloway",
            "12 Bakery, 13 Food Truck, 14 Small Cafe",
            "Trade media + numbers fit the business buyer.",
        ],
        [
            "(none of the cast)",
            "20 Gen-Z TikTok (3.8), 17 Fixed-Income (5.0)",
            "Blind spot: no founder is loud/short-form/budget-plain.",
        ],
    ],
)
para(
    doc,
    "Founders and core customers share one media diet — long-form, proof-driven, low-waste, "
    "restraint as a value — which is why the highest-fit profiles convert: the maker's voice "
    "is their voice. The mismatch is the same axis where every founder is silent.",
    italic=True,
)

# ══ PART III ══════════════════════════════════════════════════════════════
heading(doc, "Part III — Demographic Gaps (real ones)", level=1)
para(
    doc,
    "Judged against the actual coastal-SoCal population the brand wants to reflect — not "
    "against the deliberately narrow Premium buyer — two gaps are real, the rest defensible.",
)
heading(doc, "Real gaps", level=2)
table(
    doc,
    ["Gap", "Why it matters", "How v9/v10 address it"],
    [
        [
            "No Asian-American founder (v1-v8)",
            "Original eight ran Anglo + two Latino (Salas, Delgado). "
            "Coastal/OC SoCal has very large Vietnamese, Chinese, Korean, Filipino communities — "
            "central to a food-and-kitchen brand.",
            "v9 Linh Tran (Vietnamese-American, Huntington Beach) closes it — same creed, different "
            "face and background, not a different temperament.",
        ],
        [
            "Compressed age range",
            "Every founder reads 30s-50s. No elder maker (which pairs naturally "
            "with the 'made to last a decade, ships slowly' ethos) and no younger founder.",
            "v10 Hal Brunner (retired tool-and-die maker, Dana Point, 70s) closes the upper end and "
            "makes durability personal.",
        ],
    ],
)
heading(doc, "Defensible — not problems", level=2)
for b in [
    "Coastal-only geography — intentional; inland buyers route to the Family tier.",
    "Solo-maker / class uniformity — that IS the brand thesis (the lone honest maker), not an oversight.",
    "No disability signal in a founder — the customer side already covers it (profile 08, Accessibility); lower priority on the founder side.",
]:
    para(doc, b, style="List Bullet", size=10)
para(
    doc,
    "Critical constraint (revised): per profile v5 every founder is the same restrained "
    "solo-maker archetype, and the temperament should stay fixed — that is the brand. But hold "
    "two things apart: the invariant TEMPERAMENT/CREED (keep) and the per-founder VOICE/REGISTER "
    "(must move with the face). On close reading v9/v10 were in fact already largely individuated "
    "in register — Linh reasons in clay, glaze and aging, Hal in tolerances, wear and 'a part "
    "either holds or it doesn't.' The residual set-dressing risk was narrower than 'ten faces, "
    "one script': a handful of load-bearing lines stayed verbatim across founders, and one was "
    "worse than verbatim — a gallery caption ('steel and beechwood, because they age the way I "
    "want the bin to') imported the ceramicist's aging-logic into the machinist's mouth, where "
    "the frame should be wear and dimensional stability. Focus-group Panel 9 (FOCUS-GROUPS.md) "
    "named the mechanism; fixing those lines in v9/v10 (each caption now in its own founder's "
    "trade logic) is what the correct rule looks like applied: change face AND register, keep "
    "temperament. The lines that remain shared by design — the spec numbers, the core claim, the "
    "closing 'if it isn't ready you'll read that here' philosophy — are the invariant PROMISE, "
    "and SHOULD stay verbatim.",
    italic=True,
)

# ══ PART IV ═══════════════════════════════════════════════════════════════
heading(doc, "Part IV — Strategy: stay the course vs. branch", level=1)
para(
    doc,
    "Recommendation: stay the course on demographics and on Premium character. Branch only at "
    "the tier line.",
    size=11,
)
para(
    doc,
    "Demographics are already balanced where it counts; the two real gaps are now filled by "
    "v9/v10 without adding a new temperament. Premium character should be deepened, not "
    "diversified — the invariance ('the same promise no matter who's making it') is the brand "
    "asset; eight restrained makers is a coherent brand, eight personalities is a focus group.",
)
heading(doc, "Two invariances — one is the asset, one is the liability", level=2)
para(
    doc,
    "Earlier drafts of this dossier praised 'the invariance' wholesale. Focus-group Panel 9 "
    "forces a split that the praise blurred. INVARIANT PROMISE — the same exact numbers, the "
    "under-promise, the limits ledger holding steady across every rewrite — is the credibility "
    "(the comparison-shopper persona trusts the cast precisely because the claims never inflate "
    "when the story changes). INVARIANT VOICE across founders who have been deliberately "
    "individuated by ethnicity, age, and trade is the opposite — it is the set-dressing the "
    "author already flagged as a risk, now shown to have a concrete failure mode: a real reader "
    "of the matched group feels addressed by the face and then talked past by a register that "
    "isn't theirs, and a cast lined up with shared load-bearing lines reads as costumes over one "
    "script. The fix is NOT to flatten the cast back to sameness; it is to let the individuation "
    "reach the voice — the ceramicist reasoning in material and glaze, the tool-and-die man in "
    "tolerances and wear — while the temperament and the numbers stay fixed. v9/v10 were the test "
    "case: already individuated in most of their copy, they still shared a few verbatim lines, one "
    "of which (the bench caption) wore the wrong founder's worldview; correcting those is the rule "
    "in practice, and cost only a handful of sentences. This couples with the headshot gate below: "
    "a real face reading a borrowed script is the copy-side half of the same misrepresentation the "
    "gate guards against.",
)
para(
    doc,
    "Branching is warranted only at the tier boundary, where the customer profiles named the "
    "real silences:",
)
table(
    doc,
    ["Unserved audience", "Why no founder reaches them", "Right home"],
    [
        [
            "Gen-Z / values-loud (Mia, 3.8)",
            "Needs loud, short-form, stat-forward voice",
            "Family voice",
        ],
        [
            "Fixed-income (Eduardo, 5.0)",
            "Premium restraint-as-luxury talks past a budget buyer",
            "Family voice",
        ],
        [
            "Business buyers (cafe/bakery/truck)",
            "Premium 'imply, never state' can't quote tonnage/ROI",
            "B2B (extend Wes/v8)",
        ],
    ],
)
heading(doc, "New directions worth exploring (ranked by leverage)", level=2)
table(
    doc,
    ["Idea", "What it does", "Leverage"],
    [
        [
            "Face-less / collective Premium founder",
            "Leans into the invariance thesis; sidesteps the headshot gate",
            "High",
        ],
        [
            "Family-tier founder in the Family voice",
            "Closes the Mia/Eduardo gap directly",
            "High",
        ],
        [
            "Customer-as-narrator origin",
            "Removes synthetic-face need AND the narrow-character tension",
            "High",
        ],
        [
            "B2B founder buildout (extend Wes)",
            "Serves profiles 12/13/14 with a real spec sheet",
            "Medium",
        ],
        [
            "Successor / continuity angle",
            "Tests the honesty ethos under volume growth",
            "Medium",
        ],
        [
            "'What changed' / errata founder note",
            "The grading-honestly trait made literal",
            "Medium",
        ],
    ],
)

# ── gate + bottom line ────────────────────────────────────────────────────
heading(doc, "Gating caveat", level=1)
para(
    doc,
    "Nothing ships until the synthetic-headshot gate clears (handoff §6 / constraint #1). "
    "v9 and v10 are deliberately built with a labelled portrait placeholder rather than a new "
    "synthetic face, consistent with the face-less recommendation and the standing pre-launch gate.",
)
heading(doc, "Bottom line", level=2)
para(
    doc,
    "Demographics: hold — the two real gaps (Asian-American founder, elder maker) are now "
    "filled by v9/v10 without inventing a new temperament. Premium character: deepen, don't "
    "diversify — invariance of PROMISE is the brand. But invariance of VOICE across "
    "demographically individuated founders is a liability (Panel 9): either collapse to one "
    "real, proven founder (the face-less/collective and customer-as-narrator directions above "
    "do this and also clear the headshot gate), or, if a cast is kept, let each founder's "
    "register move with their face — change voice AND face, hold temperament. Branch only at the "
    "tier line, where Family / Kids / B2B voices reach the loud, budget, and business audiences "
    "the Premium founders are built not to serve. Everything above the 'restraint' line is "
    "casting fiction — use it for voice and reach strategy, not as fact about anyone real.",
    size=11,
)

doc.save(OUT)
print("Wrote:", os.path.abspath(OUT))
print("Paragraphs:", len(doc.paragraphs), "| Tables:", len(doc.tables))
