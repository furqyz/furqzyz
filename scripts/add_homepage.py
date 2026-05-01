import os
import re

root = r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı'

# Descriptions for each history unit
descriptions = {
    1: "İlk Türk devletleri, boy teşkilatı, Orhun Abideleri ve göç destanları.",
    2: "Karahanlılar, Gazneliler, Büyük Selçuklular, Haçlı Seferleri ve Anadolu Beylikleri.",
    3: "Anadolu Selçukluları, Ahilik, kervansaray sistemi ve Moğol istilası.",
    4: "Osmanlı devlet teşkilatı, Divan-ı Hümayun, tımar sistemi ve millet sistemi.",
    5: "Osmanlı kuruluşu, Rumeli fetihleri, İstanbul kuşatmaları ve Fetret Devri.",
    6: "İstanbul'un fethi, Yavuz Sultan Selim, Kanuni dönemi ve duraklama başlangıcı.",
    7: "Kriz ve ıslahat girişimleri, Celali isyanları, Köprülü dönemi ve Karlofça.",
    8: "Lale Devri, Batı tarzı ıslahatlar, Küçük Kaynarca ve Nizam-ı Cedit.",
    9: "Milliyetçilik isyanları, Tanzimat, Meşrutiyet ve Osmanlı'nın son dönemi.",
    10: "Balkan Savaşları, I. Dünya Savaşı cepheleri, Mondros Ateşkesi.",
    11: "Samsun'a çıkış, Amasya Genelgesi, Erzurum ve Sivas kongreleri.",
    12: "TBMM'nin açılışı, meclis hükümeti, İstiklal Mahkemeleri ve isyanlar.",
    13: "Doğu, Güney ve Batı cepheleri, İnönü zaferleri, Sakarya ve Büyük Taarruz.",
    14: "Atatürk'ün hayatı, eserleri ve Nutuk'ta geçen dönem (1919-1927).",
    15: "Çok partili hayat denemeleri, Şeyh Sait ve Menemen olayları.",
    16: "Cumhuriyetçilik, Milliyetçilik, Halkçılık, Laiklik, Devletçilik, İnkılapçılık.",
    17: "Saltanatın kaldırılmasından ekonomik inkılaplara tüm Atatürk devrimleri.",
    18: "Lozan'dan kalan sorunlar, Balkan Antantı, Montrö ve Hatay meselesi.",
    19: "Heykel, müzik, tiyatro, resim ve Cumhuriyet dönemi kültür inkılapları.",
    20: "İkinci Dünya Savaşı, Kore Savaşı, Demokrat Parti ve Kıbrıs meselesi.",
    21: "Bolşevik İhtilali, Basmacı Hareketi, Meiji Restorasyonu ve 1929 Krizi.",
    22: "II. Dünya Savaşı cepheleri, Türkiye'nin tutumu ve savaş sonrası düzen.",
    23: "NATO, Marshall Planı, Kore Savaşı ve Demokrat Parti iktidarı.",
    24: "Küba Krizi, Vietnam Savaşı, Kıbrıs Barış Harekâtı ve ASALA terörü.",
    25: "SSCB'nin çöküşü, Türk Cumhuriyetleri, AB süreci ve güncel gelişmeler.",
}

# Ana sayfa button html snippet (to insert after logo div in header)
HOME_BTN = '''<a href="anasayfa.html" class="hidden lg:flex items-center gap-1.5 px-3 py-2 rounded-lg text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-indigo-600 dark:hover:text-indigo-400 font-semibold text-sm transition-colors border border-transparent hover:border-slate-200 dark:hover:border-slate-700 mr-1" title="Ana Sayfaya Dön">
                    <i class="fas fa-home text-sm"></i>
                    <span>Ana Sayfa</span>
                </a>'''

HOME_BTN_ROSE = HOME_BTN.replace('hover:text-indigo-600 dark:hover:text-indigo-400', 'hover:text-rose-600 dark:hover:text-rose-400')

