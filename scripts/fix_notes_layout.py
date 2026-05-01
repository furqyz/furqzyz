import os
import re

files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]
for filename in files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove xl:col-span-2 from EKLENEN KRİTİK KAVRAMLAR sections
    content = content.replace('xl:col-span-2', '')
    
    # Change grid layouts inside these specific boxes to single column stack so they look good in masonry
    content = content.replace('grid grid-cols-1 md:grid-cols-3 gap-4', 'flex flex-col gap-4')
    content = content.replace('grid grid-cols-1 md:grid-cols-2 gap-4', 'flex flex-col gap-4')
    content = content.replace('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4', 'flex flex-col gap-4')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("HTML dosyalarındaki eklenen notların grid yapısı düzeltildi.")
