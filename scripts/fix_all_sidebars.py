import os
import re

root_dir = r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı'
turkce_dir = os.path.join(root_dir, 'turkce')

menu_structure = [
    {
        'id': 'sesBilgisiSub',
        'title': '1. Ses Bilgisi',
        'icon': 'fa-volume-up',
        'links': [
            ('ses-bilgisi-unluler.html', 'Ünlülerle İlgili Ses Olayları'),
            ('ses-bilgisi-unsuzler.html', 'Ünsüzlerle İlgili Ses Olayları'),
            ('ses-bilgisi-analiz.html', '⭐ Çıkmış Analizleri')
        ]
    },
    {
        'id': 'yazimKurallariSub',
        'title': '2. Yazım Kuralları',
        'icon': 'fa-pen-nib',
        'links': [
            ('yazim-kurallari-buyuk-harf.html', 'Büyük Harflerin Yazımı'),
            ('yazim-kurallari-sayilar-kisaltmalar.html', 'Sayıların ve Kısaltmaların Yazımı'),
            ('yazim-kurallari-bitisik-ayri.html', 'Bitişik ve Ayrı Yazılan Kelimeler'),
            ('yazim-kurallari-de-ki-mi.html', 'De, Ki, Mi Yazımı'),
            ('yazim-kurallari-ikilemeler.html', 'Düzeltme İşareti, İkilemeler ve Pekiştirmeler'),
            ('yazim-kurallari-analiz.html', '⭐ Çıkmış Analizleri')
        ]
    },
    {
        'id': 'noktalamaSub',
        'title': '3. Noktalama İşaretleri',
        'icon': 'fa-ellipsis-h',
        'links': [
            ('noktalama-nokta-virgul.html', 'Nokta ve Virgülün Kullanımı'),
            ('noktalama-noktali-virgul-iki-nokta.html', 'Noktalı Virgül ve İki Nokta'),
            ('noktalama-diger-isaretler.html', 'Soru, Ünlem, Kesme, Üç Nokta'),
            ('noktalama-analiz.html', '⭐ Çıkmış Analizleri')
        ]
    },
    {
        'id': 'yapiSekilSub',
        'title': '4. Sözcükte Yapı',
        'icon': 'fa-cubes',
        'links': [
            ('yapi-sekil-kok-ve-yapim.html', 'Kök Türleri ve Yapım Ekleri'),
            ('yapi-sekil-cekim-ekleri.html', 'İsim ve Fiil Çekim Ekleri'),
            ('yapi-sekil-sozcugun-yapisi.html', 'Sözcüğün Yapısı: Basit, Türemiş, Birleşik'),
            ('yapi-sekil-analiz.html', '⭐ Çıkmış Analizleri')
        ]
    },
    {
        'id': 'sozcukTurleriSub',
        'title': '5. Sözcük Türleri',
        'icon': 'fa-tags',
        'links': [
            ('sozcuk-turleri-isimler.html', 'İsimler (Adlar) ve İsim Tamlamaları'),
            ('sozcuk-turleri-sifatlar.html', 'Sıfatlar (Ön Adlar) ve Sıfat Tamlamaları'),
            ('sozcuk-turleri-zamirler.html', 'Zamirler (Adıllar)'),
            ('sozcuk-turleri-zarflar.html', 'Zarflar (Belirteçler)'),
            ('sozcuk-turleri-edat-baglac.html', 'Edat, Bağlaç ve Ünlem'),
            ('sozcuk-turleri-fiiller.html', 'Fiillerde Kip, Çekim ve Anlam Özellikleri'),
            ('sozcuk-turleri-fiilimsiler.html', 'Fiilimsiler (Eylemsiler)'),
            ('sozcuk-turleri-fiilde-cati.html', 'Fiilde Çatı'),
            ('sozcuk-turleri-analiz.html', '⭐ Çıkmış Analizleri')
        ]
    },
    {
        'id': 'cumleninOgeleriSub',
        'title': '6. Cümlenin Ögeleri',
        'icon': 'fa-sitemap',
        'links': [
            ('cumlenin-ogeleri-temel.html', 'Temel Ögeler: Yüklem ve Özne'),
            ('cumlenin-ogeleri-yardimci.html', 'Yardımcı Ögeler: Nesne, Dolaylı Tümleç ve Zarf Tümleci'),
            ('cumlenin-ogeleri-analiz.html', '⭐ Çıkmış Analizleri')
        ]
    },
    {
        'id': 'cumleTurleriSub',
        'title': '7. Cümle Türleri',
        'icon': 'fa-list-alt',
        'links': [
            ('cumle-turleri-yapi.html', 'Yapısına Göre Cümleler')
        ]
    }
]

flat_links = [
    
    
    ('anlatim-bozuklugu.html', '8. Anlatım Bozuklukları', 'fa-exclamation-circle')
]

