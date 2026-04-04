from generator import create_page, SVGS

menu_content = f"""
<div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Full Menu</div>
<section style="padding: 40px 20px;">
    <h1 class="section-title text-center" style="font-size:2.5rem; text-align:center; margin-bottom:16px;">Our Menu</h1>
    <p style="text-align: center; color:var(--color-muted); margin-bottom:32px;">Click a category to view the full list and prices</p>
    
    <style>
      .new-menu-grid {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
      }}
      @media (min-width: 768px) {{
        .new-menu-grid {{
          grid-template-columns: repeat(3, 1fr);
          gap: 24px;
        }}
      }}
    </style>
    
    <div class="new-menu-grid">
      <a href="biryani.html" class="menu-card" style="text-align:center;">
        {SVGS['BIRYANI']}
        <div class="menu-card-name">Biryani</div>
        <div class="menu-card-from">from ₹100</div>
      </a>
      <a href="platters.html" class="menu-card" style="text-align:center;">
        {SVGS['PLATTERS']}
        <div class="menu-card-name">Platters</div>
        <div class="menu-card-from">from ₹999</div>
      </a>
      <a href="starters.html" class="menu-card" style="text-align:center;">
        {SVGS['STARTERS']}
        <div class="menu-card-name">Starters</div>
        <div class="menu-card-from">from ₹140</div>
      </a>
      <a href="fried-rice-noodles.html" class="menu-card" style="text-align:center;">
        {SVGS['FRIED RICE']}
        <div class="menu-card-name">Fried Rice & Noodles</div>
        <div class="menu-card-from">from ₹140</div>
      </a>
      <a href="tandoori-bbq.html" class="menu-card" style="text-align:center;">
        {SVGS['TANDOORI']}
        <div class="menu-card-name">Tandoori & Arabic grill</div>
        <div class="menu-card-from">from ₹160</div>
      </a>
      <a href="soup.html" class="menu-card" style="text-align:center;">
        {SVGS['SOUP']}
        <div class="menu-card-name">Soups</div>
        <div class="menu-card-from">from ₹100</div>
      </a>
      <a href="gravy.html" class="menu-card" style="text-align:center;">
        <svg viewBox="0 0 40 40" fill="none" class="i" stroke="#F5CB00" stroke-width="1.5" style="width:40px;height:40px;margin-bottom:8px;"><path d="M10 32 C14 20 30 10 32 8 C30 10 32 26 20 30 C14 32 10 32 10 32Z"/><path d="M10 32 L22 20"/></svg>
        <div class="menu-card-name">Gravies</div>
        <div class="menu-card-from">from ₹170</div>
      </a>
      <a href="veg.html" class="menu-card" style="text-align:center;">
        {SVGS['VEG']}
        <div class="menu-card-name">Veg Specials</div>
        <div class="menu-card-from">from ₹140</div>
      </a>
      <a href="breads.html" class="menu-card" style="text-align:center;">
        <svg viewBox="0 0 40 40" fill="none" class="i" stroke="#F5CB00" stroke-width="1.5" style="width:40px;height:40px;margin-bottom:8px;"><ellipse cx="20" cy="20" rx="14" ry="10"/></svg>
        <div class="menu-card-name">Indian Breads</div>
        <div class="menu-card-from">from ₹60</div>
      </a>
      <a href="pulao.html" class="menu-card" style="text-align:center;">
        <svg viewBox="0 0 40 40" fill="none" class="i" stroke="#F5CB00" stroke-width="1.5" style="width:40px;height:40px;margin-bottom:8px;"><path d="M10 26 C10 19 13 14 20 13 C27 14 30 19 30 26"/></svg>
        <div class="menu-card-name">Pulao</div>
        <div class="menu-card-from">from ₹170</div>
      </a>
      <a href="eggs.html" class="menu-card" style="text-align:center;">
        <svg viewBox="0 0 40 40" fill="none" class="i" stroke="#F5CB00" stroke-width="1.5" style="width:40px;height:40px;margin-bottom:8px;"><ellipse cx="20" cy="20" rx="8" ry="12"/></svg>
        <div class="menu-card-name">Eggs</div>
        <div class="menu-card-from">from ₹20</div>
      </a>
      <a href="climax.html" class="menu-card" style="text-align:center;">
        {SVGS['SWEETS']}
        <div class="menu-card-name">Sweets & Drinks</div>
        <div class="menu-card-from">from ₹20</div>
      </a>
    </div>
</section>
"""
create_page("menu.html", "Full Menu — Bhai Biryani Godown Trichy", "Explore the full menu of Bhai Biryani Godown. Try our Seeraga Samba Biryani, Tandoori, Fried Rice, Soups and more.", "bbg menu, biryani godown full menu, trichy biryani menu", menu_content, True)

print("Generated menu.html hub")
