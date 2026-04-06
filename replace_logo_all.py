"""
Replace bbg-logo-filled.png with bbg-logo-new.png EVERYWHERE in all HTML files.
Also fix hero-logo border-radius:50% (new logo is badge-style, not circular).
"""
import os, re, glob

BASE = r"c:\Users\ajana\Downloads\godown briyani"

html_files = glob.glob(os.path.join(BASE, "*.html"))

total_changed = 0

for path in sorted(html_files):
    filename = os.path.basename(path)

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="cp1252") as f:
            content = f.read()

    original = content

    # 1. Replace ALL occurrences of bbg-logo-filled.png → bbg-logo-new.png
    content = content.replace("images/bbg-logo-filled.png", "images/bbg-logo-new.png")
    # Also the JSON-LD logo URL
    content = content.replace(
        "https://yourdomain.com/images/bbg-logo-filled.png",
        "https://yourdomain.com/images/bbg-logo-new.png"
    )

    # 2. Remove border-radius:50% on hero-logo (badge is not circular)
    content = re.sub(
        r'(class="hero-logo"[^>]*?)(\s*border-radius:\s*50%\s*;)',
        r'\1',
        content
    )
    # Also fix inline style that has border-radius:50% alongside width
    content = re.sub(
        r'(style="[^"]*?)(;\s*border-radius:\s*50%|border-radius:\s*50%\s*;)([^"]*?")',
        lambda m: m.group(1) + m.group(3),
        content
    )

    # 3. Fix footer-logo: ensure no border-radius there either
    content = re.sub(
        r'(class="footer-logo"[^>]*?)(\s*style="[^"]*?border-radius[^"]*?")',
        lambda m: m.group(1),
        content
    )

    if content != original:
        with open(path, "w", encoding="utf-8", errors="replace") as f:
            f.write(content)
        print(f"  ✓ {filename}")
        total_changed += 1
    else:
        print(f"  – {filename} (no change needed)")

print(f"\n=== Done: {total_changed} files updated ===")
