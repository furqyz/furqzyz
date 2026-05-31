import os
import re

# Read original HTML
with open('cografya/tuik-verileri.html', 'r', encoding='utf-8') as f:
    orig_html = f.read()

subpages = [
    {
        'filename': 'tuik-hayvancilik.html',
        'title': 'TÜİK: Hayvancılık İstatistikleri',
        'subtitle': 'TÜİK Güncel Hayvancılık, Kümes, Arıcılık ve Su Ürünleri İstatistikleri.',
        'sections': ['kucukbas', 'buyukbas', 'kumes', 'aricilik', 'balikcilik']
    },
    {
        'filename': 'tuik-tarim.html',
        'title': 'TÜİK: Tarım İstatistikleri',
        'subtitle': 'TÜİK Güncel Tarım Ürünleri Dağılımı ve Yetiştiricilik İstatistikleri.',
        'sections': ['tarim']
    },
    {
        'filename': 'tuik-nufus.html',
        'title': 'TÜİK: Nüfus ve Demografi',
        'subtitle': 'ADNKS 2025 Nüfus Sayımı, Yaş Grupları, Ortanca Yaş ve Yoğunluk İstatistikleri.',
        'sections': ['nufus']
    },
    {
        'filename': 'tuik-ekonomi.html',
        'title': 'TÜİK: Ekonomi, Enerji ve Turizm',
        'subtitle': 'Aktif Nüfus Sektörleri, Dış Ticaret, Enerji İthalatı, Elektrik Üretimi ve Liman İstatistikleri.',
        'sections': ['ekonomi-ticaret', 'turizm']
    },
    {
        'filename': 'tuik-afetler.html',
        'title': 'TÜİK: Doğal Afet İstatistikleri',
        'subtitle': 'Türkiye Heyelan, Deprem, Su Baskını, Çığ Afet Sayıları ve Can/Mal Kayıpları.',
        'sections': ['afetler']
    },
    {
        'filename': 'tuik-ormanlar.html',
        'title': 'TÜİK: Orman Varlığı',
        'subtitle': 'Geçmişten Günümüze Orman Alanı Trendleri, Ağaç Türleri ve İl Bazında Alan Oranları.',
        'sections': ['ormanlar']
    },
    {
        'filename': 'tuik-koruma.html',
        'title': 'TÜİK: Koruma Alanları',
        'subtitle': 'Ramsar Sözleşmesi Kapsamındaki 14 Sulak Alanımız ve 22 UNESCO Dünya Miras Varlığımız.',
        'sections': ['ramsar', 'unesco']
    },
    {
        'filename': 'tuik-ilkler.html',
        'title': 'TÜİK: İlkler & Sakin Şehir',
        'subtitle': 'Milli Parklar, Jeoparklar, Cittaslow Sakin Şehirler ve Turistik Mağara İstatistikleri.',
        'sections': ['cografi-ilkler']
    }
]

def extract_section(section_id):
    pattern = rf'(<section\s+id="{section_id}"[^>]*>.*?</section>)'
    match = re.search(pattern, orig_html, re.DOTALL)
    if match:
        return match.group(1)
    return ""

