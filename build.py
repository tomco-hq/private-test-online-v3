"""Static shop builder for the OmniCompost Premium site.

``products.json`` is the single source of truth for the catalog. This script
regenerates, in place:

  * the product grid (the region between the ``BUILD:SHOP`` markers) in the
    hand-built, Premium-styled pages:
      - index.html  -- the homepage shop section (#shop)
      - shop.html   -- the dedicated full-catalog page
  * one detail page per product, under ``product/<slug>.html``

Everything else on the hand-built pages is left untouched. Re-run this whenever
products.json changes:

    C:\\anaconda\\python.exe build.py

The emitted markup matches the Premium design system (.pcard cards, sage/cream
tokens, Fraunces + Inter), so the look does not change -- only the data source.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_FILE = os.path.join(BASE_DIR, "products.json")
INDEX_FILE = os.path.join(BASE_DIR, "index.html")
SHOP_FILE = os.path.join(BASE_DIR, "shop.html")
PRODUCT_DIR = os.path.join(BASE_DIR, "product")

START_MARKER = "<!-- BUILD:SHOP"
END_MARKER = "<!-- /BUILD:SHOP -->"


def money(value):
    """Format a numeric price with no trailing zeros, e.g. 385 -> '385'."""
    return "{:g}".format(value)


def rating_html(product):
    """Return the star/score/count line for a product card."""
    score = "{:.1f}".format(product["score"])
    if product.get("featured"):
        tail = "{} ({} reviews)".format(score, product["count"])
    else:
        tail = "{} ({})".format(score, product["count"])
    return "{} <i>{}</i>".format(product["stars"], tail)


def stock_html(product):
    """Return the inventory state line for a product.

    Single source: the ``stock`` count in products.json. 0 reads as sold out,
    10 or fewer as low stock, otherwise in stock.
    """
    stock = product.get("stock", 0)
    if stock <= 0:
        return '<span class="stock stock--out">Sold out</span>'
    if stock <= 10:
        return '<span class="stock stock--low">Low stock — {} left</span>'.format(stock)
    return '<span class="stock stock--in">In stock</span>'


def add_button(product, solid=None):
    """Return the add-to-cart button (wired to the shared cart.js).

    Carries ``data-s`` so cart.js can clamp quantity to the stock on hand. A
    sold-out product renders a disabled button instead.
    """
    use_solid = product.get("cta") == "solid" if solid is None else solid
    cls = "btn btn--solid add" if use_solid else "btn add"
    if product.get("stock", 0) <= 0:
        return '<button class="{cls}" disabled aria-disabled="true">Sold out</button>'.format(
            cls=cls
        )
    return (
        '<button class="{cls}" data-n="{name}" data-p="{price}" '
        'data-i="{image}" data-s="{stock}">Add to cart</button>'
    ).format(
        cls=cls,
        name=product["name"],
        price=money(product["price"]),
        image=product["image"],
        stock=product["stock"],
    )


def card_html(product, indent):
    """Return one .pcard article. Featured cards span 2x2 and show a blurb."""
    pad = " " * indent
    cat_label = product["category"].capitalize()
    badge = (
        '<span class="badge">{}</span>'.format(product["badge"])
        if product.get("badge")
        else ""
    )
    name_link = '<a href="product/{slug}.html">{name}</a>'.format(
        slug=product["slug"], name=product["name"]
    )

    if product.get("featured"):
        return (
            '{pad}<article class="pcard feature" data-cat="{cat}">\n'
            '{pad}  <div class="ph">{badge}<img src="{image}" alt="{alt}" /></div>\n'
            '{pad}  <div class="body">\n'
            '{pad}    <span class="cat">{label}</span>\n'
            "{pad}    <h3>{name_link}</h3>\n"
            '{pad}    <p class="blurb">{blurb}</p>\n'
            '{pad}    <div class="prate">{rating}</div>\n'
            '{pad}    <span class="price">${price}</span> {stock}\n'
            "{pad}    {button}\n"
            "{pad}  </div>\n"
            "{pad}</article>"
        ).format(
            pad=pad,
            cat=product["category"],
            badge=badge,
            image=product["image"],
            alt=product["alt"],
            label=cat_label,
            name_link=name_link,
            blurb=product.get("blurb", ""),
            rating=rating_html(product),
            price=money(product["price"]),
            stock=stock_html(product),
            button=add_button(product),
        )

    # Compact card -- single-line body, matching the hand-built markup.
    return (
        '{pad}<article class="pcard" data-cat="{cat}">\n'
        '{pad}  <div class="ph">{badge}<img src="{image}" alt="{alt}" /></div>\n'
        '{pad}  <div class="body"><span class="cat">{label}</span>'
        "<h3>{name_link}</h3>"
        '<div class="prate">{rating}</div>'
        '<span class="price">${price}</span> {stock}{button}</div>\n'
        "{pad}</article>"
    ).format(
        pad=pad,
        cat=product["category"],
        badge=badge,
        image=product["image"],
        alt=product["alt"],
        label=cat_label,
        name_link=name_link,
        rating=rating_html(product),
        price=money(product["price"]),
        stock=stock_html(product),
        button=add_button(product),
    )


def render_grid(products, indent):
    """Return all product cards joined, at the given indent."""
    return "\n".join(card_html(p, indent) for p in products)


def update_shop_region(path, products, card_indent, close_indent):
    """Rewrite the BUILD:SHOP region of one page in place."""
    if not os.path.exists(path):
        raise RuntimeError("%s not found" % path)

    with open(path, encoding="utf-8") as handle:
        text = handle.read()

    start = text.find(START_MARKER)
    end = text.find(END_MARKER)
    if start == -1 or end == -1:
        raise RuntimeError(
            "BUILD:SHOP markers not found in %s" % os.path.basename(path)
        )

    open_close = text.index("-->", start) + len("-->")
    grid = render_grid(products, card_indent)
    new_text = text[:open_close] + "\n" + grid + "\n" + " " * close_indent + text[end:]

    if new_text != text:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(new_text)
        print("updated %s (%d products)" % (os.path.basename(path), len(products)))
    else:
        print("%s already up to date" % os.path.basename(path))


# ---------------------------------------------------------------------------
# Per-product detail pages
# ---------------------------------------------------------------------------

# Page template. Assets/links carry a "../" prefix because the pages live in the
# product/ subfolder. Cart markup + cart.js make the cart work site-wide; the
# shared cart.js wires the .add button by its data-* attributes.
PRODUCT_PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>OmniCompost — {name}</title>
  <meta name="description" content="{meta_desc}" />
  <link rel="icon" href="../assets/logo/favicon.svg" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,300;1,9..144,400&family=Inter:wght@300;400;500;600&display=swap" />
  <style>
    :root{{--cream:#F4EDE0;--cream-deep:#EBE2D2;--sage:#5D7A5E;--sage-deep:#3D5444;
      --terra:#9B5A44;--ochre:#9A6E1D;--teal:#5B7B7A;--ink:#2A2530;--ink-soft:#564f55;--line:rgba(42,37,48,.16)}}
    *{{box-sizing:border-box;margin:0;padding:0}}
    html{{scroll-behavior:smooth}}
    body{{background:var(--cream);color:var(--ink);font-family:"Inter",system-ui,sans-serif;font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}}
    h1,h2,h3{{font-family:"Fraunces","Georgia",serif;font-weight:400;line-height:1.08;letter-spacing:-.01em}}
    em,i{{font-family:"Fraunces",serif;font-style:italic;font-weight:300;color:var(--sage-deep);font-size:.92em}}
    a{{color:inherit}}img{{display:block;max-width:100%}}
    .wrap{{max-width:1180px;margin:0 auto;padding:0 2rem}}
    .eyebrow{{font-family:"Fraunces",serif;font-style:italic;font-weight:300;color:var(--terra);font-size:1.05rem}}
    .btn{{display:inline-block;font-family:"Inter",sans-serif;font-weight:500;font-size:.82rem;letter-spacing:.1em;
      text-transform:uppercase;text-decoration:none;padding:.95rem 2rem;border:1px solid var(--ink);color:var(--ink);
      background:transparent;cursor:pointer;transition:background .25s,color .25s}}
    .btn:hover{{background:var(--ink);color:var(--cream)}}
    .btn--solid{{background:var(--sage-deep);border-color:var(--sage-deep);color:var(--cream)}}
    .btn--solid:hover{{background:var(--ink);border-color:var(--ink)}}
    .strip{{background:var(--sage-deep);color:var(--cream);text-align:center;font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;padding:.55rem 1rem}}
    header.site{{position:sticky;top:0;z-index:50;background:rgba(244,237,224,.9);backdrop-filter:saturate(140%) blur(8px);border-bottom:1px solid var(--line)}}
    .site-inner{{display:flex;align-items:center;justify-content:space-between;max-width:1180px;margin:0 auto;padding:.85rem 2rem}}
    .brand{{display:flex;align-items:center;gap:.7rem;text-decoration:none}}
    .brand img{{height:34px;width:auto}}
    .brand .word{{font-family:"Fraunces",serif;font-size:1.32rem}}
    .brand .word b{{font-weight:600;color:var(--ink)}}.brand .word span{{font-weight:400;color:var(--sage-deep)}}
    nav.main{{display:flex;gap:2rem;align-items:center}}
    nav.main a{{text-decoration:none;font-size:.82rem;letter-spacing:.04em;color:var(--ink-soft);transition:color .2s}}
    nav.main a:hover,nav.main a[aria-current]{{color:var(--ink)}}
    .cart-btn{{display:flex;align-items:center;gap:.4rem;border:1px solid var(--ink);padding:.5rem 1rem;font-size:.7rem;
      letter-spacing:.1em;text-transform:uppercase;cursor:pointer;background:transparent;color:var(--ink);font-family:"Inter"}}
    .cart-btn:hover{{background:var(--ink);color:var(--cream)}}.cart-btn b{{font-weight:600}}
    .menu-btn{{display:none;background:none;border:0;cursor:pointer;padding:.4rem}}
    .menu-btn span{{display:block;width:22px;height:1.5px;background:var(--ink);margin:5px 0}}
    .crumb{{padding:1.6rem 0 0;font-size:.78rem;letter-spacing:.04em;color:var(--ink-soft)}}
    .crumb a{{text-decoration:none}}.crumb a:hover{{color:var(--ink)}}
    .pdp{{display:grid;grid-template-columns:1.1fr 1fr;gap:3rem;padding:2.2rem 0 4rem;align-items:start}}
    .pdp .media{{border:1px solid var(--line);background:var(--cream-deep);position:relative}}
    .pdp .media img{{width:100%;height:100%;object-fit:cover;aspect-ratio:4/3}}
    .pdp .media .badge{{position:absolute;top:1rem;left:1rem;background:var(--sage-deep);color:var(--cream);
      font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;padding:.35rem .7rem}}
    .pdp .cat{{font-family:"Inter";font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--teal)}}
    .pdp h1{{font-size:clamp(2.1rem,4vw,3rem);margin:.5rem 0 .8rem}}
    .pdp .prate{{font-size:.92rem;color:var(--ochre);margin-bottom:1.1rem}}
    .pdp .price{{font-family:"Fraunces",serif;font-size:1.9rem;display:block;margin-bottom:.5rem}}
    .stock{{font-size:.74rem;letter-spacing:.08em;text-transform:uppercase}}
    .stock--in{{color:var(--sage)}}.stock--low{{color:var(--ochre)}}.stock--out{{color:var(--terra)}}
    .pdp .stockline{{margin-bottom:1.2rem}}
    .btn[disabled],.add[disabled]{{opacity:.45;cursor:not-allowed}}
    .btn[disabled]:hover{{background:transparent;color:var(--ink)}}
    .btn--solid[disabled]:hover{{background:var(--sage-deep);color:var(--cream)}}
    .pdp .desc{{color:var(--ink-soft);font-size:1.02rem;margin-bottom:1.6rem;max-width:34rem}}
    .pdp ul.specs{{list-style:none;border-top:1px dashed var(--line);margin-bottom:1.8rem}}
    .pdp ul.specs li{{padding:.7rem 0;border-bottom:1px dashed var(--line);font-size:.92rem;display:flex;gap:.7rem;align-items:baseline}}
    .pdp ul.specs li::before{{content:"—";color:var(--terra)}}
    .pdp .actions{{display:flex;gap:.8rem;flex-wrap:wrap;align-items:center}}
    .pdp .back{{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-soft);text-decoration:none}}
    .pdp .back:hover{{color:var(--ink)}}
    .scrim{{position:fixed;inset:0;background:rgba(42,37,48,.5);opacity:0;visibility:hidden;transition:.3s;z-index:90}}
    .scrim.on{{opacity:1;visibility:visible}}
    .drawer{{position:fixed;top:0;right:0;height:100%;width:min(390px,92vw);background:var(--cream);z-index:100;
      transform:translateX(100%);transition:transform .3s;display:flex;flex-direction:column;border-left:1px solid var(--line)}}
    .drawer.on{{transform:none}}
    .drawer .dh{{display:flex;justify-content:space-between;align-items:center;padding:1.3rem 1.4rem;border-bottom:1px solid var(--line)}}
    .drawer .dh b{{font-family:"Fraunces",serif;font-size:1.3rem}}
    .drawer .close{{background:none;border:0;font-size:1.3rem;cursor:pointer;color:var(--ink)}}
    .drawer .ditems{{flex:1;overflow:auto;padding:1rem 1.4rem}}
    .di{{display:flex;gap:.9rem;padding:.9rem 0;border-bottom:1px dashed var(--line);align-items:center}}
    .di img{{width:56px;height:56px;object-fit:cover;flex:none}}
    .di .n{{font-family:"Fraunces",serif;font-size:1rem}}.di .meta{{font-size:.78rem;color:var(--ink-soft)}}
    .di .qty{{display:flex;align-items:center;gap:.5rem;margin-top:.2rem}}
    .di .qty button{{width:20px;height:20px;border:1px solid var(--line);background:var(--cream);cursor:pointer;line-height:1;font-size:.9rem}}
    .di .p{{margin-left:auto;font-family:"Fraunces",serif}}
    .drawer .df{{padding:1.2rem 1.4rem;border-top:1px solid var(--line)}}
    .drawer .sub{{display:flex;justify-content:space-between;margin-bottom:.4rem;font-size:.95rem}}
    .drawer .sub b{{font-family:"Fraunces",serif;font-size:1.25rem}}
    .drawer .note{{font-size:.74rem;color:var(--ink-soft);margin-bottom:.9rem}}
    .vh{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}
    footer.site{{border-top:1px solid var(--line);padding:2.4rem 0;margin-top:1rem}}
    .foot-copy{{display:flex;justify-content:space-between;color:var(--ink-soft);font-size:.8rem;flex-wrap:wrap;gap:.6rem}}
    @media(max-width:880px){{nav.main{{display:none}}.menu-btn{{display:block}}.pdp{{grid-template-columns:1fr;gap:1.6rem}}}}
  </style>
</head>
<body>
  <div class="strip">Edition One &nbsp;·&nbsp; Complimentary delivery across Orange County</div>

  <header class="site">
    <div class="site-inner">
      <a class="brand" href="../index.html">
        <img src="../assets/logo/horizon_hero_512.png" alt="OmniCompost mark" />
        <span class="word"><b>Omni</b><span>Compost</span></span>
      </a>
      <nav class="main">
        <a href="../index.html#product">The Digester</a>
        <a href="../shop.html">Shop</a>
        <a href="../index.html#how">How it works</a>
        <a href="../newsletter.html">Newsletter</a>
        <a href="../index.html#faq">Questions</a>
      </nav>
      <div style="display:flex;align-items:center;gap:1rem">
        <button class="cart-btn" id="cartBtn" aria-haspopup="dialog" aria-controls="drawer" aria-expanded="false" aria-label="Open cart">Cart (<b id="ct">0</b>)</button>
        <button class="menu-btn" aria-label="Menu"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>

  <div class="wrap crumb"><a href="../shop.html">Shop</a> &nbsp;/&nbsp; {name}</div>

  <main class="wrap">
    <article class="pdp">
      <div class="media">{badge}<img src="../{image}" alt="{alt}" /></div>
      <div class="info">
        <span class="cat">{cat_label}</span>
        <h1>{name}</h1>
        <div class="prate">{rating}</div>
        <span class="price">${price}</span>
        <p class="stockline">{stock}</p>
        <p class="desc">{desc}</p>
        <ul class="specs">
{specs}
        </ul>
        <div class="actions">
          {add_btn}
          <a class="back" href="../shop.html">← Back to the shop</a>
        </div>
      </div>
    </article>
  </main>

  <!-- CART DRAWER -->
  <div class="scrim" id="scrim"></div>
  <aside class="drawer" id="drawer" role="dialog" aria-modal="true" aria-label="Shopping cart" tabindex="-1">
    <div class="dh"><b>Your cart</b><button class="close" id="closeC" aria-label="Close cart">✕</button></div>
    <div class="ditems" id="ditems"><p style="color:var(--ink-soft);font-size:.9rem">Your cart is empty — add something from the shop.</p></div>
    <div class="df">
      <div class="sub"><span>Subtotal</span><b id="sub">$0</b></div>
      <p class="note">Complimentary delivery &amp; setup across Orange County.</p>
      <a href="../index.html#order" class="btn btn--solid" id="checkoutBtn" style="width:100%;text-align:center">Checkout</a>
    </div>
  </aside>
  <span class="vh" id="cartLive" role="status" aria-live="polite"></span>

  <footer class="site"><div class="wrap foot-copy">
    <span>© <span id="year"></span> OmniCompost</span>
    <span><a href="../index.html">Home</a> &nbsp;·&nbsp; <a href="../shop.html">Shop</a> &nbsp;·&nbsp; <a href="../newsletter.html">Newsletter</a></span>
  </div></footer>

  <script>
    document.getElementById('year').textContent=new Date().getFullYear();
    var mb=document.querySelector('.menu-btn'),nav=document.querySelector('nav.main');
    mb.addEventListener('click',function(){{var open=nav.style.display==='flex';nav.style.display=open?'':'flex';
      if(!open){{nav.style.position='absolute';nav.style.flexDirection='column';nav.style.top='100%';nav.style.right='0';nav.style.background='var(--cream)';nav.style.padding='1.2rem 2rem';nav.style.border='1px solid var(--line)';nav.style.gap='1rem';}}}});
  </script>
  <script src="../cart.js"></script>
</body>
</html>
"""


