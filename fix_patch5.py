import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .menu-card
# Remove any 'height:...' if it's there
css = re.sub(r'\n\s*height:\s*\d+px.*?;', '', css)

# Make menu-card use justify-content: center and tight heights
# I will just find the patch 4 menu-card block and fix it.
# We know the block is like:
# .menu-card {
#   display: flex !important;
#   flex-direction: column !important;
#   align-items: center !important;
#   justify-content: center !important;
#   gap: 10px !important;
#   padding: 24px 12px 20px !important;
#   min-height: 140px !important;

# The user explicitly said:
# .menu-card { justify-content: center; gap: 10px; padding: 24px 16px; min-height: 150px; height: auto; }
css = css.replace('min-height: 140px !important;', 'min-height: 150px !important;\n  height: auto !important;')
css = css.replace('min-height: 160px !important;', 'min-height: 180px !important;')
css = css.replace('justify-content: space-between !important;', 'justify-content: center !important;')
css = css.replace('justify-content: space-between;', 'justify-content: center;')

# Add flex-grow constraints
grow_shrink_css = '''
.menu-card-icon,
.menu-card-name,
.menu-card-price {
  flex-grow: 0 !important;
  flex-shrink: 0 !important;
}
'''
if '.menu-card-icon,' not in css:
    css += grow_shrink_css

# 2. Fix the Yellow Theme everywhere to use Orange
# We previously used '#F5CB00' and 'var(--color-primary)' which WAS orange. Wait, var(--color-primary) was orange initially? Let's check.
# Let's just do a thorough replace:
css = css.replace('#F5CB00', '#e8692a')
css = css.replace('var(--color-primary)', '#e8692a')
css = css.replace('#FFD700', '#e8692a')
css = css.replace('#FFCC00', '#e8692a')
css = css.replace('#F5C518', '#e8692a')
css = css.replace('#FFC300', '#e8692a')

# The branch button hover was #1a0f00 but using variable, let's fix the call button
css = css.replace('.btn-call {\n  background: rgba(245, 203, 0, 0.1);\n  color: #e8692a;\n  border-color: rgba(245, 203, 0, 0.3);\n}', '.btn-call {\n  background: rgba(232, 105, 42, 0.1);\n  color: #e8692a;\n  border-color: rgba(232, 105, 42, 0.3);\n}')

# Wait, the user had specific rules for CTA buttons:
btn_rules = '''
/* Main CTA buttons — orange */
.btn-whatsapp-primary,
.order-btn,
.cta-btn,
button[class*="whatsapp"],
a[class*="order"] {
  background: #e8692a;
  color: #1a0f00;
  border: none;
  font-weight: 700;
}

.btn-whatsapp-primary:hover,
.order-btn:hover {
  background: #d45a1e;
}

/* Floating WhatsApp bubble */
.whatsapp-float {
  background: #25D366 !important;
}
'''
css += btn_rules

# Apply root vars
root_vars = '''
:root {
  --color-bg:        #1a0f00;
  --color-surface:   #231508;
  --color-primary:   #e8692a;
  --color-gold:      #c9a060;
  --color-text:      #f5ede0;
  --color-muted:     #9c7a5a;
  --color-whatsapp:  #25D366;
}
'''
if '--color-primary:   #e8692a;' not in css:
    css += root_vars

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

