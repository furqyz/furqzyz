import os
import re

def generate_sidebar(active_index):
    items = [
        {"title": "1. İslamiyet Öncesi Türk Tarihi", "file": "index.html" if active_index == 1 else "../index.html", "icon": "fa-landmark"},
        {"title": "2. İlk Türk İslam Devletleri", "file": "unite2.html", "icon": "fa-mosque"},
        {"title": "3. Anadolu (Türkiye) Selçuklu Devleti", "file": "unite3.html", "icon": "fa-chess-knight"},
        {"title": "4. Osmanlı Devleti Kültür ve Medeniyeti", "file": "unite4.html", "icon": "fa-landmark-dome"},
        {"title": "5. Osmanlı Devleti Kuruluş Dönemi (1299 - 1453)", "file": "unite5.html", "icon": "fa-campground"},
        {"title": "6. Osmanlı Devleti Yükselme Dönemi (1453 - 1595)", "file": "unite6.html", "icon": "fa-chess-rook"},
        {"title": "7. XVII. Yüzyılda Osmanlı Devleti (Duraklama Dönemi) (1595 - 1699)", "file": "unite7.html", "icon": "fa-hourglass-end"},
        {"title": "8. XVIII. Yüzyılda Osmanlı Devleti (Gerileme Dönemi) (1699 - 1792)", "file": "unite8.html", "icon": "fa-arrow-trend-down"},
        {"title": "9. XIX. Yüzyılda Osmanlı Devleti (Dağılma Dönemi) (1792 - 1922)", "file": "unite9.html", "icon": "fa-unlink"},
        {"title": "10. XX. Yüzyıl Başlarında Osmanlı Devleti", "file": "unite10.html", "icon": "fa-globe"},
        {"title": "11. Millî Mücadele Hazırlık Dönemi", "file": "unite11.html", "icon": "fa-bullhorn"},
        {"title": "12. I. TBMM Dönemi ve Gelişmeleri (1920 - 1923)", "file": "unite12.html", "icon": "fa-building-columns"},
        {"title": "13. Millî Mücadele Muharebeler Dönemi", "file": "unite13.html", "icon": "fa-shield-halved"},
        {"title": "14. Atatürk'ün Hayatı", "file": "unite14.html", "icon": "fa-user-tie"},
        {"title": "15. Atatürk Dönemi İç Politika", "file": "unite15.html", "icon": "fa-landmark-flag"},
        {"title": "16. Atatürk İlkeleri", "file": "unite16.html", "icon": "fa-scale-balanced"},
        {"title": "17. Atatürk İnkılapları", "file": "unite17.html", "icon": "fa-lightbulb"},
        {"title": "18. Atatürk Dönemi Türk Dış Politikası", "file": "unite18.html", "icon": "fa-earth-europe"},
        {"title": "19. Cumhuriyet Dönemi Kültür ve Medeniyeti", "file": "unite19.html", "icon": "fa-masks-theater"},
        {"title": "20. Çağdaş Türk ve Dünya Tarihi", "file": "unite20.html", "icon": "fa-earth-americas"},
        {"title": "21. XX. Yüzyıl Başlarında Dünya", "file": "unite21.html", "icon": "fa-biohazard"},
        {"title": "22. II. Dünya Savaşı (1939 - 1945)", "file": "unite22.html", "icon": "fa-fighter-jet"},
        {"title": "23. Soğuk Savaş Dönemi (1947 - 1990)", "file": "unite23.html", "icon": "fa-snowflake"},
        {"title": "24. Yumuşama (Detant) Dönemi", "file": "unite24.html", "icon": "fa-handshake-angle"},
        {"title": "25. Küreselleşen Dünya (1990 - 2026)", "file": "unite25.html", "icon": "fa-network-wired"},
    ]

    nav_html = '<nav class="space-y-1.5 max-h-[60vh] overflow-y-auto pr-1.5 custom-scrollbar">\n'
    
    for i, item in enumerate(items):
        file_path = item['file']
        if active_index == 1 and i > 0:
            file_path = f"unitler/{item['file']}"
            
        if i + 1 == active_index:
            nav_html += f'''                        <a href="{file_path}" class="flex items-center justify-between bg-gradient-to-r from-indigo-600 to-indigo-500 text-white px-3 py-3 rounded-xl font-semibold shadow-md shadow-indigo-200 dark:shadow-none transition-transform hover:scale-[1.02] mb-2 mt-2">
                            <div class="flex items-start space-x-3">
                                <i class="fas {item['icon']} w-4 text-center mt-0.5"></i>
                                <span class="text-[13px] leading-snug">{item['title']}</span>
                            </div>
                            <i class="fas fa-chevron-right text-[10px] opacity-70 shrink-0 ml-2 mt-1"></i>
                        </a>\n'''
        else:
            nav_html += f'''                        <a href="{file_path}" class="flex items-center justify-between text-slate-500 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-700/50 px-3 py-2.5 rounded-xl transition-all group">
                            <div class="flex items-start space-x-3 pr-2">
                                <i class="fas {item['icon']} text-slate-400 dark:text-slate-500 group-hover:text-indigo-500 transition-colors w-4 text-center shrink-0 mt-0.5"></i>
                                <span class="group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors text-[13px] leading-snug font-medium">{item['title']}</span>
                            </div>
                        </a>\n'''

    nav_html += '                    </nav>'
    return nav_html

