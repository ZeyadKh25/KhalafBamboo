# -*- coding: utf-8 -*-
import os
from data import (SITE_NAME, DOMAIN, FORM_ENDPOINT_EMAIL, SERVICES, PRODUCTS, FILTER_LIST,
                   PROJECTS, PROJECT_DETAILS, WHY_CARDS, TIMELINE_STEPS, VIDEOS, TESTIMONIALS, FAQS)
from templates import (pic, page, svc_card, proj_card, product_card_home, why_card,
                        video_card, testi_card, faq_item, timeline_step, esc)

OUT = os.path.dirname(os.path.abspath(__file__))

def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

# ==========================================================================
# HOMEPAGE
# ==========================================================================

def build_homepage():
    hero = """<section class="hero" id="hero">
  <div class="container hero-inner">
    <div>
      <div class="hero-badge"><b class="num">1929</b> — إرث حرفي يمتد لأكثر من تسعة عقود</div>
      <h1>أثاث خيزران مصنوع يدويًا<br><em>منذ عام 1929</em></h1>
      <p class="lead">نصمم وننتج أثاث الخيزران الفاخر المخصص، البرجولات، الغرف الصيفية، الستائر والخزائن، وحلول الأجواء الخارجية المصممة خصيصًا لأسلوبك.</p>
      <div class="hero-ctas">
        <a href="#contact" class="btn btn-primary">اطلب عرض سعر مجاني</a>
        <a href="#projects" class="btn btn-ghost">استكشف مشاريعنا</a>
      </div>
      <div class="hero-features">
        <div class="hero-feature">""" + pic("icon-hero-handmade", "صناعة يدوية") + """صناعة يدوية</div>
        <div class="hero-feature">""" + pic("icon-hero-custom", "تصاميم مخصصة") + """تصاميم مخصصة</div>
        <div class="hero-feature">""" + pic("icon-hero-premium", "خامات فاخرة") + """خامات فاخرة</div>
      </div>
    </div>
    <div class="hero-visual">
      <div class="hero-panel hp1">""" + pic("hero-panel-1", "طقم خيزران فاخر") + """</div>
      <div class="hero-panel hp2">""" + pic("hero-panel-2", "تفاصيل نسيج الخيزران") + """</div>
    </div>
  </div>
  <div class="hero-scroll"><span>مرر للأسفل</span><span class="line"></span></div>
</section>"""

    why = """<section class="why" id="why">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">لماذا خلف للخيزران</span>
      <h2 class="section-title">حرفية لا يمكن استنساخها</h2>
      <p class="section-sub">كل ما نصنعه يحمل ختم عائلة عملت بالخيزران منذ ما يقارب القرن.</p>
    </div>
  </div>
  <div class="container">
    <div class="why-grid reveal-stag">
      """ + "\n      ".join(why_card(w) for w in WHY_CARDS) + """
    </div>
  </div>
</section>"""

    services = """<section class="services" id="services">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">خدماتنا</span>
      <h2 class="section-title">من الفكرة إلى المساحة المُنجزة</h2>
      <p class="section-sub">مجموعة متكاملة من حلول الخيزران للمنازل، الفلل، المقاهي، المطاعم، والفنادق.</p>
    </div>
    <div class="svc-grid reveal-stag">
      """ + "\n      ".join(svc_card(s) for s in SERVICES) + """
    </div>
  </div>
</section>"""

    projects_section = """<section class="projects" id="projects">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">معرض الأعمال</span>
      <h2 class="section-title">مشاريع تحمل بصمتنا</h2>
      <p class="section-sub">مجموعة مختارة من المشاريع المنجزة لعملائنا من المنازل والفلل إلى المطاعم والمنتجعات.</p>
    </div>
    <div class="filters" id="filters">
      """ + "\n      ".join(f'<button class="filter-btn{" active" if f=="الكل" else ""}" data-f="{f}">{f}</button>' for f in FILTER_LIST) + """
    </div>
    <div class="proj-grid" id="projGrid">
      """ + "\n      ".join(proj_card(p) for p in PROJECTS) + """
    </div>
  </div>
</section>"""

    products_section = """<section class="products" id="products">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">الأكثر طلبًا</span>
      <h2 class="section-title">المنتجات الأكثر شعبية</h2>
      <p class="section-sub">القطع التي يختارها عملاؤنا الأكثر، جاهزة للتخصيص حسب مساحتك.</p>
    </div>
    <div class="prod-grid">
      """ + "\n      ".join(product_card_home(p, "") for p in PRODUCTS[:4]) + """
    </div>
  </div>
</section>"""

    beforeafter = """<section class="ba" id="beforeafter">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">قبل وبعد</span>
      <h2 class="section-title">شاهد التحوّل بنفسك</h2>
      <p class="section-sub">اسحب الفاصل لمقارنة المساحة قبل وبعد تدخل خلف للخيزران.</p>
    </div>
    <div class="ba-wrap reveal">
      <div class="ba-slider" id="baSlider">
        <div class="ba-before">""" + pic("before", "المساحة قبل التنفيذ") + """<span class="ba-label">قبل</span></div>
        <div class="ba-after">""" + pic("after", "المساحة بعد التنفيذ") + """<span class="ba-label">بعد</span></div>
        <div class="ba-handle" id="baHandle">""" + pic("icon-drag", "مقارنة قبل وبعد") + """</div>
      </div>
      <p class="ba-caption">جلسة حديقة خارجية — تحويل كامل خلال 12 يوم عمل</p>
    </div>
  </div>
</section>"""

    how = """<section class="how" id="how">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">آلية العمل</span>
      <h2 class="section-title">رحلتك معنا خطوة بخطوة</h2>
      <p class="section-sub">من أول اتصال إلى تسليم مشروعك، نرافقك في كل مرحلة بدقة وشفافية.</p>
    </div>
    <div class="timeline reveal">
      """ + "\n      ".join(timeline_step(s, i, len(TIMELINE_STEPS)) for i, s in enumerate(TIMELINE_STEPS)) + """
    </div>
  </div>
</section>"""

    videos = """<section class="videos" id="videos">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">لمحة مصورة</span>
      <h2 class="section-title">شاهد الحرفة تتشكل</h2>
      <p class="section-sub">من الورشة إلى موقع التركيب، إليك خلف الكواليس.</p>
    </div>
    <div class="vid-grid reveal-stag">
      """ + "\n      ".join(video_card(v) for v in VIDEOS) + """
    </div>
  </div>
</section>"""

    about = """<section class="about" id="about">
  <div class="container about-grid">
    <div class="about-art reveal">
      """ + pic("about", "ورشة خلف للخيزران منذ 1929") + """
      <span class="about-year-badge num">1929</span>
    </div>
    <div class="about-copy reveal">
      <span class="eyebrow">من نحن</span>
      <h2 class="section-title">قصة يد… بدأت بعام 1929</h2>
      <p>منذ ما يقارب القرن، والقصة لم تكن يومًا مجرد صناعة أثاث. بل هي حكاية <b>شغف وإرث عائلي</b> يتوارثه جيل بعد جيل. في كل قطعة نصنعها، تأخذ ألياف الخيزران الطبيعي طريقها لتنسج قصة تجمع بين عراقة الماضي وأناقة الحاضر.</p>
      <p>نحن أكثر من متجر أثاث؛ نحن <b>إرث عائلي</b> يمتد عبر الأجيال. نمزج بين أصالة الحرفة التقليدية وتصاميم عصرية تلبي أسلوب الحياة اليوم، لتبقى قطعنا جزءًا من منازلكم لسنوات طويلة.</p>
      <div class="about-highlights">
        <div class="ah-item"><h4>عمل عائلي</h4><p>أربعة أجيال من الحرفيين توارثوا المهنة والشغف.</p></div>
        <div class="ah-item"><h4>عقود من الخبرة</h4><p>خبرة متراكمة منذ 1929 حتى اليوم.</p></div>
        <div class="ah-item"><h4>تقليد وحداثة</h4><p>حرفية تقليدية بلمسات تصميم عصرية.</p></div>
      </div>
    </div>
  </div>
</section>"""

    stats = """<section class="stats" id="stats">
  <div class="container">
    <div class="stats-grid reveal-stag">
      <div class="stat"><div class="num" data-count="95">0</div><p>مشروع خارجي</p></div>
      <div class="stat"><div class="num" data-count="300">0</div><p>برجولة منجزة</p></div>
      <div class="stat"><div class="num" data-count="400">0</div><p>ستارة خيزران</p></div>
      <div class="stat"><div class="num">آلاف</div><p>عميل راضٍ عن الخدمة</p></div>
    </div>
  </div>
</section>"""

    testimonials = """<section class="testi" id="testimonials">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">آراء العملاء</span>
      <h2 class="section-title">ثقة نبنيها قطعة بقطعة</h2>
    </div>
    <div class="testi-grid reveal-stag">
      """ + "\n      ".join(testi_card(t) for t in TESTIMONIALS) + """
    </div>
  </div>
</section>"""

    faq = """<section class="faq" id="faq">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">الأسئلة الشائعة</span>
      <h2 class="section-title">كل ما تريد معرفته</h2>
    </div>
    <div class="faq-wrap reveal">
      """ + "\n      ".join(faq_item(f, i) for i, f in enumerate(FAQS)) + """
    </div>
  </div>
</section>"""

    final_cta = """<section class="final-cta">
  """ + pic("texture-bamboo", "", "cta-bamboo-art") + """
  <div class="container reveal" style="position:relative;z-index:2;">
    <span class="eyebrow" style="color:var(--bronze-light);justify-content:center;">جاهزون لمشروعك</span>
    <h2>لنبنِ معًا مساحتك الخارجية التي تحلم بها.</h2>
    <p>فريقنا جاهز لتحويل فكرتك إلى قطعة خيزران فاخرة تدوم لأجيال.</p>
    <a href="#contact" class="btn btn-primary">اطلب عرض سعرك المجاني</a>
  </div>
</section>"""

    # form: real POST to FormSubmit + honeypot + subject + redirect (fixes audit #1 critical finding)
    contact = f"""<section class="contact" id="contact">
  <div class="container contact-grid">
    <div class="contact-info reveal">
      <span class="eyebrow">تواصل معنا</span>
      <h2 class="section-title" style="margin-bottom:30px;">لنبدأ حديثنا</h2>
      <div class="info-row">{pic("icon-phone","هاتف")}<div><h4>واتساب / هاتف</h4><p><a href="tel:+970000000000" class="lang-en" dir="ltr">+970 00 000 0000</a></p></div></div>
      <div class="info-row">{pic("icon-email","البريد الإلكتروني")}<div><h4>البريد الإلكتروني</h4><p><a href="mailto:info@khalafbamboo.com" class="lang-en" dir="ltr">info@khalafbamboo.com</a></p></div></div>
      <div class="info-row">{pic("icon-location","العنوان")}<div><h4>العنوان</h4><p>مدينة غزة، فلسطين</p></div></div>
      <div class="social-row">
        <a href="#" aria-label="Instagram">{pic("icon-instagram","Instagram")}</a>
        <a href="#" aria-label="Facebook">{pic("icon-facebook","Facebook")}</a>
      </div>
      <div class="map-embed"><iframe src="https://maps.google.com/maps?q=Gaza%20City&t=&z=12&ie=UTF8&iwloc=&output=embed" loading="lazy" title="خريطة الموقع" sandbox="allow-scripts allow-same-origin allow-popups" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
    </div>

    <form class="form-card reveal" id="quoteForm" action="https://formsubmit.co/{FORM_ENDPOINT_EMAIL}" method="POST">
      <h3>اطلب عرض سعر مجاني</h3>
      <p>عبّئ النموذج وسيتواصل فريقنا معك خلال 24 ساعة.</p>
      <input type="hidden" name="_subject" value="طلب عرض سعر جديد — موقع خلف للخيزران">
      <input type="hidden" name="_next" value="{DOMAIN}/thank-you.html">
      <input type="hidden" name="_captcha" value="true">
      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
      <div class="form-grid">
        <div class="field"><label for="f-name">الاسم الكامل</label><input id="f-name" name="الاسم" type="text" placeholder="اسمك" required></div>
        <div class="field"><label for="f-phone">رقم الهاتف</label><input id="f-phone" name="الهاتف" type="tel" placeholder="05xxxxxxxx" required></div>
        <div class="field"><label for="f-city">المدينة</label><input id="f-city" name="المدينة" type="text" placeholder="مدينتك"></div>
        <div class="field">
          <label for="f-type">نوع المشروع</label>
          <select id="f-type" name="نوع المشروع"><option>أثاث خارجي</option><option>برجولة</option><option>غرفة صيفية</option><option>ستائر خيزران</option><option>خزائن خيزران</option><option>مشروع مخصص</option></select>
        </div>
        <div class="field"><label for="f-dim">الأبعاد التقريبية</label><input id="f-dim" name="الأبعاد" type="text" placeholder="مثال: 4×5 متر"></div>
        <div class="field">
          <label for="f-budget">الميزانية التقديرية</label>
          <select id="f-budget" name="الميزانية"><option>أقل من 1000$</option><option>1000$ - 3000$</option><option>3000$ - 7000$</option><option>أكثر من 7000$</option></select>
        </div>
        <div class="field full">
          <label for="f-desc">وصف المشروع</label>
          <textarea id="f-desc" name="وصف المشروع" rows="4" placeholder="أخبرنا المزيد عن فكرتك..."></textarea>
        </div>
      </div>
      <button type="submit" class="form-submit">إرسال الطلب</button>
    </form>
  </div>
</section>"""

    body = "\n".join([hero, why, services, projects_section, products_section, beforeafter,
                      how, videos, about, stats, testimonials, faq, final_cta, contact])

    json_ld = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "خلف للخيزران",
        "alternateName": "Khalaf Bamboo",
        "description": "شركة عائلية متخصصة بتصميم وتصنيع أثاث الخيزران الفاخر المخصص منذ عام 1929: أثاث خارجي، برجولات، غرف صيفية، ستائر وخزائن خيزران.",
        "foundingDate": "1929",
        "url": DOMAIN + "/",
        "image": DOMAIN + "/images/hero.webp",
        "address": {"@type": "PostalAddress", "addressLocality": "غزة", "addressCountry": "PS"},
        "sameAs": []
    }

    html_out = page(
        title="خلف للخيزران | أثاث خيزران فاخر منذ 1929",
        description="خلف للخيزران — نصمم وننتج أثاث الخيزران الفاخر المخصص، البرجولات، الغرف الصيفية والستائر منذ عام 1929. حرفية يدوية، خامات فاخرة، ومتانة تدوم لسنوات.",
        canonical_path="",
        body=body,
        base="",
        json_ld=json_ld,
        preload_hero=True,
    )
    write("index.html", html_out)

