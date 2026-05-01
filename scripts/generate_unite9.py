import re

def generate_sidebar(active_index):
    items = [
        {"title": "1. İslamiyet Öncesi Türk Tarihi", "file": "index.html", "icon": "fa-landmark"},
        {"title": "2. İlk Türk İslam Devletleri", "file": "unite2.html", "icon": "fa-mosque"},
        {"title": "3. Anadolu (Türkiye) Selçuklu Devleti", "file": "unite3.html", "icon": "fa-chess-knight"},
        {"title": "4. Osmanlı Devleti Kültür ve Medeniyeti", "file": "unite4.html", "icon": "fa-landmark-dome"},
        {"title": "5. Osmanlı Devleti Kuruluş Dönemi (1299 - 1453)", "file": "unite5.html", "icon": "fa-campground"},
        {"title": "6. Osmanlı Devleti Yükselme Dönemi (1453 - 1595)", "file": "unite6.html", "icon": "fa-chess-rook"},
        {"title": "7. XVII. Yüzyılda Osmanlı Devleti (Duraklama Dönemi) (1595 - 1699)", "file": "unite7.html", "icon": "fa-hourglass-end"},
        {"title": "8. XVIII. Yüzyılda Osmanlı Devleti (Gerileme Dönemi) (1699 - 1792)", "file": "unite8.html", "icon": "fa-arrow-trend-down"},
        {"title": "9. XIX. Yüzyılda Osmanlı Devleti (Dağılma Dönemi) (1792 - 1922)", "file": "unite9.html", "icon": "fa-unlink"},
    ]
    
    upcoming = [
        "10. XX. Yüzyıl Başlarında Osmanlı Devleti",
        "11. Mondros Ateşkes Antlaşması ve İlk İşgaller",
        "12. Millî Mücadele Hazırlık Dönemi",
        "13. I. TBMM Dönemi ve Gelişmeleri (1920 - 1923)",
        "14. Millî Mücadele Muharebeler Dönemi",
        "15. Atatürk'ün Hayatı",
        "16. Atatürk Dönemi İç Politika",
        "17. Atatürk İlkeleri",
        "18. Atatürk İnkılapları",
        "19. Atatürk Dönemi Türk Dış Politikası",
        "20. Cumhuriyet Dönemi Kültür ve Medeniyeti",
        "21. XX. Yüzyıl Başlarında Dünya (1918 - 1939)",
        "22. II. Dünya Savaşı (1939 - 1945)",
        "23. Soğuk Savaş Dönemi (1947 - 1990)",
        "24. Yumuşama Dönemi (1961 - 1990)",
        "25. Küreselleşen Dünya (1990 - 2026)",
    ]

    nav_html = '<nav class="space-y-1.5 max-h-[85vh] overflow-y-auto pr-1.5 custom-scrollbar">\n'
    
    for i, item in enumerate(items):
        if i + 1 == active_index:
            nav_html += f'''                        <a href="{item['file']}" class="flex items-center justify-between bg-gradient-to-r from-indigo-600 to-indigo-500 text-white px-3 py-3 rounded-xl font-semibold shadow-md shadow-indigo-200 dark:shadow-none transition-transform hover:scale-[1.02] mb-2 mt-2">
                            <div class="flex items-start space-x-3">
                                <i class="fas {item['icon']} w-4 text-center mt-0.5"></i>
                                <span class="text-[13px] leading-snug">{item['title']}</span>
                            </div>
                            <i class="fas fa-chevron-right text-[10px] opacity-70 shrink-0 ml-2 mt-1"></i>
                        </a>\n'''
        else:
            nav_html += f'''                        <a href="{item['file']}" class="flex items-center justify-between text-slate-500 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-700/50 px-3 py-2.5 rounded-xl transition-all group">
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

def update_file_sidebar(filename, active_index):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_nav = generate_sidebar(active_index)
    
    content = re.sub(r'<nav class="space-y-1.5 max-h-\[85vh\] overflow-y-auto pr-1.5 custom-scrollbar">.*?</nav>', new_nav, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

files_to_update = ['index.html', 'unite2.html', 'unite3.html', 'unite4.html', 'unite5.html', 'unite6.html', 'unite7.html', 'unite8.html']
for idx, f in enumerate(files_to_update):
    update_file_sidebar(f, idx + 1)

unite9_content = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-unlink text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">
                        KPSS Tarih Hazırlık
                    </div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">9. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">XIX. YÜZYILDA OSMANLI DEVLETİ (DAĞILMA)</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Bu ünitede Osmanlı Devleti'nin en uzun yüzyılında milliyetçilik isyanları, dağılmayı önlemek için atılan demokratik adımlar ve Avrupa devletlerinin müdahaleleri incelenmektedir.</p>
                </div>
            </header>

            <!-- KARTLAR MASONRY DÜZENİ -->
            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                
                <!-- MOR BÖLÜM -->
                <section class="category-purple note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-star text-purple-600 dark:text-purple-300"></i>
                        </div>
                        İlkler, Sonlar ve Kesin Yargılar
                    </h3>
                    <ul class="space-y-4 text-slate-800 dark:text-purple-100 font-medium">
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı'da milliyetçilik akımıyla ilk isyan eden azınlık <strong class="text-purple-700 dark:text-purple-400">Sırplar</strong> (1812 Bükreş Antlaşması ile ilk ayrıcalığı aldılar), ilk bağımsız olan azınlık ise <strong class="text-purple-700 dark:text-purple-400">Yunanlar'dır</strong> (1829 Edirne Antlaşması).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı padişahının yetkilerini kısıtlayan ve demokratikleşmenin ilk adımı sayılan belge <strong class="text-purple-700 dark:text-purple-400">Sened-i İttifak'tır</strong> (Avrupa etkisi YOKTUR).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Kanun gücünün her gücün üstünde olduğu ilk kez <strong class="text-purple-700 dark:text-purple-400">Tanzimat Fermanı (1839)</strong> ile kabul edilmiştir.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Halkın yönetime ilk kez katıldığı, parlamento (meclis) döneminin başladığı ve ilk yazılı anayasanın (Kanunuesasi) ilan edildiği olay <strong class="text-purple-700 dark:text-purple-400">I. Meşrutiyet'tir (1876)</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı Devleti ilk dış borcunu <strong class="text-purple-700 dark:text-purple-400">Kırım Savaşı</strong> sırasında <strong class="text-purple-700 dark:text-purple-400">İngiltere'den</strong> almıştır (Abdülmecit dönemi).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Toprak bütünlüğünün Avrupa garantisi altına alındığı (kendini koruyamayacağının belgelendiği) ilk antlaşma <strong class="text-purple-700 dark:text-purple-400">1856 Paris Antlaşması'dır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Boğazlar üzerindeki egemenlik haklarını son kez tek başına <strong class="text-purple-700 dark:text-purple-400">Hünkâr İskelesi Antlaşması'nda</strong> kullanmıştır.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>İlk resmî gazete <strong class="text-purple-700 dark:text-purple-400">Takvim-i Vekayi</strong> (II. Mahmut dönemi), ilk özel gazete ise Şinasi ve Agah Efendi'nin çıkardığı <strong class="text-purple-700 dark:text-purple-400">Tercüman-ı Ahval'dir</strong> (Abdülmecit dönemi).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Rejimi değiştirmeye yönelik çıkan ilk ve tek isyan <strong class="text-purple-700 dark:text-purple-400">31 Mart Vakası'dır (1909)</strong>.</span></li>
                    </ul>
                </section>

                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-crown text-yellow-600 dark:text-yellow-300"></i>
                        </div>
                        Önemli Padişahlar ve Şahsiyetler
                    </h3>
                    <ul class="space-y-4 text-slate-800 dark:text-yellow-100 font-medium">
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">II. Mahmut (Adli):</strong> Sened-i İttifak'ı imzalayan, Yeniçeri Ocağı'nı kaldıran (Vaka-i Hayriye), Divan-ı Hümayun'u kaldırıp Nazırlıkları (Bakanlıkları) kuran, "Ben tebaamın Müslümanını camide, Hristiyanını kilisede görmek isterim" diyerek eşitliği (Osmanlıcılık) savunan ıslahatçı padişahtır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Sultan Abdülmecit:</strong> Tanzimat ve Islahat Fermanlarını ilan eden, ilk kâğıt parayı (Kaime) bastıran, Bank-ı Dersaadet'i ve kitap tercümeleri için Encümen-i Daniş'i (Bilim Kurulu) kuran padişahtır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Sultan Abdülaziz:</strong> Avrupa'ya sadece seyahat amacıyla çıkan ilk ve tek padişahtır. Darüşşafaka'yı açmış, Mecelle'yi yürürlüğe sokmuştur.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Ahmet Cevdet Paşa:</strong> Osmanlı'nın medeni kanunu olan Mecelle'yi hazırlayan ünlü hukukçu ve devlet adamıdır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">II. Abdülhamit (Maarifperver):</strong> En çok okul açan padişahtır. I. ve II. Meşrutiyet'i ilan etmiştir. İslamcılık (Ümmetçilik) politikasını devletin ana politikası yapmıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Gazi Osman Paşa ve Nene Hatun:</strong> 93 Harbi'nde (1877-1878) Plevne'de (Gazi Osman Paşa) ve Erzurum Aziziye Tabyalarında (Nene Hatun) destan yazan kahramanlardır.</li>
                    </ul>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-book-open text-cyan-600 dark:text-cyan-300"></i>
                        </div>
                        Kavramlar, Vakalar ve Savaşlar
                    </h3>
                    <div class="space-y-6 text-slate-800 dark:text-cyan-100 font-medium">
                        
                        <div class="bg-cyan-50/50 dark:bg-cyan-900/20 p-4 rounded-2xl">
                            <strong class="text-cyan-800 dark:text-cyan-300 text-lg block mb-2"><i class="fas fa-fire mr-2"></i>Donanma Yangınları Şifresi: <span class="bg-cyan-200 dark:bg-cyan-800 px-2 py-0.5 rounded text-cyan-900 dark:text-cyan-100">İÇNİS</span></strong>
                            <p class="text-sm">Osmanlı donanması sırasıyla; <strong>İ</strong>nebahtı (Haçlılar), <strong>Ç</strong>eşme (Ruslar), <strong>N</strong>avarin (İngiliz-Fransız-Rus), <strong>S</strong>inop (Ruslar) baskınlarıyla yakılmıştır.</p>
                        </div>
                        
                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-2">
                            <div class="grid grid-cols-1 gap-2 text-sm">
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Vaka-i Hayriye (1826):</strong> Yeniçeri Ocağı'nın kaldırılması olayıdır. Yerine Asakir-i Mansure-i Muhammediye ordusu kurulmuştur.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Kuleli Vakası (1859) ve Çırağan Vakası (1878):</strong> Kuleli Vakası, Sultan Abdülmecit'i devirme girişimidir. Çırağan Vakası ise Ali Suavi'nin II. Abdülhamit'i indirip V. Murat'ı tekrar tahta geçirme girişimidir.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Kırım Savaşı (1853-1856):</strong> Rusya'nın "Hasta Adam" dediği Osmanlı'yı parçalamak, Kutsal Yerler Sorunu'nu bahane ederek açtığı savaştır. (Florance Nightingale bu savaşta görev almıştır).
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">93 Harbi (1877-1878):</strong> Rusların hem Kafkaslardan hem Balkanlardan saldırdığı ağır savaştır.
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- YEŞİL BÖLÜM -->
                <section class="category-green note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-emerald-900 dark:text-emerald-200">
                        <div class="bg-emerald-100 dark:bg-emerald-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-handshake text-emerald-600 dark:text-emerald-300"></i>
                        </div>
                        Sınavların Vazgeçilmezi Antlaşmalar
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-emerald-100 font-medium">
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">1829 Edirne Antlaşması:</strong></p>
                            <p class="text-sm">Yunanistan bağımsız olmuştur.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">1833 Kütahya Antlaşması:</strong></p>
                            <p class="text-sm">Kendi valimiz olan Kavalalı Mehmet Ali Paşa'nın isyanı sonucu İngiltere/Fransa baskısıyla imzalanan içler acısı antlaşmadır.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">1833 Hünkâr İskelesi Antlaşması:</strong></p>
                            <p class="text-sm">Mısır isyanında Rusya'dan yardım istenmesiyle imzalanmıştır. Boğazlar sorunu ilk kez bu antlaşmayla ortaya çıkmıştır.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">1838 Balta Limanı Ticaret Antlaşması:</strong></p>
                            <p class="text-sm">İngiltere ile imzalanmıştır. Gümrük vergileri sıfırlanmış, Osmanlı ekonomisi Avrupa'nın açık pazarı hâline gelmiştir.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">1841 Londra Boğazlar Sözleşmesi:</strong></p>
                            <p class="text-sm">Boğazlar ilk kez uluslararası bir statü kazanmıştır.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">Ayastefanos (Yeşilköy) Antlaşması (1878):</strong></p>
                            <p class="text-sm">93 Harbi sonunda Rusya ile imzalanan ancak Avrupalı devletlerin çıkarlarına ters düştüğü için yürürlüğe girmeyen (ölü doğan) antlaşmadır. (Yerine Berlin Antlaşması yapılmıştır).</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">1878 Berlin Antlaşması:</strong></p>
                            <p class="text-sm">Sırbistan, Karadağ ve Romanya bağımsız olmuştur. Ermeni Sorunu uluslararası alanda ilk kez bu antlaşmayla ortaya çıkmıştır.</p>
                        </div>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-hammer text-orange-600 dark:text-orange-300"></i>
                        </div>
                        II. Mahmut Dönemi Kritik Islahatları
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-orange-100 font-medium">
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Müsaderenin Kaldırılması:</strong>
                            <p class="text-sm">Devletin memur mallarına el koyma usulü kaldırılarak özel mülkiyet güvence altına alınmıştır.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">İlk Nüfus Sayımı:</strong>
                            <p class="text-sm">Sadece erkekler ve hayvanlar sayılmıştır. Amacı vergi verecekleri ve askere gidecekleri tespit etmektir.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Mürur Tezkeresi:</strong>
                            <p class="text-sm">İstanbul'a giriş çıkışları kontrol altına almak için uygulanan "iç vize" (pasaport) sistemidir.</p>
                        </div>
                    </div>
                </section>

                <!-- KIRMIZI BÖLÜM -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-exclamation-triangle text-red-600 dark:text-red-300"></i>
                        </div>
                        Kritik Uyarılar ve Analizler
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-red-100 font-medium">
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Baskı Unsuru Tuzağı:</strong>
                            <p class="text-sm">Sened-i İttifak ve Tanzimat Fermanı'nda "Avrupa devletlerinin baskısı" YOKTUR. Ancak Islahat Fermanı, I. ve II. Meşrutiyet'te Avrupa baskısı/etkisi VARDIR.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Tanzimat Dönemi Padişahları Tuzağı:</strong>
                            <p class="text-sm">Tanzimat Dönemi padişahları Abdülmecit, Abdülaziz ve V. Murat'tır. ÖSYM şıklara sürekli II. Mahmut'u koyar. <strong class="text-red-700 dark:text-red-400">II. Mahmut Tanzimat dönemi padişahı değildir</strong>, hazırlayıcısıdır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Islahat Fermanı'nın Kapsamı:</strong>
                            <p class="text-sm">Bu fermanla <strong class="text-red-700 dark:text-red-400">sadece gayrimüslimlere (azınlıklara)</strong> geniş haklar (memur olma, şirket/banka kurma, il genel meclisine girme, bedelli askerlik vb.) verilmiştir. Müslümanlar buna tepki göstermiştir.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Düyun-u Umumiye (1881):</strong>
                            <p class="text-sm">Devletin dış borçlarını ödeyememesi (Muharrem Kararnamesi ile iflas) üzerine kurulan komisyondur. Devletin ekonomik bağımsızlığı yok olmuştur.</p>
                        </div>
                    </div>
                </section>
            </div>
            
            <!-- SINAV HAFIZASI BÖLÜMÜ -->
            <section class="exam-memory note-card p-8 md:p-12 rounded-3xl shadow-2xl shadow-indigo-500/20 relative overflow-hidden group mt-12">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16 transition-transform group-hover:scale-150 duration-700"></div>
                <div class="absolute right-8 top-1/2 -translate-y-1/2 opacity-10 transform group-hover:rotate-12 transition-transform duration-700 pointer-events-none">
                    <i class="fas fa-brain text-[12rem] text-indigo-900"></i>
                </div>
                
                <div class="relative z-10">
                    <h3 class="text-3xl font-black mb-8 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-600 dark:text-indigo-400"></i> SINAV HAFIZASI VE DİKKAT ANALİZİ
                    </h3>
                    <p class="text-sm text-slate-500 dark:text-slate-400 mb-6 uppercase tracking-widest font-bold">Çıkmış Bilgi Soruları</p>
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2016-20-24 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Tekel usulünün kalkması ve gümrüklerin düşürülmesiyle "Osmanlı'nın Avrupa'nın açık pazarı hâline geldiği" antlaşma hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: 1838 Balta Limanı Ticaret Antlaşması</strong></p>
                        </div>
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2021-23 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Islahat Fermanı ile gayrimüslimlere verilmeyen hak nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Siyasi parti kurma hakkı (II. Meşrutiyet'te verilmiştir)</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 KPSS İptal</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Tanzimat Fermanı'nın amaçları arasında olmayan ve mülkiyeti güvence altına alan gelişme nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Müsadere usulüne son verilmesi (II. Mahmut)</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2019 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Aşağıdakilerden hangisi 19. yüzyılda (Dağılma) açılan okullardandır?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Mekteb-i Harbiye (Hendesehane 18. yüzyıldır)</strong></p>
                        </div>

                        <div class="bg-red-50 hover:bg-red-100 dark:bg-red-900/30 dark:hover:bg-red-900/50 transition-colors p-5 rounded-2xl border border-red-200 dark:border-red-800/50 backdrop-blur-sm relative lg:col-span-2">
                            <div class="absolute -top-3 -left-3 bg-red-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md flex items-center"><i class="fas fa-exclamation-circle mr-1"></i> DİKKAT: YÖNETİM ŞEKLİ TUZAĞI (2020 KPSS)</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-red-200">II. Mahmut dönemindeki ıslahatlar sayılırken şıklara "Devletin rejiminin (yönetim şeklinin) değiştiği" konur. Bu <strong class="text-red-700 dark:text-red-400">KESİNLİKLE yanlıştır</strong>. Rejim ilk kez 1876'da I. Meşrutiyet ile değişmiştir.</p>
                        </div>
                    </div>
                </div>
            </section>
"""

with open('unite8.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace main content for unite9
template = re.sub(r'<main class="flex-1 space-y-8 lg:space-y-12">.*?</main>', f'<main class="flex-1 space-y-8 lg:space-y-12">{unite9_content}\n        </main>', template, flags=re.DOTALL)

with open('unite9.html', 'w', encoding='utf-8') as f:
    f.write(template)
    
update_file_sidebar('unite9.html', 9)
