from generator import create_page, SVGS

about_content = f"""
<div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; About Us</div>
<section style="padding: 60px 20px; text-align:center;">
    <img src="images/bbg-logo-filled.png" alt="Bhai Biryani Godown logo — Since 1977 Trichy" style="width:120px; border-radius:50%; margin:0 auto 24px;">
    <h2 class="section-title">Our Heritage — Since 1977</h2>
    <p style="color:var(--color-muted); max-width:700px; margin: 16px auto 32px; line-height:1.8;">What began as a single fireplace in Trichy has fed generations. Bhai Biryani Godown was founded on the principles of authentic Kalyana style cooking using pure Seeraga Samba rice and traditional wooden fire dum preparation.</p>
    
    <div style="display:flex; justify-content:center; gap:16px; margin-bottom:48px;">
        <span style="background:var(--color-surface); padding:8px 16px; border-radius:8px; border:1px solid var(--color-gold);">1977 Founded</span>
        <span style="background:var(--color-surface); padding:8px 16px; border-radius:8px; border:1px solid var(--color-gold);">3 Branches</span>
        <span style="background:var(--color-surface); padding:8px 16px; border-radius:8px; border:1px solid var(--color-gold);">Millions Served</span>
    </div>

    <h3 style="color:var(--color-text); font-size:1.5rem; margin-bottom:24px;">Visit Our Branches</h3>
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap:24px; max-width:900px; margin:0 auto;">
        <div class="branch-card" style="background:var(--color-surface); padding:24px; border-radius:12px; border:1px solid var(--color-primary);">
            <h4 style="font-size:1.2rem; margin-bottom:8px;">TVS Tolgate</h4>
            <a href="tel:+917708863397" style="color:var(--color-primary); font-weight:700;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>7708863397</a>
        </div>
        <div class="branch-card" style="background:var(--color-surface); padding:24px; border-radius:12px; border:1px solid var(--color-primary);">
            <h4 style="font-size:1.2rem; margin-bottom:8px;">Karur Bypass</h4>
            <a href="tel:+919940963397" style="color:var(--color-primary); font-weight:700;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>9940963397</a>
        </div>
        <div class="branch-card" style="background:var(--color-surface); padding:24px; border-radius:12px; border:1px solid var(--color-primary);">
            <h4 style="font-size:1.2rem; margin-bottom:8px;">SIT Kattur</h4>
            <a href="tel:+918220363397" style="color:var(--color-primary); font-weight:700;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>8220363397</a>
        </div>
    </div>
</section>
"""
create_page("about.html", "About Us — Bhai Biryani Godown | Trichy's Heritage Biryani Since 1977", "Bhai Biryani Godown has served authentic Seeraga Samba biryani in Trichy since 1977. Our wooden fire dum cooking tradition has made us Trichy's most trusted biryani destination for over 47 years.", "about bbg, trichy biryani history", about_content, False)

contact_content = f"""
<div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Contact & Location</div>
<section style="padding: 60px 20px; text-align:center;">
    <h2 class="section-title">Get in Touch</h2>
    <p style="color:var(--color-muted); max-width:600px; margin: 16px auto 32px; line-height:1.6;">Order directly via WhatsApp for the fastest service, or call our branches for table reservations and bulk catering.</p>
    
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:24px; max-width:1000px; margin:0 auto;">
        <div class="branch-card" style="background:var(--color-surface); padding:24px; border-radius:12px; border:1px solid var(--color-primary);">
            <h3 style="font-size:1.5rem; color:var(--color-gold); margin-bottom:8px;">TVS Tolgate</h3>
            <p style="color:var(--color-text); margin-bottom:16px;">TVS Tolgate, Trichy, Tamil Nadu</p>
            <a href="tel:+917708863397" style="display:block; color:var(--color-primary); font-size:1.2rem; font-weight:700; margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>7708863397</a>
            <a href="https://wa.me/917708863397" style="background:#25D366; color:white; padding:12px 24px; border-radius:8px; font-weight:700; text-decoration:none; display:inline-block;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>WhatsApp Order</a>
        </div>
        <div class="branch-card" style="background:var(--color-surface); padding:24px; border-radius:12px; border:1px solid var(--color-primary);">
            <h3 style="font-size:1.5rem; color:var(--color-gold); margin-bottom:8px;">Karur Bypass</h3>
            <p style="color:var(--color-text); margin-bottom:16px;">Karur Bypass, Trichy, Tamil Nadu</p>
            <a href="tel:+919940963397" style="display:block; color:var(--color-primary); font-size:1.2rem; font-weight:700; margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>9940963397</a>
            <a href="https://wa.me/919940963397" style="background:#25D366; color:white; padding:12px 24px; border-radius:8px; font-weight:700; text-decoration:none; display:inline-block;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>WhatsApp Order</a>
        </div>
        <div class="branch-card" style="background:var(--color-surface); padding:24px; border-radius:12px; border:1px solid var(--color-primary);">
            <h3 style="font-size:1.5rem; color:var(--color-gold); margin-bottom:8px;">SIT Kattur</h3>
            <p style="color:var(--color-text); margin-bottom:16px;">SIT Kattur, Trichy, Tamil Nadu</p>
            <a href="tel:+918220363397" style="display:block; color:var(--color-primary); font-size:1.2rem; font-weight:700; margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>8220363397</a>
            <a href="https://wa.me/918220363397" style="background:#25D366; color:white; padding:12px 24px; border-radius:8px; font-weight:700; text-decoration:none; display:inline-block;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>WhatsApp Order</a>
        </div>
    </div>
</section>
"""
create_page("contact.html", "Contact & Location — Bhai Biryani Godown Trichy | 3 Branches", "Find Bhai Biryani Godown in Trichy. 3 branches: TVS Tolgate (7708863397), Karur Bypass (9940963397), SIT Kattur (8220363397). Order biryani on WhatsApp.", "bbg location, bbg phone number", contact_content, False)

print("Generated about and contact pages.")
