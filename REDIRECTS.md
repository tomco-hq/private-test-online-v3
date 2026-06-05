# Short-URL redirects — guide QR codes

_Last updated: 2026-06-01_1640_

The printed one-page guides carry QR codes that encode **stable short URLs**, not the
PDF's real path:

| Guide | QR encodes | Redirects to (current) |
|---|---|---|
| Kitchen | `https://omnicompost.com/g/kitchen` | `/assets/guides/kitchen-guide-v5.png` |
| Lawn | `https://omnicompost.com/g/lawn` | `/assets/guides/lawn-guide-v6.png` |
| Troubleshooting | `https://omnicompost.com/g/troubleshooting` | `/assets/guides/troubleshooting-guide.pdf` |

## Why the indirection
A printed card is permanent; the file behind it is not. Pointing the QR at `/g/<slug>`
lets us re-export the PDF (Canva finish, content fixes) and just repoint the redirect —
every card already in the world keeps working. Encode the short URL once, change only the
target.

**Use 302 (temporary)**, not 301: a 301 is cached aggressively by browsers and some
scanner apps, so a future retarget might not take. Switch a given slug to 301 only when its
destination is genuinely final.

## The rule, per host
The canonical file is **`_redirects`** in the site root (Netlify / Cloudflare Pages):

```
/g/kitchen          /assets/guides/kitchen-guide-v5.png      302
/g/lawn             /assets/guides/lawn-guide-v6.png         302
/g/troubleshooting  /assets/guides/troubleshooting-guide.pdf 302
/*                  /404.html                                404
```

Equivalents if the host differs:

**Vercel** — `vercel.json`:
```json
{ "redirects": [
  { "source": "/g/kitchen", "destination": "/assets/guides/kitchen-guide-v5.png", "permanent": false },
  { "source": "/g/lawn", "destination": "/assets/guides/lawn-guide-v6.png", "permanent": false },
  { "source": "/g/troubleshooting", "destination": "/assets/guides/troubleshooting-guide.pdf", "permanent": false }
] }
```

**Apache** — `.htaccess`:
```
Redirect 302 /g/kitchen          /assets/guides/kitchen-guide-v5.png
Redirect 302 /g/lawn             /assets/guides/lawn-guide-v6.png
Redirect 302 /g/troubleshooting  /assets/guides/troubleshooting-guide.pdf
```

**Nginx** — server block:
```
location = /g/kitchen          { return 302 /assets/guides/kitchen-guide-v5.png; }
location = /g/lawn             { return 302 /assets/guides/lawn-guide-v6.png; }
location = /g/troubleshooting  { return 302 /assets/guides/troubleshooting-guide.pdf; }
```

## Open items
- [ ] Swap kitchen/lawn targets from `.png` → final `.pdf` once the Canva PDFs are hosted.
- [ ] Confirm the production host so the right config file is the live one (`_redirects`
      assumes Netlify/Cloudflare Pages).
- [ ] These short URLs only work once the domain + host are live; until then the QR codes
      resolve to nothing. Don't print cards before the redirects are deployed.