def get_base_template():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace script and style paths to relative
    content = content.replace('href="style.css"', 'href="../style.css"')
    content = content.replace('src="script.js"', 'src="../script.js"')
    return content

def create_unit_file(unit_num, html_content):
    template = get_base_template()
    # Replace the main content
    template = re.sub(r'<main class="flex-1 space-y-8 lg:space-y-12">.*?</main>', f'<main class="flex-1 space-y-8 lg:space-y-12">\n{html_content}\n        </main>', template, flags=re.DOTALL)
    
    # Generate sidebar for this unit
    new_nav = generate_sidebar(unit_num)
    template = re.sub(r'<nav class="space-y-1.5 max-h-\[60vh\] overflow-y-auto pr-1.5 custom-scrollbar">.*?</nav>', new_nav, template, flags=re.DOTALL)
    
    with open(f'unitler/unite{unit_num}.html', 'w', encoding='utf-8') as f:
        f.write(template)

def update_existing_sidebars():
    files = [('index.html', 1)]
    for i in range(2, 21):
        files.append((f'unitler/unite{i}.html', i))
        
    for filepath, idx in files:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            new_nav = generate_sidebar(idx)
            content = re.sub(r'<nav class="space-y-1.5 max-h-\[60vh\] overflow-y-auto pr-1.5 custom-scrollbar">.*?</nav>', new_nav, content, flags=re.DOTALL)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

