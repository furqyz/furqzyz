import os
import re

files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]
for filename in files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace masonry container with CSS Grid container
    content = content.replace('class="columns-1 xl:columns-2 gap-8 space-y-8"', 'class="grid grid-cols-1 xl:grid-cols-2 gap-8 items-start"')
    # Some pages might have a slightly different spacing class if I tweaked them manually
    content = content.replace('class="columns-1 xl:columns-2 gap-6 space-y-6"', 'class="grid grid-cols-1 xl:grid-cols-2 gap-6 items-start"')
    content = content.replace('class="columns-1 lg:columns-2 gap-8 space-y-8"', 'class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-start"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("HTML dosyalarındaki kolon yapısı Grid sistemine geçirildi.")