build_homepage()
print("homepage built OK")

# ==========================================================================
# CATEGORY PAGES  (category/<slug>.html)
# ==========================================================================

def build_category_pages():
    for cat in SERVICES:
        items = [p for p in PRODUCTS if p["cat"] == cat["slug"]]
        cards = "\n      ".join(f"""<div class="prod-card">
        <div class="prod-media">{pic(p['img'], p['t'], base='../')}</div>
        <div class="prod-body"><h3>{p['t']}</h3><p>{p['d']}</p><a href="../product/{p['id']}.html" class="prod-btn">عرض التفاصيل والسعر</a></div>
      </div>""" for p in items)

        body = f"""<div class="container">
<a href="../index.html#services" class="back-link">{pic('icon-arrow','', base='../')} العودة إلى الخدمات</a>
<div class="breadcrumb"><a href="../index.html">الرئيسية</a><span class="sep">/</span><a href="../index.html#services">خدماتنا</a><span class="sep">/</span><span class="current">{cat['t']}</span></div>
<div class="cat-hero">
  <div class="cat-hero-media">{pic(cat['img'], cat['t'], base='../')}</div>
  <div class="cat-hero-copy"><h1>{cat['t']}</h1><p>{cat['d']}</p></div>
</div>
<div class="prod-grid">
  {cards}
</div>
</div>"""

        json_ld = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "الرئيسية", "item": DOMAIN + "/"},
                {"@type": "ListItem", "position": 2, "name": "خدماتنا", "item": DOMAIN + "/index.html#services"},
                {"@type": "ListItem", "position": 3, "name": cat["t"], "item": f"{DOMAIN}/category/{cat['slug']}.html"},
            ]
        }

        html_out = page(
            title=f"{cat['t']} — خلف للخيزران",
            description=cat["meta"],
            canonical_path=f"category/{cat['slug']}.html",
            body=body,
            base="../",
            og_image=f"images/{cat['img']}.webp",
            json_ld=json_ld,
            main_class="cat-page",
        )
        write(f"category/{cat['slug']}.html", html_out)
    print(f"built {len(SERVICES)} category pages OK")