# U21
u21 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-biohazard text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">21. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">XX. YÜZYIL BAŞLARINDA DÜNYA</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">1918-1939 yılları arasında SSCB'nin kuruluşu, 1929 Krizi ve totaliter rejimlerin yükselişi.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- MOR BÖLÜM -->
                <section class="category-purple note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-hammer text-purple-600 dark:text-purple-300"></i></div>
                        SSCB'nin Kurulması ve Türkistan
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-purple-100 font-medium text-sm">
                        <ul class="space-y-3">
                            <li><strong class="text-purple-800 dark:text-purple-300 block">Bolşevik İhtilali (1917):</strong> "Barış, Ekmek ve Toprak" vaadiyle Vladimir Lenin tarafından Çarlık Rusya'nın yıkılarak SSCB'nin temellerinin atılmasıdır.</li>
                            <li><strong class="text-purple-800 dark:text-purple-300 block">NEP:</strong> Lenin'in iç savaş sonrası ekonomiyi toparlamak için ilan ettiği "Yeni Ekonomi Politikası"dır.</li>
                            <li><strong class="text-purple-800 dark:text-purple-300 block">Stalin Dönemi:</strong> Tarımda özel mülkiyeti bitiren "Kolektifleştirme (Kolhoz)" çiftlikleri kuruldu. Köylülerin (Kulak) direnmesi sonucu milyonlarca kişi öldü.</li>
                        </ul>
                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl border border-purple-100 dark:border-purple-800/30">
                            <strong class="text-purple-800 dark:text-purple-300 block mb-1">Basmacı Hareketi:</strong>
                            <p>Türkistan'da Ruslara karşı "Baskın yapan" anlamına gelen, "Çar ve Ruslar defolun" parolasıyla başlayan büyük millî direniştir. Korbaşı Ergaş, Zeki Velidi Togan ve Enver Paşa önderlik etmiştir. <strong>Enver Paşa şehit düşmüştür</strong>.</p>
                        </div>
                    </div>
                </section>

                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-globe-asia text-yellow-600 dark:text-yellow-300"></i></div>
                        Ortadoğu ve Uzak Doğu
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-yellow-100 font-medium text-sm">
                        <div class="bg-yellow-50 dark:bg-yellow-900/30 p-4 rounded-xl border border-yellow-100 dark:border-yellow-800/50">
                            <strong class="text-yellow-800 dark:text-yellow-300 block mb-1">Balfour Deklarasyonu (1917):</strong>
                            <p>İngiltere'nin Filistin'de bir Yahudi Devleti (İsrail) kurulmasını onaylayan belgedir.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl">
                            <strong class="text-yellow-800 dark:text-yellow-300 block mb-1">Japonya (Meiji Restorasyonu):</strong>
                            <p>İmparator Mutsuhito'nun "Güçlü ordu, zengin ülke" parolasıyla yaptığı devrimdir. Feodalite kalktı, sanayi kuruldu.</p>
                            <div class="mt-2 bg-red-50 dark:bg-red-900/30 p-2 rounded border border-red-200 dark:border-red-800/50">
                                <strong class="text-red-700 dark:text-red-400 block mb-1 text-xs"><i class="fas fa-exclamation-triangle"></i> DİKKAT TUZAK</strong>
                                <p class="text-xs text-red-900 dark:text-red-200">Meiji restorasyonunda Latin harflerine geçiş veya kılık-kıyafet devrimi KESİNLİKLE YOKTUR.</p>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-chart-line text-cyan-600 dark:text-cyan-300"></i></div>
                        1929 Dünya Ekonomik Krizi ve Totaliter Rejimler
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-slate-800 dark:text-cyan-100 font-medium text-sm">
                        <div class="space-y-4">
                            <div class="bg-cyan-50 dark:bg-cyan-900/30 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Kara Perşembe (1929):</strong>
                                <p>ABD (New York) borsasının aniden çökmesidir. Başkan Hoover'ın tecrübesizliğine bağlanır. Yeni Başkan <strong>Roosevelt</strong> "New Deal" (Yeni Antlaşma) ile toparlamıştır.</p>
                            </div>
                            <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl">
                                <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Türkiye'ye Etkisi:</strong>
                                <p>Türkiye krize karşı "Kliring Sistemi"ni uygulamış, Milli İktisat Cemiyeti'ni kurmuş ve <strong>Devletçilik</strong> ilkesine geçmiştir.</p>
                            </div>
                        </div>
                        <div class="space-y-4">
                            <div class="bg-cyan-50 dark:bg-cyan-900/30 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Barış Çabaları:</strong>
                                <p>Locarno Antlaşması (1925) ve Briand-Kellogg Paktı (1928) ile savaş "kanun dışı" sayılmıştır.</p>
                            </div>
                            <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl">
                                <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Totaliter Rejimler:</strong>
                                <ul class="space-y-1">
                                    <li><strong>İtalya (Faşizm):</strong> Mussolini ("Kara Gömlekliler") -> "Bizim Deniz" politikası.</li>
                                    <li><strong>Almanya (Nazizm):</strong> Hitler ("Kahverengi Gömlekliler") -> "Hayat Sahası" politikası.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <section class="exam-memory note-card p-8 md:p-12 rounded-3xl shadow-2xl shadow-indigo-500/20 relative overflow-hidden group mt-12">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16 transition-transform group-hover:scale-150 duration-700"></div>
                <div class="absolute right-8 top-1/2 -translate-y-1/2 opacity-10 transform group-hover:rotate-12 transition-transform duration-700 pointer-events-none">
                    <i class="fas fa-brain text-[12rem] text-indigo-900"></i>
                </div>
                <div class="relative z-10">
                    <h3 class="text-3xl font-black mb-8 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-600 dark:text-indigo-400"></i> SINAV HAFIZASI
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2019 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Almanya'nın yayılmacılığı karşısında İngiltere Başbakanı Chamberlain'in uyguladığı politika nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Yatıştırma Politikası (Appeasement)</strong></p>
                        </div>
                    </div>
                </div>
            </section>
