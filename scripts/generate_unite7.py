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
    ]
    
    upcoming = [
        "8. XVIII. Yüzyılda Osmanlı Devleti (Gerileme Dönemi) (1699 - 1792)",
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

unite7_content = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-hourglass-end text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">
                        KPSS Tarih Hazırlık
                    </div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">7. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">XVII. YÜZYILDA OSMANLI DEVLETİ (DURAKLAMA)</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Bu ünitede Osmanlı Devleti'nin 17. yüzyılda karşılaştığı iç isyanlar, yapılan ilk radikal ıslahat denemeleri ve Batı'da toprak kayıplarının başladığı süreç incelenmektedir.</p>
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
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı Devleti ile Rusya arasında imzalanan ilk resmî antlaşma <strong class="text-purple-700 dark:text-purple-400">Bahçesaray (Çehrin) Antlaşması'dır</strong> (1681).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı Devleti'nde ilk radikal ıslahat yapan padişah <strong class="text-purple-700 dark:text-purple-400">Genç Osman'dır</strong> (II. Osman).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı Devleti'nin Batı'da en geniş sınırlara ulaştığı antlaşma <strong class="text-purple-700 dark:text-purple-400">Bucaş Antlaşması</strong> (1672), Doğu'da en geniş sınırlara ulaştığı antlaşma ise <strong class="text-purple-700 dark:text-purple-400">Ferhat Paşa Antlaşması</strong> (1590)'dır.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı'nın Batı'da ilk kez büyük çapta toprak kaybettiği antlaşma <strong class="text-purple-700 dark:text-purple-400">Karlofça Antlaşması</strong> (1699)'dır. (Bu antlaşma ile Duraklama Dönemi bitmiş, Gerileme Dönemi başlamıştır).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı tarihinde ilk defa modern ve denk bütçeyi hazırlayan kişi <strong class="text-purple-700 dark:text-purple-400">Tarhuncu Ahmet Paşa'dır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Harem dışından evlilik yaparak sarayı halka açan (sosyal alanda ilk ıslahatı yapan) ve Yeniçeri Ocağı'nı kaldırmayı düşünen ilk padişah <strong class="text-purple-700 dark:text-purple-400">Genç Osman'dır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Sancağa çıkma uygulamasını kaldıran padişah <strong class="text-purple-700 dark:text-purple-400">III. Mehmet'tir</strong>. Sancakta yetişerek tahta çıkan son padişah III. Mehmet, sancağa çıkmadan (Kafes Usulü ile) tahta çıkan ilk padişah <strong class="text-purple-700 dark:text-purple-400">I. Ahmet'tir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı'da kendi isteğiyle veya fetvayla değil, bir isyan (Yeniçeri) sonucu öldürülen ilk padişah <strong class="text-purple-700 dark:text-purple-400">Genç Osman'dır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Devlet tarihinde ilk defa bir Şeyhülislam'ı idam ettiren padişah <strong class="text-purple-700 dark:text-purple-400">IV. Murat'tır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>En küçük yaşta tahta çıkan padişah <strong class="text-purple-700 dark:text-purple-400">IV. Mehmet'tir</strong> (6 yaşında).</span></li>
                    </ul>
                </section>

                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-tools text-yellow-600 dark:text-yellow-300"></i>
                        </div>
                        Önemli Padişahlar ve Islahatçılar
                    </h3>
                    <ul class="space-y-4 text-slate-800 dark:text-yellow-100 font-medium">
                        <div class="bg-yellow-50/50 dark:bg-yellow-900/20 p-4 rounded-2xl mb-4">
                            <strong class="text-yellow-800 dark:text-yellow-300 text-lg block mb-2"><i class="fas fa-key mr-2"></i>Islahatçıların Şifresi: <span class="bg-yellow-200 dark:bg-yellow-800 px-2 py-0.5 rounded text-yellow-900 dark:text-yellow-100">TOKMAK</span></strong>
                            <p class="text-sm">Tarhuncu Ahmet Paşa, Osman (Genç), Kuyucu Murat Paşa, Murat (IV.), Ahmet (I.), Köprülüler.</p>
                        </div>
                        
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">III. Mehmet ve Tiryaki Hasan Paşa:</strong> 1596 Haçova Savaşı'nın kazanılmasıyla III. Mehmet "Eğri Fatihi", Tiryaki Hasan Paşa ise "Kanije Fatihi" unvanını almıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Genç Osman (II. Osman):</strong> Hotin Seferi sırasında askerlerin isteksizliğini görüp ocağı kaldırmak istemiş, niyeti anlaşılınca Yedikule Zindanlarında boğularak şehit edilmiştir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">IV. Murat (Bağdat Fatihi):</strong> "Irakeyn Seferi" ile Bağdat'ı almış, Koçi Bey ve Kâtip Çelebi'den devletin sorunlarıyla ilgili raporlar (risaleler) hazırlamalarını istemiştir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">I. Ahmet:</strong> Hanedanın en büyük ve akıllı üyesinin tahta geçmesini öngören "Ekber ve Erşed" sistemini getirerek kardeş katlini önlemeye çalışmıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Köprülü Mehmet Paşa:</strong> Can güvenliğini sağlamak için saraya "şartlar ileri sürerek" sadrazam olan ilk devlet adamıdır.</li>
                    </ul>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-fire text-cyan-600 dark:text-cyan-300"></i>
                        </div>
                        Kavramlar, İsyanlar ve Olaylar
                    </h3>
                    <div class="space-y-6 text-slate-800 dark:text-cyan-100 font-medium">
                        
                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-2">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-3"><i class="fas fa-exclamation-triangle mr-2"></i>XVII. Yüzyıl İsyanları</p>
                            <div class="grid grid-cols-1 gap-2 text-sm">
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">1. İstanbul (Merkez/Yeniçeri) İsyanları:</strong> "Ocak, devlet içindir" anlayışı yerine "Devlet, ocak içindir" anlayışı yerleşmiştir.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">2. Celâlî (Anadolu) İsyanları:</strong> Tımar sisteminin bozulması ve rüşvet nedeniyle halkın çıkardığı isyanlardır. Haçova Meydan Muharebesi'nden kaçan askerlerin Anadolu'ya dağılması bu isyanları kışkırtmıştır. Bu isyanların rejimle (padişahı indirmekle) hiçbir ilgisi yoktur.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">3. Suhte (Talebe) Ayaklanmaları:</strong> Medrese öğrencilerinin ve beşik ulemalığı yüzünden işsiz kalan ulemanın isyanlarıdır.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">4. Eyalet İsyanları:</strong> Eflak, Boğdan, Yemen gibi eyaletlerde çıkmıştır. Ancak Fransız İhtilali henüz yaşanmadığı için bu isyanlarda kesinlikle milliyetçilik (ulusçuluk) etkisi yoktur.
                                </div>
                            </div>
                        </div>

                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-4">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-3"><i class="fas fa-book-open mr-2"></i>Önemli Kavramlar</p>
                            <div class="flex flex-col gap-2 text-sm">
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Büyük Kaçgun:</strong> Celâlî isyanları ve devletin baskısı nedeniyle köylünün toprağını terk edip şehirlere göç etmesidir.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Vaka-i Vakvakiye (Çınar Vakası):</strong> IV. Mehmet döneminde yeniçerilerin isyan ederek 30'a yakın devlet adamını Sultanahmet'teki çınar ağaçlarına asarak idam ettikleri olaydır.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Kutsal İttifak (VARİL):</strong> II. Viyana Kuşatması'nın başarısız olmasını fırsat bilip Osmanlı'ya saldıran Haçlı devletleridir (Venedik, Avusturya, Rusya, İtalya/Malta, Lehistan).
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
                        Antlaşmalar
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-emerald-100 font-medium">
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">Zitvatorok Antlaşması (1606):</strong></p>
                            <p class="text-sm">Avusturya Arşidükü protokolde yeniden Osmanlı Padişahı'na denk sayılmıştır. Bu, Osmanlı'nın 1533 İstanbul Antlaşması ile kazandığı siyasi üstünlüğünü kaybettiğinin net belgesidir.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">Kasr-ı Şirin Antlaşması (1639):</strong></p>
                            <p class="text-sm">İran ile yapılmış olup, günümüz Türkiye - İran sınırını büyük ölçüde belirleyen antlaşmadır.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">Vasvar Antlaşması (1664):</strong></p>
                            <p class="text-sm">Avusturya'ya karşı kazanılan Uyvar Kalesi'nin fethedilmesiyle imzalanmıştır. Avrupa'da "Uyvar önünde bir Türk gibi güçlü" deyimi ortaya çıkmıştır.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">Karlofça Antlaşması (1699):</strong></p>
                            <p class="text-sm">Osmanlı'nın Batı'da ilk kez büyük çapta toprak kaybettiği antlaşmadır. Garantör devlet Avusturya olmuştur.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">İstanbul Antlaşması (1700):</strong></p>
                            <p class="text-sm">Rusya ile imzalanmıştır. Azak Kalesi Ruslara verilmiştir, böylece Rusya Karadeniz'e inmek için ilk fırsatı yakalamıştır.</p>
                        </div>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-wrench text-orange-600 dark:text-orange-300"></i>
                        </div>
                        XVII. Yüzyıl Islahatlarının Özellikleri
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-orange-100 font-medium">
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Avrupa Örnek Alınmamıştır:</strong>
                            <p class="text-sm">Avrupa (Batı) örnek ALINMAMIŞTIR. Kök sorunlara inilememiş, sorunlar baskı ve şiddet yoluyla çözülmeye çalışılmıştır.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Sürekli Olmamıştır:</strong>
                            <p class="text-sm">Islahatlar yapan kişilerin ömrüyle sınırlı kalmıştır (devlet politikası hâline gelememiştir).</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Geriye Dönüş Hedeflenmiştir:</strong>
                            <p class="text-sm">Fatih ve Kanuni (Kanun-i Kadim) dönemlerine geri dönülmek hedeflenmiştir.</p>
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
                            <strong class="text-red-800 dark:text-red-300 block mb-1">IV. Murat'ın Yasakları:</strong>
                            <p class="text-sm">Gece sokağa çıkma, içki, tütün ve kahvehane yasaklarının temel sebebi İstanbul'da çıkan büyük yangınları engellemek ve asayişi sağlamaktır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Girit'in Fethi:</strong>
                            <p class="text-sm">Venedik'in elindeki Girit Adası tam 24 yıl süren bir kuşatma sonucunda alınabilmiştir. Bu, Osmanlı donanmasının ne kadar zayıfladığının kanıtıdır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Celâlî İsyanlarının Sonuçları:</strong>
                            <p class="text-sm">ÖSYM çok sorar; Celâlî isyanları ekonomik ve sosyal temellidir. Milliyetçilik akımının (Fransız İhtilali) bu isyanlarda hiçbir etkisi yoktur.</p>
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
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2016 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Padişahın Hotin Seferi sırasında edindiği olumsuz izlenimler üzerine merkez ordusunu ıslah etmeyi düşünen kişi kimdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Genç Osman (II. Osman)</strong></p>
                        </div>
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2017 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Tımarın bozulmasıyla asayiş sarsılmış, üretim düşmüştür. Ancak şıklardaki yanlış ifade nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: "Yeniçeri sayısının azalması" yanlıştır! (Yeniçeri sayısı artmıştır)</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2018 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Celali isyanları sonucu köylerin boşalmasına ne denir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Büyük Kaçgun (Şenlendirme çeldiricidir)</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">17. yüzyıl sorunları için verilen yanlış bilgi hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Salyanesiz eyalet sayısının artması</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2023 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Avusturya arşidükünün tekrar Padişaha eşit sayılması hangi antlaşma ile olmuştur?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Zitvatorok Antlaşması</strong></p>
                        </div>

                        <div class="bg-red-50 hover:bg-red-100 dark:bg-red-900/30 dark:hover:bg-red-900/50 transition-colors p-5 rounded-2xl border border-red-200 dark:border-red-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-red-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md flex items-center"><i class="fas fa-exclamation-circle mr-1"></i> DİKKAT: KAVRAM TUZAĞI</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-red-200">17. yüzyıl ıslahatlarında Avrupa örnek alınmamıştır. Eğer soruda "Batı tarzı ıslahat yapıldığı" söylenirse o şık 17. yüzyıl için <strong class="text-red-700 dark:text-red-400">KESİNLİKLE yanlıştır</strong>, bu durum 18. yüzyılda başlayacaktır.</p>
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
                    DURAKLAMA DÖNEMİ PADİŞAHLARI
                </h3>
                
                <div class="relative">
                    <div class="flex flex-wrap items-center gap-4 text-sm font-medium">
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">1</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">III. Mehmet</span>
                        </div>
                        <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">2</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">I. Ahmet</span>
                        </div>
                        <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">3</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">I. Mustafa</span>
                        </div>
                        <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">4</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">II. Osman (Genç)</span>
                        </div>
                        <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">5</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">IV. Murat</span>
                        </div>
                        <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">6</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">Sultan İbrahim</span>
                        </div>
                        <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">7</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">IV. Mehmet</span>
                        </div>
                        <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">8</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">II. Süleyman</span>
                        </div>
                        <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">9</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">II. Ahmet</span>
                        </div>
                        <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                        <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">10</div>
                            <span class="text-slate-700 dark:text-slate-300 font-semibold">II. Mustafa</span>
                        </div>
                    </div>
                </div>
            </section>
"""

with open('unite6.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace main content for unite7
template = re.sub(r'<main class="flex-1 space-y-8 lg:space-y-12">.*?</main>', f'<main class="flex-1 space-y-8 lg:space-y-12">{unite7_content}\n        </main>', template, flags=re.DOTALL)

with open('unite7.html', 'w', encoding='utf-8') as f:
    f.write(template)
    
update_file_sidebar('unite7.html', 7)
