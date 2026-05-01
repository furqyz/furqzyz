import os
import re

html_files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]

# Hedef sıra ve karşılık gelen Tailwind renk adları
color_sequence = [
    ('purple', 'purple'),
    ('turquoise', 'cyan'),
    ('yellow', 'yellow'),
    ('green', 'emerald'),
    ('orange', 'orange'),
    ('red', 'red')
]

category_to_tailwind = {
    'purple': 'purple',
    'turquoise': 'cyan',
    'yellow': 'yellow',
    'green': 'emerald',
    'orange': 'orange',
    'red': 'red'
}

for filename in html_files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. RENKLERİ SIRAYA KOYMA
    # Regex ile section'ları bulalım. Bu biraz tricky olabilir çünkü iç içe tag'ler var.
    # HTML parçalamak yerine BeautifulSoup kullanabiliriz ama standart kütüphane regex'i ile de yapabiliriz.
    # Şablon: <section class="category-XYZ ..."> ... </section> (sonraki section'a kadar)
    
    sections = re.findall(r'(<section class="category-[a-z]+ note-card[\s\S]*?</section>)', content)
    
    if sections:
        for i, old_section in enumerate(sections):
            target_cat, target_tail = color_sequence[i % len(color_sequence)]
            
            # Eski kategoriyi bulalım
            match = re.search(r'class="category-([a-z]+)', old_section)
            if not match:
                continue
            old_cat = match.group(1)
            old_tail = category_to_tailwind.get(old_cat, old_cat)
            
            # Renk isimlerini değiştirelim
            new_section = old_section
            if old_cat != target_cat:
                new_section = new_section.replace(f'category-{old_cat}', f'category-{target_cat}')
                
                # Tailwind class'larındaki renk isimlerini (örn. yellow-500 -> cyan-500) değiştir
                # Bu işlemi yaparken sadece "-100", "-200", vb. veya "-50" eklerini kontrol edelim ki rastgele kelimeler değişmesin
                # text-yellow-900 -> text-cyan-900 vb.
                for weight in ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900']:
                    new_section = new_section.replace(f'{old_tail}-{weight}', f'{target_tail}-{weight}')
            
            content = content.replace(old_section, new_section)
    
    # 2. SON İKİ KUTUYU YAN YANA ALMA (Sadece 1, 5, 7, 10, 14 üniteleri için)
    # index.html (1) ve unite5, unite7, unite10, unite14
    target_units = ['index.html', 'unite5.html', 'unite7.html', 'unite10.html', 'unite14.html']
    if any(filename.endswith(unit) for unit in target_units):
        # Container'ın bitişini bulmalıyız.
        # En güvenli yol:
        # Son iki <section class="category-... "> i bul, onları masonry div'inden çıkarıp yeni bir div'e koy.
        # Bütün section'ları baştan arayalım:
        all_sections_updated = re.findall(r'(<section class="category-[a-z]+ note-card[\s\S]*?</section>)', content)
        if len(all_sections_updated) >= 2:
            last_two = all_sections_updated[-2:]
            
            # Bunları mevcut masonry içinden sil
            # Ancak content.replace() kullanırsak aynı section'dan iki tane varsa sıkıntı olabilir. 
            # Bu yüzden sondan replace yapacağız.
            for sec in last_two:
                content = content.replace(sec, '', 1) # Normal replace
                
            # Boşlukları temizleyelim (div kapanmadan önce)
            # </div>\s*<!-- SINAV HAFIZASI BÖLÜMÜ --> veya <!-- SINAV HAFIZASI
            # Aslında masonry container'ı kapatan </div> yi bulup, altına yeni div eklemeliyiz.
            # "</div>\n            <!-- SINAV HAFIZASI"
            
            # Yeniden inşa edelim
            new_grid = f'\n            <div class="grid grid-cols-1 xl:grid-cols-2 gap-8 mt-8">\n                {last_two[0]}\n                {last_two[1]}\n            </div>\n'
            
            # Masonry container'ı bitiren </div> i bul. O </div> dan hemen sonra new_grid eklenecek.
            pattern = r'(</div>\s*(?:<!-- SINAV HAFIZASI|\s*<section class="exam-memory))'
            content = re.sub(pattern, new_grid + r'\1', content, count=1)
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Renkler sıralandı ve belirtilen ünitelerde son iki kutu yan yana hizalandı.")