"""

# U22
u22 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-fighter-jet text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">22. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">II. DÜNYA SAVAŞI</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">1939-1945 yılları arasında dünya çapında yıkıma sebep olan savaşın kritik cepheleri ve Türkiye'nin tutumu.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- KIRMIZI BÖLÜM -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-crosshairs text-red-600 dark:text-red-300"></i></div>
                        Savaşın Seyri ve Cepheler
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-red-100 font-medium text-sm">
                        <ul class="space-y-3">
                            <li><strong class="text-red-800 dark:text-red-300 block">Başlangıç:</strong> 1 Eylül 1939'da Almanya'nın Polonya'yı işgal etmesiyle başlamıştır.</li>
                            <li><strong class="text-red-800 dark:text-red-300 block">Maginot Hattı:</strong> Fransa'nın savunma hattıdır ancak Almanlar "Yıldırım Harekâtı" ile aşarak işgal etmiştir.</li>
                            <li><strong class="text-red-800 dark:text-red-300 block">Barbarossa Harekâtı:</strong> Almanya'nın petrol için SSCB'ye saldırmasıdır ancak Stalingrad'da ağır yenilgi almışlardır.</li>
                            <li><strong class="text-red-800 dark:text-red-300 block">Pearl Harbor Baskını:</strong> Japonya'nın ABD'ye sürpriz saldırısıdır. ABD savaşa girmiştir.</li>
                        </ul>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-handshake text-orange-600 dark:text-orange-300"></i></div>
                        Konferanslar ve Savaşın Bitişi
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-orange-100 font-medium text-sm">
                        <div class="bg-orange-50 dark:bg-orange-900/30 p-4 rounded-xl border border-orange-100 dark:border-orange-800/50">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Atlantik Bildirisi (1941):</strong>
                            <p>ABD ve İngiltere'nin imzaladığı, Birleşmiş Milletler'in (BM) temeli sayılan belgedir.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl border border-orange-100 dark:border-orange-800/30">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Yalta Konferansı (1945):</strong>
                            <p>Roosevelt, Churchill ve Stalin arasında yapıldı. Almanya 4'e ayrıldı ve BM'de Veto Hakkı olan <strong>5 daimi üye (ABD, SSCB, İngiltere, Fransa, Çin)</strong> belirlendi.</p>
                        </div>
                        <div class="bg-orange-50 dark:bg-orange-900/30 p-4 rounded-xl border border-orange-100 dark:border-orange-800/50">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Savaşın Bitişi:</strong>
                            <p>Normandiya Çıkarması ile Fransa kurtarıldı ve ABD'nin Japonya'ya atom bombası atmasıyla savaş bitti.</p>
                        </div>
                    </div>
                </section>

                <!-- MOR BÖLÜM -->
                <section class="category-purple note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-shield-halved text-purple-600 dark:text-purple-300"></i></div>
                        Türkiye'nin Durumu ve Ekonomik Önlemler
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-slate-800 dark:text-purple-100 font-medium text-sm">
                        <div class="space-y-4">
                            <div class="bg-purple-50 dark:bg-purple-900/30 p-4 rounded-xl border border-purple-100 dark:border-purple-800/50">
                                <strong class="text-purple-800 dark:text-purple-300 block mb-1">Aktif Tarafsızlık:</strong>
                                <p>İsmet İnönü dönemidir. Alman tehdidine karşı Trakya'ya <strong>"Çakmak Hattı"</strong> kuruldu. Churchill, Adana ve Kahire'de Türkiye'yi ikna etmeye çalıştı.</p>
                            </div>
                            <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl">
                                <strong class="text-purple-800 dark:text-purple-300 block mb-1">Savaşa Giriş:</strong>
                                <p>Türkiye, BM'ye kurucu üye olabilmek için kâğıt üzerinde savaş ilan etti.</p>
                            </div>
                        </div>
                        <div class="space-y-4">
                            <div class="bg-purple-50 dark:bg-purple-900/30 p-4 rounded-xl border border-purple-100 dark:border-purple-800/50">
                                <strong class="text-purple-800 dark:text-purple-300 block mb-1">Ekonomik Önlemler:</strong>
                                <ul class="space-y-1">
                                    <li>Milli Korunma Kanunu</li>
                                    <li>Varlık Vergisi (Haksız kazanca karşı)</li>
                                    <li>Toprak Mahsulleri Vergisi</li>
                                </ul>
                            </div>
                            <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl border border-purple-100 dark:border-purple-800/30 relative">
                                <div class="absolute right-2 top-2 text-purple-500/10 text-4xl"><i class="fas fa-school"></i></div>
                                <strong class="text-purple-800 dark:text-purple-300 block mb-1">Köy Enstitüleri (1940):</strong>
                                <p>Hasan Ali Yücel ve İsmail Hakkı Tonguç önderliğinde açılmıştır.</p>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <section class="exam-memory note-card p-8 md:p-12 rounded-3xl shadow-2xl shadow-indigo-500/20 relative overflow-hidden group mt-12">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16 transition-transform group-hover:scale-150 duration-700"></div>
                <div class="absolute right-8 top-1/2 -translate-y-1/2 opacity-10 transform group-hover:rotate-12 transition-transform duration-700 pointer-events-none">
                    <i class="fas fa-brain text-[12rem] text-indigo-900"></i>
                </div>
                <div class="relative z-10">
                    <h3 class="text-3xl font-black mb-8 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-600 dark:text-indigo-400"></i> SINAV HAFIZASI
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2024 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Almanya'nın dörde bölünmesi ve 5 daimi üyenin veto hakkı elde ettiği konferans hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Yalta Konferansı</strong></p>
                        </div>
                    </div>
                </div>
            </section>
"""

