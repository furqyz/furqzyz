import os
import re

files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]
for filename in files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Revert back to masonry
    content = content.replace('class="grid grid-cols-1 xl:grid-cols-2 gap-8 items-start"', 'class="columns-1 xl:columns-2 gap-8 space-y-8"')
    content = content.replace('class="grid grid-cols-1 xl:grid-cols-2 gap-6 items-start"', 'class="columns-1 xl:columns-2 gap-6 space-y-6"')
    content = content.replace('class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-start"', 'class="columns-1 lg:columns-2 gap-8 space-y-8"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("HTML dosyaları eski Sütun (Masonry) düzenine döndürüldü.")
