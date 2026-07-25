# -*- coding: utf-8 -*-
import os, json, html
from data import (SITE_NAME, DOMAIN, FORM_ENDPOINT_EMAIL, SERVICES, PRODUCTS, FILTER_LIST,
                   PROJECTS, PROJECT_DETAILS, WHY_CARDS, TIMELINE_STEPS, VIDEOS, TESTIMONIALS, FAQS)

OUT = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(OUT, "images")

FONT_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
             '<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">')
# NOTE (fix): weights 300 & 900 removed — grep of the CSS showed they were never
# used (only 400/500/700/800 appear anywhere), so loading them was pure wasted bytes.

def img_size(name):
    """Return (w,h) for a generated image so we can emit real width/height attrs
    (fixes the audit's CLS finding: no image had explicit dimensions before)."""
    try:
        from PIL import Image
        with Image.open(os.path.join(IMAGES_DIR, name + ".webp")) as im:
            return im.size
    except Exception:
        return (800, 600)

_size_cache = {}
def dims(name):
    if name not in _size_cache:
        _size_cache[name] = img_size(name)
    return _size_cache[name]

def pic(name, alt, cls="", base="", extra=""):
    w, h = dims(name)
    cls_attr = f' class="{cls}"' if cls else ""
    src = f"{base}images/{name}.webp"
    return (f'<picture><source srcset="{src}" type="image/webp">'
            f'<img{cls_attr} src="{src}" alt="{html.escape(alt)}" width="{w}" height="{h}" '
            f'loading="lazy" decoding="async"{extra}></picture>')

def esc(s):
    return html.escape(s, quote=True)

# ------------------------------------------------------------------
# shared chrome: head / nav / mobile menu / footer / whatsapp / lightbox
# ------------------------------------------------------------------

def head_tags(title, description, canonical_path, base, og_image="images/hero.webp",
              json_ld=None, preload_hero=False, robots="index, follow"):
    canonical = f"{DOMAIN}/{canonical_path}"
    og_image_url = f"{DOMAIN}/images/{og_image.split('/')[-1]}"
    preload = f'<link rel="preload" as="image" href="{base}images/hero.webp">\n' if preload_hero else ""
    jsonld_block = f'<script type="application/ld+json">{json.dumps(json_ld, ensure_ascii=False)}</script>\n' if json_ld else ""
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" href="{base}favicon.png">
<link rel="apple-touch-icon" href="{base}favicon.png">
<!-- Open Graph / Twitter (fix: previously completely absent) -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(SITE_NAME)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{og_image_url}">
<meta property="og:locale" content="ar_AR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{og_image_url}">
<!-- CSP (fix: previously absent). Static site so the policy can be tight. -->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; script-src 'self'; frame-src https://www.google.com https://maps.google.com; form-action 'self' https://formsubmit.co; base-uri 'self';">
{preload}{FONT_LINK}
<link rel="stylesheet" href="{base}assets/style.css">
{jsonld_block}"""

def header_nav(base):
    return f"""<a class="skip-link" href="#main">تخطَّ إلى المحتوى</a>
<header id="nav">
  <div class="container nav-inner">
    <div class="logo">
      {pic("logo", "شعار خلف للخيزران", "logo-mark", base)}
      <div>خلف للخيزران<small>KHALAF BAMBOO · EST. 1929</small></div>
    </div>
    <nav class="nav-links">
      <a href="{base}index.html#hero">الرئيسية</a>
      <a href="{base}index.html#about">من نحن</a>
      <a href="{base}index.html#services">خدماتنا</a>
      <a href="{base}index.html#projects">مشاريعنا</a>
      <a href="{base}index.html#products">المنتجات</a>
      <a href="{base}index.html#testimonials">آراء العملاء</a>
      <a href="{base}index.html#contact">تواصل معنا</a>
    </nav>
    <a href="{base}index.html#contact" class="nav-cta">اطلب عرض سعر</a>
    <button class="burger" id="burgerBtn" aria-label="فتح القائمة" aria-expanded="false" aria-controls="mobileMenu"><span></span><span></span><span></span></button>
  </div>
</header>

<div class="mobile-menu" id="mobileMenu">
  <a href="{base}index.html#hero">الرئيسية</a>
  <a href="{base}index.html#about">من نحن</a>
  <a href="{base}index.html#services">خدماتنا</a>
  <a href="{base}index.html#projects">مشاريعنا</a>
  <a href="{base}index.html#products">المنتجات</a>
  <a href="{base}index.html#testimonials">آراء العملاء</a>
  <a href="{base}index.html#contact">تواصل معنا</a>
  <a href="{base}index.html#contact" class="nav-cta">اطلب عرض سعر</a>