# U23
u23 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-snowflake text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">23. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">SOĞUK SAVAŞ DÖNEMİ</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">1947-1990 arası Kutuplaşmalar, Demokrat Parti dönemi ve Kore Savaşı'nın etkileri.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-globe text-cyan-600 dark:text-cyan-300"></i></div>
                        Doğu ve Batı Blokları
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-cyan-100 font-medium text-sm">
                        <div class="bg-blue-50 dark:bg-blue-900/20 p-4 rounded-xl border border-blue-100 dark:border-blue-800/30">
                            <strong class="text-blue-800 dark:text-blue-300 block mb-2 text-lg">Batı Bloku (ABD Öncülüğünde):</strong>
                            <ul class="space-y-1">
                                <li><strong>Truman Doktrini:</strong> Türkiye ve Yunanistan'a mali/askeri yardım.</li>
                                <li><strong>Marshall Planı:</strong> Avrupa'yı kalkındırmak için 16 ülkeye yardım.</li>
                                <li><strong>NATO (1949):</strong> Batı'nın askerî savunma paktı.</li>
                            </ul>
                        </div>
                        <div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-xl border border-red-100 dark:border-red-800/30">
                            <strong class="text-red-800 dark:text-red-300 block mb-2 text-lg">Doğu Bloku (SSCB Öncülüğünde):</strong>
                            <ul class="space-y-1">
                                <li><strong>Cominform:</strong> Siyasi iş birliği (Yugoslavya atıldı).</li>
                                <li><strong>Comecon:</strong> Ekonomik iş birliği.</li>
                                <li><strong>Varşova Paktı (1955):</strong> Askerî ittifak.</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- YEŞİL BÖLÜM -->
                <section class="category-green note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-emerald-900 dark:text-emerald-200">
                        <div class="bg-emerald-100 dark:bg-emerald-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-fire text-emerald-600 dark:text-emerald-300"></i></div>
                        Sıcak Çatışmalar ve Ortadoğu
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-emerald-100 font-medium text-sm">
                        <div class="bg-emerald-50 dark:bg-emerald-900/30 p-4 rounded-xl border border-emerald-100 dark:border-emerald-800/50">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-1">İsrail'in Kuruluşu (1948):</strong>
                            <p>İngiltere'nin çekilmesiyle kurulmuş, Arap-İsrail savaşları başlamıştır.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl border border-emerald-100 dark:border-emerald-800/30">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-1">Kore Savaşı (1950-1953):</strong>
                            <p>Kuzey Kore'nin Güney'e saldırmasıdır. Türkiye, NATO'ya girebilmek için Tuğgeneral Tahsin Yazıcı komutasında asker göndermiştir.</p>
                        </div>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-landmark-flag text-orange-600 dark:text-orange-300"></i></div>
                        Demokrat Parti Dönemi (1950 - 1960)
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-slate-800 dark:text-orange-100 font-medium text-sm">
                        <div class="space-y-4">
                            <div class="bg-orange-50 dark:bg-orange-900/30 p-4 rounded-xl border border-orange-100 dark:border-orange-800/50">
                                <strong class="text-orange-800 dark:text-orange-300 block mb-1">Dörtlü Takrir ve Kuruluş:</strong>
                                <p>Celal Bayar, Adnan Menderes, Refik Koraltan ve Fuad Köprülü'nün verdiği önergeyle DP kurulmuştur.</p>
                            </div>
                            <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl">
                                <strong class="text-orange-800 dark:text-orange-300 block mb-1">Beyaz Devrim (1950):</strong>
                                <p>1950 seçimleriyle (Gizli oy - Açık sayım) CHP'nin 27 yıllık iktidarı kansız bir şekilde DP'ye geçmiştir.</p>
                            </div>
                        </div>
                        <div class="space-y-4">
                            <div class="bg-orange-50 dark:bg-orange-900/30 p-4 rounded-xl border border-orange-100 dark:border-orange-800/50">
                                <strong class="text-orange-800 dark:text-orange-300 block mb-1">Önemli Gelişmeler:</strong>
                                <p>Ezan Arapçaya çevrildi, Atatürk Üni. ve ODTÜ açıldı. 27 Mayıs 1960 askeri darbesiyle sona erdi.</p>
                            </div>
                            <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl">
                                <strong class="text-orange-800 dark:text-orange-300 block mb-1">Sanayi:</strong>
                                <p>1961'de <strong>"Devrim"</strong> arabaları üretildi. N. Erbakan "Gümüş Motor" projesini başlattı.</p>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <section class="exam-memory note-card p-8 md:p-12 rounded-3xl shadow-2xl shadow-indigo-500/20 relative overflow-hidden group mt-12">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16 transition-transform group-hover:scale-150 duration-700"></div>
                <div class="absolute right-8 top-1/2 -translate-y-1/2 opacity-10 transform group-hover:rotate-12 transition-transform duration-700 pointer-events-none">
                    <i class="fas fa-brain text-[12rem] text-indigo-900"></i>
                </div>
                <div class="relative z-10">
                    <h3 class="text-3xl font-black mb-8 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-600 dark:text-indigo-400"></i> SINAV HAFIZASI
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2024 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Soğuk Savaş Dönemi'ni başlatan gelişme nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: İkinci Dünya Savaşı'nın sona ermesi</strong></p>
                        </div>
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2023 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Türkiye'nin NATO'ya üye olarak kabul edilmesinde ne etkili olmuştur?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Kore Savaşı'na asker göndermesi</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">1946'da Demokrat Parti'nin kurulmasına yol açan önerge nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Dörtlü Takrir</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2019 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">SSCB'nin Batı Blokuna karşı ekonomik alanda kurduğu birlik nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: COMECON</strong></p>
                        </div>

                    </div>
                </div>
            </section>