build_category_pages()

# ==========================================================================
# PRODUCT PAGES  (product/<id>.html)
# ==========================================================================

def build_product_pages():
    cat_by_slug = {c["slug"]: c for c in SERVICES}
    for p in PRODUCTS:
        cat = cat_by_slug[p["cat"]]
        specs_rows = "\n          ".join(f'<div class="pd-spec-row"><span>{k}</span><span>{v}</span></div>' for k, v in p["specs"].items())

        body = f"""<div class="container">
<a href="../category/{p['cat']}.html" class="back-link">{pic('icon-arrow','', base='../')} العودة إلى {cat['t']}</a>
<div class="breadcrumb"><a href="../index.html">الرئيسية</a><span class="sep">/</span><a href="../category/{p['cat']}.html">{cat['t']}</a><span class="sep">/</span><span class="current">{p['t']}</span></div>
<div class="pd-grid">
  <div class="pd-gallery-main">{pic(p['img'], p['t'], base='../')}</div>
  <div>
    <span class="pd-eyebrow">{cat['t']}</span>
    <h1 class="pd-title">{p['t']}</h1>
    <div class="pd-price num">{p['price']}</div>
    <p class="pd-desc">{p['d']}</p>
    <div class="pd-specs">
      {specs_rows}
    </div>
    <div class="pd-ctas">
      <a href="../index.html#contact" class="btn btn-dark">اطلب عرض سعر لهذا المنتج</a>
      <a href="../category/{p['cat']}.html" class="btn btn-outline-dark">تصفح المزيد من {cat['t']}</a>
    </div>
  </div>
</div>
</div>"""

        json_ld = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": p["t"],
            "description": p["d"],
            "image": f"{DOMAIN}/images/{p['img']}.webp",
            "category": cat["t"],
            "brand": {"@type": "Brand", "name": "خلف للخيزران"},
            "offers": {"@type": "Offer", "priceCurrency": "USD", "availability": "https://schema.org/InStock",
                       "url": f"{DOMAIN}/product/{p['id']}.html"},
        }

        html_out = page(
            title=f"{p['t']} | {cat['t']} — خلف للخيزران",
            description=p["d"][:155],
            canonical_path=f"product/{p['id']}.html",
            body=body,
            base="../",
            og_image=f"images/{p['img']}.webp",
            json_ld=json_ld,
            main_class="cat-page",
        )
        write(f"product/{p['id']}.html", html_out)
    print(f"built {len(PRODUCTS)} product pages OK")