def add_descriptions_to_index():
    path = os.path.join(root, 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # For each unit, add description after h3 and before the "Konuya Git" div
    for unit_id, desc in descriptions.items():
        # Pattern to match the h3 for this unit followed by the "Konuya Git" div (no desc yet)
        pattern = r'(<h3 class="font-extrabold text-slate-900 dark:text-white text-lg mb-4 flex-grow">)((?:(?!<h3|<\/a>).)*?)(</h3>\s*<div class="inline-flex items-center text-indigo-600)'
        
        # More specific approach: find by unit number text
        # Replace "mb-4 flex-grow" with "mb-2 flex-grow" and add description
        pass

    # Direct replacement approach - replace the unit cards grid
    # Find the grid and replace all cards with cards that have descriptions
    card_template = '''                <a href="{url}" class="group bg-white dark:bg-slate-800 rounded-3xl p-6 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-xl hover:-translate-y-2 transition-all duration-300 relative overflow-hidden flex flex-col h-full">
                    <div class="w-12 h-12 bg-indigo-50 dark:bg-indigo-900/40 rounded-2xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                        <i class="fas {icon} text-indigo-500 dark:text-indigo-400 text-xl"></i>
                    </div>
                    <div class="text-xs font-bold text-indigo-500 dark:text-indigo-400 mb-2">{num}. Ünite</div>
                    <h3 class="font-extrabold text-slate-900 dark:text-white text-lg mb-2">{title}</h3>
                    <p class="text-slate-500 dark:text-slate-400 text-sm mb-4 flex-grow leading-relaxed">{desc}</p>
                    <div class="inline-flex items-center text-indigo-600 dark:text-indigo-400 font-bold text-sm mt-auto">
                        <span>Konuya Git</span>
                        <i class="fas fa-arrow-right ml-2 group-hover:translate-x-2 transition-transform"></i>
                    </div>
                </a>'''

    units = [
        (1, "unitler/unite1.html", "fa-landmark", "İslamiyet Öncesi Türk Tarihi"),
        (2, "unitler/unite2.html", "fa-mosque", "İlk Türk İslam Devletleri"),
        (3, "unitler/unite3.html", "fa-chess-knight", "Anadolu (Türkiye) Selçuklu Devleti"),
        (4, "unitler/unite4.html", "fa-landmark-dome", "Osmanlı Devleti Kültür ve Medeniyeti"),
        (5, "unitler/unite5.html", "fa-campground", "Osmanlı Devleti Kuruluş Dönemi (1299 - 1453)"),
        (6, "unitler/unite6.html", "fa-chess-rook", "Osmanlı Devleti Yükselme Dönemi (1453 - 1595)"),
        (7, "unitler/unite7.html", "fa-hourglass-end", "XVII. Yüzyılda Osmanlı Devleti (Duraklama Dönemi) (1595 - 1699)"),
        (8, "unitler/unite8.html", "fa-arrow-trend-down", "XVIII. Yüzyılda Osmanlı Devleti (Gerileme Dönemi) (1699 - 1792)"),
        (9, "unitler/unite9.html", "fa-unlink", "XIX. Yüzyılda Osmanlı Devleti (Dağılma Dönemi) (1792 - 1922)"),
        (10, "unitler/unite10.html", "fa-globe", "XX. Yüzyıl Başlarında Osmanlı Devleti"),
        (11, "unitler/unite11.html", "fa-bullhorn", "Millî Mücadele Hazırlık Dönemi"),
        (12, "unitler/unite12.html", "fa-building-columns", "I. TBMM Dönemi ve Gelişmeleri (1920 - 1923)"),
        (13, "unitler/unite13.html", "fa-shield-halved", "Millî Mücadele Muharebeler Dönemi"),
        (14, "unitler/unite14.html", "fa-user-tie", "Atatürk'ün Hayatı"),
        (15, "unitler/unite15.html", "fa-landmark-flag", "Atatürk Dönemi İç Politika"),
        (16, "unitler/unite16.html", "fa-scale-balanced", "Atatürk İlkeleri"),
        (17, "unitler/unite17.html", "fa-lightbulb", "Atatürk İnkılapları"),
        (18, "unitler/unite18.html", "fa-earth-europe", "Atatürk Dönemi Türk Dış Politikası"),
        (19, "unitler/unite19.html", "fa-masks-theater", "Cumhuriyet Dönemi Kültür ve Medeniyeti"),
        (20, "unitler/unite20.html", "fa-earth-americas", "Çağdaş Türk ve Dünya Tarihi"),
        (21, "unitler/unite21.html", "fa-biohazard", "XX. Yüzyıl Başlarında Dünya"),
        (22, "unitler/unite22.html", "fa-fighter-jet", "II. Dünya Savaşı (1939 - 1945)"),
        (23, "unitler/unite23.html", "fa-snowflake", "Soğuk Savaş Dönemi (1947 - 1990)"),
        (24, "unitler/unite24.html", "fa-handshake-angle", "Yumuşama (Detant) Dönemi"),
        (25, "unitler/unite25.html", "fa-network-wired", "Küreselleşen Dünya (1990 - 2026)"),
    ]

    new_cards = []
    for num, url, icon, title in units:
        desc = descriptions.get(num, "")
        new_cards.append(card_template.format(
            url=url, icon=icon, num=num, title=title, desc=desc
        ))

    # Replace the entire grid content
    grid_pattern = r'(<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">)(.*?)(</div>\s*</main>)'
    new_grid = r'\1\n' + '\n'.join(new_cards) + r'\n\n            \3'
    
    content = re.sub(grid_pattern, new_grid, content, flags=re.DOTALL)

    # Add home button to nav - insert before <nav class="hidden lg:flex
    home_btn_html = '            ' + HOME_BTN + '\n                '
    content = content.replace(
        '<!-- Dersler Menüsü -->\n                <nav class="hidden lg:flex',
        '<!-- Dersler Menüsü -->\n                ' + HOME_BTN + '\n                <nav class="hidden lg:flex'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html updated")


def add_home_btn_to_all():
    """Add Ana Sayfa button to all html pages"""
    all_html = []
    for root_dir, dirs, files in os.walk(root):
        # Skip scripts dir
        if 'scripts' in root_dir:
            continue
        for fn in files:
            if fn.endswith('.html') and fn not in ('anasayfa.html',):
                all_html.append(os.path.join(root_dir, fn))

    for path in all_html:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip if already has home button
        if 'anasayfa.html' in content and 'fas fa-home' in content:
            continue
        
        is_turkce = 'turkce' in path.replace('\\', '/').lower()
        btn = HOME_BTN_ROSE if is_turkce else HOME_BTN
        
        # Adjust path based on depth
        rel = os.path.relpath(path, root)
        depth = rel.count(os.sep)
        prefix = '../' * depth
        btn_adjusted = btn.replace('href="anasayfa.html"', f'href="{prefix}anasayfa.html"')

        if '<!-- Dersler Menüsü -->' in content:
            old = '<!-- Dersler Menüsü -->'
            content = content.replace(old, '<!-- Dersler Menüsü -->\n                ' + btn_adjusted, 1)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

    print(f"Added home button to {len(all_html)} files")


add_descriptions_to_index()
add_home_btn_to_all()
print("Done!")
