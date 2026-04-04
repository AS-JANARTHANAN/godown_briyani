import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

def replace_btn(match):
    body = match.group(0)
    # The button starts with <button and ends with </button>
    return re.sub(
        r'<button[^>]*>.*?</button>',
        '<a href="https://wa.me/917708863397?text=Hi%20I%20want%20to%20order%20the%20Biryani%20Combo" class="combo-order-btn" target="_blank">Order on WhatsApp</a>',
        body,
        flags=re.DOTALL
    )

new_text = re.sub(r'<div class="combo-body">.*?</div>', replace_btn, text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