"""

# U24
u24 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-handshake-angle text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">24. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">YUMUŞAMA (DETANT) DÖNEMİ</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Bloklar arası yumuşamanın yaşandığı dönem, Küba Krizi ve Kıbrıs Meselesinin Türkiye'ye yansımaları.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- MOR BÖLÜM -->
                <section class="category-purple note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-earth-americas text-purple-600 dark:text-purple-300"></i></div>
                        Dünyadaki Krizler ve Diplomasiler
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-purple-100 font-medium text-sm">
                        <div class="bg-purple-50 dark:bg-purple-900/30 p-4 rounded-xl border border-purple-100 dark:border-purple-800/50">
                            <strong class="text-purple-800 dark:text-purple-300 block mb-1">Küba Füze Krizi (1962):</strong>
                            <p>SSCB'nin Küba'ya, ABD'nin de Türkiye'ye (Jüpiter füzeleri) füze yerleştirmesiyle çıkan Nükleer savaşın eşiğinden dönülen en büyük krizdir.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl">
                            <strong class="text-purple-800 dark:text-purple-300 block mb-1">Vietnam Savaşı:</strong>
                            <p>Efsane boksör Muhammed Ali, "Vietnamlılar bana hiçbir kötülük yapmadılar" diyerek hapis cezasına rağmen askere gitmeyi reddetmiştir.</p>
                        </div>
                        <div class="bg-purple-50 dark:bg-purple-900/30 p-4 rounded-xl border border-purple-100 dark:border-purple-800/50">
                            <strong class="text-purple-800 dark:text-purple-300 block mb-1">Ping-Pong Diplomasisi ve Petrol Krizi:</strong>
                            <p>ABD-Çin ilişkileri "masa tenisi" ile yumuşamıştır. 1973'te OAPEC ülkeleri Batı'ya karşı petrolü bir "silah" olarak kullanmıştır.</p>
                        </div>
                    </div>
                </section>

                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-anchor text-yellow-600 dark:text-yellow-300"></i></div>
                        Türkiye'nin Dış Politikası
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-yellow-100 font-medium text-sm">
                        <div class="bg-yellow-50 dark:bg-yellow-900/30 p-4 rounded-xl border border-yellow-100 dark:border-yellow-800/50">
                            <strong class="text-yellow-800 dark:text-yellow-300 block mb-1">Kıbrıs Meselesi ve Kanlı Noel:</strong>
                            <p>Rum EOKA'ya karşı Türkler TMT'yi kurdu. 1963 "Kanlı Noel" sonrası müdahale etmek istedik ancak ABD Başkanı'nın <strong>"Johnson Mektubu"</strong> ile engellendi.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl">
                            <strong class="text-yellow-800 dark:text-yellow-300 block mb-1">1974 Kıbrıs Barış Harekâtı:</strong>
                            <p>Başbakan B. Ecevit döneminde, "Ayşe tatile çıksın" parolasıyla yapıldı. ABD, Türkiye'ye 3 yıl silah ambargosu uyguladı.</p>
                        </div>
                        <div class="bg-red-50 dark:bg-red-900/30 p-4 rounded-xl border border-red-100 dark:border-red-800/50">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">ASALA Terörü:</strong>
                            <p>1970-80'lerde Ermenilerin iddialarını tanıtmak için Türk diplomatlarını şehit ettikleri terör örgütüdür.</p>
                        </div>
                    </div>
                </section>
            </div>

            <section class="exam-memory note-card p-8 md:p-12 rounded-3xl shadow-2xl shadow-indigo-500/20 relative overflow-hidden group mt-12">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16 transition-transform group-hover:scale-150 duration-700"></div>
                <div class="absolute right-8 top-1/2 -translate-y-1/2 opacity-10 transform group-hover:rotate-12 transition-transform duration-700 pointer-events-none">
                    <i class="fas fa-brain text-[12rem] text-indigo-900"></i>
                </div>
                <div class="relative z-10">
                    <h3 class="text-3xl font-black mb-8 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-600 dark:text-indigo-400"></i> SINAV HAFIZASI
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">ABD Başkanı Johnson'ın 1964'te yazdığı mektubun amacı nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Kıbrıs Sorunu'na Türkiye'nin askerî müdahalesini engellemek</strong></p>
                        </div>
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">ABD'nin 1975-1978 yılları arasında Türkiye'ye silah ambargosu uygulamasının temel sebebi nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Kıbrıs Barış Harekâtı</strong></p>
                        </div>

                    </div>
                </div>
            </section>
"""

