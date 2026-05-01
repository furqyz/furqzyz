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
    ]
    
    upcoming = [
        "9. XIX. Yüzyılda Osmanlı Devleti (Dağılma Dönemi) (1792 - 1922)",
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
    
    content = re.sub(r'<nav class="space-y-1.5 max-h-\[60vh\] overflow-y-auto pr-1.5 custom-scrollbar">.*?</nav>', new_nav, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

update_file_sidebar('index.html', 1)
update_file_sidebar('unite2.html', 2)
update_file_sidebar('unite3.html', 3)
update_file_sidebar('unite4.html', 4)
update_file_sidebar('unite5.html', 5)
update_file_sidebar('unite6.html', 6)
update_file_sidebar('unite7.html', 7)

unite8_content = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-arrow-trend-down text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">
                        KPSS Tarih Hazırlık
                    </div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">8. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">XVIII. YÜZYILDA OSMANLI DEVLETİ (GERİLEME)</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Bu ünitede Osmanlı Devleti'nin Batı'nın üstünlüğünü kabul ederek Batı tarzı ıslahatlara başladığı, Karadeniz ve Kırım üzerindeki hakimiyetini kaybettiği dönem incelenmektedir.</p>
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
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Batı'nın (Avrupa'nın) üstünlüğünün ve askerî gücünün ilk defa kabul edildiği antlaşma <strong class="text-purple-700 dark:text-purple-400">1718 Pasarofça Antlaşması'dır</strong> (Bu antlaşma ile Lale Devri başlamıştır).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı'nın tarihinde ilk defa savaş tazminatı ödediği devlet <strong class="text-purple-700 dark:text-purple-400">Rusya'dır</strong> (1774 Küçük Kaynarca Antlaşması ile).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Halkı tamamen Türk ve Müslüman olan bir toprak parçası <strong class="text-purple-700 dark:text-purple-400">(Kırım)</strong> ilk defa kaybedilmiştir.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Halifelik makamı, uluslararası bir antlaşmada siyasi bir güç olarak ilk defa <strong class="text-purple-700 dark:text-purple-400">Küçük Kaynarca Antlaşması'nda</strong> (Kırım ile dini bağları korumak için) kullanılmıştır.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Batı tarzında ilk askerî ıslahatı yapan padişah <strong class="text-purple-700 dark:text-purple-400">I. Mahmut'tur</strong>. Batı tarzında açılan ilk teknik okul ise <strong class="text-purple-700 dark:text-purple-400">Hendesehane'dir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı donanması, İnebahtı'dan sonra tarihindeki ikinci büyük yıkımı 1770 yılındaki <strong class="text-purple-700 dark:text-purple-400">Çeşme Baskını</strong> ile yaşamış, Ruslar donanmamızı yakmıştır.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>İlk özel matbaa Lale Devri'nde (İbrahim Müteferrika önderliğinde) kurulmuştur. Matbaada basılan ilk eser Vani Mehmet Efendi'nin <strong class="text-purple-700 dark:text-purple-400">"Van Kulu Lügati"</strong> adlı sözlüğüdür. İlk devlet matbaası (Matbaa-i Amire) ise <strong class="text-purple-700 dark:text-purple-400">III. Selim</strong> döneminde kurulmuştur.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı Devleti'nin topraklarını korumak için ilk defa <strong class="text-purple-700 dark:text-purple-400">Denge Politikası</strong> uyguladığı olay, Napolyon komutasındaki Fransa'nın Mısır'ı işgalidir (Rusya ve İngiltere'den yardım alınmıştır).</span></li>
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
                        <div class="bg-yellow-50/50 dark:bg-yellow-900/20 p-4 rounded-2xl mb-4">
                            <strong class="text-yellow-800 dark:text-yellow-300 text-lg block mb-2"><i class="fas fa-key mr-2"></i>Padişahlar Şifresi: <span class="bg-yellow-200 dark:bg-yellow-800 px-2 py-0.5 rounded text-yellow-900 dark:text-yellow-100">3-1-3-1-3</span></strong>
                            <p class="text-sm">III. Ahmet, I. Mahmut, III. Mustafa, I. Abdülhamit, III. Selim</p>
                        </div>
                        
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">III. Ahmet:</strong> Lale Devri'nin padişahıdır. Dönemin sadrazamı Nevşehirli Damat İbrahim Paşa, ünlü minyatür ustası Levni, ünlü şairi ise Nedim'dir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">28 Mehmet Çelebi:</strong> Lale Devri'nde Paris'e gönderilen ilk geçici elçidir. Yazdığı "Paris Sefaretnamesi", Osmanlı'nın Batı'ya açılan ilk penceresi kabul edilir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Humbaracı Ahmet Paşa (Comte de Bonneval):</strong> I. Mahmut döneminde getirilip Humbaracı Ocağı'nı ıslah eden ve "Müslüman olup Ahmet adını alan" ilk Batılı askerî uzmandır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Baron de Tott:</strong> III. Mustafa döneminde Avrupa'dan getirilen, Sürat Topçuları ile Tersane Hendesehanesi'ni kuran uzmandır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">I. Abdülhamit:</strong> Ulufe alım satımını yasaklayan, cülus bahşişini kaldıran ve yabancı uzmanların Müslüman olma/Osmanlı kıyafeti giyme zorunluluğunu kaldıran padişahtır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">III. Selim:</strong> Dönemindeki tüm yeniliklere "Nizam-ı Cedit" (Yeni Düzen) adı verilen, planlı ve programlı (radikal) ıslahat yapan ilk padişahtır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Yusuf Agâh Efendi:</strong> III. Selim döneminde Londra'ya atanan ilk daimî (kalıcı) elçidir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Cezzar Ahmet Paşa:</strong> Napolyon'u Akka Kalesi önlerinde mağlup eden Nizam-ı Cedit ordusunun efsanevi komutanıdır.</li>
                    </ul>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-book-open text-cyan-600 dark:text-cyan-300"></i>
                        </div>
                        Kavramlar, Projeler ve İsyanlar
                    </h3>
                    <div class="space-y-6 text-slate-800 dark:text-cyan-100 font-medium">
                        
                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-2">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-3"><i class="fas fa-map mr-2"></i>Önemli Projeler ve Politikalar</p>
                            <div class="grid grid-cols-1 gap-2 text-sm">
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Makyavelizm:</strong> "Amaca ulaşmak için her türlü araca başvurmanın mubah sayılması"dır. (Avrupa'nın 18. yüzyıldaki temel dış politikasıdır).
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Dakya Projesi:</strong> Rusya ve Avusturya'nın Osmanlı'yı paylaşarak Balkanlarda ortaklaşa kurmayı planladıkları devletin adıdır.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Grek Projesi:</strong> Rus Prensi Potemkin'in, İstanbul merkezli yeni bir Bizans İmparatorluğu kurma projesidir.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Esham Sistemi:</strong> Devletin iç borçlanmaya gitmesidir (Kâğıt paraya geçişin ilk aşamasıdır). III. Mustafa getirmiş, I. Abdülhamit uygulamıştır.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">İrad-ı Cedit:</strong> III. Selim'in kurduğu Nizam-ı Cedit ordusunun masraflarını karşılamak için oluşturulan özel devlet hazinesidir.
                                </div>
                            </div>
                        </div>

                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-4">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-3"><i class="fas fa-fire mr-2"></i>Dönemi Kapatan İsyanlar</p>
                            <div class="flex flex-col gap-2 text-sm">
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Patrona Halil İsyanı (1730):</strong> Lale Devri'ni kesin olarak sona erdiren isyandır. (İsyancılar yeniliklere değil lükse karşı oldukları için matbaaya dokunmamışlardır).
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Kabakçı Mustafa İsyanı (1807):</strong> III. Selim'in tahttan indirilip Nizam-ı Cedit yeniliklerinin tamamen sona erdiği gerici isyandır.
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
                        Antlaşmalar ve Kırım'ın Kopuşu
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-emerald-100 font-medium">
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">Prut Antlaşması (1711):</strong></p>
                            <p class="text-sm">Azak Kalesi geri alınmış ve kaybedilen toprakları geri alma umudu doğmuştur.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">Pasarofça Antlaşması (1718):</strong></p>
                            <p class="text-sm">Belgrat kaybedilmiş, Batı'nın üstünlüğü resmen kabul edilip "Lale Devri" başlamıştır.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">Belgrat Antlaşması (1739):</strong></p>
                            <p class="text-sm">18. yüzyılda Osmanlı'nın imzaladığı son kazançlı antlaşmadır. Karadeniz'in Türk gölü olduğu son kez onaylanmıştır. Fransa arabuluculuk yaptığı için Fransa'ya verilen kapitülasyonlar 1740'ta sürekli (daimi) hâle getirilmiştir.</p>
                        </div>

                        <div class="border-l-4 border-emerald-500 pl-4 py-2 mt-6 bg-emerald-50/50 dark:bg-emerald-900/20 rounded-r-xl">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-2"><i class="fas fa-map-marked-alt mr-2"></i>KIRIM'IN KOPUŞ AŞAMALARI (ÇOK ÖNEMLİ):</strong>
                            <ul class="space-y-3 text-sm">
                                <li><strong class="text-emerald-700 dark:text-emerald-400">1. Küçük Kaynarca Antlaşması (1774):</strong> Kırım bağımsız olmuştur. (Ayrıca Rusya'ya kapitülasyonlar verilmiş, Ortodoksları himaye etme hakkı tanınmıştır).</li>
                                <li><strong class="text-emerald-700 dark:text-emerald-400">2. Aynalıkavak Tenkihnamesi (1779):</strong> Rusya yanlısı Şahin Giray'ın Kırım Hanı olması Osmanlı tarafından mecburen onaylanmıştır.</li>
                                <li><strong class="text-emerald-700 dark:text-emerald-400">3. Yaş Antlaşması (1792):</strong> Kırım'ın Rusya'ya ait olduğu kesin olarak kabul edilmiş ve Osmanlı'da Dağılma Dönemi başlamıştır.</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-hammer text-orange-600 dark:text-orange-300"></i>
                        </div>
                        XVIII. Yüzyıl Islahatlarının Özellikleri
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-orange-100 font-medium">
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Avrupa Örnek Alındı:</strong>
                            <p class="text-sm">Avrupa'nın (Batı'nın) üstünlüğü ilk defa kabul edilmiş ve kurumları örnek alınmıştır.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">En Çok Askerî Alanda:</strong>
                            <p class="text-sm">En çok Askerî alanda ıslahat yapılmıştır.</p>
                        </div>
                        <div class="bg-orange-50 dark:bg-orange-900/30 p-4 rounded-xl border border-orange-300 dark:border-orange-700/50">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1 flex items-center"><i class="fas fa-ban mr-2 text-red-500"></i>Hukuk Islahatı Yoktur!</strong>
                            <p class="text-sm">Hukuk alanında hiçbir ıslahat yapılmamıştır!</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Lale Devri Özellikleri:</strong>
                            <p class="text-sm">Lale Devri'nde matbaa, çiçek aşısı, itfaiye (Tulumbacılar), kâğıt-çuha fabrikaları, kütüphaneler ve Batı mimarisi (Barok-Rokoko) görülür; ancak Lale Devri'nde <strong class="text-orange-700 dark:text-orange-400">askerî ıslahat KESİNLİKLE YOKTUR.</strong></p>
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
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Çiçek Aşısı Tuzağı:</strong>
                            <p class="text-sm">Lale Devri'nde her ne kadar Batı (Avrupa) örnek alınsa da, bu dönemde uygulanan Çiçek Aşısı Batı'dan değil, Doğu'dan (İran'dan) getirilmiştir.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Okul Ayrımları Tuzağı:</strong>
                            <p class="text-sm">İsimleri birbirine çok benzeyen okullara dikkat edilmelidir. Mühendishane-i Bahr-i Hümayun (Deniz) <strong class="text-red-700 dark:text-red-400">I. Abdülhamit</strong> döneminde, Mühendishane-i Berr-i Hümayun (Kara) ise <strong class="text-red-700 dark:text-red-400">III. Selim</strong> döneminde açılmıştır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Matbaanın Gelişi:</strong>
                            <p class="text-sm">Lale Devri'nde matbaa getirildiğinde ulemanın tepkisinden çekinildiği için "dinî eserlerin basımı yasaklanmış", hattatların işsiz kalmaması için dinî eserlerin çoğaltılması hattatlara bırakılmıştır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Halifeliğin Kullanımı:</strong>
                            <p class="text-sm">Küçük Kaynarca Antlaşması'nda "Kırım dini açıdan Osmanlı halifesine bağlı kalacaktır" maddesinin temel amacı, halkı Müslüman olan Kırım ile kültürel ve manevi bağları koparmamaktır.</p>
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
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2015-18 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Batı'nın üstünlüğünün kabul edilerek Lale Devri'nin başlaması hangi antlaşma iledir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: 1718 Pasarofça Antlaşması</strong></p>
                        </div>
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2016 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Rusya'ya kapitülasyonların verilmesi, konsolosluk açma hakkı ve Kırım'ın bağımsız olması hangi antlaşmadır?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Küçük Kaynarca Antlaşması</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">"Avrupa tarzında ilk eğitim kurumları (Hendesehane) Lale Devri'nde açıldı." yargısı neden yanlıştır?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Lale Devri'nde askerî ıslahat yoktur. Hendesehane I. Mahmut dönemindedir.</strong></p>
                        </div>

                        <div class="bg-red-50 hover:bg-red-100 dark:bg-red-900/30 dark:hover:bg-red-900/50 transition-colors p-5 rounded-2xl border border-red-200 dark:border-red-800/50 backdrop-blur-sm relative lg:col-span-3">
                            <div class="absolute -top-3 -left-3 bg-red-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md flex items-center"><i class="fas fa-exclamation-circle mr-1"></i> DİKKAT: ISLAHAT ALANI TUZAĞI</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-red-200">"18. yüzyılda idari, mali, askerî ve teknik alanlarda ıslahat yapılmıştır." Ancak şıklara konulan <strong class="text-red-700 dark:text-red-400">"Hukuk alanında ıslahat yapılmıştır" ifadesi KESİNLİKLE YANLIŞTIR.</strong> Osmanlı'da hukuk ıslahatları (Mecelle vb.) 19. yüzyılda başlayacaktır.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- DÖNEM PADİŞAHLARI KRONOLOJİSİ -->
            <section class="bg-white dark:bg-slate-800 p-8 md:p-12 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 mt-12 overflow-hidden">
                <h3 class="text-3xl font-black mb-8 flex items-center text-slate-900 dark:text-white">
                    <div class="bg-slate-100 dark:bg-slate-700 p-3 rounded-2xl mr-4 text-slate-600 dark:text-slate-300">
                        <i class="fas fa-hourglass-half"></i>
                    </div>
                    GERİLEME DÖNEMİ PADİŞAHLARI (3-1-3-1-3 Şifresi)
                </h3>
                
                <div class="relative">
                    <div class="flex flex-wrap items-center gap-4 text-sm font-medium">
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">1</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">III. Ahmet</span>
                        </div>
                        <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">2</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">I. Mahmut</span>
                        </div>
                        <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">3</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">III. Mustafa</span>
                        </div>
                        <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">4</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">I. Abdülhamit</span>
                        </div>
                        <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">5</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">III. Selim</span>
                        </div>
                    </div>
                </div>
            </section>
"""

with open('unite7.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace main content for unite8
template = re.sub(r'<main class="flex-1 space-y-8 lg:space-y-12">.*?</main>', f'<main class="flex-1 space-y-8 lg:space-y-12">{unite8_content}\n        </main>', template, flags=re.DOTALL)

with open('unite8.html', 'w', encoding='utf-8') as f:
    f.write(template)
    
update_file_sidebar('unite8.html', 8)
