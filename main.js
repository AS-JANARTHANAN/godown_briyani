'use strict';

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   CONFIG — update with real shop number
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
const CONFIG = {
  whatsapp: '917708863397',
  shopName: 'Bhai Biryani Godown',
};

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   WHATSAPP ORDER FUNCTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
function orderOnWhatsApp(itemName, price) {
  const msg = encodeURIComponent(
    `Hello ${CONFIG.shopName}! \n\nI'd like to order:\n\n` +
    ` *${itemName}*\n` +
    ` Price: ${price}\n\n` +
    `Please confirm availability and share delivery/pickup details. Thank you!`
  );
  window.open(`https://wa.me/${CONFIG.whatsapp}?text=${msg}`, '_blank');
}

function generalWhatsAppOrder() {
  const msg = encodeURIComponent(
    `Hello ${CONFIG.shopName}! \n\nI'd like to place an order. Please share the menu or let me know what's available today. Thank you!`
  );
  window.open(`https://wa.me/${CONFIG.whatsapp}?text=${msg}`, '_blank');
}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   PARALLAX ENGINE (JS-based for iOS compatibility)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
function initParallax() {
  const parallaxEls = document.querySelectorAll('[data-parallax-speed]');
  if (!parallaxEls.length) return;

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reducedMotion) return;

  function onScroll() {
    const scrollY = window.scrollY;
    parallaxEls.forEach(el => {
      const section = el.closest('.parallax-section');
      if (!section) return;
      const rect = section.getBoundingClientRect();
      const inView = rect.bottom > 0 && rect.top < window.innerHeight;
      if (!inView) return;
      const speed = parseFloat(el.dataset.parallaxSpeed) || 0.35;
      const offset = (scrollY - section.offsetTop) * speed;
      el.style.transform = `translateY(${offset}px)`;
    });
  }

  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => { onScroll(); ticking = false; });
      ticking = true;
    }
  }, { passive: true });

  onScroll();
}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   SCROLL REVEAL (Intersection Observer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
function initScrollReveal() {
  const items = document.querySelectorAll('.reveal');
  if (!items.length) return;

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -30px 0px' });

  items.forEach(el => observer.observe(el));
}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   BOTTOM NAV — highlight active link
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
function initBottomNav() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.bottom-nav a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   MOBILE MENU DRAWER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
function initMobileMenu() {
  const hamburger = document.getElementById('hamburger');
  const overlay   = document.getElementById('mobileMenuOverlay');
  if (!hamburger || !overlay) return;

  hamburger.addEventListener('click', () => {
    overlay.classList.toggle('open');
    const isOpen = overlay.classList.contains('open');
    hamburger.setAttribute('aria-expanded', isOpen);
  });
  overlay.addEventListener('click', e => {
    if (e.target === overlay) {
      overlay.classList.remove('open');
      hamburger.setAttribute('aria-expanded', 'false');
    }
  });
}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   MENU FILTER TABS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
function initMenuFilter() {
  const tabs  = document.querySelectorAll('.tab-pill');
  const cards = document.querySelectorAll('.menu-card');
  if (!tabs.length) return;

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const filter = tab.dataset.filter;
      cards.forEach(card => {
        const match = filter === 'all' || card.dataset.category === filter;
        card.style.display = match ? 'flex' : 'none';
      });
    });
  });
}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   GALLERY AUTO-SCROLL — duplicate for infinite loop
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
function initGallery() {
  const track = document.querySelector('.gallery-track');
  if (!track) return;
  const items = Array.from(track.children);
  items.forEach(item => track.appendChild(item.cloneNode(true)));
}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   INIT ALL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
document.addEventListener('DOMContentLoaded', () => {
  initParallax();
  initScrollReveal();
  initBottomNav();
  initMobileMenu();
  initMenuFilter();
  initGallery();
});

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   REUSABLE YOUTUBE EMBED COMPONENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
class YouTubeEmbed extends HTMLElement {
  connectedCallback() {
    this.rawUrl = this.getAttribute('url');
    this.videoId = this.extractId(this.rawUrl);
    
    if (!this.videoId) {
      this.innerHTML = '<div style="position:absolute;top:0;left:0;width:100%;height:100%;background:#1c1c14;border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px;text-align:center;"><p style="color:#f5f0e0;margin-bottom:16px;font-size:14px;">Invalid Video Link</p><a href="' + this.rawUrl + '" target="_blank" style="background:#F5CB00;color:#121210;padding:10px 20px;border-radius:24px;font-weight:bold;text-decoration:none;font-size:14px;">Watch on YouTube</a></div>';
      return;
    }

    this.renderIframe();
  }

  extractId(url) {
    if (!url) return null;
    const regExp = /^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=|shorts\/)([^#\&\?]*).*/;
    const match = url.match(regExp);
    return (match && match[2].length === 11) ? match[2] : null;
  }

  renderIframe() {
    const embedUrl = 'https://www.youtube.com/embed/' + this.videoId;
    
    this.classList.add('short-wrap');
    this.style.display = 'block';
    
    this.innerHTML = `
      <!-- Loading Skeleton -->
      <div class="yt-skeleton" style="position:absolute;top:0;left:0;width:100%;height:100%;background:#1c1c14;border-radius:16px;display:flex;align-items:center;justify-content:center;z-index:1;">
         <div style="width:40px;height:40px;border:3px solid rgba(255,215,0,0.3);border-top-color:#F5CB00;border-radius:50%;animation:spin 1s linear infinite;"></div>
      </div>
      
      <!-- Video Iframe -->
      <iframe 
        src="${embedUrl}" 
        title="YouTube Video" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen 
        loading="lazy"
        onload="this.previousElementSibling.style.display='none';"
        style="position:absolute; top:0; left:0; width:100%; height:100%; border:none; z-index:2; border-radius:16px;">
      </iframe>
    `;

    if (!document.getElementById('yt-spin-style')) {
      const style = document.createElement('style');
      style.id = 'yt-spin-style';
      style.innerHTML = '@keyframes spin { to { transform: rotate(360deg); } }';
      document.head.appendChild(style);
    }
  }
}
customElements.define('youtube-embed', YouTubeEmbed);
