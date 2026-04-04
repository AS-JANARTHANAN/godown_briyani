import sys

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# find the last occurrence of <!-- --- BRANCHES SECTION --- -->
start_idx = content.rfind('<!-- --- BRANCHES SECTION --- -->')
# find the next footer
end_idx = content.find('<!-- --- FOOTER --- -->', start_idx)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Now fix the CSS
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace border colors from orange to var(--color-primary)
css = css.replace('border: 1px solid rgba(232, 105, 42, 0.15);', 'border: 1px solid var(--color-primary);')
css = css.replace('border-color: rgba(232, 105, 42, 0.4);', 'border-color: var(--color-primary);')
css = css.replace('color: #9c7a5a', 'color: var(--color-muted)') # tags color to muted

# Button call colors to yellow theme (var(--color-primary) is #F5CB00)
css = css.replace('background: rgba(232, 105, 42, 0.1);', 'background: rgba(245, 203, 0, 0.1);')
css = css.replace('color: #e8692a;', 'color: var(--color-primary);')
css = css.replace('border-color: rgba(232, 105, 42, 0.3);', 'border-color: rgba(245, 203, 0, 0.3);')
css = css.replace('background: #e8692a;', 'background: var(--color-primary);')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