</div>"""

def footer_html(base):
    return f"""<footer>
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">{pic("logo", "شعار خلف للخيزران", "", base)}خلف للخيزران</div>
        <p>حرفية خيزران أصيلة توارثتها أربعة أجيال منذ عام 1929. نصنع مساحات خارجية تدوم.</p>
      </div>
      <div class="footer-col">
        <h4>روابط سريعة</h4>
        <ul>
          <li><a href="{base}index.html#about">من نحن</a></li>
          <li><a href="{base}index.html#services">خدماتنا</a></li>
          <li><a href="{base}index.html#projects">مشاريعنا</a></li>
          <li><a href="{base}index.html#contact">تواصل معنا</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>تابعنا</h4>
        <ul>
          <li><a href="#">إنستغرام</a></li>
          <li><a href="#">فيسبوك</a></li>
          <li><a href="#">واتساب</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>ساعات العمل</h4>
        <ul>
          <li>السبت - الخميس: 9 ص - 6 م</li>
          <li>الجمعة: مغلق</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 خلف للخيزران. جميع الحقوق محفوظة.</span>
      <span class="lang-en" dir="ltr">Khalaf Bamboo — Since 1929</span>
    </div>
  </div>
</footer>

<a class="wa-fab" href="https://wa.me/970000000000" target="_blank" rel="noopener" aria-label="تواصل عبر واتساب">
  {pic("icon-whatsapp", "واتساب", "", base)}
</a>

<div class="lightbox" id="lightbox">
  <button class="lightbox-close" id="lightboxClose" aria-label="إغلاق">{pic("icon-close", "إغلاق", "", base)}</button>
  <div class="lightbox-content" id="lightboxContent"></div>
</div>

<script src="{base}assets/app.js"></script>"""

def page(title, description, canonical_path, body, base="", og_image="images/hero.webp",
         json_ld=None, preload_hero=False, extra_body_class="", main_class=""):
    main_attr = f' class="{main_class}"' if main_class else ""
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
{head_tags(title, description, canonical_path, base, og_image, json_ld, preload_hero)}
</head>
<body{f' class="{extra_body_class}"' if extra_body_class else ""}>
{header_nav(base)}
<main id="main" tabindex="-1"{main_attr}>
{body}
</main>
{footer_html(base)}
</body>
</html>
"""

# ------------------------------------------------------------------
# reusable content-card renderers
# ------------------------------------------------------------------

def svc_card(s):
    return f"""<div class="svc-card">
    <div class="svc-media">{pic(s['img'], s['t'])}</div>
    <div class="svc-body">
      <h3>{s['t']}</h3><p>{s['d']}</p>
      <a href="category/{s['slug']}.html" class="svc-link">اعرف أكثر {pic('icon-arrow','')}</a>
    </div>
  </div>"""

def proj_card(p):
    return f"""<div class="proj-card" data-cat="{p['cat']}" data-href="project/{p['slug']}.html">
    <div class="proj-media">{pic(p['img'], p['t'])}<span class="proj-tag">{p['cat']}</span></div>
    <div class="proj-info"><h3>{p['t']}</h3><div class="loc">{p['loc']}</div><p>{p['d']}</p><span class="proj-btn">عرض المشروع {pic('icon-arrow','')}</span></div>
  </div>"""

def product_card_home(p, svc_title):
    return f"""<div class="prod-card">
    <div class="prod-media">{pic(p['img'], p['t'])}</div>
    <div class="prod-body"><h3>{p['t']}</h3><p>{p['d']}</p><a href="product/{p['id']}.html" class="prod-btn">التفاصيل والسعر</a></div>
  </div>"""

def why_card(w):
    return f"""<div class="why-card">
    {pic(w['icon'], w['t'], 'why-icon')}
    <h3>{w['t']}</h3>
    <p>{w['d']}</p>
  </div>"""

def video_card(v):
    return f"""<div class="vid-card" data-lightbox-src="images/{v['img']}.webp" data-lightbox-alt="{esc(v['t'])}" style="cursor:pointer">
    {pic(v['img'], v['t'], 'bg')}
    <div class="vid-overlay"><div class="vid-play">{pic('icon-play','تشغيل')}</div><span>{v['t']}</span></div>
  </div>"""

def testi_card(t):
    stars = "".join(pic('icon-star','') for _ in range(5))
    return f"""<div class="testi-card">
    {pic('icon-quote','', 'testi-quote')}
    <div class="testi-stars">{stars}</div>
    <p>&quot;{t['q']}&quot;</p>
    <div class="testi-person"><div class="testi-avatar">{t['n'][0]}</div><div><h4>{t['n']}</h4><span>{t['role']}</span></div></div>
  </div>"""

def faq_item(f, i):
    open_cls = " open" if i == 0 else ""
    style = ' style="max-height:200px"' if i == 0 else ""
    return f"""<div class="faq-item{open_cls}">
    <button class="faq-q" aria-expanded="{'true' if i==0 else 'false'}">{f['q']}{pic('icon-plus','')}</button>
    <div class="faq-a"{style}><p>{f['a']}</p></div>
  </div>"""

def timeline_step(s, i, total):
    connector = '<div class="tl-connector"></div>' if i < total - 1 else ""
    return f"""<div class="tl-step">
    <div class="tl-ring-col">
      <div class="tl-ring">{pic('icon-ring','')}<span class="n num">{i+1}</span></div>
      {connector}
    </div>
    <div class="tl-body"><h3>{s['t']}</h3><p>{s['d']}</p></div>
  </div>"""

print("templates module loaded OK")
