import os
import re

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cografya_dir = os.path.join(root_dir, 'cografya')

menu_structure = [
    {
        'id': 'konumSub',
        'title': '1. Ünite: Coğrafi Konum',
        'icon': 'fa-compass',
        'colorClass': 'text-emerald-500',
        'hoverClass': 'hover:text-emerald-600 dark:hover:text-emerald-400',
        'activeClass': 'text-emerald-600 dark:text-emerald-400 font-bold',
        'links': [
            ('enlem-boylam.html', 'Enlem - Boylam'),
            ('kuzeye-dogru.html', 'Kuzey\'e Doğru'),
            ('sinir-kapilari.html', 'Türkiye\'nin Sınır Kapıları')
        ]
    },
    {
        'id': 'iklimSub',
        'title': '2. Ünite: İklim ve Bitki Örtüsü',
        'icon': 'fa-cloud-sun-rain',
        'colorClass': 'text-sky-500',
        'hoverClass': 'hover:text-sky-600 dark:hover:text-sky-400',
        'activeClass': 'text-sky-600 dark:text-sky-400 font-bold',
        'links': [
            ('basinc-merkezleri.html', 'Basınç Merkezleri'),
            ('ruzgar-yonleri.html', 'Rüzgarlar ve Rüzgar Gülleri'),
            ('nem-turleri.html', 'Nem Türleri ve Dağılımı'),
            ('yagis-mevsimleri.html', 'Yağış Mevsimleri'),
            ('yagis-turleri.html', 'Yağış Türleri ve Oluşumları'),
            ('yagisli-yoreler.html', 'Türkiye\'nin Yağışlı Yöreleri'),
            ('iklim-cesitleri.html', 'Türkiye\'de İklim Çeşitleri'),
            ('bitki-ortusu.html', 'Bitki Örtüsü Bölgeleri'),
            ('flora-bolgeleri.html', 'Flora Bölgeleri'),
            ('agac-turleri.html', 'Ağaç Türleri')
        ]
    },
    {
        'id': 'fizikiSub',
        'title': '3. Ünite: Fiziki Özellikler',
        'icon': 'fa-mountain',
        'colorClass': 'text-teal-500',
        'hoverClass': 'hover:text-teal-600 dark:hover:text-teal-400',
        'activeClass': 'text-teal-600 dark:text-teal-400 font-bold',
        'links': [
            ('turkiyenin-daglari.html', 'Türkiye\'nin Dağları'),
            ('ova-ve-platolar.html', 'Ova ve Platolar'),
            ('delta-ovalari.html', 'Delta Ovaları'),
            ('masif-araziler.html', 'Masif Araziler'),
            ('deprem-bolgeleri.html', 'Deprem Bölgeleri'),
            ('karstik-kayaclar.html', 'Karstik Kayaçlar'),
            ('kumullar.html', 'Türkiye\'de Kumullar'),
            ('ruzgar-sekillendirme.html', 'Rüzgar Şekillendirme'),
            ('vadi-turleri.html', 'Türkiye\'nin Vadi Türleri'),
            ('goller.html', 'Türkiye\'nin Gölleri'),
            ('korfezler.html', 'Türkiye\'nin Körfezleri'),
            ('su-varligi.html', 'Türkiye\'nin Su Varlığı ve Havzalar'),
            ('kiyi-tipleri.html', 'Türkiye\'nin Kıyı Tipleri'),
            ('kiyi-sekilleri.html', 'Türkiye\'nin Kıyı Şekilleri'),
            ('sahanlik.html', 'Kıta Sahanlığı (Sahanlık)'),
            ('toprak-turleri.html', 'Türkiye\'nin Toprak Türleri'),
            ('gecitler.html', 'Karayolu Geçitleri ve Boğazları')
        ]
    },
    {
        'id': 'nufusSub',
        'title': '4. Ünite: Nüfus ve Yerleşme',
        'icon': 'fa-people-group',
        'colorClass': 'text-violet-500',
        'hoverClass': 'hover:text-violet-600 dark:hover:text-violet-400',
        'activeClass': 'text-violet-600 dark:text-violet-400 font-bold',
        'links': [
            ('nufus-dagilisi.html', 'Nüfusun Dağılışı'),
            ('koy-alti-yerlesmeleri.html', 'Köy Altı Yerleşmeleri'),
            ('mesken-tipleri.html', 'Kırsal Mesken Tipleri')
        ]
    },
    {
        'id': 'ekonomiSub',
        'title': '5. Ünite: Ekonomik Coğrafya',
        'icon': 'fa-chart-line',
        'colorClass': 'text-amber-500',
        'hoverClass': 'hover:text-amber-600 dark:hover:text-amber-400',
        'activeClass': 'text-amber-600 dark:text-amber-400 font-bold',
        'links': [
            ('tarim-urunleri.html', 'Tarım Ürünleri Dağılımı'),
            ('hayvancilik.html', 'Türkiye\'de Hayvancılık'),
            ('maden-isletmeleri.html', 'Maden İşletmeleri ve Tesisleri'),
            ('petrol-boruhatlari.html', 'Petrol Boru Hatları'),
            ('dogalgaz-boruhatlari.html', 'Doğal Gaz Boru Hatları'),
            ('demiryollari.html', 'Demiryolları ve YHT Ağı'),
            ('otoyollar.html', 'Türkiye\'nin Otoyolları'),
            ('limanlar.html', 'Denizyolu Limanları'),
            ('ramsar-alanlari.html', 'Türkiye\'nin Ramsar Alanları')
        ]
    },
    {
        'id': 'bolgelerSub',
        'title': '6. Ünite: Bölgeler Coğrafyası',
        'icon': 'fa-map',
        'colorClass': 'text-rose-500',
        'hoverClass': 'hover:text-rose-600 dark:hover:text-rose-400',
        'activeClass': 'text-rose-600 dark:text-rose-400 font-bold',
        'links': [
            ('bolgeler-cografyasi.html', 'İşlevsel Bölgeler (GAP, DAP...)')
        ]
    },
    {
        'id': 'tuikSub',
        'title': '7. Ünite: Güncel TÜİK Verileri',
        'icon': 'fa-square-poll-vertical',
        'colorClass': 'text-red-500',
        'hoverClass': 'hover:text-red-600 dark:hover:text-red-400',
        'activeClass': 'text-red-600 dark:text-red-400 font-bold',
        'links': [
            ('tuik-hayvancilik.html', 'TÜİK: Hayvancılık'),
            ('tuik-tarim.html', 'TÜİK: Tarım'),
            ('tuik-nufus.html', 'TÜİK: Nüfus (ADNKS)'),
            ('tuik-ekonomi.html', 'TÜİK: Ekonomi & Turizm'),
            ('tuik-afetler.html', 'TÜİK: Doğal Afetler'),
            ('tuik-ormanlar.html', 'TÜİK: Orman Varlığı'),
            ('tuik-koruma.html', 'TÜİK: Koruma Alanları'),
            ('tuik-ilkler.html', 'TÜİK: İlkler & Sakin Şehir')
        ]
    }
]

