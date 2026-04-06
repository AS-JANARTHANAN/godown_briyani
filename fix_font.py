"""
Replace Catamaran font with Baloo Thambi 2 across all HTML files.
Baloo Thambi 2 is the closest Google Font match to the bold
Tamil shop-sign style seen on the BBG menu board.
"""
import os, glob

BASE = r"c:\Users\ajana\Downloads\godown briyani"

OLD_LINK = 'https://fonts.googleapis.com/css2?family=Catamaran:wght@900&display=swap'
NEW_LINK = 'https://fonts.googleapis.com/css2?family=Baloo+Thambi+2:wght@800&display=swap'

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

    # Replace font URL in <link> tags
    content = content.replace(OLD_LINK, NEW_LINK)

    if content != original:
        with open(path, "w", encoding="utf-8", errors="replace") as f:
            f.write(content)
        print(f"  ✓ {fname}")
        changed += 1
    else:
        print(f"  – {fname}")

print(f"\n=== {changed} HTML files updated ===")
