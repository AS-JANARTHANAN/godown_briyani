import re

file_path = 'menu.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Strip the inline <style> we don't need
content = re.sub(r'<style>.*?\.new-menu-grid.*?</style>\s*', '', content, flags=re.DOTALL)

# 2. Change <div class="new-menu-grid"> to <div class="menu-grid">
content = content.replace('<div class="new-menu-grid">', '<div class="menu-grid">')

# 3. Fix each a-tag structure
def fix_card(match):
    anchor_start = match.group(1) # <a href="..." class="menu-card" style="...">
    svg = match.group(2)          # <svg ...>...</svg>
    name = match.group(3)         # <div class="menu-card-name">...</div>
    price_tag = match.group(4)    # <div class="menu-card-from">...</div> or none
    
    # Clean anchor inline style
    anchor_clean = re.sub(r'\s*style="[^"]*"', '', anchor_start)
    
    # Extract inner text
    name_text = re.sub(r'<[^>]+>', '', name).strip()
    price_text = re.sub(r'<[^>]+>', '', price_tag).strip() if price_tag else ""
    
    # Construct new HTML
    new_html = f"{anchor_clean}\n"
    new_html += f'        <div class="menu-card-icon">\n          {svg}\n        </div>\n'
    new_html += f'        <span class="menu-card-name">{name_text}</span>\n'
    if price_text:
        new_html += f'        <span class="menu-card-from">{price_text}</span>\n'
    new_html += "      </a>"
    return new_html

# Regex to match the individual cards in menu.html
# Group 1: anchor open tag
# Group 2: svg tag
# Group 3: name div
# Group 4: price div (optional, for full menu there might be strong tag)
pattern = r'(<a\s+[^>]*?class="[^\"]*?menu-card[^\"]*?"[^>]*>)\s*(<svg[\s\S]*?</svg>)\s*(<div class="menu-card-name">[\s\S]*?</div>)\s*(<div class="menu-card-from">[\s\S]*?</div>)?\s*</a>'

content = re.sub(pattern, fix_card, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Menu.html structured.")
