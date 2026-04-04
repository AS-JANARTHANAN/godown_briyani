import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The review blocks we want to add
bottom_nav_link = '''        <a href="testimonials.html">
            <span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg></span>
            Reviews
        </a>
    </nav>'''

desktop_link = '''<a href="about.html">About</a>
                <a href="contact.html">Contact</a>
                <a href="testimonials.html">Reviews</a>'''

footer_link = '''<a href="menu.html">Menu</a>
            <a href="contact.html">Contact</a>
            <a href="testimonials.html">Reviews</a>'''

mobile_menu_link = '''<a href="about.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg> About Us</a>
            <a href="testimonials.html"><svg viewBox="0 0 24 24" fill="none" stroke="#F5CB00" stroke-width="2" class="i"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg> Reviews</a>'''

for file in html_files:
    if file == 'testimonials.html':
        continue # I already added links to this one manually!

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add to bottom-nav
    if '<a href="testimonials.html">' not in content:
        # bottom-nav
        content = re.sub(r'\s*</nav>', '\n' + bottom_nav_link, content, count=1)
        
        # desktop-links
        content = content.replace('<a href="about.html">About</a>\n                <a href="contact.html">Contact</a>', desktop_link)
        
        # footer-links
        content = content.replace('<a href="menu.html">Menu</a>\n            <a href="contact.html">Contact</a>', footer_link)
        # alternate footer spacing
        content = content.replace('<a href="menu.html">Menu</a>\n      <a href="contact.html">Contact</a>', '<a href="menu.html">Menu</a>\n      <a href="contact.html">Contact</a>\n      <a href="testimonials.html">Reviews</a>')

        # mobile-menu
        content = content.replace('<a href="about.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg> About Us</a>', mobile_menu_link)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