build_product_pages()

# ==========================================================================
# PROJECT PAGES  (project/<slug>.html)
# ==========================================================================

def build_project_pages():
    for p in PROJECTS:
        det = PROJECT_DETAILS.get(p["slug"], {})
        g1, g2, g3 = p["img"], f"{p['img']}-2", f"{p['img']}-3"

        def gallery_link(name, alt):
            w, h = 700, 520
            return (f'<a href="#" data-lightbox-src="../images/{name}.webp" data-lightbox-alt="{esc(alt)}">'
                    f'{pic(name, alt, base="../")}</a>')

        phases = det.get("phases", [])
        phases_html = []
        for i, ph in enumerate(phases):
            line = '<div class="prj-phase-line"></div>' if i < len(phases) - 1 else ""
            phases_html.append(f"""<div class="prj-phase">
        <div><div class="prj-phase-num">{i+1}</div>{line}</div>
        <div class="prj-phase-body"><h4>{ph['t']}</h4><p>{ph['d']}</p></div>
      </div>""")
        phases_block = "\n      ".join(phases_html)
        materials_block = "\n          ".join(f"<li>{m}</li>" for m in det.get("materials", []))

        body = f"""<div class="container">
<a href="../index.html#projects" class="back-link">{pic('icon-arrow','', base='../')} العودة إلى معرض الأعمال</a>
<div class="breadcrumb"><a href="../index.html">الرئيسية</a><span class="sep">/</span><a href="../index.html#projects">معرض الأعمال</a><span class="sep">/</span><span class="current">{p['t']}</span></div>

<span class="eyebrow">{p['cat']}</span>
<h1 class="section-title" style="margin-bottom:10px;">{p['t']}</h1>
<p class="section-sub" style="margin-bottom:34px;">{p['d']}</p>

<div class="prj-gallery">
  {gallery_link(g1, p['t'])}
  {gallery_link(g2, p['t'] + ' - 2')}
  {gallery_link(g3, p['t'] + ' - 3')}
</div>

<div class="prj-layout">
  <div class="prj-body">
    <div class="prj-meta">
      <div><h4>الموقع</h4><p>{det.get('location', p['loc'])}</p></div>
      <div><h4>مدة التنفيذ</h4><p>{det.get('duration','—')}</p></div>
      <div><h4>المساحة</h4><p>{det.get('area','—')}</p></div>
      <div><h4>التصنيف</h4><p>{det.get('category', p['cat'])}</p></div>
    </div>

    <h3 class="prj-section-title">كيف تعاملنا مع صاحب المشروع</h3>
    <p>{det.get('story','')}</p>

    <h3 class="prj-section-title">مراحل تنفيذ المشروع</h3>
    <div class="prj-phases">
      {phases_block}
    </div>
  </div>

  <div>
    <div class="prj-side-card prj-testimonial">
      <h4>رأي صاحب المشروع</h4>
      <p>&quot;{det.get('testiQ','')}&quot;</p>
      <div class="who">{det.get('testiN','')}</div>
    </div>
    <div class="prj-side-card">
      <h4>الخامات المستخدمة</h4>
      <ul class="prj-materials">
          {materials_block}
      </ul>
    </div>
    <a href="../index.html#contact" class="btn btn-primary" style="width:100%; justify-content:center;">اطلب مشروعًا مشابهًا</a>
  </div>
</div>
</div>"""

        json_ld = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "الرئيسية", "item": DOMAIN + "/"},
                {"@type": "ListItem", "position": 2, "name": "معرض الأعمال", "item": DOMAIN + "/index.html#projects"},
                {"@type": "ListItem", "position": 3, "name": p["t"], "item": f"{DOMAIN}/project/{p['slug']}.html"},
            ]
        }

        html_out = page(
            title=f"{p['t']} | معرض الأعمال — خلف للخيزران",
            description=p["d"],
            canonical_path=f"project/{p['slug']}.html",
            body=body,
            base="../",
            og_image=f"images/{p['img']}.webp",
            json_ld=json_ld,
            main_class="cat-page",
        )
        write(f"project/{p['slug']}.html", html_out)
    print(f"built {len(PROJECTS)} project pages OK")

