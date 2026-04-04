import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

regex_target = r'\s*<a href="testimonials\.html">\s*<span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke=".*?" stroke-width="2" class="i"><path d="M12 2l3\.09 6\.26L22 9\.27l-5 4\.87 1\.18 6\.88L12 17\.77l-6\.18 3\.25L7 14\.14 2 9\.27l6\.91-1\.01L12 2z"/></svg></span>\s*Reviews\s*</a>\s*(</nav>)'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Search for the bottom-nav Reviews link right before </nav>
    if re.search(regex_target, content):
        content = re.sub(regex_target, r'\n    \1', content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed from {file}")
