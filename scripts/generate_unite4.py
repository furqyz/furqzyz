import re

def generate_sidebar(active_index):
    items = [
        {"title": "1. İslamiyet Öncesi Türk Tarihi", "file": "index.html", "icon": "fa-landmark"},
        {"title": "2. İlk Türk İslam Devletleri", "file": "unite2.html", "icon": "fa-mosque"},
        {"title": "3. Anadolu (Türkiye) Selçuklu Devleti", "file": "unite3.html", "icon": "fa-chess-knight"},
        {"title": "4. Osmanlı Devleti Kültür ve Medeniyeti", "file": "unite4.html", "icon": "fa-landmark-dome"},
    ]
    
    upcoming = [
        "5. Osmanlı Devleti Kuruluş Dönemi (1299 - 1453)",
        "6. Osmanlı Devleti Yükselme Dönemi (1453 - 1595)",
        "7. XVII. Yüzyılda Osmanlı Devleti (Duraklama Dönemi) (1595 - 1699)",
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

unite4_content = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-landmark-dome text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">
                        KPSS Tarih Hazırlık
                    </div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">4. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">OSMANLI DEVLETİ KÜLTÜR VE MEDENİYETİ</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Bu ünitede Osmanlı Devleti'nin devlet teşkilatı, hukuk sistemi, eğitim, ekonomi, toprak yönetimi ve önemli bilim insanları incelenmektedir.</p>
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
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı'da "Sultan" unvanını kullanan ilk padişah <strong class="text-purple-700 dark:text-purple-400">Orhan Bey'dir</strong> (Sultanü'l Guzat).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>İlk düzenli ordu (Yaya ve Müsellem), ilk medrese (İznik Orhaniyesi), ilk saray (Bursa Sarayı) ve ilk Divan teşkilatı <strong class="text-purple-700 dark:text-purple-400">Orhan Bey</strong> döneminde kurulmuştur.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Devşirme sistemini (Pençik) uygulayan ve Kapıkulu Ocağı'nı kuran ilk padişah <strong class="text-purple-700 dark:text-purple-400">I. Murat'tır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Batı tarzında yapılan ilk eser <strong class="text-purple-700 dark:text-purple-400">III. Ahmet Çeşmesi</strong>, Batı tarzında yapılan ilk cami ise <strong class="text-purple-700 dark:text-purple-400">Nuruosmaniye Camii'dir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı'da açılan ilk banka <strong class="text-purple-700 dark:text-purple-400">Bank-ı Dersaadet</strong> (Galata bankerleri), millî sermayeli ilk banka <strong class="text-purple-700 dark:text-purple-400">Memleket Sandıkları'dır</strong> (Ziraat Bankasının temeli).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı'da açılan ilk resim sergisi <strong class="text-purple-700 dark:text-purple-400">Şeker Ahmet Paşa'ya</strong> aittir.</span></li>
                    </ul>
                </section>

                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-user-graduate text-yellow-600 dark:text-yellow-300"></i>
                        </div>
                        Önemli Şahsiyetler ve Bilim İnsanları
                    </h3>
                    <ul class="space-y-4 text-slate-800 dark:text-yellow-100 font-medium">
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Mimar Sinan:</strong> Çıraklık eseri Şehzade Camii, kalfalık eseri Süleymaniye Camii, ustalık eseri ise Edirne'deki Selimiye Camii'dir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Osman Hamdi Bey:</strong> Sanayi-i Nefise Mektebi'nin ve Arkeoloji Müzesi'nin kurucusudur. Kaplumbağa Terbiyecisi ve Silah Tacirleri en önemli tablolarıdır. Osmanlı'nın ilk müzecisidir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Akşemseddin:</strong> Fatih Sultan Mehmet'in hocasıdır. Mikrobiyolojinin babası sayılır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Kâtip Çelebi:</strong> 17. yüzyılın en büyük âlimlerindendir. Keşf-üz Zünun (Bibliyografya) ve Cihannüma (Coğrafya/Harita) adlı eserleri yazmıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Levni ve Nakkaş Osman:</strong> Osmanlı'nın en ünlü minyatür (tasvir) ustalarıdır. Gül Koklayan Fatih portresi Nakkaş Sinan Bey'e aittir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Piri Reis ve Seydi Ali Reis:</strong> Ünlü denizcilerdir. Piri Reis'in Kitab-ı Bahriye, Seydi Ali Reis'in Mir'atü'l Memalik (Ülkelerin Aynası) eseri meşhurdur.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Sabuncuoğlu Şerafettin:</strong> "Türk Plastik Cerrahisinin Babası"dır. Deneysel farmakoloji ile uğraşmış, Kitabül Cerrahiyetül Haniye ve Mücerrebname adlı eserleri yazmıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Naima:</strong> Osmanlı Devleti'nin ilk resmî tarih yazıcısıdır (Vakanüvis).</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Lagari Hasan Çelebi:</strong> Dünya tarihinin roketle uçan ilk insanıdır (IV. Murat dönemi).</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Erzurumlu İbrahim Hakkı:</strong> Matematik ve astronomi ile uğraşmış, Marifetname adlı ünlü eseri yazmıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Koçi Bey:</strong> IV. Murat'a devletin gidişatındaki bozulmalar ve çözüm yolları ile ilgili ünlü risalesini (raporunu) sunan bilgindir.</li>
                    </ul>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-sitemap text-cyan-600 dark:text-cyan-300"></i>
                        </div>
                        Kavramlar, Kurumlar ve Eyalet Sistemi
                    </h3>
                    <div class="space-y-6 text-slate-800 dark:text-cyan-100 font-medium">
                        
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-cyan-200 dark:border-cyan-800/40">
                            <strong class="text-cyan-800 dark:text-cyan-300 text-lg block mb-2"><i class="fas fa-crown mr-2"></i>Veraset Değişiklikleri Şifresi</strong>
                            <ul class="space-y-2 text-sm">
                                <li><strong class="text-cyan-700 dark:text-cyan-400">Osman Bey:</strong> Ülke hükümdar ve ailesinin ortak malıdır.</li>
                                <li><strong class="text-cyan-700 dark:text-cyan-400">I. Murat:</strong> Ülke hükümdar ve oğullarının malıdır.</li>
                                <li><strong class="text-cyan-700 dark:text-cyan-400">Fatih S. Mehmet:</strong> Ülke padişahındır (Kardeş katli yasallaştı).</li>
                                <li><strong class="text-cyan-700 dark:text-cyan-400">I. Ahmet:</strong> Ekber ve Erşed sistemi (Hanedanın en büyük ve akıllı üyesi başa geçer - Taht kavgası bitti).</li>
                            </ul>
                        </div>

                        <div class="bg-cyan-50/50 dark:bg-cyan-900/20 p-4 rounded-2xl">
                            <strong class="text-cyan-800 dark:text-cyan-300 text-lg block mb-2"><i class="fas fa-archway mr-2"></i>Sarayın Bölümleri</strong>
                            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-sm">
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong class="text-cyan-700 dark:text-cyan-400 block mb-0.5">Birun (Dış):</strong> Devlet işleri burada yürütülür.</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong class="text-cyan-700 dark:text-cyan-400 block mb-0.5">Enderun (İç):</strong> Saray okuludur. Devşirmeler yetiştirilir.</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong class="text-cyan-700 dark:text-cyan-400 block mb-0.5">Harem:</strong> Padişahın ve ailesinin özel hayat alanı.</span>
                            </div>
                        </div>

                        <div class="flex flex-col gap-2 text-sm">
                            <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Bedergâh vs. Çıkma:</strong>
                                <p><strong class="text-cyan-600 dark:text-cyan-500">Bedergâh (Kapıya Çıkma):</strong> Acemi Oğlanlar Ocağından eğitimini tamamlayanların usta birliklerine (Yeniçeri Ocağı'na) geçişine denir.</p>
                                <p class="mt-1"><strong class="text-cyan-600 dark:text-cyan-500">Çıkma:</strong> Enderun'daki öğrencilerin taşrada görevlendirilmesine veya medrese öğrencilerinin başarısızlığı sonucu verilen cezaya denir.</p>
                            </div>
                            <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Şuhudul Hâl:</strong> Kadıların mahkemede kesin karar vermeden önce olayın geçtiği yörenin güvenilir kişilerine danışmasından oluşan heyettir.
                            </div>
                            <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Sahn-ı Seman Medresesi:</strong> Fatih Sultan Mehmet döneminde açılan ve İstanbul Üniversitesi'nin temeli sayılan yükseköğretim kurumudur.
                            </div>
                            <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Ordu ve Eğitim Kavramları:</strong> Ulufe (3 aylık maaş), Cülus Bahşişi (Padişah değişikliği bahşişi), Gülbank (Yeniçeri duası). Eğitim Sıbyan Mektebinde "Amin Alayı" ile başlar.
                            </div>
                        </div>

                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-4">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-3"><i class="fas fa-map-marked-alt mr-2"></i>Eyalet Sistemi</p>
                            <div class="space-y-3">
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Salyaneli (Yıllıklı / Maaşlı) Eyaletler:</strong> Merkeze uzak olan eyaletlerdir (Mısır, Bağdat, Yemen vb.). Bu bölgelerde Tımar sistemi uygulanmaz, vergiler peşin olarak İltizam usulü ile toplanır.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Salyanesiz (Yıllıksız / Maaşsız) Eyaletler:</strong> Merkeze yakın olan eyaletlerdir (Rumeli, Anadolu, Sivas vb.). Bu bölgelerde vergi toplamak için Tımar sistemi uygulanır.
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- YEŞİL BÖLÜM -->
                <section class="category-green note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-emerald-900 dark:text-emerald-200">
                        <div class="bg-emerald-100 dark:bg-emerald-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-coins text-emerald-600 dark:text-emerald-300"></i>
                        </div>
                        Sınıflar, Sosyal Yapı ve Vergiler
                    </h3>
                    <div class="space-y-6 text-slate-800 dark:text-emerald-100 font-medium">
                        
                        <div class="bg-emerald-50/50 dark:bg-emerald-900/20 p-4 rounded-2xl">
                            <p class="font-bold text-emerald-800 dark:text-emerald-300 mb-2"><i class="fas fa-layer-group mr-2"></i>Yöneten Sınıflar</p>
                            <ul class="space-y-2 text-sm">
                                <li><strong class="text-emerald-700 dark:text-emerald-400">Seyfiye (Askerî ve İdari):</strong> Kılıç ehlidir. (Sadrazam, Vezir, Beylerbeyi, Yeniçeri Ağası, Kaptan-ı Derya)</li>
                                <li><strong class="text-emerald-700 dark:text-emerald-400">İlmiye (Din, Eğitim, Hukuk):</strong> Medrese mezunu, doğuştan Müslüman ve Türk olmak zorunludur. (Şeyhülislam, Kazasker, Kadı, Müderris)</li>
                                <li><strong class="text-emerald-700 dark:text-emerald-400">Kalemiye (Bürokrasi, Yazışma, Maliye):</strong> Kalem ehlidir. (Defterdar, Nişancı, Reisülküttap)</li>
                            </ul>
                        </div>

                        <div class="border-t border-emerald-200 dark:border-emerald-800/50 pt-4">
                            <p class="font-bold text-emerald-800 dark:text-emerald-300 mb-3"><i class="fas fa-file-invoice-dollar mr-2"></i>Önemli Vergiler</p>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-sm">
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-emerald-100 dark:border-emerald-800"><strong class="text-emerald-700 dark:text-emerald-400 block mb-0.5">Avarız</strong> Savaş, afet gibi olağanüstü durumlarda halktan toplanan vergi.</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-emerald-100 dark:border-emerald-800"><strong class="text-emerald-700 dark:text-emerald-400 block mb-0.5">Ağnam</strong> Küçükbaş hayvancılıkla uğraşanlardan alınan vergi.</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-emerald-100 dark:border-emerald-800"><strong class="text-emerald-700 dark:text-emerald-400 block mb-0.5">İspençe</strong> Gayrimüslim çiftçilerin ödediği toprak/tarım vergisi.</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-emerald-100 dark:border-emerald-800"><strong class="text-emerald-700 dark:text-emerald-400 block mb-0.5">Öşür (Aşar)</strong> Müslümanlardan ürün karşılığı alınan vergi.</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-emerald-100 dark:border-emerald-800"><strong class="text-emerald-700 dark:text-emerald-400 block mb-0.5">Haraç</strong> Gayrimüslimlerden ürün karşılığı alınan vergi.</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-emerald-100 dark:border-emerald-800"><strong class="text-emerald-700 dark:text-emerald-400 block mb-0.5">Cizye</strong> Gayrimüslimlerden askerlik yapmamaları karşılığı alınan vergi.</span>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-users-cog text-orange-600 dark:text-orange-300"></i>
                        </div>
                        Divan-ı Hümayun ve Üyeleri
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-orange-100 font-medium">
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Sadrazam (Veziriazam):</strong>
                            <p class="text-sm">Padişahın mührünü taşır. Padişah sefere katılmazsa "Serdar-ı Ekrem" unvanıyla ordunun başına geçer. Emirlerine <em class="text-slate-600 dark:text-slate-400">Buyruldu</em> denir.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Kazasker (Kadıasker):</strong>
                            <p class="text-sm">Adalet ve Millî Eğitim Bakanıdır. Kadıları ve müderrisleri atar. (İlmiye sınıfı)</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Defterdar:</strong>
                            <p class="text-sm">Maliye Bakanıdır. Bütçeyi yapar, Ruznamçe (günlük) defterlerini tutar. (Kalemiye sınıfı)</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Nişancı:</strong>
                            <p class="text-sm">Padişahın tuğrasını çeker. Dirlik (tımar) topraklarının kaydını Tahrir Defterlerine tutar. Örfi hukukun divandaki temsilcisidir.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Reisülküttap:</strong>
                            <p class="text-sm">17. yüzyıla kadar Nişancıya bağlıyken, diplomasi önem kazanınca ayrılarak Dışişleri Bakanı olmuştur.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Şeyhülislam (Müftü):</strong>
                            <p class="text-sm">Divanın asil üyesi değildir, sadece alınan kararların dine uygun olup olmadığı hakkında "Fetva" verir.</p>
                        </div>
                    </div>
                </section>

                <!-- KIRMIZI BÖLÜM -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-exclamation-triangle text-red-600 dark:text-red-300"></i>
                        </div>
                        Padişah Belgeleri, Toprak Yönetimi ve Uyarılar
                    </h3>
                    <div class="space-y-6 text-slate-800 dark:text-red-100 font-medium">
                        
                        <div class="border-l-4 border-red-400 pl-4 py-3 bg-red-50/50 dark:bg-red-900/20 rounded-r-xl">
                            <strong class="text-red-800 dark:text-red-300 block mb-2">Padişahın Yazılı Belgeleri:</strong>
                            <ul class="space-y-1.5 text-sm list-none ml-1">
                                <li><strong class="text-red-700 dark:text-red-400">Ferman:</strong> Yazılı emir</li>
                                <li><strong class="text-red-700 dark:text-red-400">Hatt-ı Hümayun:</strong> Yazılı beyan</li>
                                <li><strong class="text-red-700 dark:text-red-400">Müsadere:</strong> Haksız kazanç sağlayan memurun malına el koyma</li>
                                <li><strong class="text-red-700 dark:text-red-400">Beratname:</strong> Göreve atama belgesi</li>
                            </ul>
                        </div>

                        <div class="border-t border-red-200 dark:border-red-800/50 pt-4">
                            <strong class="text-red-800 dark:text-red-300 block mb-3"><i class="fas fa-seedling mr-2"></i>MİRİ ARAZİ (Devlete Ait Topraklar)</strong>
                            <div class="space-y-2 text-sm">
                                <div class="bg-white/60 dark:bg-black/10 p-3 rounded-xl border border-red-200 dark:border-red-800/40">
                                    <strong class="text-red-700 dark:text-red-400 block mb-0.5">Dirlik (Tımar):</strong> Geliri devlet memurlarına ve askerlere maaş karşılığı verilir (Has, Zeamet, Tımar).
                                </div>
                                <div class="bg-white/60 dark:bg-black/10 p-3 rounded-xl border border-red-200 dark:border-red-800/40">
                                    <strong class="text-red-700 dark:text-red-400 block mb-0.5">Mukataa:</strong> Geliri doğrudan doğruya (iltizam usulüyle) devlet hazinesine giden topraklardır.
                                </div>
                                <div class="bg-white/60 dark:bg-black/10 p-3 rounded-xl border border-red-200 dark:border-red-800/40">
                                    <strong class="text-red-700 dark:text-red-400 block mb-0.5">Malikane:</strong> Üstün hizmet gösteren devlet adamlarına veya iltizamın ömür boyu verildiği kişilere ayrılan topraklardır.
                                </div>
                                <div class="bg-white/60 dark:bg-black/10 p-3 rounded-xl border border-red-200 dark:border-red-800/40">
                                    <strong class="text-red-700 dark:text-red-400 block mb-0.5">Paşmaklık:</strong> Geliri padişah kızlarına ve harem kadınlarına ayrılan topraklardır.
                                </div>
                                <div class="bg-white/60 dark:bg-black/10 p-3 rounded-xl border border-red-200 dark:border-red-800/40">
                                    <strong class="text-red-700 dark:text-red-400 block mb-0.5">Yurtluk:</strong> Geliri sınır boylarında oturanlara ayrılan topraklardır.
                                </div>
                                <div class="bg-white/60 dark:bg-black/10 p-3 rounded-xl border border-red-200 dark:border-red-800/40">
                                    <strong class="text-red-700 dark:text-red-400 block mb-0.5">Ocaklık:</strong> Geliri kale muhafızlarına ve tersanecilere ayrılan topraklardır.
                                </div>
                            </div>
                        </div>

                        <div class="border-l-4 border-red-400 pl-4 py-2 mt-4">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">İltizam Sistemi:</strong>
                            <p class="text-sm">Devletin nakit para ihtiyacını karşılamak için merkeze uzak eyaletlerin vergi toplama hakkının açık artırmayla (ihaleyle) "Mültezim" adı verilen kişilere satılmasıdır.</p>
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
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2015 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Şehzadelerin 12 yaşında "Çelebi Sultan" unvanıyla sancaklara gönderilmesinin nedeni nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Yönetimde ve askerî alanda tecrübe kazanmaları</strong></p>
                        </div>
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2016 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Divan-ı Hümayun'da padişahı temsil eden kalemiye (bürokrasi) sınıfı üyeleri kimlerdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Nişancı, Defterdar ve Reisülküttap</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2017 / 2021</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Padişahların, halkın derdini dinlemesi ve yöneticilerin haksızlıklarını gidermek için yayınladığı fermanlara ne denir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Adaletname</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2018 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Gayrimüslim çiftçinin ödediği vergiye "İspençe" denmesi, Osmanlı hukuk sisteminde neyin kanıtıdır?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: İkili bir yapının olduğu</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Ülke yönetimi hakkında yöneticilere öğüt veren eserlere ne denir? (Örn: Kutadgu Bilig, Koçi Bey Risalesi)<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Siyasetname</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2023 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">İltizam (ihaleyle vergi toplama) ve Malikane (ömür boyu kiralama) Osmanlı maliyesinde doğrudan ne için uygulanan sistemlerdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Nakit (hazine) ihtiyacını karşılamak</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2024 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Gayrimüslimlerden ürün karşılığında Haraç alınırken; Müslümanlardan ürün karşılığında hangi vergi alınır?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Öşür</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2025 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Topkapı Sarayı'nın ihtiyaçları, tamiratı ve bakım işlerinden sorumlu olan görevli kimdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Şehremini</strong></p>
                        </div>
                        
                        <!-- ÖSYM KELİME TUZAĞI (Geniş Kart) -->
                        <div class="md:col-span-2 lg:col-span-3 bg-indigo-50/80 dark:bg-indigo-900/30 p-6 rounded-2xl border border-indigo-200 dark:border-indigo-800/50 flex items-start mt-2">
                            <i class="fas fa-exclamation-circle text-indigo-500 mt-1 mr-4 text-3xl"></i>
                            <div>
                                <p class="font-black text-indigo-800 dark:text-indigo-300 mb-2">ÖSYM KELİME TUZAKLARI (SINIFLAR)</p>
                                <p class="text-sm font-medium text-slate-700 dark:text-slate-300 leading-relaxed flex flex-wrap gap-x-6 gap-y-2">
                                    <span><strong class="text-indigo-700 dark:text-indigo-400">Ehl-i Şer:</strong> Şeriat ehli yani İlmiye sınıfı</span>
                                    <span><strong class="text-indigo-700 dark:text-indigo-400">Ehl-i Örf:</strong> Seyfiye sınıfı</span>
                                    <span><strong class="text-indigo-700 dark:text-indigo-400">Ehl-i Kalem:</strong> Kalemiye sınıfı</span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
"""

with open('unite3.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Remove the II. Türk Beylikleri Künyesi from template structure for unite4 since it's unit specific
template = re.sub(r'<!-- DEVLETLER KÜNYESİ \(FULL WIDTH\) -->.*?</section>', '', template, flags=re.DOTALL)

# Replace main content for unite4
template = re.sub(r'<main class="flex-1 space-y-8 lg:space-y-12">.*?</main>', f'<main class="flex-1 space-y-8 lg:space-y-12">{unite4_content}\n        </main>', template, flags=re.DOTALL)

# Set correct sidebar
new_nav = generate_sidebar(4)
template = re.sub(r'<nav class="space-y-1.5 max-h-\[60vh\] overflow-y-auto pr-1.5 custom-scrollbar">.*?</nav>', new_nav, template, flags=re.DOTALL)

with open('unite4.html', 'w', encoding='utf-8') as f:
    f.write(template)

