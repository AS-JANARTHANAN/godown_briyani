"""
Script to replace the Tamil text element in the navbar with an image element across all HTML files.
"""
import os, glob, re

BASE = r"c:\Users\ajana\Downloads\godown briyani"
html_files = glob.glob(os.path.join(BASE, "*.html"))

changed = 0

for path in sorted(html_files):
    fname = os.path.basename(path)
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="cp1252") as f:
            content = f.read()

    original = content

    # Replace <div class="navbar-tamil">பாய் பிரியாணி குடோன்</div> with the image
    # Note: we use regular expressions to handle possible spacing variations
    pattern = re.compile(r'<div class="navbar-tamil"[^>]*>பாய் பிரியாணி குடோன்</div>')
    replacement = r'<img src="images/tamil_text_golden_yellow.png" alt="பாய் பிரியாணி குடோன்" class="navbar-tamil-img">'
    
    content = pattern.sub(replacement, content)

    if content != original:
        with open(path, "w", encoding="utf-8", errors="replace") as f:
            f.write(content)
        print(f"  ✓ {fname}")
        changed += 1
    else:
        print(f"  – {fname} (NO MATCH)")

print(f"\n=== {changed} HTML files updated ===")
