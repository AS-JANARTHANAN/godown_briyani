import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'testimonials.html']

reviews_mobile_link = '''<a href="testimonials.html">
        <svg viewBox="0 0 24 24" fill="none" stroke="#F5CB00" stroke-width="2" class="i"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
        Reviews
      </a>'''
      
reviews_desktop_link = '''<a href="testimonials.html">Reviews</a>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add to mobile-menu-panel ONLY IF NOT PRESENT
    if 'href="testimonials.html"' not in content:
        # Add to the end of mobile menu panel before closing div
        # Find inner HTML of mobile-menu-panel
        content = re.sub(
            r'(<div class="mobile-menu-panel">.*?)(</div>)',
            lambda m: m.group(1) + reviews_mobile_link + '\n    ' + m.group(2),
            content,
            flags=re.DOTALL
        )
        
        # 2. Add to desktop-links
        content = re.sub(
            r'(<div\s?[^>]*?class="desktop-links"[^>]*>.*?)(</div>)',
            lambda m: m.group(1) + '    ' + reviews_desktop_link + '\n    ' + m.group(2),
            content,
            flags=re.DOTALL
        )
        
        # 3. Add to footer links
        content = re.sub(
            r'(<div class="footer-links">.*?)(</div>)',
            lambda m: m.group(1) + reviews_desktop_link + '\n        ' + m.group(2),
            content,
            flags=re.DOTALL
        )
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
