"""Generate founder-profile.docx from the v5 inferred-author analysis (CANONICAL).

Standalone, professional styling (not the OmniCompost Premium design system) —
this is a meta/analysis artifact about the repo's author, not a customer-facing
deliverable. Source of record is founder-profile-v5.md.

v5 adds the "invariance method": reading five invented founder About pages for what
stayed constant across all of them. That yields a new evidence item (#4 — a single
involuntary value system under every mask) and a new tension (wide register range,
narrow character range), and upgrades "honest grading" to a corroborated trait.
"""

import os

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "founder-profile.docx")

INK = RGBColor(0x1A, 0x1A, 0x1A)
MUTED = RGBColor(0x66, 0x66, 0x66)
ACCENT = RGBColor(0x3A, 0x5A, 0x40)  # muted sage, label color


def build():
    doc = Document()

    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(11)
    normal.font.color.rgb = INK

    # --- Title block ---
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = title.add_run("OmniCompost — Inferred Author Profile")
    run.bold = True
    run.font.size = Pt(22)
    run.font.color.rgb = INK

    sub = doc.add_paragraph()
    sub_run = sub.add_run(
        "An evidence-based inference drawn from the project files — "
        "not a verified biography."
    )
    sub_run.italic = True
    sub_run.font.size = Pt(11)
    sub_run.font.color.rgb = MUTED

    meta = doc.add_paragraph()
    meta_run = meta.add_run(
        "Compiled 2026-06-04  ·  Canonical  ·  Source of record: founder-profile-v5.md"
    )
    meta_run.font.size = Pt(9)
    meta_run.font.color.rgb = MUTED

    # --- How to read this profile ---
    doc.add_heading("How to read this profile", level=1)
    doc.add_paragraph(
        "Each claim is split into what was observed (checkable facts in the repo) "
        "and what is inferred (interpretation you can disagree with without doubting "
        "the facts). Every claim carries a confidence level and a source."
    )
    caveat = doc.add_paragraph()
    cl = caveat.add_run("Sampling caveat: ")
    cl.bold = True
    caveat.add_run(
        "this is drawn entirely from one project's files. It describes who the "
        "author is in this repo — filtered through a deliberately curated artifact "
        "— and may not generalize beyond it."
    )
    method = doc.add_paragraph()
    ml = method.add_run("New in v5 — the invariance method: ")
    ml.bold = True
    method.add_run(
        "the author was asked to invent five unrelated founders (a designer, a "
        "materials scientist, a cabinetmaker, a community gardener, a biology teacher) "
        "for five About-page mockups. Their biographies were free to differ and did. "
        "Whatever stayed identical across all five anyway is the author leaking through "
        "the mask — evidence about the writer, not the characters. It is the strongest "
        "new signal here because it isn't circular: one honest changelog could be "
        "ordinary QA, but five unprompted personas all preaching the same sermon is the "
        "author's own default."
    )

    # --- Thesis ---
    doc.add_heading("Thesis", level=1)
    doc.add_paragraph(
        "A brand operator who treats voice as an instrument — runs four "
        "deliberately-opposed audience registers without bleeding them, grades their "
        "own work in public, and ships visible craft ahead of the (costly) backend. "
        "What v5 adds: beneath the four registers sits a single, involuntary value "
        "system — measured honesty, under-promise, the solo maker who controls the "
        "whole chain — that the author reaches for whenever they invent from scratch. "
        "The range is in register; the person underneath does not vary."
    )
    fals = doc.add_paragraph()
    fr = fals.add_run(
        "Falsifier: if the five invented founders had genuinely different values — one "
        "a hype-driven scaler, one indifferent to disclosure — the single-involuntary-"
        "ethos claim would be wrong. They did not; the biographies changed and the creed "
        "did not."
    )
    fr.italic = True
    fr.font.color.rgb = MUTED

    # --- What the evidence supports ---
    doc.add_heading("What the evidence supports", level=1)

    add_claim(
        doc,
        "1. They engineer registers, not just pages",
        observed="Four audience voices kept as separate systems — Premium "
        "(“imply, never state”), B2B (states tonnage and ROI), Mainstream "
        "Family, Kids — with an explicit rule that mixing them “destroys the brand.”",
        inferred="A brand strategist's discipline, not a stylist's taste. Taste is "
        "one setting they can dial, not their identity.",
        confidence="High",
        source="omnicompost-design-system, omnicompost-b2b-design-system.",
    )
    add_claim(
        doc,
        "2. They build for their future self",
        observed="Single source of truth (products.json → build.py), one shared "
        "cart.js with “no logic fork,” “never hand-edit a generated page,” "
        "timestamps and “Don't” lists on living docs.",
        inferred="The instinct is to design out the chance of a quiet, later mistake.",
        confidence="High on the practices; Medium on the psychology — much lives in "
        "instructions written to an AI collaborator, so it shows how they delegate as "
        "much as how they work unaided.",
        source="CLAUDE.md, CONTENT-GUIDE.md, repo conventions.",
    )
    add_claim(
        doc,
        "3. They grade honestly",
        observed="Numeric ratings (9.4, 9.6) with deductions explained; the demo "
        "checkout named openly as the main remaining gap.",
        inferred="Under-promising is deliberate; specificity does the persuading that "
        "adjectives would do elsewhere.",
        confidence="High",
        source="REVIEW.md, SUMMARY.md, products.json copy.",
    )
    add_claim(
        doc,
        "4. The values don't vary even when the biography is free to  (NEW)",
        observed="Across five founder pages with unrelated backstories, the constants "
        "are near-total: the same measured facts every time (5 gal/day, 50–90% water, "
        "two weeks unattended, a household of four, fourteen prototypes, powder-coated "
        "steel + beechwood + a brass tap); the same creed in every mouth (“I'd rather "
        "under-promise in plain words than oversell in bold ones”); and the same origin "
        "shape — a lone maker who couldn't find an honest, quiet, un-ugly product, built "
        "it, checks each unit by hand, ships slowly, and foregrounds what it can't do.",
        inferred="This is the author's involuntary default, not a Premium-tier costume. "
        "When invention is unconstrained, they re-write themselves. It promotes “honest "
        "grading” (#3) from a practice that could be QA to a genuine identity trait, "
        "with independent, non-circular corroboration.",
        confidence="High that the invariance exists (checkable across the five files); "
        "Medium that it reflects the author's own character rather than a reused "
        "template they were efficiently copying.",
        source="about-pages/about-premium-real{,-v2,-v3,-v4,-v4b,-v5}.html "
        "(Mercer / Whitaker / Brandt / Calloway / Vance).",
    )

    # --- Tensions ---
    doc.add_heading("Tensions they're aware of", level=1)

    add_bullet(
        doc,
        "Polishes past done",
        " — the grading habit can refine what already shipped instead of advancing "
        "what hasn't. (Inferred; Medium.)",
    )
    add_bullet(
        doc,
        "Front-of-house leads back-of-house — by budget, not blind spot.",
        " Checkout has been the standing gap across versions; what holds it back is "
        "that the backend (payments, hosting, a real provider) costs money while the "
        "marketing surface is free to keep improving. A constraint, not a lapse. "
        "(Observed gap; cost reason stated by the author. High.)",
    )
    add_bullet(
        doc,
        "Wide register range, narrow character range. (NEW)",
        " The author code-switches four audience voices flawlessly, yet every person "
        "they invent is the same archetype — a restrained solo maker who distrusts "
        "marketing and controls the whole chain. They can imagine many ways to talk and "
        "apparently one kind of human to be. (Inferred; Medium — could be deliberate "
        "brand cohesion, but the sameness extends to values a brand wouldn't need to fix.)",
    )
    add_bullet(
        doc,
        "Rules can over-fire",
        " — the human-writing pass had to reject two of the author's own over-zealous "
        "edits; the doctrine is strong enough to need a check against itself. "
        "(Observed; High.)",
    )

    # --- Held loosely ---
    doc.add_heading("Held loosely (low confidence — guesses, not evidence)", level=1)
    add_bullet(
        doc,
        "Coastal-California identity",
        " — inferred from place-names in the copy (Costa Mesa, Laguna, San Clemente, "
        "Encinitas, Oceanside), which is audience-targeting and may say more about the "
        "customer than the author. The author also reaches for it reflexively when "
        "inventing — five for five are coastal SoCal makers — which is mild evidence "
        "it's native, but still weak. (Low.)",
    )
    add_bullet(
        doc,
        "Won't pass off the synthetic as real",
        " — across all five pages the author flagged the AI-generated headshots as a "
        "hard pre-launch gate, never letting a fake face stand unlabelled. Consistent "
        "with the honesty trait, but could be ordinary risk-aversion. (Low–Medium.)",
    )
    add_bullet(
        doc,
        "Reading taste / media diet",
        " — unsupported; v1's Kinfolk / New Yorker tags were removed for exactly this "
        "reason. (Low.)",
    )

    # --- One line ---
    doc.add_heading("In one line", level=1)
    close = doc.add_paragraph()
    cr = close.add_run(
        "Four voices over one unchanging creed: when this author invents a person from "
        "nothing, they write the same measured, under-promising solo maker five times — "
        "proof the honesty isn't a register they deploy but the temperament they can't "
        "switch off."
    )
    cr.italic = True

    # --- Appendix ---
    doc.add_heading("Appendix — how this read was refined", level=1)
    add_bullet(
        doc,
        "v1",
        " — drew a Premium aesthete; accurate but partial, with "
        "invented pop-culture tags.",
    )
    add_bullet(
        doc,
        "v2",
        " — corrected the central error (the author deploys the "
        "Premium voice, isn't defined by it); added code-switching and failure modes.",
    )
    add_bullet(doc, "v3", " — separated evidence from guesswork; added “held loosely.”")
    add_bullet(
        doc,
        "v4",
        " — added inline citations, per-claim confidence, the "
        "observed-vs-inferred seam, a falsifier and sampling caveat; corrected the "
        "backend lag from “blind spot” to “budget constraint.”",
    )
    add_bullet(
        doc,
        "v5",
        " — added the invariance method: read five invented founders "
        "for their constants, not their content. Yielded evidence item #4 (the "
        "involuntary single ethos) and the “wide register range, narrow character "
        "range” tension; upgraded “honest grading” to a corroborated identity trait.",
    )

    # --- Note for a future branding page ---
    doc.add_heading("Note for a future branding page", level=1)
    doc.add_paragraph(
        "Still third-person analysis. A public “About” page would need a voice decision "
        "and should soften or cut the “tensions” section — the “narrow character range” "
        "line in particular is fair in a working doc but reads as a jab in public. The "
        "invariance finding, though, is the most flattering thing here when phrased "
        "forward: “the same promise no matter who's making it” is a brand line, not a "
        "criticism."
    )

    doc.save(OUT_PATH)
    print("Wrote", OUT_PATH)


def add_claim(doc, heading, observed, inferred, confidence, source):
    """A sub-heading followed by labelled Observed / Inferred / Confidence / Source."""
    doc.add_heading(heading, level=2)
    _labelled(doc, "Observed", observed)
    _labelled(doc, "Inferred", inferred)
    _labelled(doc, "Confidence", confidence)
    _labelled(doc, "Source", source)


def _labelled(doc, label, text):
    p = doc.add_paragraph()
    lab = p.add_run(label + ": ")
    lab.bold = True
    lab.font.color.rgb = ACCENT
    p.add_run(text)


def add_bullet(doc, lead, rest):
    p = doc.add_paragraph(style="List Bullet")
    lead_run = p.add_run(lead)
    lead_run.bold = True
    p.add_run(rest)


if __name__ == "__main__":
    build()
