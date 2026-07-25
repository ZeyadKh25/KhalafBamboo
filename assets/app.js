/* ============================================================
   خلف للخيزران — shared site JS
   NOTE on architecture: this file intentionally contains almost
   no innerHTML-based content rendering. Every page's real content
   (services, products, projects, FAQ, testimonials...) is written
   directly in that page's HTML at build time. This file only
   handles UI *behavior* (menus, accordions, sliders, a modal).
   That fixes the "innerHTML-injected content = latent XSS surface"
   finding from the audit: there is no user data flowing into any
   innerHTML call anywhere in this file.
   ============================================================ */

/* ===== skip-link (fix: #main had no tabindex, so the browser scrolled but never
   actually moved keyboard focus there — the link visually "did nothing"). We add
   tabindex="-1" in the HTML *and* force focus() here, since some browsers don't
   reliably focus a hash target even when it is focusable. ===== */
(function(){
  const skip = document.querySelector('.skip-link');
  const mainEl = document.getElementById('main');
  if(!skip || !mainEl) return;
  skip.addEventListener('click', (e)=>{
    e.preventDefault();
    mainEl.focus();
    mainEl.scrollIntoView({behavior:'smooth', block:'start'});
  });
})();

/* ===== NAV scroll state (passive listener = perf fix) ===== */
(function(){
  const navEl = document.getElementById('nav');
  if(!navEl) return;
  window.addEventListener('scroll', ()=>{
    navEl.classList.toggle('scrolled', window.scrollY > 40);
  }, {passive:true});
})();

/* ===== mobile menu (a11y fix: aria-expanded, Escape to close, focus handling) ===== */
(function(){
  const burger = document.getElementById('burgerBtn');
  const mobileMenu = document.getElementById('mobileMenu');
  if(!burger || !mobileMenu) return;

  function openMenu(){
    mobileMenu.classList.add('open');
    burger.setAttribute('aria-expanded','true');
    const firstLink = mobileMenu.querySelector('a');
    if(firstLink) firstLink.focus();
  }
  function closeMenu(returnFocus){
    mobileMenu.classList.remove('open');
    burger.setAttribute('aria-expanded','false');
    if(returnFocus) burger.focus();
  }
  burger.addEventListener('click', ()=>{
    mobileMenu.classList.contains('open') ? closeMenu(true) : openMenu();
  });
  mobileMenu.querySelectorAll('a').forEach(a=>a.addEventListener('click', ()=>closeMenu(false)));
  document.addEventListener('keydown', (e)=>{
    if(e.key === 'Escape' && mobileMenu.classList.contains('open')) closeMenu(true);
  });
})();

/* ===== reveal on scroll ===== */
(function(){
  const revealEls = document.querySelectorAll('.reveal, .reveal-stag');
  if(!revealEls.length) return;
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} });
  },{threshold:.15});
  revealEls.forEach(el=>io.observe(el));
})();

/* ===== project filter (homepage only) — toggles pre-rendered cards, no re-render/innerHTML ===== */
(function(){
  const filters = document.getElementById('filters');
  if(!filters) return;
  filters.addEventListener('click', (e)=>{
    const btn = e.target.closest('.filter-btn');
    if(!btn) return;
    filters.querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    const f = btn.dataset.f;
    document.querySelectorAll('#projGrid .proj-card').forEach(card=>{
      const show = (f === 'الكل' || card.dataset.cat === f);
      card.style.display = show ? '' : 'none';
    });
  });
  document.querySelectorAll('#projGrid .proj-card').forEach(card=>{
    card.addEventListener('click', ()=>{ window.location.href = card.dataset.href; });
    card.style.cursor = 'pointer';
  });
})();

/* ===== before/after slider (homepage only) — drag listener now attached/detached dynamically
   instead of a permanent window-level pointermove (perf fix from the audit) ===== */
(function(){
  const baSlider = document.getElementById('baSlider');
  const baHandle = document.getElementById('baHandle');
  if(!baSlider || !baHandle) return;
  const baAfter = baSlider.querySelector('.ba-after');

  function setSlide(x){
    const rect = baSlider.getBoundingClientRect();
    let pct = ((x - rect.left) / rect.width) * 100;
    pct = Math.max(4, Math.min(96, pct));
    baAfter.style.clipPath = `inset(0 ${100-pct}% 0 0)`;
    baHandle.style.right = `${100-pct}%`;
  }
  function onMove(e){ setSlide(e.clientX); }
  function onUp(){
    window.removeEventListener('pointermove', onMove);
    window.removeEventListener('pointerup', onUp);
  }
  baHandle.addEventListener('pointerdown', ()=>{
    window.addEventListener('pointermove', onMove);
    window.addEventListener('pointerup', onUp);
  });
  baSlider.addEventListener('click', (e)=> setSlide(e.clientX));
})();

