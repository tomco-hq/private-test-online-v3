// OmniCompost — shared cart. Persisted in localStorage, synced across pages/tabs.
(function () {
  const CART_KEY = 'oc_cart';
  let cart = [];
  try { cart = JSON.parse(localStorage.getItem(CART_KEY)) || []; } catch (e) { cart = []; }
  const save = () => { try { localStorage.setItem(CART_KEY, JSON.stringify(cart)); } catch (e) {} };

  const $ = (id) => document.getElementById(id);
  const ditems = $('ditems'), ct = $('ct'), sub = $('sub');
  const drawer = $('drawer'), scrim = $('scrim'), live = $('cartLive');
  const empty = '<p style="color:var(--ink-soft); font-size:.9rem">Your cart is empty — add something from the shop.</p>';

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

  function render() {
    save();
    const n = cart.reduce((a, c) => a + c.q, 0);
    if (ct) ct.textContent = n;
    if (live) live.textContent = n === 0 ? 'Cart is empty' : (n + (n === 1 ? ' item' : ' items') + ' in cart');
    if (!ditems) return; // page has only the count badge (e.g. newsletter)
    if (!cart.length) { ditems.innerHTML = empty; if (sub) sub.textContent = '$0'; return; }
    ditems.innerHTML = cart.map((c, idx) =>
      `<div class="di"><img src="${c.i}" alt=""><div><div class="n">${c.n}</div>` +
      `<div class="qty"><button data-d="${idx}" aria-label="Decrease">−</button>` +
      `<span class="meta">Qty ${c.q}</span><button data-u="${idx}" aria-label="Increase">+</button></div></div>` +
      `<div class="p">$${c.p * c.q}</div></div>`).join('');
    if (sub) sub.textContent = '$' + cart.reduce((a, c) => a + c.p * c.q, 0);
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

  // ── Orange County delivery gate ──────────────────────────────────────────
  // Delivery and setup are limited to Orange County, CA. Checkout stays locked
  // until the shopper enters a postcode inside the OC ranges. Client-side only.
  const ZIP_KEY = 'oc_zip';
  const inOC = (z) => /^\d{5}$/.test(z) &&
    ((+z >= 90620 && +z <= 90899) || (+z >= 92600 && +z <= 92899));

  if (checkoutBtn && checkoutBtn.tagName === 'BUTTON') {
    const df = checkoutBtn.parentNode;
    const gate = document.createElement('div');
    gate.className = 'ocgate';
    gate.innerHTML =
      '<label for="ocZip">Delivery postcode</label>' +
      '<input id="ocZip" inputmode="numeric" maxlength="5" autocomplete="postal-code" placeholder="e.g. 92614">' +
      '<p class="ocmsg" id="ocMsg" role="status" aria-live="polite"></p>';
    df.insertBefore(gate, checkoutBtn);

    if (!document.getElementById('ocGateStyle')) {
      const st = document.createElement('style');
      st.id = 'ocGateStyle';
      st.textContent =
        '.ocgate{margin-bottom:.9rem}' +
        '.ocgate label{display:block;font-size:.74rem;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-soft);margin-bottom:.35rem}' +
        '.ocgate input{width:100%;padding:.55rem .65rem;border:1px solid var(--line);background:var(--cream);font:inherit;font-size:.95rem;color:var(--ink)}' +
        '.ocgate input:focus{outline:2px solid var(--sage);outline-offset:-1px}' +
        '.ocmsg{font-size:.74rem;margin:.4rem 0 0;min-height:1em}' +
        '.ocmsg.ok{color:var(--sage)}.ocmsg.bad{color:var(--terra)}' +
        '#checkoutBtn[disabled]{opacity:.45;cursor:not-allowed}';
      document.head.appendChild(st);
    }

    const zipInput = $('ocZip'), zipMsg = $('ocMsg');
    const applyGate = () => {
      const z = zipInput.value.trim();
      if (!z) {
        checkoutBtn.disabled = true;
        zipMsg.textContent = ''; zipMsg.className = 'ocmsg';
      } else if (inOC(z)) {
        checkoutBtn.disabled = false;
        zipMsg.textContent = 'Within our delivery area.'; zipMsg.className = 'ocmsg ok';
        try { localStorage.setItem(ZIP_KEY, z); } catch (e) {}
      } else {
        checkoutBtn.disabled = true;
        zipMsg.textContent = 'Outside Orange County — delivery isn’t available here yet.';
        zipMsg.className = 'ocmsg bad';
      }
    };
    try { zipInput.value = localStorage.getItem(ZIP_KEY) || ''; } catch (e) {}
    zipInput.addEventListener('input', applyGate);
    applyGate();
    checkoutBtn.onclick = () => { if (!checkoutBtn.disabled) closeC(); };
  }

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
