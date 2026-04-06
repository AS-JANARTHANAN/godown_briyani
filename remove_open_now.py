import os, glob, re

BASE = r'c:\Users\ajana\Downloads\godown briyani'
html_files = glob.glob(os.path.join(BASE, '*.html'))

for path in html_files:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(path, 'r', encoding='cp1252') as f:
            content = f.read()
            
    original = content
    # Remove the branch-status div
    content = re.sub(r'<div class="branch-status open">● Open Now</div>\s*', '', content)

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Removed Open Now from {os.path.basename(path)}')