/* ===== stats counter (homepage only) — requestAnimationFrame instead of setInterval (perf fix) ===== */
(function(){
  const statNums = document.querySelectorAll('.stat .num[data-count]');
  if(!statNums.length) return;
  const statIO = new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
      if(!entry.isIntersecting) return;
      const el = entry.target;
      const target = +el.dataset.count;
      const duration = 1400;
      let start = null;
      function tick(ts){
        if(start === null) start = ts;
        const progress = Math.min(1, (ts - start) / duration);
        el.textContent = Math.round(progress * target) + "+";
        if(progress < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
      statIO.unobserve(el);
    });
  },{threshold:.5});
  statNums.forEach(el=>statIO.observe(el));
})();

/* ===== FAQ accordion (static markup, just toggles classes) ===== */
(function(){
  const items = document.querySelectorAll('.faq-item');
  if(!items.length) return;
  items.forEach(item=>{
    const btn = item.querySelector('.faq-q');
    const a = item.querySelector('.faq-a');
    btn.addEventListener('click', ()=>{
      const isOpen = item.classList.contains('open');
      items.forEach(o=>{ o.classList.remove('open'); o.querySelector('.faq-a').style.maxHeight = null; o.querySelector('.faq-q').setAttribute('aria-expanded','false'); });
      if(!isOpen){ item.classList.add('open'); a.style.maxHeight = a.scrollHeight + "px"; btn.setAttribute('aria-expanded','true'); }
    });
  });
})();

/* ===== lightbox (a11y fix: role=dialog/aria-modal, Escape closes, focus is trapped + restored) ===== */
(function(){
  const lightbox = document.getElementById('lightbox');
  if(!lightbox) return;
  const lightboxContent = document.getElementById('lightboxContent');
  const closeBtn = document.getElementById('lightboxClose');
  let lastFocused = null;

  function openLightbox(src, alt){
    lastFocused = document.activeElement;
    lightboxContent.innerHTML = `<img src="${src}" alt="${alt || ''}" loading="lazy" decoding="async">`;
    lightbox.classList.add('open');
    lightbox.setAttribute('role','dialog');
    lightbox.setAttribute('aria-modal','true');
    closeBtn.focus();
    document.addEventListener('keydown', trapKey);
  }
  function closeLightbox(){
    lightbox.classList.remove('open');
    document.removeEventListener('keydown', trapKey);
    if(lastFocused) lastFocused.focus();
  }
  function trapKey(e){
    if(e.key === 'Escape'){ closeLightbox(); return; }
    if(e.key === 'Tab'){
      // single focusable element (close button) while open -> keep focus locked on it
      e.preventDefault();
      closeBtn.focus();
    }
  }
  closeBtn.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e)=>{ if(e.target === lightbox) closeLightbox(); });

  // event delegation: any element with data-lightbox-src opens the modal (used by
  // project galleries and video grids on any page, without per-element listeners)
  document.addEventListener('click', (e)=>{
    const trigger = e.target.closest('[data-lightbox-src]');
    if(!trigger) return;
    e.preventDefault();
    openLightbox(trigger.dataset.lightboxSrc, trigger.dataset.lightboxAlt || '');
  });
})();

/* ===== contact form (homepage only) =====
   Real submission via FormSubmit (see README for the one-time setup step
   required: replace the placeholder email in the form's action attribute
   and confirm the activation email FormSubmit sends on first submission).
   We do NOT preventDefault — the browser performs a real POST and the
   audit's #1 critical finding ("the form doesn't actually send anything")
   is fixed by that real submission, not by a fake JS success message. */
(function(){
  const form = document.getElementById('quoteForm');
  if(!form) return;
  form.addEventListener('submit', () => {
    const btn = form.querySelector('.form-submit');
    if(btn){ btn.disabled = true; btn.textContent = "جاري الإرسال..."; }
    // no preventDefault: let the real POST to FormSubmit proceed
  });
})();
