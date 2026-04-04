import os

filepath = 'build_index.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target_block = """      <div class="story-stats" style="display:flex; justify-content:center; gap:16px; border:none;">
         <span style="background:var(--color-surface); padding:8px 16px; border-radius:20px; font-size:0.9rem; border:1px solid var(--color-gold);"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><path d="M12 2c0 0-6 7.5-6 12s4.5 8 6 8 6-3.5 6-8-6-12-6-12z"/><path d="M12 12c0 0-2 2-2 4s1.5 3 2 3 2-1.5 2-3-2-4-2-4z"/></svg>Wooden Fire</span>
         <span style="background:var(--color-surface); padding:8px 16px; border-radius:20px; font-size:0.9rem; border:1px solid var(--color-gold);"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><path d="M2 22 22 2"/><path d="M12 2v10"/><path d="M12 12h10"/><path d="M6 8v6"/><path d="M6 14h6"/><path d="M18 14v6"/><path d="M12 20h6"/></svg>Seeraga Samba</span>
         <span style="background:var(--color-surface); padding:8px 16px; border-radius:20px; font-size:0.9rem; border:1px solid var(--color-gold);"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="i" style="width:20px;height:20px;vertical-align:middle;margin-right:6px;"><circle cx="12" cy="16" r="6"/><path d="M10 10l2-4 2 4z"/><path d="M8 8l4-2 4 2"/></svg>Kalyana Style</span>
      </div>"""

replacement_block = """      <div class="story-stats" style="display:grid; grid-template-columns: repeat(3, 1fr); gap:12px; max-width: 380px; margin: 0 auto; border:none; padding:0;">
         <div style="background:var(--color-surface); padding:16px 8px; border-radius:16px; font-size:0.9rem; border:1px solid var(--color-gold); text-align:center; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
            <svg viewBox="0 0 24 24" fill="none" stroke="var(--color-gold)" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" style="width:28px;height:28px;display:block;margin:0 auto 10px;">
              <path d="M8 21L16 15M16 21L8 15"/>
              <path d="M12 15C12 15 6 9 10 3C10 3 16 7 15 11C14.3 13.8 12 15 12 15Z"/>
            </svg>
            <span style="display:block; line-height:1.3; font-weight:600;">Wooden<br>Fire</span>
         </div>
         <div style="background:var(--color-surface); padding:16px 8px; border-radius:16px; font-size:0.9rem; border:1px solid var(--color-gold); text-align:center; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
            <svg viewBox="0 0 24 24" fill="none" stroke="var(--color-gold)" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" style="width:28px;height:28px;display:block;margin:0 auto 10px;">
              <path d="M12 21V5"/>
              <path d="M12 5C12 5 10 1 8 3C8 3 10 7 12 5Z"/>
              <path d="M12 10C12 10 8 7 5 9C5 9 8 13 12 10Z"/>
              <path d="M12 10C12 10 16 7 19 9C19 9 16 13 12 10Z"/>
              <path d="M12 15C12 15 9 13 6 16C6 16 9 19 12 15Z"/>
              <path d="M12 15C12 15 15 13 18 16C18 16 15 19 12 15Z"/>
            </svg>
            <span style="display:block; line-height:1.3; font-weight:600;">Seeraga<br>Samba</span>
         </div>
         <div style="background:var(--color-surface); padding:16px 8px; border-radius:16px; font-size:0.9rem; border:1px solid var(--color-gold); text-align:center; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
            <svg viewBox="0 0 24 24" fill="none" stroke="var(--color-gold)" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" style="width:28px;height:28px;display:block;margin:0 auto 10px;">
              <path d="M22 10C18 16 10 18 2 12C6 6 14 4 22 10Z"/>
              <path d="M2 12S6 15 12 15S22 10 22 10"/>
              <circle cx="8" cy="11.5" r="1"/>
              <circle cx="12" cy="11" r="1.5"/>
              <circle cx="16" cy="10" r="1"/>
            </svg>
            <span style="display:block; line-height:1.3; font-weight:600;">Kalyana<br>Style</span>
         </div>
      </div>"""

if target_block in content:
    content = content.replace(target_block, replacement_block)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced stats successfully!")
else:
    print("Target block not found. Checking if it was already replaced or if formatting changed.")
