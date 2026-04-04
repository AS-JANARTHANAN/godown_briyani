import re

# Page config: (filename, bg_image, sub_label, title, tagline, breadcrumb_name)
pages = [
    (
        "starters.html",
        "images/dishes/starters/chicken-65-boneless.webp",
        "Starters & Appetizers",
        "STARTERS",
        "Crispy, Spicy & Bold",
        "Starters",
    ),
    (
        "fried-rice-noodles.html",
        "images/dishes/friedrice/mixed-fried-rice.webp",
        "Wok-Tossed Favourites",
        "FRIED RICE & NOODLES",
        "Indo-Chinese Done Right",
        "Fried Rice &amp; Noodles",
    ),
    (
        "tandoori-bbq.html",
        "images/dishes/tandoori/tandoori-chicken.webp",
        "Tandoori &amp; Arabic Grill",
        "TANDOORI & GRILL",
        "Flame-Kissed Perfection",
        "Tandoori &amp; BBQ",
    ),
    (
        "soup.html",
        "images/dishes/friedrice/mushroom-fried-rice.webp",  # closest warm dish; no soup folder
        "Hot &amp; Hearty",
        "SOUPS",
        "Warmth in Every Sip",
        "Soups",
    ),
    (
        "gravy.html",
        "images/dishes/main-course/pepper-chicken-masala.webp",
        "Rich Gravies &amp; Curries",
        "GRAVIES",
        "Bold Flavours, Deep Spices",
        "Gravies",
    ),
    (
        "breads.html",
        "images/dishes/breads/butter-naan.webp",
        "From the Tandoor",
        "BREADS",
        "Soft, Fluffy &amp; Fresh",
        "Breads",
    ),
    (
        "pulao.html",
        "images/dishes/briyani/chicken-plain-biryani.webp",  # closest to pulao
        "Fragrant &amp; Light",
        "PULAO",
        "Aromatic Rice, Pure Comfort",
        "Pulao",
    ),
    (
        "eggs.html",
        "images/dishes/starters/kaadai-65.webp",  # closest egg-like starter
        "Egg Specials",
        "EGGS",
        "Simple. Satisfying. Always Fresh.",
        "Eggs",
    ),
    (
        "climax.html",
        "images/dishes/sweets/kalyana-bread-halwa.webp",
        "Sweets &amp; Drinks",
        "SWEETS & DRINKS",
        "End on a Sweet Note",
        "Sweets &amp; Drinks",
    ),
]

def make_hero(bg_image, sub_label, title, tagline, breadcrumb_name):
    return f"""
<section class="page-hero">
    <div class="page-hero-bg" data-parallax-speed="0.3" style="background-image: url('{bg_image}'); opacity:0.6;"></div>
    <div class="page-hero-overlay"></div>
    <div class="page-hero-content" style="padding-top:100px;">
        <p class="page-hero-sub" style="color:var(--color-gold);">{sub_label}</p>
        <h1 class="page-hero-title">{title}</h1>
        <p style="color:var(--color-text); margin-top:16px;">{tagline}</p>
    </div>
</section>
<div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; {breadcrumb_name}</div>
"""

for filename, bg_image, sub_label, title, tagline, breadcrumb_name in pages:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if hero already exists
    if 'class="page-hero"' in content:
        print(f"SKIP {filename} - already has hero")
        continue

    # Find the insertion point: after the mobile menu drawer closing div, before page content
    # Look for the pattern: "<!-- ═══ PAGE CONTENT ═══ -->"
    marker = "<!-- ═══ PAGE CONTENT ═══ -->"
    
    if marker in content:
        hero_html = make_hero(bg_image, sub_label, title, tagline, breadcrumb_name)
        # Replace the marker + whatever breadcrumb/section was directly after
        # We'll insert hero right after the marker
        # First, remove any existing breadcrumb that's inline on line 69
        # Replace the old breadcrumb+section opener if it's on same line
        old_pattern = marker + r"\n\s*<div class='breadcrumb'>[^<]*<a href='index\.html'>Home</a>[^<]*</div>"
        new_part = marker + "\n" + hero_html
        new_content = re.sub(old_pattern, new_part, content, flags=re.DOTALL)
        
        if new_content == content:
            # fallback: just insert after marker
            new_content = content.replace(marker, marker + "\n" + hero_html)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"DONE {filename}")
    else:
        print(f"WARN {filename} - marker not found, trying fallback")
        # Fallback: insert after mobile menu overlay closing
        fallback_marker = "<!-- ═══ PAGE CONTENT ═══ -->"
        if fallback_marker not in content:
            # Try after </div> of mobile menu panel
            insert_after = "    </div>\n</div>\n\n    <!-- ═══ PAGE CONTENT ═══ -->"
            print(f"  No marker in {filename}")

print("Done!")
