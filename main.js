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
   INSTAGRAM REELS — Play/Pause & Mute/Unmute
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
function toggleReelPlay(tapArea) {
  const card = tapArea.closest('.reel-card');
  const video = card.querySelector('.reel-video');
  const icon = card.querySelector('.reel-play-icon');
  
  if (video.paused) {
    video.play();
    // Show play icon briefly
    icon.innerHTML = '<svg viewBox="0 0 24 24" fill="white" width="48" height="48"><path d="M8 5v14l11-7z"/></svg>';
  } else {
    video.pause();
    // Show pause icon
    icon.innerHTML = '<svg viewBox="0 0 24 24" fill="white" width="48" height="48"><path d="M6 4h4v16H6zM14 4h4v16h-4z"/></svg>';
  }
  
  // Flash the icon
  icon.classList.add('show');
  clearTimeout(icon._hideTimer);
  icon._hideTimer = setTimeout(() => {
    icon.classList.remove('show');
  }, 600);
}

function toggleReelMute(btn, event) {
  if (event) {
    event.preventDefault();
    event.stopPropagation();
  }
  const card = btn.closest('.reel-card') || btn.closest('.yt-card') || btn.parentElement;
  const video = card.querySelector('video') || card.querySelector('.reel-video');
  const mutedIcon = btn.querySelector('.icon-muted');
  const unmutedIcon = btn.querySelector('.icon-unmuted');
  
  video.muted = !video.muted;
  
  if (video.muted) {
    mutedIcon.style.display = '';
    unmutedIcon.style.display = 'none';
  } else {
    mutedIcon.style.display = 'none';
    unmutedIcon.style.display = '';
  }
}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   REUSABLE SWIPE DECK — JioHotstar-style stacked cards
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
function initSwipeDeck() {
  document.querySelectorAll('.swipe-deck').forEach(function(deck) {
    var dotsContainer = deck.parentElement.querySelector('.swipe-dots');
    var dots = dotsContainer ? dotsContainer.querySelectorAll('.swipe-dot') : [];
    var cards = deck.querySelectorAll('.swipe-card');
    var total = cards.length;
    if (total === 0) return;

    var current = 0, startX = 0, startY = 0, dragX = 0;
    var isDragging = false, isHoriz = null, SNAP = 60;

    function layout(animated) {
      for (var i = 0; i < total; i++) {
        var c = cards[i];
        var diff = ((i - current) % total + total) % total;

        if (animated) c.classList.remove('no-transition');
        else c.classList.add('no-transition');

        if (diff === 0) {
          c.style.transform = 'translateX(0) translateY(0) scale(1)';
          c.style.opacity = '1';
          c.style.zIndex = 10;
          c.style.pointerEvents = 'auto';
        } else if (diff === 1) {
          c.style.transform = 'translateX(20px) translateY(10px) scale(0.95)';
          c.style.opacity = '1';
          c.style.zIndex = 9;
          c.style.pointerEvents = 'none';
        } else if (diff === 2) {
          c.style.transform = 'translateX(40px) translateY(20px) scale(0.90)';
          c.style.opacity = '0.7';
          c.style.zIndex = 8;
          c.style.pointerEvents = 'none';
        } else {
          c.style.transform = 'translateX(60px) translateY(30px) scale(0.85)';
          c.style.opacity = '0';
          c.style.zIndex = 0;
          c.style.pointerEvents = 'none';
        }
      }
      dots.forEach(function(d, i) { d.classList.toggle('swipe-dot-active', i === current); });
    }

    function dragFront(dx) {
      var c = cards[current];
      c.classList.add('no-transition');
      c.style.transform = 'translateX(' + dx + 'px) rotate(' + (dx * 0.04) + 'deg) scale(1)';
      var progress = Math.min(Math.abs(dx) / 200, 1);
      var nextIdx = (current + 1) % total;
      var next = cards[nextIdx];
      next.classList.add('no-transition');
      next.style.transform = 'translateX(' + (20 - 20 * progress) + 'px) translateY(' + (10 - 10 * progress) + 'px) scale(' + (0.95 + 0.05 * progress) + ')';
      var next2Idx = (current + 2) % total;
      if (total > 2) {
        var next2 = cards[next2Idx];
        next2.classList.add('no-transition');
        next2.style.transform = 'translateX(' + (40 - 20 * progress) + 'px) translateY(' + (20 - 10 * progress) + 'px) scale(' + (0.90 + 0.05 * progress) + ')';
        next2.style.opacity = '' + (0.7 + 0.3 * progress);
      }
    }

    function goTo(idx) {
      current = ((idx % total) + total) % total;
      layout(true);
    }

    deck.addEventListener('touchstart', function(e) {
      startX = e.touches[0].clientX; startY = e.touches[0].clientY;
      isDragging = true; isHoriz = null; dragX = 0;
    }, { passive: true });

    deck.addEventListener('touchmove', function(e) {
      if (!isDragging) return;
      var dx = e.touches[0].clientX - startX;
      var dy = e.touches[0].clientY - startY;
      if (isHoriz === null) isHoriz = Math.abs(dx) > Math.abs(dy);
      if (!isHoriz) { isDragging = false; layout(true); return; }
      e.preventDefault(); dragX = dx; dragFront(dragX);
    }, { passive: false });

    deck.addEventListener('touchend', function() {
      if (!isDragging) return; isDragging = false;
      if (Math.abs(dragX) > SNAP) { dragX < 0 ? goTo(current + 1) : goTo(current - 1); }
      else layout(true);
      dragX = 0;
    });

    deck.addEventListener('touchcancel', function() { isDragging = false; layout(true); dragX = 0; });

    deck.addEventListener('mousedown', function(e) {
      e.preventDefault(); startX = e.clientX; isDragging = true; dragX = 0;
      deck.classList.add('dragging');
    });
    document.addEventListener('mousemove', function(e) {
      if (!isDragging) return; dragX = e.clientX - startX; dragFront(dragX);
    });
    document.addEventListener('mouseup', function() {
      if (!isDragging) return; isDragging = false;
      deck.classList.remove('dragging');
      if (Math.abs(dragX) > SNAP) { dragX < 0 ? goTo(current + 1) : goTo(current - 1); }
      else layout(true);
      dragX = 0;
    });

    layout(false);
  });
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
  initSwipeDeck();
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
