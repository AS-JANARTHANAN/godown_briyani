import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(
    r'<button[^>]*class=["\'][^"\']*yellow[^"\']*["\'][^>]*>.*?</button>',
    '<a href="https://wa.me/917708863397?text=Hi%20I%20want%20to%20order%20the%20Biryani%20Combo" class="combo-order-btn" target="_blank">Order on WhatsApp</a>',
    text,
    flags=re.IGNORECASE | re.DOTALL
)

# Alternatively, if there's an inline style with comboWhatsAppOrder
text = re.sub(
    r'<button[^>]*comboWhatsAppOrder\(\)[^>]*>.*?</button>',
    '<a href="https://wa.me/917708863397?text=Hi%20I%20want%20to%20order%20the%20Biryani%20Combo" class="combo-order-btn" target="_blank">Order on WhatsApp</a>',
    text,
    flags=re.IGNORECASE | re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

css_to_add = '''
.combo-order-btn {
  display: block;
  width: 100%;
  padding: 14px;
  background: #e8692a;
  color: #1a0f00;
  text-align: center;
  font-weight: 700;
  font-size: 0.95rem;
  border-radius: 10px;
  text-decoration: none;
  margin-top: 16px;
  transition: background 0.2s;
  -webkit-tap-highlight-color: transparent;
}

.combo-order-btn:hover,
.combo-order-btn:active {
  background: #d45a1e;
}
'''
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.combo-order-btn {' not in css:
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css + '\n' + css_to_add)

