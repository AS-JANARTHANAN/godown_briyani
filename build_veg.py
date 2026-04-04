from generator import create_page, SVGS
from build_menus import menu_section_html

veg_starters = [
    ("Gobi (65/Manchurian/Chilli)", "₹140/₹180/₹180", ""),
    ("Mushroom (65/Manchurian/Chilli)", "₹150/₹200/₹200", ""),
    ("Paneer (65/Manchurian/Chilli)", "₹180/₹220/₹220", ""),
    ("Paneer Pepper Onion", "₹220", ""),
    ("Dragon Paneer", "₹250", ""),
    ("Paneer Tikka", "₹250", ""),
    ("Salt & Pepper Mushroom", "₹220", "")
]

veg_gravy = [
    ("Kadai (Paneer/Veg)", "₹220/₹200", ""),
    ("Masala (Mushroom/Gobi)", "₹200/₹170", ""),
    ("Mix Veg Curry", "₹200", ""),
    ("Paneer Butter Masala", "₹220", ""),
    ("Paneer Tikka Masala", "₹250", "")
]

veg_content = f"""
<section class="page-hero">
    <div class="page-hero-bg" data-parallax-speed="0.3" style="background-image: url('images/theme/gallery-1.webp'); opacity:0.3;"></div>
    <div class="page-hero-overlay"></div>
    <div class="page-hero-content" style="padding-top:100px;">
        <p class="page-hero-sub" style="color:var(--color-gold);">Fresh & Flavourful</p>
        <h1 class="page-hero-title">VEG SPECIALS</h1>
    </div>
</section>
<div class='breadcrumb'><a href='index.html'>Home</a> &nbsp;/&nbsp; Veg Specials</div>
<section style='padding: 60px 20px;'>
    {menu_section_html("Veg Starters", veg_starters, True)}
    {menu_section_html("Veg Gravy", veg_gravy, True)}
</section>
"""

create_page("veg.html", "Veg Specials | Bhai Biryani Godown Trichy", "Explore pure veg starters and gravies at Bhai Biryani Godown. Try our Paneer Tikka, Gobi 65, and Mix Veg Curry.", "veg starters Trichy, veg gravy BBG", veg_content)

print("Generated veg.html")
