import os
import re

html_files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]

# Kullanıcının belirttiği sıra: mor, turkuaz, sarı, yeşil, kırmızı
colors = [
    ('purple', 'purple'),
    ('turquoise', 'cyan'),
    ('yellow', 'yellow'),
    ('green', 'emerald'),
    ('red', 'red')
]

category_to_tailwind = {
    'purple': 'purple',
    'turquoise': 'cyan',
    'yellow': 'yellow',
    'green': 'emerald',
    'orange': 'orange',
    'red': 'red',
    'blue': 'blue',
    'indigo': 'indigo'
}

for filename in html_files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Adım 1: Sondaki ayrık grid yapısını (son iki kutuyu içeren) tamamen silip, içindekileri ana masonry container'ına geri alacağız.
    # Grid bloğunu yakalayalım:
    grid_pattern = r'<div class="grid grid-cols-1 xl:grid-cols-2 gap-8 mt-8">\s*(<section[\s\S]*?</section>)\s*(<section[\s\S]*?</section>)\s*</div>'
    
    match = re.search(grid_pattern, content)
    if match:
        sec1 = match.group(1)
        sec2 = match.group(2)
        
        # Grid div'ini tamamen temizle
        content = re.sub(grid_pattern, '', content)
        
        # Ana masonry container'ın kapanış div'ini bul ve sec1, sec2'yi o div kapanmadan hemen öncesine ekle
        masonry_end_pattern = r'(</div>)\s*(<!-- SINAV HAFIZASI|\s*<section class="exam-memory)'
        content = re.sub(masonry_end_pattern, f'\n{sec1}\n{sec2}\n\\1\n\\2', content, count=1)

    # Adım 2: Tüm sectionları sırayla düz DOM sırasına göre renklendir.
    all_sections = re.findall(r'(<section class="category-[a-z]+ note-card[\s\S]*?</section>)', content)
    
    new_content = content
    for i, old_section in enumerate(all_sections):
        target_cat, target_tail = colors[i % len(colors)]
        
        match_cat = re.search(r'class="category-([a-z]+)', old_section)
        if not match_cat: continue
        old_cat = match_cat.group(1)
        old_tail = category_to_tailwind.get(old_cat, old_cat)
        
        new_section = old_section
        if old_cat != target_cat:
            new_section = new_section.replace(f'category-{old_cat}', f'category-{target_cat}')
            for weight in ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900']:
                new_section = new_section.replace(f'{old_tail}-{weight}', f'{target_tail}-{weight}')
                
        new_content = new_content.replace(old_section, new_section, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
print("Sayfa istenilen tam orijinal haline (Masonry) ve sıralı renklere geri döndürüldü.")
