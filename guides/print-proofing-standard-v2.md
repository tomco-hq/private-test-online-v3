# Print Proofing Standard (v2)

_Last updated: 2026-05-30_1430. Supersedes `../../Kitchen 1 Sheet Guide/Print Proofing Standard.md`._

Pre-print checks for every physical OmniCompost piece. Screen previews hide what
fails in print — small-type legibility, CMYK shift, glare on a sealed surface,
content lost in the trim. Run this before committing any piece to a print run.

**Scope:** the two-sided laminated field guide, the 5×7 companion cards (Starter,
Troubleshooting), the 4×6 fridge magnet. Add new pieces to the table as made.

> **v2 note — this is the one guide with almost no dogma to cut.** Its rules are
> physics (reflective CMYK runs darker than backlit RGB) and accessibility (type
> floors for older eyes), not taste. The review confirmed the numbers rather than
> loosening them. The exceptions below are about *when a check doesn't apply*,
> not about relaxing a floor.

---

## Universal checklist (every piece)

1. **Print at 100% / "Actual size."** Never "Fit to page" — it silently scales.
   Verify with a ruler against true dimensions.
2. **Proof on the real stock**, not copy paper. Card stock for cards, magnet
   sheet (or matte photo paper) for the magnet, the actual laminate for the guide.
3. **Read small type at arm's length**, under normal kitchen/outdoor light.
4. **Minimum type:** body ≥ **8 pt**, captions/labels ≥ **7 pt**. Below 7 pt is a
   fail at print size.
5. **Color (RGB → CMYK):** confirm greens don't muddy and terracotta/ochre don't
   shift. For commercial printing, request a **CMYK proof**.
6. **Margins & bleed:** critical content ≥ **1/8″** from trim; add **1/8″ bleed**
   to anything running to the edge (hero bands, full-width zones).
7. **Finish-specific check:** proof *after* the finish — lamination adds glare;
   magnet backing bows thin stock.

---

## Per-piece specs

| Piece | True size | Stock / finish | Smallest type now | Bleed items | Main risk |
|---|---|---|---|---|---|
| **Field guide (2-sided)** | 8.5 × 11 in | Laminated, matte | Body ~10–12 pt | Color zones, hero edges | Glare on seal; duplex registration |
| **Starter Card** | 5 × 7 in | Card stock | Foot 9 px (~6.75 pt) | Photo hero band | Foot line borderline — verify, bump if needed |
| **Troubleshooting Card** | 5 × 7 in | Card stock | Cause/fix 11 px, foot 9 px | Row fills | Dense 3-column grid; confirm columns don't crowd |
| **Fridge magnet** | 4 × 6 in | Magnet sheet | Labels ~8.5 px (~6.4 pt) | Color blocks | **Highest risk** — labels at/under the floor |

Notes:
- px→pt at 96 dpi: 8.5 px ≈ 6.4 pt, 9 px ≈ 6.75 pt, 12 px ≈ 9 pt. Anything under
  ~9.5 px (≈7 pt) needs a real-size legibility check before sign-off.
- The **matte / cream-paper** choice is deliberate anti-glare design — keep it;
  do not switch to white or gloss to "brighten" a piece.

---

## Finish-specific

- **Lamination (guide):** matte only — gloss reintroduces the glare cream paper
  avoids. After sealing, re-check dashed rules and lighter text still read, and
  that the two sides register.
- **Magnet:** proof the assembled magnet flat on a fridge, not just the sheet.
- **Cards:** if corners are die-cut, confirm the radius doesn't clip content.

## Proofing priority order

1. **Fridge magnet** (smallest type). 2. **5×7 cards.** 3. **Laminated guide**
(proof after sealing).

## Spec-accuracy reminder (separate from print)

Print-proofing checks *legibility and color*, not *correctness*. The temperature
(55–77°F), moisture ("wrung-out sponge"), and feeding cadence appear on multiple
pieces and must (a) match the product manual and (b) stay synced across pieces —
**and now also match the website**, where the same numbers appear in the Field
Notes issues (e.g. the "draw the tea every fortnight, dilute half-and-half" copy
in `notes/march-2026.html`). A spec drift between print and web is the new failure
mode the finished site introduced. That fact-check is an open item independent of
any print proof.

## Exceptions

- **Exception (digital-only piece):** none of this applies to a piece that will
  only ever be a screen PDF or web page — no CMYK proof, no stock, no bleed.
  The website Field Notes are digital; they follow the design-system voice rules,
  not this standard. Don't run a print checklist on a thing that won't be printed.
- **Exception (type floor on a large-format piece):** the 7–8 pt floors assume
  arm's-length reading of a hand-held sheet. A poster read from across a room can
  go *larger*-only; the floor is a minimum, never a target to design down to.
- **Exception (proofless reprint):** an unchanged reprint on the *same stock and
  press* doesn't need a fresh full proof — but any change to stock, finish,
  printer, or content resets that, because the failure modes here are all
  material-and-device specific.

> **Adding a brand-new exception here?** Run the three-part minting test in
> `README.md` (recurring, named-justifiable-reason, would-otherwise-mislead).
> One instance is an exception; three is a pattern — promote it into the rule.
> (Be especially strict here: these rules are physics and accessibility, so a
> real new exception is rare — usually a *new material or finish*, not taste.)