# Generate the pages
for page in subpages:
    filename = page['filename']
    title = page['title']
    subtitle = page['subtitle']
    
    sections_content = ""
    for sid in page['sections']:
        sections_content += extract_section(sid) + "\n\n"
        
    page_html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - KPSS Coğrafya</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                    }}
                }}
            }}
        }}
    </script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body class="bg-slate-50 text-slate-900 leading-relaxed antialiased">

    <!-- Header -->
    <header class="sticky top-0 z-50 bg-white/80 dark:bg-slate-900/80 backdrop-blur-md shadow-sm px-4 py-4 border-b border-slate-200 dark:border-slate-800 transition-colors duration-300">
        <div class="max-w-[1600px] mx-auto flex justify-between items-center px-4 md:px-8">
            <div class="flex items-center space-x-4">
                <div class="bg-gradient-to-br from-emerald-500 to-teal-600 text-white p-2.5 rounded-xl shadow-lg shadow-emerald-200/50 dark:shadow-emerald-900/50">
                    <i class="fas fa-earth-americas text-lg"></i>
                </div>
                <h1 class="text-2xl font-extrabold tracking-tight">KPSS <span class="bg-clip-text text-transparent bg-gradient-to-r from-emerald-600 to-teal-600 dark:from-emerald-400 dark:to-teal-400">Ders Notlarım</span></h1>
            </div>
            <div class="flex items-center space-x-4">
                <a href="../index.html" class="hidden lg:flex items-center gap-1.5 px-3 py-2 rounded-lg text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-emerald-600 dark:hover:text-emerald-400 font-semibold text-sm transition-colors border border-transparent hover:border-slate-200 dark:hover:border-slate-700 mr-1" title="Ana Sayfaya Dön">
                    <i class="fas fa-home text-sm"></i>
                    <span>Ana Sayfa</span>
                </a>
                <nav class="hidden lg:flex items-center space-x-1 mr-2">
                    <a href="../tarih.html" class="px-3 py-2 rounded-lg font-bold text-sm transition-colors text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-700 dark:hover:text-slate-200 font-semibold">Tarih</a>
                    <a href="../turkce.html" class="px-3 py-2 rounded-lg font-bold text-sm transition-colors text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-700 dark:hover:text-slate-200 font-semibold">Türkçe</a>
                    <a href="../cografya.html" class="px-3 py-2 rounded-lg font-bold text-sm transition-colors bg-emerald-50 dark:bg-emerald-900/30 text-emerald-600 dark:text-emerald-400">Coğrafya</a>
                    <a href="#" class="px-3 py-2 rounded-lg text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-700 dark:hover:text-slate-200 font-semibold text-sm transition-colors">Vatandaşlık</a>
                </nav>
                
                <div class="hidden md:flex items-center bg-slate-100 dark:bg-slate-800 rounded-full px-4 py-2 border border-slate-200 dark:border-slate-700 focus-within:ring-2 focus-within:ring-emerald-500 transition-all relative z-50">
                    <i class="fas fa-search text-slate-400"></i>
                    <input type="text" id="searchInput" placeholder="Notlarda ara..." class="bg-transparent border-none outline-none ml-2 text-sm text-slate-800 dark:text-slate-200 placeholder-slate-400 w-48 lg:w-64" autocomplete="off">
                    <div id="searchResults" class="absolute top-full right-0 mt-3 w-80 bg-white dark:bg-slate-800 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-700 hidden flex-col max-h-[70vh] overflow-y-auto z-50 custom-scrollbar divide-y divide-slate-100 dark:divide-slate-700/50"></div>
                </div>
                
                <button id="dark-mode-toggle" class="p-3 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 transition-all border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300">
                    <i class="fas fa-moon dark:hidden text-lg"></i>
                    <i class="fas fa-sun hidden dark:block text-yellow-400 text-lg"></i>
                </button>
            </div>
        </div>
    </header>

    <div class="max-w-[1600px] mx-auto flex flex-col lg:flex-row gap-8 lg:gap-12 p-4 md:p-8 lg:px-12">
        
        <!-- Sidebar Navigation -->
        <aside class="w-full lg:w-72 shrink-0"></aside>

        <!-- Main Content -->
        <main class="flex-1 space-y-8 lg:space-y-12">
            
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="relative z-10 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                    <div>
                        <a href="../cografya.html" class="inline-flex items-center text-emerald-600 dark:text-emerald-400 hover:text-emerald-800 dark:hover:text-emerald-300 font-bold text-sm mb-4 transition-colors">
                            <i class="fas fa-arrow-left mr-2"></i>Coğrafya Ana Menüye Dön
                        </a>
                        <h2 class="text-3xl md:text-4xl font-black text-slate-900 dark:text-white leading-tight tracking-tight uppercase">{title}</h2>
                        <p class="text-slate-500 dark:text-slate-400 mt-2 text-sm">{subtitle}</p>
                    </div>
                    <div class="shrink-0">
                        <span class="inline-flex items-center bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-400 font-black text-xs px-4 py-2.5 rounded-2xl border border-emerald-100 dark:border-emerald-900/50 uppercase tracking-widest shadow-sm">
                            <i class="fas fa-calendar-check mr-2 text-emerald-500"></i> TÜİK 2025 Güncellemesi
                        </span>
                    </div>
                </div>
            </header>

            {sections_content}

        </main>
    </div>

    <!-- Scriptler -->
    <script>
        function toggleSidebarSection(id, btn) {{
            const nav = document.getElementById(id);
            const chevron = document.getElementById(id + '-chevron');
            nav.classList.toggle('hidden');
            chevron.classList.toggle('rotate-180');
        }}

        function toggleSubNav(id, btn) {{
            const nav = document.getElementById(id);
            const chevron = document.getElementById(id + '-chevron');
            nav.classList.toggle('hidden');
            chevron.classList.toggle('rotate-180');
        }}
    </script>
    
    <!-- Arama motorunu aktifleştiren script -->
    <script src="../assets/js/script.js"></script>
</body>
</html>
"""
    
    out_path = os.path.join('cografya', filename)
    with open(out_path, 'w', encoding='utf-8') as f_out:
        f_out.write(page_html)
    print(f"Generated {filename} successfully.")

# Delete old tuik-verileri.html
old_path = 'cografya/tuik-verileri.html'
if os.path.exists(old_path):
    os.remove(old_path)
    print("Deleted old tuik-verileri.html successfully.")
