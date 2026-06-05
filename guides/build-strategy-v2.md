# Static-Site Build Strategy (v2)

_Last updated: 2026-05-30_1430. Supersedes `../../DIFFERENCES.md`._

The v1 doc was a side-by-side of two specific TomCo builds (`tomco-site` v1
desktop-first vs `tomco-site-mobile-first` v2). That comparison still lives in
the original file. **This v2 lifts the durable lessons out of that case study
and states them as reusable defaults** — then checks each against what the
OmniCompost site actually did.

---

## 1. Responsive: default to mobile-first

Write base rules for the phone (single column, tight padding) and enhance *up*
with `min-width` queries. Mobile-first means the default layout is the smallest
screen and wider layouts are additions — which matches how most traffic arrives
and avoids the "desktop grid, then fight it back down" churn of `max-width`.

```css
.product-grid { grid-template-columns: 1fr; }              /* base = mobile */
@media (min-width: 481px) { .product-grid { grid-template-columns: repeat(2,1fr); } }
@media (min-width: 721px) { .product-grid { grid-template-columns: repeat(3,1fr); } }
```

> **Against this site:** OmniCompost uses a pragmatic mix — `max-width: 880px`
> breakpoints that collapse the shop grid to 2-up and span the feature card.
> That's desktop-first, and it was the right call *here* (see exception) because
> the design was conceived at desktop width first. The default is mobile-first;
> this site is a justified exception, not a contradiction.

## 2. Fluid type with `clamp()`

Scale type smoothly between a floor and ceiling instead of stepping at
breakpoints: `h1 { font-size: clamp(2.2rem, 4.6vw, 3.4rem); }`. This site uses
exactly this for the notes headings and hero. Cheap, robust, no media queries.

## 3. Container queries for component-local sizing

When a component appears in 1-, 2-, and 3-column contexts, size its internals to
the *component's* width (`cqi`), not the viewport — so a card caption reads right
regardless of grid column count. Use when a component is genuinely reused at
multiple widths; skip it for one-context components (overkill).

## 4. Single source of truth for content

**The highest-leverage decision in both builds.** Keep catalog/content data in
one file and generate pages from it; never hand-maintain the same product across
multiple HTML files.

- TomCo: `products.json` → `build.py`.
- OmniCompost: `products.json` → `build.py` regenerates the grid (between
  `<!-- BUILD:SHOP -->` markers) in `index.html` + `shop.html` **and** writes one
  `product/<slug>.html` per SKU. Adding `stock` to every product was a one-file
  edit that propagated to 9 cards + 9 PDPs on the next `build.py` run.

Derive **site identity** the same way — one env var (`SITE_HOST`), not a field
buried in the content file:

```python
SITE_HOST = os.environ.get("TOMCO_SITE_HOST", "").rstrip("/")
```

## 5. Deploy: match `BASE_PATH` to where it's served

GitHub Pages *project* sites serve from a subpath, so they must be built with the
matching `BASE_PATH`. A root-relative build (`BASE_PATH=""`) points `/style.css`
and `/assets/...` at the domain root and 404s under a subpath. Both past TomCo
breakages were this. Make the rewriter idempotent (strip-then-apply, record the
last applied value) so flipping between local and subpath builds is one env var.

**Set leading-slash env vars from PowerShell, never Git Bash** — MSYS rewrites
`/private-test-online` into a Windows path and corrupts the build. (Same family
as the `C:\anaconda\python.exe` path-mangling that bit this build under Bash.)

## 6. Server-render features; reserve JS-injection for transient UI

Prefer server-rendered (or build-time-rendered) markup; let JS only *attach
behavior* to existing nodes. JS-injected controls pop in after load (layout
shift), are invisible to no-JS clients and crawlers, and show a different tree to
a11y tooling on first paint. The legitimate exception is **transient overlay UI**
(lightbox, the cart drawer's dynamic contents) — created/owned by JS by design.

> **Against this site:** the shop grid and PDPs are build-time-rendered (good).
> The cart drawer *contents*, and the OC-gate field injected into the drawer
> footer, are JS-built — correct, because both are transient/stateful overlay UI
> that doesn't need to be crawlable. The principle and its exception both hold.

## Exceptions

- **Exception (desktop-first is fine when the design is):** if a site is
  conceived and judged at desktop width and mobile is a true secondary view (a
  Premium marketing page reviewed on a designer's 27″ display), desktop-first
  `max-width` queries are clearer than forcing mobile-first. OmniCompost is this
  case. Don't refactor a working desktop-first site to mobile-first for purity.
- **Exception (skip the build step):** single-source + `build.py` pays off at
  ~5+ repeated items or any per-item detail pages. For a 3-page brochure site
  with no catalog, a build pipeline is ceremony — hand-write it.
- **Exception (JS-injection for a strict A/B):** TomCo v1 kept controls
  JS-injected specifically to hold markup identical across an A/B test. A
  deliberate measurement constraint can override the server-render default — but
  name the reason, as v1 did, or it's just a layout-shift bug.

> **Adding a brand-new exception here?** Run the three-part minting test in
> `README.md` (recurring, named-justifiable-reason, would-otherwise-mislead).
> One instance is an exception; three is a pattern — promote it into the rule.
