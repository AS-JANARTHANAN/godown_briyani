import re

files = ['index.html', 'menu.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the menu grid section and replace it entirely
    # The start is <section style="padding: 60px 20px;"> or similar for index,
    # and <section style="padding: 40px 20px;"> for menu.html
    # We can match from <div class="new-menu-grid"> to the end of the section
    
    replacement = '''<div class="menu-grid">

    <a href="biryani.html" class="menu-card">
      <div class="menu-card-icon">
        <svg viewBox="0 0 40 40" fill="none" stroke="#F5CB00" stroke-width="1.5" class="i"><ellipse cx="20" cy="26" rx="14" ry="7"/><path d="M6 26 C6 34 34 34 34 26"/><path d="M10 26 C10 19 13 14 20 13 C27 14 30 19 30 26"/><line x1="20" y1="13" x2="20" y2="9"/><line x1="16" y1="10" x2="20" y2="9"/><line x1="24" y1="10" x2="20" y2="9"/></svg>
      </div>
      <span class="menu-card-name">Biryani</span>
      <span class="menu-card-from">from ?100</span>
    </a>

    <a href="platters.html" class="menu-card">
      <div class="menu-card-icon">
        <svg viewBox="0 0 40 40" fill="none" stroke="#F5CB00" stroke-width="1.5" class="i"><circle cx="20" cy="22" r="14"/><circle cx="20" cy="22" r="10"/><ellipse cx="20" cy="10" rx="5" ry="2"/></svg>
      </div>
      <span class="menu-card-name">Platters</span>
      <span class="menu-card-from">from ?999</span>
    </a>

    <a href="starters.html" class="menu-card">
      <div class="menu-card-icon">
        <svg viewBox="0 0 40 40" fill="none" stroke="#F5CB00" stroke-width="1.5" class="i"><ellipse cx="26" cy="14" rx="8" ry="6" transform="rotate(-30 26 14)"/><path d="M21 18 L12 30"/><line x1="10" y1="30" x2="14" y2="34"/><line x1="12" y1="28" x2="16" y2="32"/></svg>
      </div>
      <span class="menu-card-name">Starters</span>
      <span class="menu-card-from">from ?140</span>
    </a>

    <a href="fried-rice-noodles.html" class="menu-card">
      <div class="menu-card-icon">
        <svg viewBox="0 0 40 40" fill="none" stroke="#F5CB00" stroke-width="1.5" class="i"><path d="M8 20 C8 30 32 30 32 20"/><ellipse cx="20" cy="20" rx="12" ry="4"/><line x1="15" y1="10" x2="18" y2="22"/><line x1="25" y1="9" x2="22" y2="22"/></svg>
      </div>
      <span class="menu-card-name">Fried Rice</span>
      <span class="menu-card-from">from ?140</span>
    </a>

    <a href="tandoori-bbq.html" class="menu-card">
      <div class="menu-card-icon">
        <svg viewBox="0 0 40 40" fill="none" stroke="#F5CB00" stroke-width="1.5" class="i"><path d="M20 8 C20 8 28 16 28 23 C28 28 24 32 20 32 C16 32 12 28 12 23 C12 16 20 8 20 8Z"/><path d="M20 18 C20 18 24 22 24 25 C24 27 22 29 20 29"/></svg>
      </div>
      <span class="menu-card-name">Tandoori & BBQ</span>
      <span class="menu-card-from">from ?160</span>
    </a>

    <a href="soup.html" class="menu-card">
      <div class="menu-card-icon">
        <svg viewBox="0 0 40 40" fill="none" stroke="#F5CB00" stroke-width="1.5" class="i"><path d="M8 24 C8 32 32 32 32 24 L30 20 L10 20 Z"/><line x1="14" y1="12" x2="14" y2="16"/><line x1="20" y1="10" x2="20" y2="16"/><line x1="26" y1="12" x2="26" y2="16"/></svg>
      </div>
      <span class="menu-card-name">Soups</span>
      <span class="menu-card-from">from ?100</span>
    </a>

    <a href="gravy.html" class="menu-card">
      <div class="menu-card-icon">
        <svg viewBox="0 0 40 40" fill="none" stroke="#F5CB00" stroke-width="1.5" class="i"><path d="M10 32 C14 20 30 10 32 8 C30 10 32 26 20 30 C14 32 10 32 10 32Z"/><path d="M10 32 L22 20"/></svg>
      </div>
      <span class="menu-card-name">Gravies</span>
      <span class="menu-card-from">from ?170</span>
    </a>

    <a href="bulk-orders.html" class="menu-card">
      <div class="menu-card-icon">
        <svg viewBox="0 0 40 40" fill="none" stroke="#F5CB00" stroke-width="1.5" class="i"><rect x="8" y="12" width="24" height="22" rx="2"/><line x1="8" y1="18" x2="32" y2="18"/><line x1="15" y1="8" x2="15" y2="14"/><line x1="25" y1="8" x2="25" y2="14"/><rect x="14" y="22" width="4" height="4"/><rect x="22" y="22" width="4" height="4"/></svg>
      </div>
      <span class="menu-card-name">Bulk Orders</span>
      <span class="menu-card-from">Weddings & Events</span>
    </a>

    <!-- Full menu — spans full width -->
    <a href="menu.html" class="menu-card full-menu">
      <span class="menu-card-name">Full Menu</span>
      <span>All items ?</span>
    </a>

  </div>'''

    # Remove the embedded <style> and .new-menu-grid entirely
    content = re.sub(r'<style>.*?\.new-menu-grid\s*{.*?</style>\s*<div class="new-menu-grid">.*?</div>\s*(</section>|<!-- ---)', replacement + r'\n\1', content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated menu layout.")