build_project_pages()

# ==========================================================================
# thank-you.html (FormSubmit redirect target)
# ==========================================================================

def build_thank_you():
    body = """<section class="cat-page" style="text-align:center; padding-top:180px;">
  <div class="container">
    <span class="eyebrow" style="justify-content:center;">تم الإرسال</span>
    <h1 class="section-title">شكرًا لتواصلك معنا!</h1>
    <p class="section-sub" style="margin:0 auto 30px;">استلمنا طلبك بنجاح، وسيتواصل معك فريقنا خلال 24 ساعة لمناقشة تفاصيل مشروعك.</p>
    <a href="index.html" class="btn btn-dark">العودة إلى الموقع</a>
  </div>
</section>"""
    html_out = page(
        title="تم استلام طلبك — خلف للخيزران",
        description="شكرًا لتواصلك مع خلف للخيزران، سيتواصل معك فريقنا قريبًا.",
        canonical_path="thank-you.html",
        body=body,
        base="",
    )
    write("thank-you.html", html_out)

build_thank_you()
print("thank-you page built OK")

# ==========================================================================
# robots.txt + sitemap.xml  (fix: previously absent entirely; now lists
# every REAL crawlable URL, which only exists because of the move away
# from hash-based routing)
# ==========================================================================

def build_seo_files():
    urls = ["", "thank-you.html"]
    urls += [f"category/{c['slug']}.html" for c in SERVICES]
    urls += [f"product/{p['id']}.html" for p in PRODUCTS]
    urls += [f"project/{p['slug']}.html" for p in PROJECTS]

    sitemap_entries = "\n".join(
        f"  <url><loc>{DOMAIN}/{u}</loc></url>" for u in urls
    )
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_entries}
</urlset>
"""
    write("sitemap.xml", sitemap)

    robots = f"""User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""
    write("robots.txt", robots)
    print(f"sitemap.xml written with {len(urls)} real URLs, robots.txt written")

build_seo_files()

