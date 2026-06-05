# Adding Content to the OmniCompost Site — User Guide

_Last updated: 2026-05-30_1430_

A plain-language walkthrough of how to change each part of the site, which
program to open, and what to watch for. No framework knowledge needed — this is a
folder of files, not an app.

## Before you start — the two kinds of pages

There are **generated** pages and **hand-written** pages, and the difference
decides where you make a change.

- **Generated** (don't edit by hand): the shop grids on `index.html` /
  `shop.html`, and every page in `product/`. These come out of `products.json`
  through `build.py`. Edit the data, re-run the build, the pages update.
- **Hand-written** (edit directly): `newsletter.html`, the Field Notes issues in
  `notes/`, and the editorial parts of `index.html` outside the shop grid.

> **Golden rule:** if it's a product, change `products.json` and rebuild. If it's
> words or pictures on an editorial page, edit that page's HTML.

## What to open

| Job | Program |
|---|---|
| Edit `products.json`, HTML, or `cart.js` | Any text editor. VS Code is ideal; Notepad works. |
| Run the build | **PowerShell** (not Git Bash — it mangles the Python path). |
| Run a quick script / experiment | Jupyter Notebook (Anaconda), if you prefer. |
| Preview the result | A browser, served locally (see "Previewing" below). |

The build command, run from inside the site folder in PowerShell:

```powershell
C:\anaconda\python.exe build.py
```

It prints what it updated and is safe to run repeatedly.

---

## 1. Add, edit, or remove a product

1. Open **`products.json`**.
2. Copy an existing object inside `"products": [ ... ]` and edit the fields. The
   important ones:
   - `id` — internal, unique (e.g. `oc-care-kit`).
   - `slug` — becomes the page URL `product/<slug>.html`. **Don't change a slug
     later** — it orphans the old page and breaks links.
   - `name` — shown to shoppers; also the cart's line key, so keep names unique.
   - `price` — a plain number, **no `$`** (the site adds it). `385`, not `$385`.
   - `category` — used for the shop filter chips and the card label.
   - `featured` — `true` makes a big 2×2 card with a `blurb`.
   - `image` / `alt` — path under `assets/img/...` and its alt text (see §4).
   - `image2` / `alt2` *(optional)* — a second photo for the detail page. When
     present, the PDP shows a small thumbnail strip and lets shoppers swap the
     main image. Omit it and the page shows a single image as before.
   - `stars` / `score` / `count` — the rating line (e.g. `"★★★★★"`, `4.9`, `312`).
   - `stock` — how many you have (see §2).
   - `blurb` (short), `desc` (long, for the detail page), `details` (the spec
     bullet list on the detail page).
3. Save, then in PowerShell run `C:\anaconda\python.exe build.py`.
4. Preview (see below). The new product now appears on the homepage shop, the
   full shop page, and has its own `product/<slug>.html`.

**Remove a product:** delete its object from `products.json` and rebuild. (Note:
the old `product/<slug>.html` file isn't auto-deleted — remove it by hand if you
want it gone.)

**Writing the copy:** Premium voice only — complete sentences, exact numbers, no
exclamation points, noun-first. The `omnicompost-design-system` skill has the
full rules; match the tone of the existing products.

## 2. Change stock / mark something sold out

Stock is just the `stock` number in `products.json`:

- A number above 10 → shows **In stock**.
- 1–10 → shows **Low stock — N left**.
- `0` → shows **Sold out**, the Add-to-cart button is disabled, and the cart
  won't let anyone exceed available stock.

Change the number, rebuild, done. To pull an item temporarily, set `stock` to
`0` rather than deleting it (keeps the page and link alive).

## 3. Add a Field Notes (newsletter archive) issue

These live in **`notes/`** and are hand-written HTML — no build step.

1. Copy the most recent issue file in `notes/` (e.g. `april-2026.html`) to a new
   name like `notes/may-2026.html`.
2. Edit the headline, date, body paragraphs, and figures. Keep the existing
   structure (`<article class="note">`, `<figure>`, `<figcaption>`).
3. Add a link to the new issue from wherever the issues are listed (the
   newsletter/archive page).
4. Use 1–2 local images per issue (see §4). Premium voice throughout.

No `build.py` needed — just save and preview.

## 4. Add an image

1. Put the file in **`assets/img/`** (or a subfolder there). Use local files
   only — never link to an image on another website (it can vanish or change).
2. Reference it by its path: in `products.json` as `"image": "assets/img/your-photo.jpg"`,
   or in an HTML page as `<img src="assets/img/your-photo.jpg" alt="...">`.
   (On `product/` pages the path needs a `../` prefix because those pages sit one
   folder deeper — but the build handles product images for you.)
3. **Always write meaningful `alt` text** — it's read aloud by screen readers and
   shown if the image fails to load.
4. Keep the muted, natural Premium look. The `omnicompost-image-sourcing` skill
   covers where to find and how to vet photos.

## 5. Edit the newsletter signup

Open **`newsletter.html`**. The copy and layout are plain HTML you can edit
directly. To make the form actually send signups somewhere, set the
`ESP_ENDPOINT` value near the form script to your email provider's form URL.
While it's an empty string, the form is in **demo mode** (it pretends to succeed
but sends nothing). **Never paste an API key or password into this file** — use a
form URL only.

## 6. Edit homepage text, FAQ, "how it works"

These sections of **`index.html`** are hand-written. Edit the text between the
relevant tags directly. The **one** part of `index.html` to leave alone is the
shop grid between the `<!-- BUILD:SHOP -->` and `<!-- /BUILD:SHOP -->` comments —
that's generated, and the build will overwrite anything you put there.

---

## Previewing your changes

You need a local server (opening the file directly breaks the cart and images).

**Easiest — Python, in PowerShell, from the site folder:**

```powershell
C:\anaconda\python.exe -m http.server 8000
```

Then open `http://localhost:8000/` in your browser. Leave the PowerShell window
open while you look; press `Ctrl+C` to stop. After editing CSS/JS, hard-refresh
with `Ctrl+F5` (the server doesn't auto-reload).

(If you'd rather have Claude verify a change, that's the `static-site-preview`
skill — it inspects the live page directly.)

## A safe checklist for any change

1. Edit the right file (product → `products.json`; editorial → the page itself).
2. If you touched `products.json`, run `build.py` in PowerShell.
3. Start the local server and look at the page in a browser.
4. Check the part you changed **and** the cart still opens and adds items.
5. Keep the Premium voice; no exclamation points; exact numbers.

## When in doubt

- Product behaving oddly after an edit? Re-run `build.py` — a hand-edit to a
  generated page gets wiped on the next build by design.
- Image not showing? Check the path and that the file is really in `assets/img/`.
- Cart not opening on a new page? It needs the cart markup + `<script src="cart.js">`
  (or `../cart.js` in `product/`). Copy it from an existing page.
- Anything about voice, color, or type → `omnicompost-design-system` skill.
- Anything about the shop mechanics → `omnicompost-commerce` skill.
