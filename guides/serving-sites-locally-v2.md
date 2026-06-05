# Serving a Site Locally (v2)

_Last updated: 2026-05-30_1430. Supersedes `../../HOW-TO-SERVE.md`._

Previewing a static site (plain HTML/CSS/JS) on this machine. No build step
needed. There are now **two** ways to do it; pick by who needs to *see* the page.

> **v2 change — preferred method first.** The v1 guide only covered Python's
> `http.server`. This whole OmniCompost build was previewed and verified through
> the **Claude Preview MCP server** instead, because it lets Claude inspect the
> live DOM, run `preview_eval`, read console logs, and screenshot — none of which
> a bare `http.server` exposes. That's now method A. Plain `http.server` is
> method B, for when you (the human) just want a URL in your own browser.

---

## Method A — Claude Preview MCP server (Claude needs to verify)

This is the method that verified inventory states, the OC gate, and the cart
across all pages in this build. Claude drives it through the `preview_*` tools:

- `preview_start` — boots a server rooted at a folder; returns a `serverId` + port.
- `preview_eval` — runs JS in the page (read DOM, fetch routes, check state).
- `preview_console_logs` / `preview_network` — catch errors and failed requests.
- `preview_screenshot` — visual check (layout only; use `preview_inspect` for
  exact CSS values).
- `preview_list` / `preview_stop` — manage running servers.

**Document root gotcha (cost us a 404 this build):** the server root is the
folder you start it in. For this site that's `omnicompost-premium-site/`, so
routes are `/index.html`, `/shop.html`, `/product/<slug>.html`,
`/notes/<issue>.html` — **not** `/omnicompost-premium-site/...`, which 404s.
Always confirm the root before chasing a "missing file."

**Servers stop.** A `serverId` from a previous session is usually dead. Run
`preview_list` first; if it's empty, `preview_start` again and use the new id.

Use this method whenever the goal is *Claude confirms the change works* — it
keeps verification in-loop instead of asking you to eyeball it.

---

## Method B — Python `http.server` (you want a URL)

Works in **any** terminal (cmd, PowerShell, Windows Terminal):

```
C:\anaconda\python.exe -m http.server 8000 --directory "C:\path\to\your\folder"
```

- `8000` — the port. Change it to run multiple servers at once (e.g. `8001`).
- `--directory` — sets the web root. `localhost:8000/` maps to this folder.
  Omit it to serve the current working directory.
- Quote the path (project paths contain spaces). No trailing backslash.
- Leave the terminal open — closing it kills the server. `Ctrl+C` stops it.

The server is locked to its `--directory` (`..` traversal is blocked).

### Check / stop a port

**PowerShell:**
```
Get-NetTCPConnection -LocalPort 8000 -State Listen
$p = (Get-NetTCPConnection -LocalPort 8000 -State Listen).OwningProcess
Stop-Process -Id $p -Force
```

**cmd:**
```
netstat -ano | findstr :8000
taskkill /PID <pid> /F
```

---

## Notes (both methods)

- **Browser caching** — neither server sends cache-busting headers. After
  editing CSS/JS, hard-refresh with `Ctrl+F5`. (With Method A, `preview_eval`
  fetches are not cached the same way — a `fetch('/cart.js')` sees the file on
  disk, which is why it's reliable for verifying edits landed.)
- **No live reload** — refresh manually after every edit.
- **One server per port** — a second server on a busy port fails with "address
  already in use." Use another port or stop the first.
- **Static only** — both serve files as-is. A Python app (Flask/Django) is
  started by running its own script, not by serving the folder.

## Exceptions

- **Exception (use B over A):** when *you*, not Claude, are doing the visual
  review across many manual interactions, plain `http.server` + your own browser
  is lower-friction than narrating clicks through MCP tools. A loses its
  advantage the moment a human is the one looking.
- **Exception (neither — open the file):** a single self-contained page with no
  `fetch()`/relative-route dependencies (e.g. an early `index.html` mockup) opens
  fine via `file://`. You only need a server once the page requests sibling files
  (this site does: `cart.js`, `products`-driven routes, images).
- **Exception (real backend):** the moment checkout (Snipcart) or a server-side
  form handler lands, "static serving" stops being the whole story — Snipcart's
  JS runs client-side and is fine, but a custom order endpoint needs its own
  process. Revisit then.

> **Adding a brand-new exception here?** Run the three-part minting test in
> `README.md` (recurring, named-justifiable-reason, would-otherwise-mislead).
> One instance is an exception; three is a pattern — promote it into the rule.
