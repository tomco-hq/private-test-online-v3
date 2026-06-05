# Image Sourcing — Review Layer (v2)

_Last updated: 2026-05-30_1430. Reviews the `omnicompost-image-sourcing` skill against the finished site._

The skill remains authoritative. This file records what the build confirmed,
what looks stale, and the exceptions worth remembering.

## Confirmed by the build

- **Host locally, never hotlink.** Every image on the site is a local file under
  `assets/img/` (18 vetted Premium photographs, reused across hero, gallery,
  PDPs, and the expanded Field Notes). No remote URLs to rot. The skill's rule
  held.
- **Craft AND fit, fit fails more often.** The newsletter photos were chosen by
  register, not just quality — `watering-can-plaster`, `greens-bowl-wood`,
  `coffee-carafe-kitchen`, `earthworm-soil-macro`, `seedling-dark-soil` all sit
  in the muted Premium register. The "route a too-plain shot to Family, never
  force a fit" discipline is why the set still reads as one tier.
- **Reuse beats re-sourcing.** Expanding the three Field Notes issues added six
  figures with **zero new downloads** — all from the existing vetted set. The
  cheapest vetted image is the one already on disk and already passed.

## Looks stale — verify before trusting

> **De-dogma — the "Write/Edit tools have faulted (ENOENT/EBADF)" warning.** The
> skill says to fall back to Python-through-Bash for file writes because Write/
> Edit faulted in past sessions. **Not observed this build** — Write and Edit
> worked reliably across products.json, build.py, cart.js, and 15+ HTML/MD files.
> Treat the Python-fallback as a *contingency*, not the default. Reach for it
> only if Write/Edit actually errors; defaulting to it adds friction and burns
> the "verbose over terse" budget for no reason. (Bash *did* still mangle the
> `C:\anaconda\python.exe` path — use PowerShell for shell work, per global prefs.)

- The **source status table** (Unsplash CDN 200 / API 401, Openverse open,
  Wikimedia 403, Pexels key-walled) is dated; the skill itself says status
  drifts. Re-probe before a new sourcing run rather than trusting the table.

## Exceptions

- **Exception (subagent threshold):** the skill says spin a subagent for ~8+
  candidate images to keep image tokens out of the main thread. This build did
  **no** new sourcing, so the threshold wasn't tested here — but it matches the
  token-levers guide's ~8 line for subagent break-even. Below 8, vet inline.
- **Exception (eyeball loop):** if the user wants to see candidates themselves,
  vet in the main thread even past 8 — the subagent's token saving isn't worth
  losing the interactive "show me, I'll pick" loop. Judge per task.
- **Exception (illustration tiers):** none of the stock-sourcing workflow applies
  to Kids, which is illustration-first and gated on a commission (see
  `../ROADMAP.md` Phase 2). Don't route stock photography there.

> **Adding a brand-new exception here?** Run the three-part minting test in
> `README.md` (recurring, named-justifiable-reason, would-otherwise-mislead).
> One instance is an exception; three is a pattern — promote it into the rule.
