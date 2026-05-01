import os
import re

html_files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]

# Sadece bu başlık mor kalacak — diğerleri indigo olacak
ALLOWED_PURPLE_KEYWORDS = [
    'ilkler', 'sonlar', 'kesin yargı', 'ilk ', ' ilk'
]

category_to_tailwind = {
    'purple': 'purple',
    'indigo': 'indigo',
}

for filename in html_files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    all_sections = re.findall(r'(<section class="category-purple note-card[\s\S]*?</section>)', content)
    
    new_content = content
    for old_section in all_sections:
        # Başlığı bul
        title_match = re.search(r'<h3[^>]*>([\s\S]*?)</h3>', old_section)
        if not title_match:
            # Başlık bulunamadıysa indigo yap
            pass_to_indigo = True
        else:
            raw_title = title_match.group(1)
            clean_title = re.sub(r'<[^>]+>', '', raw_title).strip().lower()
            # Başlıkta izin verilen anahtar kelime var mı?
            pass_to_indigo = not any(kw in clean_title for kw in ALLOWED_PURPLE_KEYWORDS)
        
        if pass_to_indigo:
            # category-purple → category-indigo
            new_section = old_section.replace('category-purple', 'category-indigo')
            # Tailwind renk classlarını değiştir: purple-X → indigo-X
            for weight in ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900']:
                new_section = new_section.replace(f'purple-{weight}', f'indigo-{weight}')
            new_content = new_content.replace(old_section, new_section, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
print("Gereksiz mor kutucuklar indigo (lacivert/çivit) renge dönüştürüldü. Sadece 'İlkler, Sonlar ve Kesin Yargılar' mor kaldı.")