# U25
u25 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-network-wired text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">25. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">KÜRESELLEŞEN DÜNYA</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">SSCB'nin dağılmasından günümüze yaşanan siyasi gelişmeler, Bosna Savaşı ve Türkiye'nin bilimsel başarıları.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-flag text-cyan-600 dark:text-cyan-300"></i></div>
                        SSCB'nin Dağılması ve Türk Cumhuriyetleri
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-cyan-100 font-medium text-sm">
                        <div class="bg-cyan-50 dark:bg-cyan-900/30 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">SSCB'nin Çöküşü:</strong>
                            <p>Gorbaçov'un Glasnost ve Perestroika politikaları başarısız oldu, 1991'de SSCB dağıldı ve BDT kuruldu.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Azerbaycan ve Karabağ:</strong>
                            <p>Ebulfez Elçibey ve Haydar Aliyev ("Bir millet, iki devlet"). Hocalı Katliamı'nın yaşandığı Karabağ, 2020 operasyonuyla kurtarılmıştır.</p>
                        </div>
                        <div class="bg-cyan-50 dark:bg-cyan-900/30 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">TİKA:</strong>
                            <p>Orta Asya'da bağımsızlığını kazanan Türk cumhuriyetlerine kültürel ve ekonomik destek sağlamak için kurulmuştur.</p>
                        </div>
                    </div>
                </section>

                <!-- YEŞİL BÖLÜM -->
                <section class="category-green note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-emerald-900 dark:text-emerald-200">
                        <div class="bg-emerald-100 dark:bg-emerald-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-euro-sign text-emerald-600 dark:text-emerald-300"></i></div>
                        Avrupa Birliği ve Balkanlar
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-emerald-100 font-medium text-sm">
                        <div class="bg-emerald-50 dark:bg-emerald-900/30 p-4 rounded-xl border border-emerald-100 dark:border-emerald-800/50">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-1">Avrupa Birliği (AB):</strong>
                            <p>Maastricht (Ekonomik) ve Kopenhag (Siyasi) Kriterleriyle kuruldu. Türkiye 1999 Helsinki Zirvesi'nde "Aday Ülke" oldu.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-1">Bosna Savaşı (1992-1995):</strong>
                            <p>Sırpların Srebrenitsa Katliamı'nı yaptığı savaştır. Liderleri <strong>"Bilge Kral" Aliya İzzetbegoviç</strong>'tir. Dayton Antlaşması ile sona ermiştir.</p>
                        </div>
                    </div>
                </section>

                <!-- KIRMIZI BÖLÜM -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-atom text-red-600 dark:text-red-300"></i></div>
                        Türkiye'nin Bilim Dünyası ve Gelişmeler
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-slate-800 dark:text-red-100 font-medium text-sm">
                        <div class="bg-red-50 dark:bg-red-900/30 p-4 rounded-xl border border-red-100 dark:border-red-800/50">
                            <strong class="text-red-800 dark:text-red-300 block mb-2 text-lg">Önemli Şahsiyetler:</strong>
                            <ul class="space-y-2">
                                <li><strong class="text-red-700 dark:text-red-400">Oktay Sinanoğlu:</strong> Dünyanın en genç profesörü, "Türk Aynştaynı".</li>
                                <li><strong class="text-red-700 dark:text-red-400">Aziz Sancar:</strong> DNA onarımı, 2015 Nobel Kimya Ödülü.</li>
                                <li><strong class="text-red-700 dark:text-red-400">Gazi Yaşargil:</strong> Yüzyılın Beyin Cerrahı.</li>
                                <li><strong class="text-red-700 dark:text-red-400">Fuat Sezgin:</strong> İslam bilim tarihi araştırmacısı.</li>
                            </ul>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl">
                            <strong class="text-red-800 dark:text-red-300 block mb-2 text-lg">Güncel Gelişmeler:</strong>
                            <ul class="space-y-2">
                                <li><strong class="text-red-700 dark:text-red-400">Savunma Sanayii:</strong> Altay (Tank), Hürkuş (Uçak), Anka/Bayraktar (İHA/SİHA), Göktürk (Uydu).</li>
                                <li><strong class="text-red-700 dark:text-red-400">Arap Baharı:</strong> 2010'da Tunus'ta M. Buazizi'nin kendini yakmasıyla başlayan Ortadoğu halk ayaklanmalarıdır.</li>
                            </ul>
                        </div>
                    </div>
                </section>
            </div>

            <section class="exam-memory note-card p-8 md:p-12 rounded-3xl shadow-2xl shadow-indigo-500/20 relative overflow-hidden group mt-12">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16 transition-transform group-hover:scale-150 duration-700"></div>
                <div class="absolute right-8 top-1/2 -translate-y-1/2 opacity-10 transform group-hover:rotate-12 transition-transform duration-700 pointer-events-none">
                    <i class="fas fa-brain text-[12rem] text-indigo-900"></i>
                </div>
                <div class="relative z-10">
                    <h3 class="text-3xl font-black mb-8 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-600 dark:text-indigo-400"></i> SINAV HAFIZASI
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2024 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">1991'de SSCB'den ayrılan devletler arasında Türkiye tarafından bağımsızlığı en erken tanınan devlet hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Azerbaycan</strong></p>
                        </div>
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2017 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Bosna Savaşı sırasında Bosna-Hersek'in bağımsızlığında rol oynayan "Bilge Lider" kimdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Aliya İzzetbegoviç</strong></p>
                        </div>

                    </div>
                </div>
            </section>
"""

create_unit_file(21, u21)
create_unit_file(22, u22)
create_unit_file(23, u23)
create_unit_file(24, u24)
create_unit_file(25, u25)

# Ensure unit 20 is re-created with the correct 25-item sidebar as well
# Wait, my update_existing_sidebars() will handle 2-20, so 20's old content is kept but sidebar updated.
# This means unit 20 will still be "Çağdaş Türk ve Dünya Tarihi" overview!
update_existing_sidebars()

print("Units 21-25 generated successfully. Sidebar expanded to 25 items.")