def product_page_html(product):
    """Return the full HTML for one product detail page."""
    badge = (
        '<span class="badge">{}</span>'.format(product["badge"])
        if product.get("badge")
        else ""
    )
    specs = "\n".join(
        "          <li>{}</li>".format(item) for item in product.get("details", [])
    )
    desc = product.get("desc") or product.get("blurb", "")
    meta = desc.replace('"', "&quot;")
    return PRODUCT_PAGE.format(
        name=product["name"],
        meta_desc=meta,
        badge=badge,
        image=product["image"],
        alt=product["alt"],
        cat_label=product["category"].capitalize(),
        rating=rating_html(product),
        price=money(product["price"]),
        stock=stock_html(product),
        desc=desc,
        specs=specs,
        add_btn=add_button(product, solid=True),
    )


def build_product_pages(products):
    """Write product/<slug>.html for every product."""
    if not os.path.isdir(PRODUCT_DIR):
        os.makedirs(PRODUCT_DIR)

    written = 0
    for product in products:
        path = os.path.join(PRODUCT_DIR, product["slug"] + ".html")
        html = product_page_html(product)
        existing = None
        if os.path.exists(path):
            with open(path, encoding="utf-8") as handle:
                existing = handle.read()
        if existing != html:
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(html)
            written += 1
    print("product pages: %d written, %d total" % (written, len(products)))


def main():
    with open(PRODUCTS_FILE, encoding="utf-8") as handle:
        products = json.load(handle)["products"]

    # index.html grid is indented 10 spaces; shop.html grid 6 spaces.
    update_shop_region(INDEX_FILE, products, card_indent=10, close_indent=10)
    update_shop_region(SHOP_FILE, products, card_indent=6, close_indent=6)
    build_product_pages(products)
    print("done -- %d product(s)" % len(products))


if __name__ == "__main__":
    main()
