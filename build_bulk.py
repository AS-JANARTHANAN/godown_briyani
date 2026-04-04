from generator import create_page, SVGS

bulk_html = f"""
<section class="page-hero">
    <div class="page-hero-bg" data-parallax-speed="0.3" style="background-image: url('images/theme/hero-bg.webp'); opacity: 0.5;"></div>
    <div class="page-hero-overlay"></div>
    <div class="page-hero-content" style="padding-top:100px;">
        <p class="page-hero-sub" style="color:var(--color-gold);">Wholesale & Catering</p>
        <h1 class="page-hero-title" style="font-size: clamp(2rem, 6vw, 3.5rem);">Feeding a Crowd?<br>We've Got You Covered.</h1>
        <p style="color:var(--color-text); margin-top:16px;">Wholesale biryani, party platters & catering — Trichy's most trusted bulk biryani supplier since 1977</p>
    </div>
</section>

<div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Bulk Orders & Catering</div>

<section style="padding: 60px 20px;">
    <p class="section-label text-center" style="text-align: center;">For 10+ People</p>
    <h2 class="section-title text-center" style="text-align: center; margin-bottom: 8px;">Wholesale Biryani</h2>
    <p style="text-align: center; color:var(--color-primary); font-weight:700; margin-bottom: 32px;">1 Padi = Serves 10 People</p>
    
    <div class="menu-grid">
        <div class="dish-row">
            <span class="dish-name">1 Padi Chicken Biryani</span>
            <span class="dish-price">₹1,500</span>
        </div>
        <div class="dish-row">
            <span class="dish-name">1 Padi Mutton Biryani</span>
            <span class="dish-price">₹2,700</span>
        </div>
        <div class="dish-row">
            <span class="dish-name">1 Padi Plain Biryani</span>
            <span class="dish-price">₹1,000</span>
        </div>
        <div class="dish-row">
            <span class="dish-name">1 Padi Mushroom Biryani</span>
            <span class="dish-price">₹1,200</span>
        </div>
        <div class="dish-row">
            <span class="dish-name">1 Padi Curd Rice</span>
            <span class="dish-price">₹800</span>
        </div>
    </div>
</section>

<section style="padding: 60px 20px; background:var(--color-surface);">
    <p class="section-label text-center" style="text-align: center;">Bulk Starters & Sides</p>
    <h2 class="section-title text-center" style="text-align: center; margin-bottom: 8px;">1 Kg Starters</h2>
    <p style="text-align: center; color:var(--color-primary); font-weight:700; margin-bottom: 32px;">1 Kg = Serves 10 People</p>
    
    <div class="menu-grid">
        <div class="dish-row"><span class="dish-name">1 Kg Chicken 65 (Bone)</span><span class="dish-price">₹500</span></div>
        <div class="dish-row"><span class="dish-name">1 Kg Chicken 65 (Boneless)</span><span class="dish-price">₹750</span></div>
        <div class="dish-row"><span class="dish-name">1 Kg Chicken Pepper Masala</span><span class="dish-price">₹700</span></div>
        <div class="dish-row"><span class="dish-name">1 Kg Chettinad Chicken</span><span class="dish-price">₹700</span></div>
        <div class="dish-row"><span class="dish-name">1 Kg Chicken Chukka</span><span class="dish-price">₹700</span></div>
        <div class="dish-row"><span class="dish-name">1 Kg Mutton Chukka</span><span class="dish-price">₹1,300</span></div>
        <div class="dish-row"><span class="dish-name">1 Kg Mushroom 65</span><span class="dish-price">₹500</span></div>
        <div class="dish-row"><span class="dish-name">1 Kg Gobi 65</span><span class="dish-price">₹500</span></div>
        <div class="dish-row"><span class="dish-name">1 Kg Bread Halwa</span><span class="dish-price">₹400</span></div>
    </div>
    
    <div style="text-align:center; margin-top:40px;">
        <a href="https://wa.me/919940963397?text=Hi%2C%20I%20am%20interested%20in%20a%20bulk%2Fparty%20order%20from%20Bhai%20Biryani%20Godown.%20Please%20share%20details." target="_blank" style="background:var(--color-primary); color:#1a0f00; padding:16px 32px; border-radius:12px; font-weight:700; text-decoration:none; display:inline-block; font-size:1.1rem;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>Order in Bulk on WhatsApp</a>
    </div>
</section>

<section style="padding: 80px 20px;">
    <h2 class="section-title text-center" style="text-align: center; margin-bottom: 24px;">Planning a Wedding, Corporate Lunch or Family Function?</h2>
    <p style="text-align: center; color:var(--color-muted); max-width:700px; margin: 0 auto 32px; line-height:1.6;">Bhai Biryani Godown undertakes all party and event catering in Trichy. From intimate family gatherings to large wedding receptions, we prepare Seeraga Samba biryani in authentic kalyana style — the same tradition since 1977.</p>
    
    <div style="max-width:600px; margin:0 auto; display:grid; grid-template-columns: 1fr; gap:12px;">
       <div style="background:var(--color-surface); padding:16px; border-radius:8px;">✓ Wedding & Reception Catering</div>
       <div style="background:var(--color-surface); padding:16px; border-radius:8px;">✓ Corporate Lunch / Office Parties</div>
       <div style="background:var(--color-surface); padding:16px; border-radius:8px;">✓ Birthday & Anniversary Functions</div>
       <div style="background:var(--color-surface); padding:16px; border-radius:8px;">✓ Religious & Cultural Events</div>
       <div style="background:var(--color-surface); padding:16px; border-radius:8px;">✓ Bulk Delivery to Your Venue</div>
       <div style="background:var(--color-surface); padding:16px; border-radius:8px;">✓ Custom Menu Planning Available</div>
    </div>
    
    <div style="text-align:center; margin-top:40px;">
        <a href="https://wa.me/919940963397?text=Hi%2C%20I%20need%20details%20about%20event%20catering." style="display:inline-block; border: 2px solid var(--color-primary); color:var(--color-text); padding:12px 24px; border-radius:8px; font-weight:700; text-decoration:none; margin-right:12px;">Enquire for Catering</a>
        <a href="tel:+919940963397" style="display:inline-block; background:var(--color-primary); color:#1a0f00; padding:12px 24px; border-radius:8px; font-weight:700; text-decoration:none;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>Call 9940963397</a>
    </div>
</section>

<section style="padding: 60px 20px; background:var(--color-surface);">
    <h2 class="section-title text-center" style="text-align: center; margin-bottom: 32px;">Why Choose BBG For Bulk?</h2>
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap:20px; max-width:1000px; margin:0 auto; text-align:center;">
       <div>
         <div style="font-size:40px; margin-bottom:12px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><path d="M12 2c0 0-6 7.5-6 12s4.5 8 6 8 6-3.5 6-8-6-12-6-12z"/><path d="M12 12c0 0-2 2-2 4s1.5 3 2 3 2-1.5 2-3-2-4-2-4z"/></svg></div>
         <h3 style="font-size:1.1rem; color:var(--color-text); margin-bottom:8px;">Since 1977</h3>
         <p style="color:var(--color-muted); font-size:0.9rem;">Proven legacy in Trichy.</p>
       </div>
       <div>
         <div style="font-size:40px; margin-bottom:12px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><path d="M2 22 22 2"/><path d="M12 2v10"/><path d="M12 12h10"/><path d="M6 8v6"/><path d="M6 14h6"/><path d="M18 14v6"/><path d="M12 20h6"/></svg></div>
         <h3 style="font-size:1.1rem; color:var(--color-text); margin-bottom:8px;">Seeraga Samba</h3>
         <p style="color:var(--color-muted); font-size:0.9rem;">Authentic kalyana style.</p>
       </div>
       <div>
         <div style="font-size:40px; margin-bottom:12px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><rect x="4" y="6" width="16" height="12" rx="2"/><path d="M8 6v12"/><path d="M16 6v12"/></svg></div>
         <h3 style="font-size:1.1rem; color:var(--color-text); margin-bottom:8px;">Wooden Fire</h3>
         <p style="color:var(--color-muted); font-size:0.9rem;">Traditional dum cooking.</p>
       </div>
       <div>
         <div style="font-size:40px; margin-bottom:12px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><rect x="2" y="8" width="14" height="10" rx="1"/><path d="M16 14h4l2-4h-6"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg></div>
         <h3 style="font-size:1.1rem; color:var(--color-text); margin-bottom:8px;">Timely Delivery</h3>
         <p style="color:var(--color-muted); font-size:0.9rem;">3 branches across Trichy.</p>
       </div>
    </div>
</section>
"""

create_page(
    filename="bulk-orders.html",
    title="Bulk Biryani Orders & Catering — Bhai Biryani Godown Trichy | Weddings & Events",
    meta_desc="Wholesale biryani supplier in Trichy for weddings, corporate events, and family functions. 1 Padi (10 servings) Chicken Biryani from ₹1500. Mutton Biryani bulk orders. Contact Bhai Biryani Godown — 9940963397.",
    keywords="bulk biryani Trichy, wholesale biryani Trichy, catering Trichy, 1 padi biryani",
    content=bulk_html,
    include_json_ld=False
)
