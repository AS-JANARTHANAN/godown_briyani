import os
from generator import create_page, SVGS

def menu_section_html(title, items, is_veg=False):
    html = f"""
<div style="margin-bottom: 32px;">
    <h3 style="color:var(--color-gold); font-family:'Playfair Display', serif; font-size:1.5rem; margin-bottom:16px;">{title}</h3>
    <div class="menu-grid">
"""
    dot_color = "var(--leaf)" if is_veg else "var(--red-dot)"
    
    for name, price, badge in items:
        badge_html = f" <span style='font-size:0.8rem; background:rgba(245,203,0,0.1); color:var(--color-primary); padding:2px 6px; border-radius:4px; margin-left:8px;'>{badge}</span>" if badge else ""
        html += f"""
        <div class="dish-row">
            <span class="dish-name"><span style="display:inline-block; width:12px; height:12px; border:2px solid {dot_color}; margin-right:8px; border-radius:2px;"></span>{name}{badge_html}</span>
            <span class="dish-price">{price}</span>
        </div>
"""
    html += """
    </div>
</div>
"""
    return html

# ----------------- BIRYANI -----------------
biryani_items = [
    ("Egg Biryani", "₹120", ""),
    ("Chicken Plain Biryani", "₹100", ""),
    ("Mutton Plain Biryani", "₹150", ""),
    ("Chicken Biryani", "₹150", ""),
    ("Chicken 65 Biryani", "₹170", ""),
    ("Mutton Biryani", "₹250", ""),
    ("Prawn Biryani", "₹250", ""),
    ("Kaadai 65 Biryani", "₹220", ""),
    ("Fish Biryani", "₹250", "")
]
biryani_content = f"""
<section class="page-hero">
    <div class="page-hero-bg" data-parallax-speed="0.3" style="background-image: url('images/dishes/briyani/chicken-biryani.webp'); opacity:0.6;"></div>
    <div class="page-hero-overlay"></div>
    <div class="page-hero-content" style="padding-top:100px;">
        <p class="page-hero-sub" style="color:var(--color-gold);">The Royal Aroma of Seeraga Samba</p>
        <h1 class="page-hero-title">BIRYANI</h1>
        <p style="color:var(--color-text); margin-top:16px;">Small Grain, Big Flavour</p>
    </div>
</section>
<div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Biryani</div>
<section style="padding: 60px 20px;">
    {menu_section_html("Our Biryani Collection", biryani_items, False)}
</section>
"""
create_page("biryani.html", "Biryani Menu | Bhai Biryani Godown Trichy", "Order Seeraga Samba biryani in Trichy. Chicken Biryani ₹150, Mutton Biryani ₹250. Authentic dum biryani.", "seeraga samba biryani, chicken biryani trichy, mutton biryani", biryani_content)

# ----------------- PLATTERS -----------------
platters_content = f"""
<section class="page-hero">
    <div class="page-hero-bg" data-parallax-speed="0.3" style="background-image: url('images/theme/gallery-4.webp'); opacity:0.6;"></div>
    <div class="page-hero-overlay"></div>
    <div class="page-hero-content" style="padding-top:100px;">
        <p class="page-hero-sub" style="color:var(--color-gold);">The Ultimate Feast</p>
        <h1 class="page-hero-title">BBG PLATTERS</h1>
    </div>
</section>
<div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Platters</div>
<section style="padding: 60px 20px;">
    <div style="background:var(--color-surface); padding:24px; border-radius:12px; border:1px solid var(--color-primary); margin-bottom:32px;">
        <h3 style="font-size:1.8rem; color:var(--color-gold); margin-bottom:8px;">999 BBG PLATTER</h3>
        <p style="color:var(--color-primary); font-weight:700; margin-bottom:16px;">Couple Platter, Serves 2 — ₹999</p>
        <p style="color:var(--color-muted); line-height:1.6;">Includes: 2 pcs fish finger, 2 pcs moru moru chicken, butter naan 1, plain gravy, chicken rice (manchow), chicken noodles (mongolian), chicken biryani, lemon fish 6 pcs, dragon prawn 6 pcs, hot pepper chicken 6 pcs, 1 elaneer payasam, 1 goli soda.</p>
    </div>
    
    <div style="background:var(--color-surface); padding:24px; border-radius:12px; border:1px solid var(--color-primary);">
        <h3 style="font-size:1.8rem; color:var(--color-gold); margin-bottom:8px;">1999 BBG PLATTER</h3>
        <p style="color:var(--color-primary); font-weight:700; margin-bottom:16px;">Family Platter, Serves 4 — ₹1999</p>
        <p style="color:var(--color-muted); line-height:1.6;">Includes: triple flavor kebab 9 pcs, 4 pcs fish finger, 3 pcs moru moru chicken, butter kulcha 1, plain gravy, chicken rice (manchow), chicken noodles (mongolian), 1 chicken/mutton biryani, chicken drumsticks 2 pcs, lemon fish 6 pcs, dragon prawn 6 pcs, hot pepper chicken 6 pcs, salt and pepper prawn 6 pcs, elaneer payasam 2, goli soda 2.</p>
    </div>
</section>
"""
create_page("platters.html", "BBG Platters | Bhai Biryani Godown — Couple & Family Platters Trichy", "999 BBG Couple Platter (serves 2) and 1999 BBG Family Platter (serves 4) at Bhai Biryani Godown Trichy. Complete feast.", "bbg platters, family platter, couple meal biryani", platters_content)

# ----------------- SOUP -----------------
soup_items = [("Pepper Soup - Veg", "₹100", ""), ("Pepper Soup - Chicken", "₹110", ""), ("Sweet Corn Soup - Veg", "₹100", ""), ("Sweet Corn Soup - Chicken", "₹110", ""), ("Hot & Sour Soup - Veg", "₹100", ""), ("Hot & Sour Soup - Chicken", "₹110", ""), ("Clear Soup - Veg", "₹100", ""), ("Clear Soup - Chicken", "₹110", ""), ("Tomato Soup", "₹100", ""), ("Cream Soup - Mushroom", "₹100", ""), ("Cream Soup - Chicken", "₹110", ""), ("Manchow Soup - Veg", "₹100", ""), ("Manchow Soup - Chicken", "₹110", ""), ("Mutton Bone Soup", "₹120", ""), ("Mutton Pepper Soup", "₹120", "")]
soup_content = f"""
<div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Soups</div>
<section style="padding: 60px 20px;">{menu_section_html("Warm & Comforting Soups", soup_items, False)}</section>
"""
create_page("soup.html", "Soups Menu | Bhai Biryani Godown Trichy", "Hot soups including Mutton Bone Soup, Pepper Soup, and Cream Soups at BBG.", "soups, mutton bone soup", soup_content)

print("Generated priority menus.")
