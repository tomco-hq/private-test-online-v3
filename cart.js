// OmniCompost — shared cart. Persisted in localStorage, synced across pages/tabs.
// Identical file in the Premium and Family sites; tier-agnostic by design.
(function () {
  const CART_KEY = 'oc_cart';
  let cart = [];
  try { cart = JSON.parse(localStorage.getItem(CART_KEY)) || []; } catch (e) { cart = []; }
  const save = () => { try { localStorage.setItem(CART_KEY, JSON.stringify(cart)); } catch (e) {} };

  const $ = (id) => document.getElementById(id);
  const ditems = $('ditems'), ct = $('ct'), sub = $('sub');
  const drawer = $('drawer'), scrim = $('scrim'), live = $('cartLive');
  const empty = '<p style="color:var(--ink-soft); font-size:.9rem">Your cart is empty — add something from the shop.</p>';

  // ── Regional shipping ──────────────────────────────────────────────────────
  // One ZIP entry drives a flat shipping cost by region tier. Orders over
  // FREE_SHIP_MIN ship free. This replaces the old Orange-County-only gate: we
  // now ship everywhere, OC just gets the cheapest tier. Client-side estimate
  // only — the authoritative charge is computed server-side at checkout.
  const ZIP_KEY = 'oc_zip';
  const FREE_SHIP_MIN = 150; // free shipping threshold (one number to tune)
  const SHIP_TIERS = {
    oc:    { label: 'Orange County',                    cost: 7  }, // low
    metro: { label: 'L.A. / San Diego / Inland Empire', cost: 12 }, // medium
    rest:  { label: 'rest of California & nationwide',   cost: 20 }, // high
  };
  // L.A. + San Diego + Inland Empire ZIP prefixes (3-digit). OC is matched by
  // exact range first, so the 906xx overlap resolves to OC, not metro.
  const METRO_PREFIXES = [
    '900','901','902','903','904','905','907','908','910','911','912','913',
    '914','915','917','918',          // Los Angeles County
    '919','920','921',                // San Diego County
    '922','923','924','925',          // Inland Empire (Riverside / San Bernardino)
  ];
  const zipTier = (z) => {
    if (!/^\d{5}$/.test(z)) return null;
    const n = +z;
    if ((n >= 90620 && n <= 90899) || (n >= 92600 && n <= 92899)) return 'oc';
    if (METRO_PREFIXES.includes(z.slice(0, 3))) return 'metro';
    return 'rest';
  };

  let zipInput = null, shipLine = null;
  const foot = sub ? sub.closest('.df, .dfoot') : null;
  if (foot) {
    const box = document.createElement('div');
    box.className = 'shipbox';
    box.innerHTML =
      '<label for="ocZip">Shipping postcode</label>' +
      '<input id="ocZip" inputmode="numeric" maxlength="5" autocomplete="postal-code" placeholder="e.g. 92614">' +
      '<p class="shipline" id="shipLine" role="status" aria-live="polite"></p>';
    const checkout = foot.querySelector('#checkoutBtn');
    if (checkout) foot.insertBefore(box, checkout); else foot.appendChild(box);
    zipInput = $('ocZip'); shipLine = $('shipLine');

    if (!document.getElementById('shipStyle')) {
      const st = document.createElement('style');
      st.id = 'shipStyle';
      st.textContent =
        '.shipbox{margin:.6rem 0 .9rem}' +
        '.shipbox label{display:block;font-size:.74rem;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-soft);margin-bottom:.35rem}' +
        '.shipbox input{width:100%;padding:.55rem .65rem;border:1px solid var(--line);background:var(--cream);font:inherit;font-size:.95rem;color:var(--ink)}' +
        '.shipbox input:focus{outline:2px solid var(--sage);outline-offset:-1px}' +
        '.shipline{font-size:.78rem;margin:.45rem 0 0;min-height:1em;color:var(--ink-soft)}' +
        '.shipline.ok{color:var(--sage)}';
      document.head.appendChild(st);
    }
    try { zipInput.value = localStorage.getItem(ZIP_KEY) || ''; } catch (e) {}
    zipInput.addEventListener('input', () => {
      const z = zipInput.value.trim();
      if (/^\d{5}$/.test(z)) { try { localStorage.setItem(ZIP_KEY, z); } catch (e) {} }
      render();
    });
  }

  const FOCUSABLE = 'a[href],button:not([disabled]),input,[tabindex]:not([tabindex="-1"])';
  let lastFocus = null;

  // Keep focus inside the drawer while it is open (focus-trap).
  const trap = (e) => {
    if (e.key === 'Escape') { closeC(); return; }
    if (e.key !== 'Tab' || !drawer) return;
    const items = [...drawer.querySelectorAll(FOCUSABLE)].filter(el => el.offsetParent !== null);
    if (!items.length) return;
    const first = items[0], last = items[items.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  };

  const openC = () => {
    if (!drawer) return;
    lastFocus = document.activeElement;
    drawer.classList.add('on'); if (scrim) scrim.classList.add('on');
    const cb = $('cartBtn'); if (cb) cb.setAttribute('aria-expanded', 'true');
    const closeBtn = $('closeC'); if (closeBtn) closeBtn.focus(); else drawer.focus();
    document.addEventListener('keydown', trap);
  };
  const closeC = () => {
    if (drawer) drawer.classList.remove('on'); if (scrim) scrim.classList.remove('on');
    const cb = $('cartBtn'); if (cb) cb.setAttribute('aria-expanded', 'false');
    document.removeEventListener('keydown', trap);
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  };

  function shipMsg(total) {
    if (!shipLine) return;
    if (!cart.length) { shipLine.textContent = ''; shipLine.className = 'shipline'; return; }
    const tier = zipTier(zipInput ? zipInput.value.trim() : '');
    if (!tier) {
      shipLine.textContent = 'Enter your postcode for a shipping estimate.';
      shipLine.className = 'shipline';
      return;
    }
    const t = SHIP_TIERS[tier];
    if (total >= FREE_SHIP_MIN) {
      shipLine.textContent = 'Free shipping to ' + t.label + ' on orders over $' + FREE_SHIP_MIN + '.';
      shipLine.className = 'shipline ok';
    } else {
      shipLine.textContent = t.label.charAt(0).toUpperCase() + t.label.slice(1) +
        ' shipping: $' + t.cost + '. Add $' + (FREE_SHIP_MIN - total) + ' for free shipping.';
      shipLine.className = 'shipline';
    }
  }

  function render() {
    save();
    const n = cart.reduce((a, c) => a + c.q, 0);
    if (ct) ct.textContent = n;
    if (live) live.textContent = n === 0 ? 'Cart is empty' : (n + (n === 1 ? ' item' : ' items') + ' in cart');
    if (!ditems) return; // page has only the count badge (e.g. newsletter)
    if (!cart.length) { ditems.innerHTML = empty; if (sub) sub.textContent = '$0'; shipMsg(0); return; }
    ditems.innerHTML = cart.map((c, idx) =>
      `<div class="di"><img src="${c.i}" alt=""><div><div class="n">${c.n}</div>` +
      `<div class="qty"><button data-d="${idx}" aria-label="Decrease">−</button>` +
      `<span class="meta">Qty ${c.q}</span><button data-u="${idx}" aria-label="Increase">+</button></div></div>` +
      `<div class="p">$${c.p * c.q}</div></div>`).join('');
    const total = cart.reduce((a, c) => a + c.p * c.q, 0);
    if (sub) sub.textContent = '$' + total;
    shipMsg(total);
    ditems.querySelectorAll('[data-u]').forEach(b => b.onclick = () => {
      const c = cart[+b.dataset.u]; const cap = c.s || Infinity;
      if (c.q < cap) c.q++; render();
    });
    ditems.querySelectorAll('[data-d]').forEach(b => b.onclick = () => { const i = +b.dataset.d; if (--cart[i].q <= 0) cart.splice(i, 1); render(); });
  }

  document.querySelectorAll('.add').forEach(b => b.onclick = () => {
    if (b.disabled || b.getAttribute('aria-disabled') === 'true') return;
    const n = b.dataset.n, p = +b.dataset.p, i = b.dataset.i;
    const s = b.dataset.s ? +b.dataset.s : Infinity;
    const e = cart.find(c => c.n === n);
    if (e) { e.s = e.s || s; if (e.q < e.s) e.q++; }
    else cart.push({ n, p, i, q: 1, s });
    render(); openC();
  });

  const cartBtn = $('cartBtn'), closeBtn = $('closeC'), checkoutBtn = $('checkoutBtn');
  if (cartBtn) cartBtn.onclick = openC;
  if (closeBtn) closeBtn.onclick = closeC;
  if (scrim) scrim.onclick = closeC;
  if (checkoutBtn && checkoutBtn.tagName === 'BUTTON') checkoutBtn.onclick = () => closeC();

  // shop filters (no-op if no chips on the page)
  const cards = [...document.querySelectorAll('.pcard')];
  document.querySelectorAll('.chip').forEach(chip => chip.onclick = () => {
    document.querySelectorAll('.chip').forEach(c => c.classList.remove('on'));
    chip.classList.add('on');
    const f = chip.dataset.f;
    cards.forEach(c => c.style.display = (f === 'all' || c.dataset.cat === f) ? '' : 'none');
  });

  // reflect persisted cart on load + sync across tabs
  render();
  window.addEventListener('storage', e => {
    if (e.key === CART_KEY) { try { cart = JSON.parse(e.newValue) || []; } catch (_) { cart = []; } render(); }
  });
})();
