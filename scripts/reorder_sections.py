import os
import re

html_files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]

# İstenen DOM sırası
category_order = {
    'purple': 1,
    'yellow': 2,
    'turquoise': 3,
    'cyan': 3, # Just in case
    'green': 4,
    'emerald': 4, # Just in case
    'orange': 5,
    'red': 6
}

for filename in html_files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Masonry container'ını bul
    # <div class="columns-1 xl:columns-2 gap-8 space-y-8"> ve ilk </div> arası
    # Daha güvenli yol: tüm sectionları bulup sıraya dizip, ilk section'ın başladığı yerle son section'ın bittiği yer arasına yerleştirmek.
    
    sections = re.findall(r'(<section class="category-[a-z]+ note-card[\s\S]*?</section>)', content)
    
    if not sections:
        continue
        
    # Her section'ın kategorisini bul ve sıralama anahtarı oluştur
    def get_sort_key(section_html):
        match = re.search(r'class="category-([a-z]+)', section_html)
        if match:
            cat = match.group(1)
            return category_order.get(cat, 99)
        return 99

    # Sadece exam-memory sınıfı olmayanları sıralayalım, gerçi exam-memory genelde category- sınıfı taşımaz ama yine de güvenli olalım.
    # regex'imizde `class="category-[a-z]+ note-card` var, exam-memory'de yok. Bu yüzden güvendeyiz.
    
    sorted_sections = sorted(sections, key=get_sort_key)
    
    # HTML içindeki sectionları sırayla değiştirmek zor olabilir çünkü uzunluklar/içerikler değişecek.
    # Bunun yerine, tüm eski sectionları silebilir ve ilk section'ın bulunduğu yere hepsini birden yazabiliriz.
    
    # Ancak content.replace() kullanırsak, ilk section'ı tüm sıralı sectionlar ile değiştirip diğerlerini silebiliriz.
    new_content = content
    
    # 1. Eski sectionları içerikten çıkar (yerine placeholder bırakmayalım, sadece ilkine bırakalım)
    first_section_placeholder = "<!-- SORTED_SECTIONS_PLACEHOLDER -->"
    
    for i, sec in enumerate(sections):
        if i == 0:
            new_content = new_content.replace(sec, first_section_placeholder, 1)
        else:
            new_content = new_content.replace(sec, "", 1)
            
    # Boş kalan satırları temizlemek iyi olabilir ama çok da sorun değil.
    
    # 2. Sıralı sectionları birleştir
    joined_sections = "\n                ".join(sorted_sections)
    
    # 3. Placeholder yerine koy
    new_content = new_content.replace(first_section_placeholder, joined_sections)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
print("Tüm ünitelerdeki kartlar görseldeki gibi DOM sırasına dizildi (Mor -> Sarı -> Turkuaz -> Yeşil -> Turuncu -> Kırmızı).")
