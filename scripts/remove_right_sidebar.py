import os
import re

files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]
for filename in files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Revert wrapper classes
    content = content.replace('max-w-[1800px] mx-auto flex flex-col xl:flex-row gap-6 lg:gap-8 p-4 md:p-6 lg:px-8', 'max-w-[1600px] mx-auto flex flex-col lg:flex-row gap-8 lg:gap-12 p-4 md:p-8 lg:px-12')
    content = content.replace('w-full xl:w-72 shrink-0', 'w-full lg:w-72 shrink-0')
    
    # Remove Right Sidebar
    pattern = r'\s*<!-- Sağ Sidebar \(Hap Bilgiler\) -->\s*<aside class="w-full xl:w-\[320px\] shrink-0 hidden xl:block">[\s\S]*?</aside>'
    content = re.sub(pattern, '', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("HTML dosyaları eski haline döndürüldü.")
