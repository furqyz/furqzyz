import os
import re

html_files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]

# Renk eşleştirmeleri ve anahtar kelimeleri
categories = {
    'purple': {
        'tailwind': 'purple',
        'keywords': ['ilk', 'son', 'kesin', 'kavram', 'özellik', 'anlayış', 'gelişme', 'ıslahat', 'yenilik', 'genel', 'önemli özellikler']
    },
    'yellow': {
        'tailwind': 'yellow',
        'keywords': ['şahsiyet', 'isim', 'siyasi', 'kişi', 'isyan', 'padişah', 'devlet', 'hükümdar', 'lider', 'komutan', 'ayaklanma']
    },
    'turquoise': {
        'tailwind': 'cyan',
        'keywords': ['savaş', 'söz', 'kültür', 'medeniyet', 'muharebe', 'sefer', 'cephe', 'mimari', 'sanat', 'edebiyat', 'bilim', 'ordu']
    },
    'green': {
        'tailwind': 'emerald',
        'keywords': ['antlaşma', 'pakt', 'barış', 'sözleşme', 'ferman', 'bildiri', 'berat', 'diplomasi']
    },
    'orange': {
        'tailwind': 'orange',
        'keywords': ['konferans', 'kongre', 'meclis', 'görevli', 'genelge', 'kurum', 'örgüt', 'cemiyet', 'politika', 'arayış', 'teşkilat', 'parti', 'kanun', 'görüşme']
    },
    'red': {
        'tailwind': 'red',
        'keywords': ['kritik', 'uyarı', 'analiz', 'ipucu', 'not', 'dikkat', 'ekleme']
    }
}

category_to_tailwind = {
    'purple': 'purple',
    'turquoise': 'cyan',
    'yellow': 'yellow',
    'green': 'emerald',
    'orange': 'orange',
    'red': 'red'
}

def guess_category(title):
    title_lower = title.lower()
    
    # 1. Kırmızı (Kritik Uyarılar) çok belirgin
    for kw in categories['red']['keywords']:
        if kw in title_lower:
            return 'red'
            
    # 2. Yeşil (Antlaşmalar)
    for kw in categories['green']['keywords']:
        if kw in title_lower:
            return 'green'
            
    # 3. Turuncu (Konferans, Kongre vs)
    for kw in categories['orange']['keywords']:
        if kw in title_lower:
            return 'orange'
            
    # 4. Turkuaz (Savaş, Söz, Kültür)
    for kw in categories['turquoise']['keywords']:
        if kw in title_lower:
            return 'turquoise'
            
    # 5. Sarı (Şahsiyet, İsim, Siyasi)
    for kw in categories['yellow']['keywords']:
        if kw in title_lower:
            return 'yellow'
            
    # 6. Mor (İlkler, Sonlar)
    for kw in categories['purple']['keywords']:
        if kw in title_lower:
            return 'purple'
            
    # Varsayılan
    return 'purple'

for filename in html_files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    all_sections = re.findall(r'(<section class="category-[a-z]+ note-card[\s\S]*?</section>)', content)
    
    new_content = content
    for old_section in all_sections:
        # Başlığı bul
        title_match = re.search(r'<h3[^>]*>([\s\S]*?)</h3>', old_section)
        if not title_match:
            continue
            
        # Başlık içinden HTML taglerini temizle ve metni al
        raw_title = title_match.group(1)
        clean_title = re.sub(r'<[^>]+>', '', raw_title).strip()
        
        target_cat = guess_category(clean_title)
        target_tail = categories[target_cat]['tailwind']
        
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
        
print("Tüm kartlar başlıklarına/içeriklerine göre yeniden semantik renklerine kavuşturuldu.")
