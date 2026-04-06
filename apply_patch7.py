"""
PATCH 7 — apply_patch7.py
Handles multi-file changes: logo swap, Tamil nav text, Wooden Fire → Wood Fired
"""
import os, re

BASE = r"c:\Users\ajana\Downloads\godown briyani"

HTML_FILES = [
    "index.html", "about.html", "menu.html", "contact.html",
    "biryani.html", "starters.html", "tandoori-bbq.html",
    "fried-rice-noodles.html", "soup.html", "gravy.html",
    "eggs.html", "breads.html", "veg.html", "bulk-orders.html",
    "platters.html", "pulao.html", "testimonials.html", "climax.html",
]

CATAMARAN_FONT = '''  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Catamaran:wght@900&display=swap" rel="stylesheet">'''

# Tamil text div to insert after logo img inside navbar-brand / nav anchor
TAMIL_DIV = '      <div class="navbar-tamil">பாய் பிரியாணி குடோன்</div>'

def patch_file(filename):
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        print(f"  SKIP (not found): {filename}")
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="cp1252") as f:
            content = f.read()

    original = content
    changed = []

    # ── FIX 1: Replace nav-logo img src with bbg-logo-new.png ──────────────
    # Pattern: any img with class="nav-logo" — replace src
    new_logo_img = '<img src="images/bbg-logo-new.png" alt="Bhai Biryani Godown" class="navbar-logo" width="120" height="60">'

    # Replace the nav img (class nav-logo) — various formats
    old_navlogo_pattern = re.compile(
        r'<img\s+src="images/bbg-logo(?:-filled|-outline)?\.png"[^>]*class="nav-logo"[^>]*/?>',
        re.DOTALL
    )
    if old_navlogo_pattern.search(content):
        content = old_navlogo_pattern.sub(new_logo_img, content)
        changed.append("nav-logo img replaced")

    # Also replace index.html's special anchor structure for the nav
    # index.html uses <a href="index.html" aria-label="..."><img class="nav-logo">
    # We need to add the Tamil div after the img + wrap in navbar-brand class
    # Only for index.html which has different nav structure
    if filename == "index.html":
        # index.html nav anchor: <a href="index.html" aria-label="...">
        old_nav_anchor = re.compile(
            r'(<a href="index\.html" aria-label="Bhai Biryani Godown Home">)\s*'
            r'(<img[^>]*class="navbar-logo"[^>]*/?>)\s*'
            r'(</a>)',
            re.DOTALL
        )
        def replace_index_nav(m):
            return (
                '<a href="index.html" class="navbar-brand" aria-label="Bhai Biryani Godown Home">\n'
                f'        {m.group(2)}\n'
                f'        {TAMIL_DIV.strip()}\n'
                '      </a>'
            )
        new_content = old_nav_anchor.sub(replace_index_nav, content)
        if new_content != content:
            content = new_content
            changed.append("index.html navbar-brand + Tamil div added")
    else:
        # Other pages: look for nav-logo-link anchor + nav-logo img
        old_nav_link = re.compile(
            r'(<a href="index\.html" class="nav-logo-link"[^>]*>)\s*'
            r'(<img[^>]*class="navbar-logo"[^>]*/?>)\s*'
            r'(</a>)',
            re.DOTALL
        )
        def replace_other_nav(m):
            return (
                '<a href="index.html" class="navbar-brand nav-logo-link" aria-label="Bhai Biryani Godown Home">\n'
                f'                {m.group(2)}\n'
                f'                <div class="navbar-tamil">பாய் பிரியாணி குடோன்</div>\n'
                '            </a>'
            )
        new_content = old_nav_link.sub(replace_other_nav, content)
        if new_content != content:
            content = new_content
            changed.append("navbar-brand + Tamil div added")

    # ── FIX 2: Add Catamaran font to <head> if not present ──────────────────
    if 'Catamaran' not in content:
        content = content.replace('</head>', CATAMARAN_FONT + '\n</head>', 1)
        changed.append("Catamaran font added")

    # ── FIX 3: "Wooden Fire" → "Wood Fired" (visible text only) ─────────────
    # Only replace visible pill/heading text, not aria-labels / alt texts describing the process
    wooden_fire_text = re.compile(r'\bWooden Fire\b')
    if wooden_fire_text.search(content):
        content = wooden_fire_text.sub('Wood Fired', content)
        changed.append("Wooden Fire → Wood Fired")

    # ── Write if changed ─────────────────────────────────────────────────────
    if content != original:
        with open(path, "w", encoding="utf-8", errors="replace") as f:
            f.write(content)
        print(f"  ✓ {filename}: {', '.join(changed)}")
    else:
        print(f"  – {filename}: no changes needed")


print("=== PATCH 7: Applying multi-file HTML changes ===\n")
for fn in HTML_FILES:
    patch_file(fn)

print("\n=== Done ===")
