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
    ]
    
    upcoming = [
        "16. Atatürk İlkeleri",
        "17. Atatürk İnkılapları",
        "18. Atatürk Dönemi Türk Dış Politikası",
        "19. Cumhuriyet Dönemi Kültür ve Medeniyeti",
        "20. XX. Yüzyıl Başlarında Dünya (1918 - 1939)",
        "21. II. Dünya Savaşı (1939 - 1945)",
        "22. Soğuk Savaş Dönemi (1947 - 1990)",
        "23. Yumuşama Dönemi (1961 - 1990)",
        "24. Küreselleşen Dünya (1990 - 2026)",
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

    for title in upcoming:
        nav_html += f'''                        <button class="w-full flex items-center justify-between text-slate-500 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-700/50 px-3 py-2.5 rounded-xl transition-all group text-left">
                            <div class="flex items-start space-x-3 pr-2">
                                <i class="fas fa-lock text-slate-300 dark:text-slate-600 group-hover:text-indigo-400 transition-colors w-4 text-center shrink-0 mt-0.5"></i>
                                <span class="group-hover:text-slate-700 dark:group-hover:text-slate-200 transition-colors text-[13px] leading-snug">{title}</span>
                            </div>
                            <span class="text-[9px] font-bold bg-slate-100 dark:bg-slate-800 text-slate-400 dark:text-slate-500 px-1.5 py-0.5 rounded-md shrink-0 group-hover:bg-indigo-100 group-hover:text-indigo-600 transition-colors uppercase tracking-wider">Yakında</span>
                        </button>\n'''

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
    for i in range(2, 12):
        files.append((f'unitler/unite{i}.html', i))
        
    for filepath, idx in files:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            new_nav = generate_sidebar(idx)
            content = re.sub(r'<nav class="space-y-1.5 max-h-\[60vh\] overflow-y-auto pr-1.5 custom-scrollbar">.*?</nav>', new_nav, content, flags=re.DOTALL)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

# UNIT 12
u12 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-building-columns text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">12. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">I. TBMM DÖNEMİ VE GELİŞMELERİ</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Milli Mücadele'yi yürüten kurucu ve savaşçı meclisin özellikleri, çıkardığı kanunlar ve karşılaştığı isyanları incelediğimiz ünitedir.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- MOR BÖLÜM -->
                <section class="category-purple note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-star text-purple-600 dark:text-purple-300"></i></div>
                        Genel Özellikler ve İlkler
                    </h3>
                    <ul class="space-y-4 text-slate-800 dark:text-purple-100 font-medium">
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span><strong class="text-purple-700 dark:text-purple-400">Kurucu Meclistir:</strong> Yeni bir devlet, yeni bir ordu kurmuş ve yeni bir anayasa (1921 Teşkilat-ı Esasiye) yapmıştır.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span><strong class="text-purple-700 dark:text-purple-400">İhtilalcidir:</strong> Hem İstanbul Hükümeti'ne hem de İtilaf Devletleri'ne başkaldırmıştır.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span><strong class="text-purple-700 dark:text-purple-400">Demokratik ve Ulusçudur:</strong> Üyeleri halkın seçimiyle gelmiştir. İçinde azınlık milletvekili yoktur.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span><strong class="text-purple-700 dark:text-purple-400">Savaşçı Meclistir:</strong> Kurtuluş Savaşı'nı (Muharebeler dönemini) yönetmiştir.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span><strong class="text-purple-700 dark:text-purple-400">İnkılapçı DEĞİLDİR:</strong> I. TBMM'nin yaptığı ilk ve tek inkılap Saltanat'ın kaldırılmasıdır. (Diğer tüm inkılapları 1923'te açılan II. TBMM yapacaktır).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span><strong class="text-purple-700 dark:text-purple-400">Meclis Hükümeti Sistemi:</strong> Meclis başkanı, hükümetin de başkanıdır (Başbakanlık veya Cumhurbaşkanlığı makamı yoktur). Güçler birliği (yasama, yürütme, yargı) ilkesi uygulanmıştır.</span></li>
                    </ul>
                </section>

                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-users text-yellow-600 dark:text-yellow-300"></i></div>
                        Meclisteki Gruplar ve Şahsiyetler
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-yellow-100 font-medium">
                        <div class="bg-white/40 dark:bg-black/10 p-4 rounded-xl">
                            <strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Meclis İçindeki Gruplar:</strong>
                            <p class="text-sm">Müdafaa-i Hukuk (M. Kemal'in grubu), İstiklal, Tesanüt, Yeşil Ordu, Halk Zümresi, Reform (Islahat).</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2 bg-red-50/50 dark:bg-red-900/20 rounded-r-xl">
                            <strong class="text-red-700 dark:text-red-400 block mb-1">DİKKAT TUZAK!</strong>
                            <p class="text-sm text-red-900 dark:text-red-200">ÖSYM şıklara "Felâh-ı Vatan" grubunu koyar. Felâh-ı Vatan I. TBMM'de değil, Son Osmanlı Mebusan Meclisi'ndedir.</p>
                        </div>
                        <div class="bg-white/40 dark:bg-black/10 p-4 rounded-xl">
                            <strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">İlk Hükümet İcra Vekilleri:</strong>
                            <p class="text-sm">Meclis Başkanı: <strong>Mustafa Kemal</strong><br>Millî Savunma Bakanı: <strong>Fevzi Çakmak</strong><br>Genelkurmay Başkanı: <strong>İsmet İnönü</strong><br>Sağlık Bakanı: <strong>Dr. Adnan Adıvar</strong></p>
                        </div>
                        <li class="bg-yellow-50/50 dark:bg-yellow-900/20 p-3 rounded-xl list-none"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Şerif Bey:</strong> I. TBMM açıldığında "En Yaşlı Üye" sıfatıyla açılış konuşmasını yapan Sinop mebusudur.</li>
                    </div>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-gavel text-cyan-600 dark:text-cyan-300"></i></div>
                        Çıkarılan Kanunlar ve TBMM'ye Karşı İsyanlar
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-slate-800 dark:text-cyan-100 font-medium">
                        <div class="space-y-4">
                            <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                <strong class="text-cyan-800 dark:text-cyan-300 block mb-2 text-lg">Çıkarılan Önemli Kanunlar:</strong>
                                <p class="text-sm leading-relaxed">Ağnam Vergisi (İlk kanundur), Hıyanet-i Vataniye, Firariler, İstiklal Mahkemelerinin kurulması, Nisab-ı Müzakere (İç tüzük), Men-i Müskirat (İçki yasağı), Başkomutanlık, Teşkilat-ı Esasiye.</p>
                            </div>
                            <div class="border-l-4 border-red-400 pl-4 py-3 bg-red-50/50 dark:bg-red-900/20 rounded-r-xl">
                                <strong class="text-red-700 dark:text-red-400 block mb-1"><i class="fas fa-exclamation-triangle mr-1"></i> DİKKAT TUZAK!</strong>
                                <p class="text-sm text-red-900 dark:text-red-200">ÖSYM şıklara <strong>Takrir-i Sükûn Kanunu'nu</strong> koyar. Bu kanun 1925'te Şeyh Sait isyanı için çıkarılmıştır, I. TBMM döneminde KESİNLİKLE YOKTUR.</p>
                            </div>
                            <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Bilecik Görüşmeleri (1920):</strong>
                                <p class="text-sm">İstanbul Hükümeti'nin (Tevfik Paşa Hükümeti) I. TBMM'yi hukuken tanıdığı ilk olaydır. (Amasya'da Temsil Heyeti tanınmıştı, Bilecik'te TBMM tanındı).</p>
                            </div>
                        </div>
                        
                        <div class="bg-white/60 dark:bg-slate-800/60 p-5 rounded-2xl border border-cyan-100 dark:border-cyan-800">
                            <strong class="text-cyan-800 dark:text-cyan-300 block text-lg mb-3 border-b border-cyan-200 dark:border-cyan-800 pb-2">İsyanların Sınıflandırması</strong>
                            <ul class="space-y-3 text-sm">
                                <li><strong class="text-cyan-700 dark:text-cyan-400 block">Doğrudan İstanbul Hükümeti:</strong> Ahmet Anzavur ve Kuvay-ı İnzibatiye (Halifelik Ordusu).</li>
                                <li><strong class="text-cyan-700 dark:text-cyan-400 block">İstanbul Hükümeti + İtilaf Devletleri:</strong> Bolu, Düzce, Hendek, Adapazarı isyanlarıdır. (İngilizlerin bu isyanları desteklemesinin KİLİT AMACI: Boğazların kontrolünü TBMM'ye karşı korumaktır).</li>
                                <li><strong class="text-cyan-700 dark:text-cyan-400 block">Eskiden Kuvayımilliyeci Olup İsyan Edenler:</strong> Çerkez Ethem ve Demirci Mehmet Efe (Düzenli orduya girmek istemedikleri için isyan etmişlerdir).</li>
                            </ul>
                        </div>
                    </div>
                </section>
            </div>
"""

# UNIT 13
u13 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-shield-halved text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">13. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">MİLLÎ MÜCADELE MUHAREBELER DÖNEMİ</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Doğu, Güney ve Batı cephelerindeki savaşlar, antlaşmalar ve büyük kahramanlık destanlarının anlatıldığı dönemdir.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- KIRMIZI (DOĞU) VE TURUNCU (GÜNEY) BÖLÜM -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-mountain-sun text-red-600 dark:text-red-300"></i></div>
                        Doğu Cephesi (Ermenistan'a Karşı)
                    </h3>
                    <div class="space-y-3 text-slate-800 dark:text-red-100 font-medium mb-8">
                        <p class="text-sm"><strong>Kazım Karabekir (Şark Fatihi)</strong> komutasındaki 15. Kolordu savaşmıştır (Osmanlı'dan kalan düzenli ordu vardır).</p>
                        <div class="bg-red-50/80 dark:bg-red-900/30 p-3 rounded-xl border border-red-100 dark:border-red-800/50">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Gümrü Antlaşması (1920):</strong>
                            <p class="text-sm">TBMM'nin ilk siyasi ve askerî başarısıdır. Sevr'i reddeden ve TBMM'yi tanıyan ilk devlet Ermenistan'dır. Metinde ilk defa "Türkiye" kelimesi geçmiştir.</p>
                        </div>
                    </div>

                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-orange-900 dark:text-orange-200 pt-6 border-t border-red-100 dark:border-red-800/50">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-fire-flame-curved text-orange-600 dark:text-orange-300"></i></div>
                        Güney Cephesi (Fransa ve Ermenilere Karşı)
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-orange-100 font-medium">
                        <p class="text-sm">Düzenli ordu yoktur, sadece Kuvayımilliye savaşmıştır. Sütçü İmam, Rıdvan Hoca (Maraş), Şahin Bey (Antep), Yüzbaşı Ali Saip (Urfa) önemli kahramanlardır.</p>
                        <div class="bg-orange-50/80 dark:bg-orange-900/30 p-3 rounded-xl border border-orange-100 dark:border-orange-800/50">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Ankara Antlaşması (1921):</strong>
                            <p class="text-sm">Sakarya Savaşı sonrası Fransa ile imzalanmış, bu cephe kapanmıştır. TBMM'yi tanıyan ilk İtilaf Devleti Fransa olmuştur. (Hatay Fransa mandasındaki Suriye'ye bırakıldı = Misakımilliden verilen 2. taviz).</p>
                        </div>
                        <div class="border-l-4 border-orange-400 pl-4 py-3 bg-orange-100/50 dark:bg-orange-900/40 rounded-r-xl">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-2"><i class="fas fa-medal mr-1"></i> UNVAN VE MADALYA TUZAĞI (DİKKAT!)</strong>
                            <ul class="text-sm space-y-2">
                                <li><strong>Unvan Alanlar (Sırasıyla):</strong> Antep (Gazi-1921), Maraş (Kahraman-1973), Urfa (Şanlı-1984).</li>
                                <li><strong>Madalya Alanlar (Sırasıyla):</strong> İnebolu (1924), Maraş (1925), Antep (2008), Urfa (2016).</li>
                                <li class="text-xs opacity-80 italic">Not: İnebolu'nun ilçe bazında ilk madalyayı almasının sebebi, silahların taşındığı İSTİKLAL YOLU'nun başlangıcı olmasıdır.</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- MOR BÖLÜM (BATI CEPHESİ) -->
                <section class="category-purple note-card p-6 md:p-8 rounded-3xl xl:col-span-1">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-khanda text-purple-600 dark:text-purple-300"></i></div>
                        Batı Cephesi (Yunanistan'a Karşı)
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-purple-100 font-medium text-sm">
                        
                        <div class="bg-white/40 dark:bg-black/10 p-4 rounded-xl border border-purple-100 dark:border-purple-800/30 relative">
                            <strong class="text-purple-800 dark:text-purple-300 block text-lg mb-1">I. İnönü Savaşı (1921):</strong>
                            <p class="mb-2">Düzenli ordunun ilk zaferidir. Sonuçları <strong class="bg-purple-200 dark:bg-purple-800 px-1.5 rounded text-purple-900 dark:text-purple-100">TALİM</strong> şifresiyle bilinir:</p>
                            <ul class="list-disc pl-4 space-y-1 mb-3">
                                <li><strong>T</strong>eşkilat-ı Esasiye (1921 Anayasası)</li>
                                <li><strong>A</strong>fganistan Dostluk Antlaşması (Tanıyan ilk Müslüman ülke)</li>
                                <li><strong>L</strong>ondra Konferansı</li>
                                <li><strong>İ</strong>stiklal Marşı'nın Kabulü</li>
                                <li><strong>M</strong>oskova Antlaşması (Batum Gürcistan'a verildi = İLK taviz)</li>
                            </ul>
                            <div class="bg-red-50 dark:bg-red-900/20 p-2 rounded border border-red-200 dark:border-red-800/50 text-xs">
                                <strong class="text-red-700 dark:text-red-400 block mb-1">Londra Konferansı Tuzağı:</strong> İtilaf devletleri ikilik çıkarmak için hem İstanbul'u hem TBMM'yi çağırdı. İstanbul delegesi Tevfik Paşa, "Sözü milletin asıl temsilcisi olan TBMM heyetine bırakıyorum" diyerek İtilaf Devletleri'nin planını bozmuştur.
                            </div>
                        </div>

                        <div class="bg-white/40 dark:bg-black/10 p-3 rounded-xl border border-purple-100 dark:border-purple-800/30">
                            <strong class="text-purple-800 dark:text-purple-300 block text-base mb-1">II. İnönü Savaşı:</strong>
                            <p>M. Kemal, İsmet Paşa'ya: "Siz orada yalnız düşmanı değil, milletin makûs (kötü) talihini de yendiniz." telgrafını çekmiştir.</p>
                        </div>

                        <div class="bg-red-50/50 dark:bg-red-900/20 p-3 rounded-xl border border-red-100 dark:border-red-800/30">
                            <strong class="text-red-800 dark:text-red-300 block text-base mb-1">Kütahya-Eskişehir Savaşları:</strong>
                            <p>Düzenli ordunun <strong>ilk ve tek yenilgisidir.</strong> Ordu Sakarya nehrinin doğusuna çekilmiştir. Bunun üzerine <strong class="text-purple-700 dark:text-purple-400">Başkomutanlık Kanunu</strong> çıkarılmış, M. Kemal sivil hayata (askerliğe) dönmüş ve Tekalif-i Milliye Emirleri'ni yayınlamıştır.</p>
                        </div>

                        <div class="bg-white/40 dark:bg-black/10 p-3 rounded-xl border border-purple-100 dark:border-purple-800/30">
                            <strong class="text-purple-800 dark:text-purple-300 block text-base mb-1">Sakarya Meydan Muharebesi (Subaylar Savaşı):</strong>
                            <p>Türklerin son savunma savaşıdır (1683 Viyana'dan beri süren geri çekiliş durmuştur). M. Kemal'e Gazi ve Mareşallik verilmiştir. Kars Antlaşması imzalanmış, Doğu sınırımız <strong class="underline">KESİNLEŞMİŞTİR</strong>.</p>
                        </div>

                        <div class="bg-white/40 dark:bg-black/10 p-3 rounded-xl border border-purple-100 dark:border-purple-800/30">
                            <strong class="text-purple-800 dark:text-purple-300 block text-base mb-1">Büyük Taarruz (Rum Sındığı):</strong>
                            <p>"Ordular, ilk hedefiniz Akdeniz'dir." Yunanlılar denize dökülmüş, Fevzi Çakmak Mareşal olmuştur.</p>
                        </div>

                    </div>
                </section>

                <!-- TURKUAZ BÖLÜM (LOZAN VE MUDANYA) -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-file-signature text-cyan-600 dark:text-cyan-300"></i></div>
                        Mudanya ve Lozan Antlaşmaları
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-slate-800 dark:text-cyan-100 font-medium">
                        
                        <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-5 rounded-2xl border border-cyan-100 dark:border-cyan-800/50 relative">
                            <div class="absolute right-4 top-4 text-cyan-500/10 text-6xl"><i class="fas fa-hand-holding-hand"></i></div>
                            <strong class="text-cyan-800 dark:text-cyan-300 block text-xl mb-3 border-b border-cyan-200 dark:border-cyan-800 pb-2 relative z-10">Mudanya Ateşkesi (1922)</strong>
                            <ul class="space-y-2 text-sm relative z-10">
                                <li>Doğu Trakya, İstanbul ve Boğazlar savaşılmadan kurtarılmıştır.</li>
                                <li>Bu durum Osmanlı Devleti'nin <strong>hukuken sona erdiğinin</strong> kanıtıdır.</li>
                                <li>Doğu Trakya'yı teslim alması için <strong class="text-cyan-700 dark:text-cyan-400">Refet Bele</strong> (Trakya Yüksek Komiseri) görevlendirilmiştir.</li>
                            </ul>
                        </div>
                        
                        <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-5 rounded-2xl border border-cyan-100 dark:border-cyan-800/50 relative">
                            <div class="absolute right-4 top-4 text-cyan-500/10 text-6xl"><i class="fas fa-globe"></i></div>
                            <strong class="text-cyan-800 dark:text-cyan-300 block text-xl mb-3 border-b border-cyan-200 dark:border-cyan-800 pb-2 relative z-10">Lozan Barış Antlaşması (1923)</strong>
                            <ul class="space-y-2 text-sm relative z-10">
                                <li>İsmet İnönü heyet başkanıdır.</li>
                                <li><strong class="text-red-600 dark:text-red-400">Taviz verilmeyen iki konu:</strong> Ermeni yurdu ve Kapitülasyonlar.</li>
                                <li><strong class="text-orange-600 dark:text-orange-400">Çözülemeyen (sonraya bırakılan) TEK konu:</strong> Musul (Irak Sınırı).</li>
                            </ul>
                        </div>

                    </div>
                </section>
            </div>
"""

# UNIT 14
u14 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-user-tie text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">14. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">ATATÜRK'ÜN HAYATI VE ESERLERİ</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Gazi Mustafa Kemal Atatürk'ün askeri kariyeri, yazdığı eserler ve özellikle "Nutuk" hakkındaki kritik bilgilerin yer aldığı ünitedir.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-medal text-yellow-600 dark:text-yellow-300"></i></div>
                        Hayatı ve Askerî Başarıları
                    </h3>
                    <div class="space-y-5 text-slate-800 dark:text-yellow-100 font-medium">
                        <div class="bg-white/40 dark:bg-black/10 p-4 rounded-xl">
                            <strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-2 border-b border-yellow-200 dark:border-yellow-800/50 pb-2">Etkilendiği Kişiler:</strong>
                            <ul class="grid grid-cols-2 gap-2 text-sm">
                                <li><strong class="text-yellow-700 dark:text-yellow-400">Ziya Gökalp:</strong> Milliyetçilik</li>
                                <li><strong class="text-yellow-700 dark:text-yellow-400">Namık Kemal:</strong> Vatanseverlik</li>
                                <li><strong class="text-yellow-700 dark:text-yellow-400">Tevfik Fikret:</strong> İnkılapçılık</li>
                                <li><strong class="text-yellow-700 dark:text-yellow-400">J.J. Rousseau:</strong> Yurttaşlık</li>
                            </ul>
                        </div>
                        <div class="bg-white/40 dark:bg-black/10 p-4 rounded-xl">
                            <strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Görevleri:</strong>
                            <p class="text-sm">İlk görev yeri <strong>Şam'dır</strong>.<br>I. Dünya Savaşı'nda sırasıyla <strong class="text-yellow-700 dark:text-yellow-400">Çanakkale, Kafkasya, Suriye-Filistin (Şifre: ÇIKIS)</strong> cephelerinde savaşmıştır.</p>
                        </div>
                    </div>
                </section>

                <!-- MOR BÖLÜM VE KIRMIZI TUZAK -->
                <section class="category-purple note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-book-open text-purple-600 dark:text-purple-300"></i></div>
                        Eserleri ve Nutuk (ÇOK ÖNEMLİ!)
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-purple-100 font-medium">
                        <div class="bg-purple-50/80 dark:bg-purple-900/40 p-4 rounded-xl border border-purple-100 dark:border-purple-800/50">
                            <strong class="text-purple-800 dark:text-purple-300 block text-lg mb-1">Eserleri:</strong>
                            <p class="text-sm">Geometri kitabı, Cumalı Ordugahı, Zabit ve Kumandan ile Hasbihal, Vatandaş İçin Medeni Bilgiler (Manevi kızı Afet İnan adıyla yayımlanmıştır).</p>
                        </div>
                        
                        <div class="bg-purple-50/80 dark:bg-purple-900/40 p-4 rounded-xl border border-purple-100 dark:border-purple-800/50 relative overflow-hidden">
                            <div class="absolute right-0 top-0 text-purple-500/10 text-6xl"><i class="fas fa-book"></i></div>
                            <strong class="text-purple-800 dark:text-purple-300 block text-xl mb-1 relative z-10">NUTUK (1919 - 1927):</strong>
                            <p class="text-sm relative z-10">1919'da "Samsun'a çıktım" ile başlar, 1927'deki "Gençliğe Hitabe" ile biter. Geliri <strong>Türk Hava Kurumu'na (THK)</strong> bırakılmıştır.</p>
                        </div>

                        <div class="border-l-4 border-red-500 pl-4 py-3 bg-red-50 dark:bg-red-900/30 rounded-r-xl shadow-sm mt-6">
                            <strong class="text-red-700 dark:text-red-400 block mb-2 text-lg"><i class="fas fa-radiation mr-1"></i> NUTUK TUZAĞI (ÖSYM FAVORİSİ)</strong>
                            <p class="text-sm text-red-900 dark:text-red-200 mb-2">Nutuk <strong>SADECE 1919-1927</strong> arası olayları kapsar.</p>
                            <div class="grid grid-cols-2 gap-2 text-sm">
                                <div class="bg-white/60 dark:bg-black/20 p-2 rounded">
                                    <strong class="text-green-600 dark:text-green-400"><i class="fas fa-check"></i> Nutuk'ta VARDIR:</strong><br>Kurtuluş Savaşı, Lozan, Cumhuriyetin İlanı, Şeyh Sait isyanı.
                                </div>
                                <div class="bg-white/60 dark:bg-black/20 p-2 rounded border border-red-200 dark:border-red-800/50">
                                    <strong class="text-red-600 dark:text-red-400"><i class="fas fa-times"></i> KESİNLİKLE YOKTUR:</strong><br>Harf İnkılabı (1928), Serbest Cumhuriyet Fırkası (1930), Menemen Olayı (1930), Soyadı Kanunu (1934).
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- YEŞİL BÖLÜM -->
                <section class="category-green note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-emerald-900 dark:text-emerald-200">
                        <div class="bg-emerald-100 dark:bg-emerald-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-dove text-emerald-600 dark:text-emerald-300"></i></div>
                        Miras ve Vefat
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-slate-800 dark:text-emerald-100 font-medium">
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-2 text-lg">Miras Bıraktığı Kurum ve Kişiler:</strong>
                            <p class="text-sm">Atatürk mirasının gelirlerini; Türk Tarih Kurumu, Türk Dil Kurumu, İsmet İnönü'nün çocuklarının eğitimi ve kız kardeşi Makbule Atadan'a bırakmıştır.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-2 text-lg">Vefat Süreci:</strong>
                            <p class="text-sm mb-1">Okuduğu son eser: <strong>Belleten dergisi</strong>.</p>
                            <p class="text-sm">Vefat ettiğinde Meclis Başkanı <strong>Abdülhalik Renda</strong>, Başbakan ise <strong>Celal Bayar'dır</strong>.</p>
                        </div>
                    </div>
                </section>
            </div>
"""

# UNIT 15
u15 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-landmark-flag text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">15. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">ATATÜRK DÖNEMİ İÇ POLİTİKA</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Çok partili hayata geçiş denemeleri, siyasi partiler, rejime yönelik isyanlar ve milliyetçilik refleksli olaylar bu ünitenin konusudur.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-users-viewfinder text-cyan-600 dark:text-cyan-300"></i></div>
                        Siyasi Partiler
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-cyan-100 font-medium">
                        
                        <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-1 text-lg">Cumhuriyet Halk Fırkası (CHF):</strong>
                            <p class="text-sm">Kurucusu M. Kemal'dir. Türkiye'nin <strong>ilk partisidir</strong>. Ekonomide "Devletçilik" ilkesini savunmuştur.</p>
                        </div>
                        
                        <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-1 text-lg">Terakkiperver Cumhuriyet Fırkası (1924):</strong>
                            <p class="text-sm mb-2">Türkiye'nin <strong>ilk muhalefet partisidir</strong>. Kurucuları: Kazım Karabekir, Ali Fuat, Refet, Adnan, Rauf (<strong class="bg-cyan-200 dark:bg-cyan-800 px-1 rounded text-cyan-900 dark:text-cyan-100">KARAR</strong> şifresi). Ekonomide liberalizmi benimsemiştir.</p>
                            <p class="text-sm text-red-600 dark:text-red-400">Parti tüzüğündeki "Dini inançlara saygılıdır" maddesi isyancıları cesaretlendirmiş ve Şeyh Sait İsyanı sonrasında kapatılmıştır.</p>
                        </div>

                        <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-1 text-lg">Serbest Cumhuriyet Fırkası (1930):</strong>
                            <p class="text-sm">İkinci muhalefet partisidir. <strong>1929 Dünya Ekonomik Krizinin (Kara Perşembe)</strong> etkilerini azaltmak için bizzat M. Kemal'in isteğiyle <strong>Ali Fethi Okyar</strong> tarafından kurulmuştur. Olayların kontrolden çıkacağı endişesiyle kurucusu tarafından kendi kendini feshetmiştir (kapatmıştır).</p>
                        </div>
                    </div>
                </section>

                <!-- KIRMIZI BÖLÜM -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-fire text-red-600 dark:text-red-300"></i></div>
                        Rejime Yönelik Tehditler ve İsyanlar
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-red-100 font-medium">
                        
                        <div class="bg-red-50/80 dark:bg-red-900/30 p-4 rounded-xl border border-red-100 dark:border-red-800/50">
                            <strong class="text-red-800 dark:text-red-300 block mb-1 text-lg">Şeyh Sait İsyanı (1925):</strong>
                            <p class="text-sm mb-2">Cumhuriyet rejimine (laikliğe) karşı çıkan <strong>ilk büyük isyandır</strong>. İngilizler Musul'u kaybetmemizi sağlamak için bu isyanı kışkırtmıştır.</p>
                            <p class="text-sm"><strong>Sonuçları:</strong> Ali Fethi Okyar istifa etmiş, sertlik yanlısı İsmet İnönü Hükümeti kurulmuştur. <strong>"Takrir-i Sükûn Kanunu"</strong> (1925-1929) çıkarılmış ve İstiklal Mahkemeleri görev yapmıştır.</p>
                        </div>

                        <div class="bg-red-50/80 dark:bg-red-900/30 p-4 rounded-xl border border-red-100 dark:border-red-800/50">
                            <strong class="text-red-800 dark:text-red-300 block mb-1 text-lg">İzmir Suikastı (1926):</strong>
                            <p class="text-sm">M. Kemal'e yönelik suikast girişimidir. İstiklal Mahkemelerinin görev yaptığı <strong>son olaydır</strong>. M. Kemal tarihi <em>"Benim naçiz vücudum elbet bir gün toprak olacaktır..."</em> sözünü burada söylemiştir.</p>
                        </div>

                        <div class="bg-white/60 dark:bg-slate-800/60 p-4 rounded-xl border border-red-200 dark:border-red-800/50 relative overflow-hidden">
                            <div class="absolute right-0 top-0 bg-red-500 text-white text-[10px] font-black px-2 py-1 rounded-bl-lg">ÇİFTE TUZAK</div>
                            <strong class="text-red-800 dark:text-red-300 block mb-1 text-lg">Menemen (Kubilay) Olayı (1930):</strong>
                            <p class="text-sm mb-3">Rejime yönelik ikinci büyük isyandır. Asteğmen Kubilay şehit edilmiştir.</p>
                            <ul class="text-sm space-y-2 border-t border-red-200 dark:border-red-800/50 pt-2">
                                <li><strong class="text-red-600 dark:text-red-400">TUZAK 1:</strong> Bu olay Serbest Cumhuriyet Fırkası kapatıldıktan <strong>SONRA</strong> çıkmıştır (Partinin kapatılma nedeni değildir).</li>
                                <li><strong class="text-red-600 dark:text-red-400">TUZAK 2:</strong> Menemen olayında isyancıları İstiklal Mahkemeleri DEĞİL, askerî mahkeme olan <strong>Divan-ı Harp</strong> yargılamıştır.</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-flag text-orange-600 dark:text-orange-300"></i></div>
                        Milliyetçilik Refleksli Diğer Olaylar
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-slate-800 dark:text-orange-100 font-medium">
                        
                        <div class="bg-orange-50/80 dark:bg-orange-900/30 p-4 rounded-xl border border-orange-100 dark:border-orange-800/50">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1 text-lg">Bursa Olayı:</strong>
                            <p class="text-sm">Ezanın Türkçe okunmasına gösterilen tepkidir. M. Kemal "Bu bir din meselesi değil, dil meselesidir" demiştir.</p>
                        </div>
                        
                        <div class="bg-orange-50/80 dark:bg-orange-900/30 p-4 rounded-xl border border-orange-100 dark:border-orange-800/50">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1 text-lg">Vagon-Li (Wagons-Lits) Olayı (1933):</strong>
                            <p class="text-sm">Fransız demiryolu şirketinde Türkçe konuşulmasının yasaklanması üzerine öğrencilerin çıkardığı milliyetçi olaydır.</p>
                        </div>
                        
                        <div class="bg-orange-50/80 dark:bg-orange-900/30 p-4 rounded-xl border border-orange-100 dark:border-orange-800/50">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1 text-lg">Bozkurt - Lotus Olayı (1926):</strong>
                            <p class="text-sm">Türk gemisi (Bozkurt) ile Fransız gemisinin (Lotus) Ege'de çarpışmasıdır. Türkiye'yi Lahey Adalet Divanında dönemin Adalet Bakanı Mahmut Esat (Bozkurt) başarıyla savunmuştur.</p>
                        </div>
                        
                        <div class="bg-orange-50/80 dark:bg-orange-900/30 p-4 rounded-xl border border-orange-100 dark:border-orange-800/50">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1 text-lg">Razgrad Olayı (1933):</strong>
                            <p class="text-sm">Bulgaristan'ın Razgrad şehrinde bulunan Türk mezarlıklarının Bulgarlar tarafından tahrip edilmesine karşı, İstanbul'daki Türk öğrencilerin Bulgar mezarlarına çelenk bırakarak verdiği "medeni ve milliyetçi" tepkidir.</p>
                        </div>
                    </div>
                </section>
            </div>
"""

create_unit_file(12, u12)
create_unit_file(13, u13)
create_unit_file(14, u14)
create_unit_file(15, u15)

update_existing_sidebars()

print("Units 12, 13, 14, 15 generated successfully.")
