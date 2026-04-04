import os
import re

# 1. Update menu-card-from to menu-card-price in HTML files
html_files = ['index.html', 'menu.html']
for f_name in html_files:
    with open(f_name, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('menu-card-from', 'menu-card-price')
    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(html)
        
# 2. Insert branches section into index.html
branches_html = '''
  <!-- --- BRANCHES SECTION --- -->
  <section class="branches-section" id="branches">
    <div class="section-label text-center">FIND US</div>
    <h2 class="section-title text-center">Our Branches</h2>
    <p class="section-sub text-center" style="color:#9c7a5a; text-align:center; margin-bottom:28px;">3 locations across Trichy — dine in or order on WhatsApp</p>

    <div class="branches-grid">

      <!-- BRANCH 1: TVS Tolgate -->
      <div class="branch-card">
        <div class="branch-photo">
          <img
            src="images/branches/tvs-tolgate.jpg"
            alt="Bhai Biryani Godown TVS Tolgate Trichy"
            loading="lazy"
            onerror="this.style.display='none'"
          />
          <div class="branch-status open">? Open Now</div>
        </div>
        <div class="branch-body">
          <div class="branch-header">
            <div>
              <h3 class="branch-name">TVS Tolgate</h3>
              <p class="branch-locality">Trichy, Tamil Nadu</p>
            </div>
            <div class="branch-rating">
              <span class="rating-stars">? 3.6</span>
              <span class="rating-count">(249)</span>
            </div>
          </div>
          <p class="branch-address">
            <svg viewBox="0 0 16 16" fill="#9c7a5a" width="14" height="14">
              <path d="M8 1a5 5 0 0 0-5 5c0 4 5 9 5 9s5-5 5-9a5 5 0 0 0-5-5zm0 7a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"/>
            </svg>
            TVS Tolgate Roundabout, Pudukottai Main Rd
          </p>
          <p class="branch-tags">Dine-in · Drive-through · No-contact delivery</p>
          <div class="branch-actions">
            <a href="tel:+917708863397" class="branch-btn btn-call">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
              </svg>
              Call
            </a>
            <a href="https://wa.me/917708863397?text=Hi%20Bhai%20Biryani%20Godown%20TVS%20Tolgate%2C%20I%20want%20to%20place%20an%20order."
               target="_blank" rel="noopener" class="branch-btn btn-whatsapp">
              <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/>
              </svg>
              WhatsApp
            </a>
            <a href="https://maps.google.com/?q=Bhai+Biryani+Godown+TVS+Tolgate+Trichy"
               target="_blank" rel="noopener" class="branch-btn btn-directions">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16">
                <polygon points="3 11 22 2 13 21 11 13 3 11"/>
              </svg>
              Directions
            </a>
          </div>
        </div>
      </div>

      <!-- BRANCH 2: Karur Bypass -->
      <div class="branch-card">
        <div class="branch-photo">
          <img
            src="images/branches/karur-bypass.jpg"
            alt="Bhai Biryani Godown Karur Bypass Trichy"
            loading="lazy"
            onerror="this.style.display='none'"
          />
          <div class="branch-status open">? Open Now</div>
        </div>
        <div class="branch-body">
          <div class="branch-header">
            <div>
              <h3 class="branch-name">Karur Bypass</h3>
              <p class="branch-locality">Trichy, Tamil Nadu</p>
            </div>
            <div class="branch-rating">
              <span class="rating-stars">? 4.4</span>
              <span class="rating-count">(163)</span>
            </div>
          </div>
          <p class="branch-address">
            <svg viewBox="0 0 16 16" fill="#9c7a5a" width="14" height="14">
              <path d="M8 1a5 5 0 0 0-5 5c0 4 5 9 5 9s5-5 5-9a5 5 0 0 0-5-5zm0 7a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"/>
            </svg>
            Vijay Towers, Karur Bypass Rd
          </p>
          <p class="branch-tags">Dine-in · Drive-through · No-contact delivery</p>
          <div class="branch-actions">
            <a href="tel:+919940963397" class="branch-btn btn-call">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
              </svg>
              Call
            </a>
            <a href="https://wa.me/919940963397?text=Hi%20Bhai%20Biryani%20Godown%20Karur%20Bypass%2C%20I%20want%20to%20place%20an%20order."
               target="_blank" rel="noopener" class="branch-btn btn-whatsapp">
              <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/>
              </svg>
              WhatsApp
            </a>
            <a href="https://maps.google.com/?q=Bhai+Biryani+Godown+Karur+Bypass+Trichy"
               target="_blank" rel="noopener" class="branch-btn btn-directions">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16">
                <polygon points="3 11 22 2 13 21 11 13 3 11"/>
              </svg>
              Directions
            </a>
          </div>
        </div>
      </div>

      <!-- BRANCH 3: SIT Kattur -->
      <div class="branch-card">
        <div class="branch-photo">
          <img
            src="images/branches/sit-kattur.jpg"
            alt="Bhai Biryani Godown SIT Kattur Trichy"
            loading="lazy"
            onerror="this.style.display='none'"
          />
          <div class="branch-status open">? Open Now</div>
        </div>
        <div class="branch-body">
          <div class="branch-header">
            <div>
              <h3 class="branch-name">SIT Kattur</h3>
              <p class="branch-locality">Trichy, Tamil Nadu</p>
            </div>
            <div class="branch-rating">
              <span class="rating-stars">? 4.8</span>
              <span class="rating-count">(392)</span>
            </div>
          </div>
          <p class="branch-address">
            <svg viewBox="0 0 16 16" fill="#9c7a5a" width="14" height="14">
              <path d="M8 1a5 5 0 0 0-5 5c0 4 5 9 5 9s5-5 5-9a5 5 0 0 0-5-5zm0 7a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"/>
            </svg>
            SIT Campus Road, Kattur, Trichy
          </p>
          <p class="branch-tags">Dine-in · Drive-through · No-contact delivery</p>
          <div class="branch-actions">
            <a href="tel:+918220363397" class="branch-btn btn-call">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
              </svg>
              Call
            </a>
            <a href="https://wa.me/918220363397?text=Hi%20Bhai%20Biryani%20Godown%20SIT%20Kattur%2C%20I%20want%20to%20place%20an%20order."
               target="_blank" rel="noopener" class="branch-btn btn-whatsapp">
              <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/>
              </svg>
              WhatsApp
            </a>
            <a href="https://maps.google.com/?q=Bhai+Biryani+Godown+SIT+Kattur+Trichy"
               target="_blank" rel="noopener" class="branch-btn btn-directions">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16">
                <polygon points="3 11 22 2 13 21 11 13 3 11"/>
              </svg>
              Directions
            </a>
          </div>
        </div>
      </div>

    </div>
  </section>
'''

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Only insert if it's not already there
if 'class="branches-section"' not in html:
    html = html.replace('<!-- --- FOOTER --- -->', branches_html + '\\n  <!-- --- FOOTER --- -->')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
# 3. Append new CSS to styles.css using raw bytes to avoid encoding failures
css_append = b'''

/* -- POST MATCH CSS UPDATES -- */

/* GRID WRAPPER */
.menu-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  padding: 0 16px 24px;
  width: 100%;
  box-sizing: border-box;
}

/* SINGLE CARD */
.menu-card {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 10px !important;
  padding: 24px 12px 20px !important;
  min-height: 140px !important;
  width: 100% !important;
  box-sizing: border-box !important;
  border-radius: 16px !important;
  background: #231508 !important;
  border: 1px solid rgba(232, 105, 42, 0.15) !important;
  text-decoration: none !important;
  transition: border-color 0.2s, background 0.2s !important;
  cursor: pointer !important;
  -webkit-tap-highlight-color: transparent !important;
}

.menu-card:hover,
.menu-card:active {
  border-color: #e8692a !important;
  background: rgba(232, 105, 42, 0.08) !important;
}

/* ICON */
.menu-card-icon {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 44px !important;
  height: 44px !important;
  background: none !important;
  border: none !important;
  border-radius: 0 !important;
  padding: 0 !important;
}

.menu-card-icon svg {
  width: 36px;
  height: 36px;
}

/* NAME */
.menu-card-name {
  font-size: 0.875rem !important;
  font-weight: 700 !important;
  color: #f5ede0 !important;
  text-align: center !important;
  line-height: 1.3 !important;
  background: none !important;
  border: none !important;
  padding: 0 !important;
  margin: 0 !important;
}

/* PRICE */
.menu-card-price {
  font-size: 0.75rem !important;
  color: #e8692a !important;
  text-align: center !important;
  background: none !important;
  border: none !important;
  padding: 0 !important;
  margin: 0 !important;
}

/* FULL MENU CARD */
.menu-card.full-menu {
  grid-column: 1 / -1 !important;
  flex-direction: row !important;
  justify-content: center !important;
  gap: 12px !important;
  min-height: 60px !important;
  background: #e8692a !important;
  border-color: #e8692a !important;
}

.menu-card.full-menu .menu-card-name {
  color: #1a0f00 !important;
  font-size: 1rem !important;
}

/* DESKTOP */
@media (min-width: 768px) {
  .menu-grid {
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 16px !important;
    padding: 0 32px 32px !important;
  }

  .menu-card {
    min-height: 160px !important;
    padding: 28px 16px 24px !important;
  }

  .menu-card-name {
    font-size: 1rem !important;
  }

  .menu-card-price {
    font-size: 0.875rem !important;
  }
}

/* BRANCHES SECTION */
.branches-section {
  padding: 48px 16px;
}

.section-sub {
  color: #9c7a5a;
  font-size: 0.9rem;
  margin-top: 4px;
  margin-bottom: 28px;
}

.branches-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

@media (min-width: 768px) {
  .branches-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
  }
}

.branch-card {
  background: #231508;
  border: 1px solid rgba(232, 105, 42, 0.15);
  border-radius: 16px;
  overflow: hidden;
  transition: border-color 0.2s;
}

.branch-card:hover {
  border-color: rgba(232, 105, 42, 0.4);
}

.branch-photo {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  background: #1a0f00;
  overflow: hidden;
}

.branch-photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.branch-status {
  position: absolute;
  top: 10px;
  left: 10px;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.7rem;
  font-weight: 700;
  backdrop-filter: blur(6px);
}

.branch-status.open {
  background: rgba(0, 0, 0, 0.6);
  color: #4ade80;
}

.branch-status.closed {
  background: rgba(0, 0, 0, 0.6);
  color: #f87171;
}

.branch-body {
  padding: 14px 16px 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.branch-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 8px;
}

.branch-name {
  font-size: 1rem;
  font-weight: 700;
  color: #f5ede0;
  margin: 0;
  line-height: 1.2;
}

.branch-locality {
  font-size: 0.75rem;
  color: #9c7a5a;
  margin: 2px 0 0;
}

.branch-rating {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  flex-shrink: 0;
}

.rating-stars {
  font-size: 0.85rem;
  font-weight: 700;
  color: #f59e0b;
  white-space: nowrap;
}

.rating-count {
  font-size: 0.7rem;
  color: #9c7a5a;
}

.branch-address {
  display: flex;
  align-items: flex-start;
  gap: 6px;
  font-size: 0.78rem;
  color: #9c7a5a;
  margin: 0;
  line-height: 1.4;
}

.branch-address svg {
  flex-shrink: 0;
  margin-top: 1px;
}

.branch-tags {
  font-size: 0.7rem;
  color: #6b5040;
  margin: 0;
}

.branch-actions {
  display: flex;
  gap: 8px;
  margin-top: 4px;
  flex-wrap: wrap;
}

.branch-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 7px 12px;
  border-radius: 8px;
  font-size: 0.75rem;
  font-weight: 600;
  text-decoration: none;
  border: 1px solid transparent;
  transition: all 0.15s;
  white-space: nowrap;
  -webkit-tap-highlight-color: transparent;
}

.btn-call {
  background: rgba(232, 105, 42, 0.1);
  color: #e8692a;
  border-color: rgba(232, 105, 42, 0.3);
}

.btn-call:hover, .btn-call:active {
  background: #e8692a;
  color: #1a0f00;
}

.btn-whatsapp {
  background: rgba(37, 211, 102, 0.1);
  color: #25D366;
  border-color: rgba(37, 211, 102, 0.3);
}

.btn-whatsapp:hover, .btn-whatsapp:active {
  background: #25D366;
  color: #fff;
}

.btn-directions {
  background: rgba(96, 165, 250, 0.1);
  color: #60a5fa;
  border-color: rgba(96, 165, 250, 0.3);
}

.btn-directions:hover, .btn-directions:active {
  background: #60a5fa;
  color: #1a0f00;
}

'''

with open('styles.css', 'ab') as f:
    f.write(css_append)

print("Applied Patches")