def generate_sidebar(current_filename, prefix=""):
    sidebar = f'''        <aside class="w-full lg:w-72 shrink-0">
            <div class="sticky top-28 space-y-4">
                <div class="bg-white dark:bg-slate-800 rounded-2xl shadow-sm border border-slate-100 dark:border-slate-700 overflow-hidden">
                    <button onclick="toggleSidebarSection('cografyaNav', this)" class="w-full text-xs font-bold text-slate-400 dark:text-slate-500 uppercase tracking-widest p-4 flex items-center justify-between hover:bg-slate-50 dark:hover:bg-slate-700/50 transition-colors cursor-pointer">
                        <span class="flex items-center"><i class="fas fa-earth-americas mr-2"></i> COĞRAFYA ÜNİTELERİ</span>
                        <i class="fas fa-chevron-down transition-transform duration-300 rotate-180" id="cografyaNav-chevron"></i>
                    </button>
                    <div class="px-3 pb-3">
                        <nav id="cografyaNav" class="space-y-1.5 max-h-[80vh] overflow-y-auto pr-1.5 custom-scrollbar">
'''
    
    active_accordion = None
    for group in menu_structure:
        for link, _ in group['links']:
            if current_filename == link:
                active_accordion = group['id']
                break

    for group in menu_structure:
        is_open = (group['id'] == active_accordion)
        hidden_class = '' if is_open else 'hidden'
        rotate_class = 'rotate-180' if is_open else ''
        
        sidebar += f'''                            <!-- {group['title']} -->
                            <div class="space-y-1 mt-2">
                                <button onclick="toggleSubNav('{group['id']}', this)" class="w-full flex items-center justify-between bg-slate-50 dark:bg-slate-700/50 text-slate-700 dark:text-slate-200 px-3 py-3 rounded-xl font-semibold transition-transform hover:scale-[1.02] mb-1">
                                    <div class="flex items-start space-x-3">
                                        <i class="fas {group['icon']} w-4 text-center mt-0.5 {group['colorClass']}"></i>
                                        <span class="text-[13px] leading-snug">{group['title']}</span>
                                    </div>
                                    <i class="fas fa-chevron-down text-[10px] opacity-70 shrink-0 ml-2 mt-1 transition-transform {rotate_class}" id="{group['id']}-chevron"></i>
                                </button>
                                <div id="{group['id']}" class="pl-7 pr-2 py-1 space-y-1 {hidden_class}">\n'''
        
        for link, title in group['links']:
            is_active = (current_filename == link)
            active_font = group['activeClass'] if is_active else f"font-medium text-slate-500 dark:text-slate-400 {group['hoverClass']}"
            active_icon = '' if is_active else 'opacity-50'
            sidebar += f'''                                    <a href="{prefix}{link}" class="block text-[12.5px] {active_font} py-1.5 transition-colors"><i class="fas fa-caret-right mr-1.5 {active_icon}"></i>{title}</a>\n'''
            
        sidebar += '''                                </div>\n                            </div>\n'''

    sidebar += '''                        </nav>
                    </div>
                </div>
            </div>
        </aside>'''
    return sidebar

# Update cografya.html
cografya_html_path = os.path.join(root_dir, 'cografya.html')
if os.path.exists(cografya_html_path):
    with open(cografya_html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    sidebar_html = generate_sidebar('cografya.html', prefix='cografya/')
    content = re.sub(r'<aside class="w-full lg:w-72 shrink-0">.*?</aside>', sidebar_html, content, flags=re.DOTALL)
    with open(cografya_html_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Update all files in cografya/
if os.path.exists(cografya_dir):
    cografya_files = [f for f in os.listdir(cografya_dir) if f.endswith('.html')]
    for filename in cografya_files:
        fpath = os.path.join(cografya_dir, filename)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        sidebar_html = generate_sidebar(filename, prefix='')
        if '<aside class="w-full lg:w-72 shrink-0">' in content:
            content = re.sub(r'<aside class="w-full lg:w-72 shrink-0">.*?</aside>', sidebar_html, content, flags=re.DOTALL)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Geography sidebars synchronized successfully.")
