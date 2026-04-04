import os

emojis = {
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><path d="M12 2c0 0-6 7.5-6 12s4.5 8 6 8 6-3.5 6-8-6-12-6-12z"/><path d="M12 12c0 0-2 2-2 4s1.5 3 2 3 2-1.5 2-3-2-4-2-4z"/></svg>': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><path d="M12 2c0 0-6 7.5-6 12s4.5 8 6 8 6-3.5 6-8-6-12-6-12z"/><path d="M12 12c0 0-2 2-2 4s1.5 3 2 3 2-1.5 2-3-2-4-2-4z"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><path d="M2 22 22 2"/><path d="M12 2v10"/><path d="M12 12h10"/><path d="M6 8v6"/><path d="M6 14h6"/><path d="M18 14v6"/><path d="M12 20h6"/></svg>': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><path d="M2 22 22 2"/><path d="M12 2v10"/><path d="M12 12h10"/><path d="M6 8v6"/><path d="M6 14h6"/><path d="M18 14v6"/><path d="M12 20h6"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><circle cx="12" cy="16" r="6"/><path d="M10 10l2-4 2 4z"/><path d="M8 8l4-2 4 2"/></svg>': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><circle cx="12" cy="16" r="6"/><path d="M10 10l2-4 2 4z"/><path d="M8 8l4-2 4 2"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><rect x="4" y="6" width="16" height="12" rx="2"/><path d="M8 6v12"/><path d="M16 6v12"/></svg>': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><rect x="4" y="6" width="16" height="12" rx="2"/><path d="M8 6v12"/><path d="M16 6v12"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><rect x="2" y="8" width="14" height="10" rx="1"/><path d="M16 14h4l2-4h-6"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><rect x="2" y="8" width="14" height="10" rx="1"/><path d="M16 14h4l2-4h-6"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>'
}

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    for emoji, svg in emojis.items():
        if emoji in content:
            content = content.replace(emoji + " ", svg) # First try replacing text WITH trailing space to avoid double spacing
            content = content.replace(emoji, svg) # Then replace whatever is left without space
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Replaced emojis in {filepath}")

if __name__ == "__main__":
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith((".html", ".py")):
                replace_in_file(os.path.join(root, file))
