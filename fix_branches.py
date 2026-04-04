import sys

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the branches section inserted before footer
start_marker = '<!-- --- BRANCHES SECTION --- -->'
end_marker = '<!-- --- FOOTER --- -->'
if start_marker in content and end_marker in content:
    # find the last occurrence of start_marker
    start_idx = content.rfind(start_marker)
    end_idx = content.find(end_marker, start_idx)
    if start_idx != -1 and end_idx != -1:
        # cut it out
        content = content[:start_idx] + content[end_idx:]

# 2. Find the old BRANCH SELECTOR and replace it
import re

old_selector_pattern = r'<!-- --- BRANCH SELECTOR --- -->\s*<section.*?>.*?</section>'
# We need to be careful with greedy matching
# The old branch selector has <section style="padding: 40px 20px;">
# Let's find it using a simpler regex

old_start = content.find('<!-- --- BRANCH SELECTOR --- -->')
if old_start != -1:
    # find the closing </section> for this section
    # The next section after it is "<!-- --- ABOUT TEASER --- -->" or similar?
    # Let's find the next <!-- ---
    next_section = content.find('<!-- ---', old_start + 10)
    if next_section != -1:
        old_content = content[old_start:next_section]
        # Replace it with our new HTML
        new_branches_html = '''<!-- --- BRANCH SELECTOR (NEW) --- -->
  <section class="branches-section" id="branches">
    <div class="section-label" style="text-align: center;">FIND US</div>
    <h2 class="section-title" style="text-align: center;">Our Branches</h2>
    <p class="section-sub" style="text-align: center;">3 locations across Trichy — dine in or order on WhatsApp</p>

    <div class="branches-grid">

      <!-- BRANCH 1: TVS Tolgate -->
      <div class="branch-card">
        <div class="branch-photo">
          <img
            src="images/theme/branch-tvs.jpg"
            alt="Bhai Biryani Godown TVS Tolgate Trichy"
            loading="lazy"
            onerror="this.src='images/branches/tvs-tolgate.jpg'; this.onerror=function(){this.style.display='none'};"
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
            <svg viewBox="0 0 16 16" fill="var(--color-primary)" width="14" height="14">
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
            src="images/theme/branch-karur.jpg"
            alt="Bhai Biryani Godown Karur Bypass Trichy"
            loading="lazy"
            onerror="this.src='images/branches/karur-bypass.jpg'; this.onerror=function(){this.style.display='none'};"
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
            <svg viewBox="0 0 16 16" fill="var(--color-primary)" width="14" height="14">
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
            src="images/theme/branch-sit.jpg"
            alt="Bhai Biryani Godown SIT Kattur Trichy"
            loading="lazy"
            onerror="this.src='images/branches/sit-kattur.jpg'; this.onerror=function(){this.style.display='none'};"
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
            <svg viewBox="0 0 16 16" fill="var(--color-primary)" width="14" height="14">
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
\n'''
        content = content.replace(old_content, new_branches_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Moved branches section.')

# 3. Update branches theme in styles.css to be YELLOW
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace border-color with var(--color-primary)
css = css.replace('border: 1px solid rgba(232, 105, 42, 0.15);', 'border: 1px solid var(--color-primary);')
css = css.replace('border-color: rgba(232, 105, 42, 0.4);', 'border-color: var(--color-primary);')
css = css.replace('color: #9c7a5a', 'color: var(--color-muted)') # make descriptions match theme

# Button colors
# Call button -> yellow theme
css = css.replace('.btn-call {\n  background: rgba(232, 105, 42, 0.1);\n  color: #e8692a;\n  border-color: rgba(232, 105, 42, 0.3);\n}', '.btn-call {\n  background: rgba(245, 203, 0, 0.1);\n  color: var(--color-primary);\n  border-color: rgba(245, 203, 0, 0.3);\n}')
css = css.replace('.btn-call:hover, .btn-call:active {\n  background: #e8692a;\n  color: #1a0f00;\n}', '.btn-call:hover, .btn-call:active {\n  background: var(--color-primary);\n  color: #1a0f00;\n}')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Yellow theme applied.')
