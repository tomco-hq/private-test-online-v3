# Design System — Review Layer (v2)

_Last updated: 2026-05-30_1610. Reviews the `omnicompost-design-system` skill against the finished Premium site._

The skill is still authoritative and still loads automatically. This file does
**not** restate it — it records the places where building a real, commercial
Premium *website* (not a print one-sheet) justified bending a rule, so those
exceptions are remembered instead of re-litigated each session.

## What held up exactly as written

- **One audience per artifact.** The whole site is Premium — cream `#F4EDE0`,
  Fraunces + Inter, sage/terracotta/ochre/teal by zone-role, sharp corners,
  dashed rules, Roman numerals. No Kids or Family color or voice leaked in. The
  skill's "biggest failure mode is drift" warning was respected and the site
  reads as one voice top to bottom.
- **Voice discipline.** Zero exclamation points across index, shop, PDPs, and all
  three Field Notes issues. Noun-first titles ("The spring wake-up", "On compost
  tea"). Exact numbers ("two litres, diluted half-and-half", "below 50°F"). The
  expanded newsletter copy stayed in-column even at 2.5× the length.
- **Zone color by meaning.** Tools/Operations/Tips kept their fixed roles.

## Justified exceptions the website earned

These are **web-commerce exceptions**, valid for the *site* tier of Premium work.
They do **not** transfer to the print field guides, which stay strict.

| Rule in the skill | Exception taken on the site | Why it's justified |
|---|---|---|
| Print Premium voice avoids overt ratings/social proof | Added owner ratings (4.9/5) + numeric scores on cards, PDPs, testimonials | A storefront needs social proof to convert; also honors the standing preference to show a visible numeric rating on every deliverable. |
| Guides never carry price or a sales CTA | Added "$385" + Add-to-cart, full shop, cart drawer, checkout | It's a shop. A commerce site without a price or a buy button isn't Premium-restrained, it's broken. |
| "No bullet lists inside cards — flowing prose" | PDPs use a 4-item `.specs` list | Spec lists are a scannability convention buyers expect on a product page; prose specs would read as precious. Prose is kept for *editorial* surfaces (hero, Field Notes), lists for *transactional* ones. |
| Custom SVG line art, object-first | Built a line-art digester SVG to stand in for missing product photography | Stays inside the iconography register; it's a placeholder for a real shoot, flagged as such. |
| Testimonials not a print device | Added a testimonials section + pull-quote with OC place-names (Newport, Laguna, San Clemente) | Localizes the Premium pitch to the actual Orange County buyer; place-specificity *is* the Premium move, executed in a web idiom. |

## The governing principle behind the exceptions

The skill is written for **print field guides**. A **commercial website** is a
different artifact with conversion obligations a one-sheet doesn't have. The
right reading: *keep the Premium **voice and visual system** intact, but allow
the **commerce furniture** (price, cart, ratings, spec lists, testimonials) the
print guides don't need.* Every exception above adds furniture; none of them
changes the voice. That's the line. An exception that softened the voice — an
exclamation point, a round-number measurement, a "you'll love it" — would not be
justified and was not taken.

## Reconciliation — done 2026-05-30

The scraps brand documents (`brand_style_guide.html`, `web_style_guide.html`,
`image_style_guide.html`, `logo_usage_guide.html`) cover the **same ground as the
skills** — palette, type, positioning, logo, per-tier image rules. Two sources of
brand truth is a drift risk, so they were reconciled against the
`omnicompost-design-system` and `omnicompost-image-sourcing` skills. Verdict by
field:

| Field | Result |
|---|---|
| Cream `#F4EDE0`, sage `#5D7A5E`, terracotta `#9B5A44`, ochre `#9A6E1D`, teal `#5B7B7A` | ✅ Match across all four scraps + skill + live site. |
| Type stack — Fraunces + Inter (Premium) | ✅ Match everywhere. |
| Three-tier positioning (Premium / Kids / Family) | ✅ Match. |
| **Premium body ink** | ⚠️ **Drift found + fixed.** Two near-identical inks exist: **`#2A2530`** = body ink (text/rules/icons, what the live site uses) and **`#1C1917`** = *logo/knockout-only* ink (universal monogram, favicon, foil). `web_style_guide.html` wrongly used `#1C1917` as the Premium web body/button ink. **Corrected** to `#2A2530` in that file. |
| Skill gap | The skill listed only `#2A2530` and never named `#1C1917`, which is *why* the drift was possible. **Added** `#1C1917` to the skill palette as the logo/knockout-only token, with a "two inks" note. |

**Net:** the scraps are now consistent with the skill; the skill is still the
single authoritative source. The four documents stay as **reference** (per the
README) — not forked into v2 guides. Re-run this check if any scrap's palette or
type is edited. `image_style_guide.html` and `logo_usage_guide.html` showed no
palette/type conflicts (image guide already carries `#2A2530` as Ink and lists
`#1C1917` correctly as *Universal* ink).

## Recommendation

Do **not** fold the commerce exceptions into the skill body yet. They are correct
for the *site* sub-tier but would mislead someone using the skill for a magnet or
a laminated guide. If a second and third commercial surface (the Family and Kids
shops on the roadmap) take the same exceptions, *then* add a short "commerce
surfaces" section to the skill.

> **Adding a brand-new exception (or commerce-surface deviation) here?** Run the
> three-part minting test in `README.md` (recurring, named-justifiable-reason,
> would-otherwise-mislead) — and hold voice exceptions to a higher bar than
> furniture ones: adding a price or a spec list is furniture; an exclamation
> point or a round-number measurement softens the *voice* and is almost never
> justified. One data point is an exception; **three is a pattern** — promote it
> into the skill and delete it from here.
