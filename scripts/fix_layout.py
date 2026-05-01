import os
import re

files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]
for filename in files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove the broken wrapper that makes it full width
    pattern1 = r'</div>\s*</div>\s*<div class="columns-1 gap-8 space-y-8">\s*<!-- EKLENEN KRİTİK KAVRAMLAR -->'
    content = re.sub(pattern1, '<!-- EKLENEN KRİTİK KAVRAMLAR -->', content)
    
    # Also remove the closing div of that wrapper if it exists before SINAV HAFIZASI
    pattern2 = r'</section>\s*</div>\s*(<!-- SINAV HAFIZASI|\s*<section class="exam-memory)'
    content = re.sub(pattern2, r'</section>\n            </div>\n            \1', content)

    # Let's write a smarter regex if the above is too specific:
    # Actually, let's just find and replace the exact strings we injected.
    # In `add_notes2.py`, we injected:
    # `\n            </div>\n            <div class=\"columns-1 gap-8 space-y-8\">\n` + content_to_add + `\n            </div>\n`
    # We want to replace `\n            </div>\n            <div class="columns-1 gap-8 space-y-8">\n` with `\n`
    # And replace the trailing `\n            </div>\n` before `<!-- SINAV HAFIZASI` with nothing (since it balances the container we didn't close).

    # Let's try to do it robustly:
    content = content.replace('</div>\n            <div class="columns-1 gap-8 space-y-8">\n                <!-- EKLENEN KRİTİK KAVRAMLAR -->', '<!-- EKLENEN KRİTİK KAVRAMLAR -->')
    content = content.replace('</div>\n            <div class="columns-1 gap-8 space-y-8">\n\n                <!-- EKLENEN KRİTİK KAVRAMLAR -->', '<!-- EKLENEN KRİTİK KAVRAMLAR -->')
    content = content.replace('</div>\n            <div class="columns-1 gap-8 space-y-8">\n<!-- EKLENEN KRİTİK KAVRAMLAR -->', '<!-- EKLENEN KRİTİK KAVRAMLAR -->')
    
    # Wait, the closing div we added after content_to_add was `\n            </div>\n` right before `<!-- SINAV HAFIZASI`.
    # Let's fix the nesting. We want <!-- EKLENEN KRİTİK KAVRAMLAR --> to be INSIDE the masonry grid.
    # So we remove the `</div>` that was before it, and we don't need the `<div class="columns-1 gap-8 space-y-8">`.
    # And we KEEP the `</div>` after it to close the masonry grid!
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("HTML dosyaları düzeltildi.")
