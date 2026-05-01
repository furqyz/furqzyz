import os
import re

html_files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]

for filename in html_files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the wrongly placed grid container that is right before the masonry closing </div>
    # Structure:
    # <div class="grid grid-cols-1 xl:grid-cols-2 gap-8 mt-8">
    # ...
    # </div>
    # </div>
    # <!-- SINAV HAFIZASI
    
    # We will capture the whole grid container:
    pattern = r'(<div class="grid grid-cols-1 xl:grid-cols-2 gap-8 mt-8">[\s\S]*?</div>)\s*(</div>)\s*(<!-- SINAV HAFIZASI|\s*<section class="exam-memory)'
    
    # And we swap the grid container with the </div>
    content = re.sub(pattern, r'\2\n            \1\n            \3', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Son iki kutunun grid yapısı masonry container'ının dışına çıkarıldı.")