def generate_sidebar(current_filename, prefix=""):
    sidebar = '''        <aside class="w-full lg:w-72 shrink-0">
            <div class="sticky top-28 space-y-4">
                <div class="bg-white dark:bg-slate-800 rounded-2xl shadow-sm border border-slate-100 dark:border-slate-700 overflow-hidden">
                    <button onclick="toggleSidebarSection('turkceNav', this)" class="w-full text-xs font-bold text-slate-400 dark:text-slate-500 uppercase tracking-widest p-4 flex items-center justify-between hover:bg-slate-50 dark:hover:bg-slate-700/50 transition-colors cursor-pointer">
                        <span class="flex items-center"><i class="fas fa-language mr-2"></i> TÜRKÇE ÜNİTELERİ</span>
                        <i class="fas fa-chevron-down transition-transform duration-300 rotate-180" id="turkceNav-chevron"></i>
                    </button>
                    <div class="px-3 pb-3">
                        <nav id="turkceNav" class="space-y-1.5 max-h-[80vh] overflow-y-auto pr-1.5 custom-scrollbar">
'''
    unit_map = {
        'ses-bilgisi': 'sesBilgisiSub',
        'yazim-kurallari': 'yazimKurallariSub',
        'noktalama': 'noktalamaSub',
        'yapi-sekil': 'yapiSekilSub',
        'sozcuk-turleri': 'sozcukTurleriSub',
        'cumlenin-ogeleri': 'cumleninOgeleriSub',
        'cumle-turleri': 'cumleTurleriSub'
    }
    
    active_accordion = None
    for k, v in unit_map.items():
        if current_filename.startswith(k):
            active_accordion = v
            break

    for group in menu_structure:
        is_open = (group['id'] == active_accordion)
        hidden_class = '' if is_open else 'hidden'
        rotate_class = 'rotate-180' if is_open else ''
        
        sidebar += f'''                            <!-- {group['title']} -->
                            <div class="space-y-1 mt-2">
                                <button onclick="toggleSubNav('{group['id']}', this)" class="w-full flex items-center justify-between bg-slate-50 dark:bg-slate-700/50 text-slate-700 dark:text-slate-200 px-3 py-3 rounded-xl font-semibold transition-transform hover:scale-[1.02] mb-1">
                                    <div class="flex items-start space-x-3">
                                        <i class="fas {group['icon']} w-4 text-center mt-0.5 text-rose-500"></i>
                                        <span class="text-[13px] leading-snug">{group['title']}</span>
                                    </div>
                                    <i class="fas fa-chevron-down text-[10px] opacity-70 shrink-0 ml-2 mt-1 transition-transform {rotate_class}" id="{group['id']}-chevron"></i>
                                </button>
                                <div id="{group['id']}" class="pl-7 pr-2 py-1 space-y-1 {hidden_class}">\n'''
        
        for link, title in group['links']:
            is_active = (current_filename == link)
            active_font = 'font-bold text-rose-600 dark:text-rose-400' if is_active else 'font-medium text-slate-500 dark:text-slate-400 hover:text-rose-600 dark:hover:text-rose-400'
            active_icon = '' if is_active else 'opacity-50'
            sidebar += f'''                                    <a href="{prefix}{link}" class="block text-[12.5px] {active_font} py-1.5 transition-colors"><i class="fas fa-caret-right mr-1.5 {active_icon}"></i>{title}</a>\n'''
            
        sidebar += '''                                </div>\n                            </div>\n'''

    for link, title, icon in flat_links:
        is_active = (current_filename == link)
        bg_class = 'bg-rose-50 dark:bg-rose-900/20' if is_active else 'bg-slate-50 dark:bg-slate-700/50 hover:scale-[1.02]'
        text_class = 'text-rose-700 dark:text-rose-300' if is_active else 'text-slate-700 dark:text-slate-200'
        icon_class = 'text-rose-600' if is_active else 'text-rose-500'
        
        sidebar += f'''                            <div class="space-y-1 mt-2">
                                <a href="{prefix}{link}" class="w-full flex items-center justify-between {bg_class} {text_class} px-3 py-3 rounded-xl font-semibold transition-transform mb-1">
                                    <div class="flex items-start space-x-3">
                                        <i class="fas {icon} w-4 text-center mt-0.5 {icon_class}"></i>
                                        <span class="text-[13px] leading-snug">{title}</span>
                                    </div>
                                </a>
                            </div>\n'''

    sidebar += '''                        </nav>
                    </div>
                </div>
            </div>
        </aside>'''
    return sidebar

turkce_html_path = os.path.join(root_dir, 'turkce.html')
with open(turkce_html_path, 'r', encoding='utf-8') as f:
    content = f.read()

sidebar_html = generate_sidebar('turkce.html', prefix='turkce/')
content = re.sub(r'<aside class="w-full lg:w-72 shrink-0">.*?</aside>', sidebar_html, content, flags=re.DOTALL)
with open(turkce_html_path, 'w', encoding='utf-8') as f:
    f.write(content)

turkce_files = [f for f in os.listdir(turkce_dir) if f.endswith('.html')]
for filename in turkce_files:
    fpath = os.path.join(turkce_dir, filename)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    sidebar_html = generate_sidebar(filename, prefix='')
    if '<aside class="w-full lg:w-72 shrink-0">' in content:
        content = re.sub(r'<aside class="w-full lg:w-72 shrink-0">.*?</aside>', sidebar_html, content, flags=re.DOTALL)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Sidebars fixed with new subtopic included.")
