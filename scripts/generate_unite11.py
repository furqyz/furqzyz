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
        {"title": "10. XX. Yüzyıl Başlarında Osmanlı Devleti", "file": "unite10.html", "icon": "fa-globe"},
        {"title": "11. Millî Mücadele Hazırlık Dönemi", "file": "unite11.html", "icon": "fa-bullhorn"},
    ]
    
    upcoming = [
        "12. I. TBMM Dönemi ve Gelişmeleri (1920 - 1923)",
        "13. Millî Mücadele Muharebeler Dönemi",
        "14. Atatürk'ün Hayatı",
        "15. Atatürk Dönemi İç Politika",
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

files_to_update = ['index.html', 'unite2.html', 'unite3.html', 'unite4.html', 'unite5.html', 'unite6.html', 'unite7.html', 'unite8.html', 'unite9.html', 'unite10.html']
for idx, f in enumerate(files_to_update):
    update_file_sidebar(f, idx + 1)

unite11_content = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-bullhorn text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">
                        KPSS Tarih Hazırlık
                    </div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">11. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">MİLLÎ MÜCADELE HAZIRLIK DÖNEMİ</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Mustafa Kemal'in Samsun'a çıkışından, kongreler dönemine, Temsil Heyeti'nin kurulmasından Misakımilli'nin kabulüne kadar olan direniş örgütlenmesini anlatan ünitedir.</p>
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
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Mustafa Kemal'in Milli Mücadele'yi başlatmak için attığı ilk adım <strong class="text-purple-700 dark:text-purple-400">Samsun'a çıkıştır</strong> (9. Ordu Müfettişi sıfatıyla bölgedeki güvenliği sağlamak ve silahları toplamak için gönderilmiştir).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Milli bilincin uyandırıldığı ve İzmir'in işgalinin protesto edildiği ilk belge <strong class="text-purple-700 dark:text-purple-400">Havza Genelgesi'dir</strong>. (Mustafa Kemal bu genelgeden sonra ilk kez İstanbul'a geri çağrılmıştır).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Milli Mücadele'nin amacı, gerekçesi ve yönteminin belirlendiği ilk belge <strong class="text-purple-700 dark:text-purple-400">Amasya Genelgesi'dir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Ulusal egemenlikten (millet iradesi / rejim değişikliği) ilk defa üstü kapalı bahsedilen yer <strong class="text-purple-700 dark:text-purple-400">Amasya Genelgesi'dir</strong> ("Milletin bağımsızlığını yine milletin azmi ve kararı kurtaracaktır" maddesi).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Manda ve himayenin ilk reddedildiği yer <strong class="text-purple-700 dark:text-purple-400">Erzurum Kongresi</strong>, kesin reddedildiği yer <strong class="text-purple-700 dark:text-purple-400">Sivas Kongresi'dir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Temsil Heyeti'nin elde ettiği ilk siyasi başarı, Sivas Kongresi sonrası <strong class="text-purple-700 dark:text-purple-400">Damat Ferit Paşa Hükümeti'ni istifa ettirmesidir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Temsil Heyeti'nin ilk yürütme yetkisini kullanması, Sivas Kongresi'nde <strong class="text-purple-700 dark:text-purple-400">Ali Fuat Cebesoy'u Batı Cephesi Komutanlığına atamasıdır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Temsil Heyeti'nin İstanbul Hükümetince ilk kez resmen/hukuken tanındığı olay <strong class="text-purple-700 dark:text-purple-400">Amasya Görüşmeleri'dir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>"Kuvayımilliye" kavramını belgelerde ilk kez kullanan kişi Milli Kongre Cemiyeti kurucusu <strong class="text-purple-700 dark:text-purple-400">Dr. Esat Işık'tır</strong>.</span></li>
                    </ul>
                </section>

                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-user-tie text-yellow-600 dark:text-yellow-300"></i>
                        </div>
                        Önemli Şahsiyetler ve Tarihi Sözler
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-yellow-100 font-medium">
                        <div class="bg-yellow-50/50 dark:bg-yellow-900/20 p-4 rounded-2xl relative">
                            <div class="absolute right-4 top-4 text-yellow-500/20 dark:text-yellow-500/10 text-4xl"><i class="fas fa-quote-right"></i></div>
                            <strong class="text-yellow-800 dark:text-yellow-300 text-lg block mb-1">"Geldikleri Gibi Giderler"</strong>
                            <p class="text-sm">Mustafa Kemal'in 13 Kasım 1918'de İstanbul'a geldiğinde işgal donanmalarını görünce yaveri Cevat Abbas'a söylediği tarihi sözdür.</p>
                        </div>
                        
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Ali Fuat Cebesoy:</strong> Amasya Genelgesi'ni imzalayan komutanlardandır, bu belgeyi "Mukaddes İttifak" olarak nitelendirmiştir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Rauf Orbay:</strong> Son Osmanlı Mebusan Meclisi'nde Misakımilli kararlarının alınmasını sağlayan "Felâh-ı Vatan" (Vatanın Kurtuluşu) grubunu kurmuştur.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Celaleddin Arif Bey:</strong> Misakımilli kararlarının kabul edildiği Son Osmanlı Mebusan Meclisi'nin son başkanıdır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Kâzım Karabekir:</strong> Erzurum Kongresi'nde artık sivil olan Mustafa Kemal'e "Ben ve kolordum emrinizdeyiz Paşam" diyerek en büyük desteği vermiştir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Ali Galip ve Muhittin Paşa:</strong> Sivas Kongresi'ni engellemek için İstanbul Hükümeti tarafından görevlendirilen Elazığ (Ali Galip) ve Ankara (Muhittin Paşa) valileridir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Manastırlı Hamdi (Martonaltı):</strong> 16 Mart 1920'de İstanbul'un işgal edildiğini ve meclisin basıldığını Mustafa Kemal'e telgrafla gizlice haber veren telgrafçıdır.</li>
                    </div>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-file-signature text-cyan-600 dark:text-cyan-300"></i>
                        </div>
                        Kritik Belgeler ve Gelişmeler
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-cyan-100 font-medium">
                        
                        <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-2 text-lg">Amasya Genelgesi (22 Haz 1919)</strong>
                            <p class="text-sm">Milli Mücadele'nin manifestosudur. <strong>Gerekçe:</strong> Vatanın bütünlüğü ve milletin istiklali tehlikededir. Mustafa Kemal bu genelgeden sonra "Artık İstanbul Anadolu'ya hâkim değil, tabi (bağlı) olmak zorundadır" demiştir.</p>
                        </div>

                        <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50 relative overflow-hidden">
                            <div class="absolute right-0 top-0 text-cyan-500/10 text-6xl -mr-2 -mt-2"><i class="fas fa-user-minus"></i></div>
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-2 text-lg">"Sine-i Millete Dönüş"</strong>
                            <p class="text-sm">Mustafa Kemal, Amasya Genelgesi'nden sonra, Erzurum Kongresi'nden önce çok sevdiği askerlik mesleğinden istifa etmiştir (Artık sivildir).</p>
                        </div>
                        
                        <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-2 text-lg">Erzurum Kongresi (Tem-Ağu 1919)</strong>
                            <p class="text-sm">Toplanış amacı ve yapısı bölgesel, aldığı kararlar ulusaldır. "Milli sınırlar içinde vatan bir bütündür, parçalanamaz" denilerek ilk kez vatan sınırlarından bahsedilmiştir. Temsil Heyeti 9 kişiyle kurulmuştur.</p>
                        </div>
                        
                        <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-2 text-lg">Sivas Kongresi (Eyl 1919)</strong>
                            <p class="text-sm">Her yönüyle ulusal bir kongredir. Tüm yararlı cemiyetler "Anadolu ve Rumeli Müdafaa-i Hukuk Cemiyeti" adı altında birleştirilmiştir. Halkı doğru bilgilendirmek için İrade-i Milliye gazetesi çıkarılmıştır. (Mustafa Kemal bu kongre günlerinde ABD'li General Harbord ile görüşmüştür).</p>
                        </div>
                    </div>
                </section>

                <!-- YEŞİL BÖLÜM -->
                <section class="category-green note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-emerald-900 dark:text-emerald-200">
                        <div class="bg-emerald-100 dark:bg-emerald-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-hand-holding-hand text-emerald-600 dark:text-emerald-300"></i>
                        </div>
                        Misakımilli ve İşgale Karşı Önlemler
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-emerald-100 font-medium">
                        
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-5 rounded-2xl relative">
                            <div class="absolute right-4 top-4 text-emerald-500/20 dark:text-emerald-500/10 text-5xl"><i class="fas fa-scroll"></i></div>
                            <strong class="text-emerald-800 dark:text-emerald-300 block text-lg mb-2 relative z-10">Misakımilli (Milli Yemin - 12 Oca 1920)</strong>
                            <p class="text-sm mb-3 relative z-10">Son Osmanlı Mebusan Meclisi'nde kabul edilmiştir. Tam bağımsızlık hedeflenmiştir. Kapitülasyonlar kesin olarak reddedilmiş; Kars, Ardahan, Batum (Elviye-i Selase), Batı Trakya ve Arap diyarları için gerekirse <strong>Halk Oylamasına (Referandum)</strong> başvurulabileceği belirtilmiştir.</p>
                        </div>
                        
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-2">İstanbul'un İşgaline Karşı Önlemler (16 Mart 1920):</strong>
                            <ul class="list-disc pl-4 space-y-1 text-sm">
                                <li>İstanbul ile tüm haberleşme kesilmiş,</li>
                                <li>Anadolu'dan toplanan vergilerin İstanbul'a gönderilmesi yasaklanmış,</li>
                                <li>İtilaf Devletleri'nin asker sevkiyatını engellemek için <strong>Geyve ve Ulukışla demiryolları</strong> tahrip edilmiştir.</li>
                            </ul>
                        </div>
                        
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-2">Yararlı Basın-Yayın:</strong>
                            <p class="text-sm">İrade-i Milliye (Sivas'ta), Hakimiyet-i Milliye (TBMM'nin yarı resmi gazetesi), Anadolu Ajansı (Halide Edip ve Yunus Nadi), Albayrak, Minber (M. Kemal ve Ali Fethi Okyar), Sebilürreşad.</p>
                        </div>
                    </div>
                </section>

                <!-- KIRMIZI BÖLÜM -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-exclamation-triangle text-red-600 dark:text-red-300"></i>
                        </div>
                        Kritik Öneme Sahip Uyarılar ve Analizler
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-slate-800 dark:text-red-100 font-medium">
                        <div class="border-l-4 border-red-400 pl-4 py-2 bg-white/40 dark:bg-black/10 rounded-r-xl">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Erzurum Kongresi İstifa Tuzağı:</strong>
                            <p class="text-sm">Sivil olan Mustafa Kemal ve Rauf Orbay'ın Erzurum Kongresi'ne delege olarak katılabilmesi için <strong class="text-red-700 dark:text-red-400">Cevat Dursunoğlu ve Kâzım Yurdalan</strong> kongreden istifa etmiştir. (ÖSYM bu ikiliyi çok sorar!).</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2 bg-white/40 dark:bg-black/10 rounded-r-xl">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Temsil Heyeti ile TBMM Ayrımı:</strong>
                            <p class="text-sm">Temsil Heyeti Amasya Genelgesi'nde fikren doğmuş, Erzurum'da kurulmuş, Sivas'ta tüm yurdu temsil eder hâle gelmiş, <strong>TBMM açılınca görevi sona ermiştir</strong>. (Temsil Heyeti hiçbir antlaşma imzalamamıştır).</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2 bg-white/40 dark:bg-black/10 rounded-r-xl">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Genelge ile Görüşmeler Ayrımı:</strong>
                            <p class="text-sm">Amasya Genelgesi komutanların imzaladığı bir "başkaldırı" bildirisidir. Amasya Görüşmeleri ise aylar sonra İstanbul Hükümeti ile Temsil Heyeti'nin masaya oturduğu <strong>tanınma</strong> olayıdır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2 bg-white/40 dark:bg-black/10 rounded-r-xl">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Misakımilli'de Olmayanlar:</strong>
                            <p class="text-sm">Misakımilli kararlarında "Ulusal Egemenlik / Milli İrade / Rejim" ile ilgili bir karar <strong class="text-red-700 dark:text-red-400">KESİNLİKLE YOKTUR</strong>. Sadece "Ulusal Bağımsızlık" ve sınır kararları vardır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2 bg-white/40 dark:bg-black/10 rounded-r-xl md:col-span-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Cemiyetler Tuzağı:</strong>
                            <p class="text-sm">"Sulh ve Selameti Osmaniye", "İslam Teali" ve "Kürt Teali" cemiyetleri isimleri olumlu gibi görünse de milli varlığa düşman (zararlı) cemiyetlerdir.</p>
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
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative lg:col-span-2">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md flex items-center"><i class="fas fa-exclamation-circle mr-1"></i> MİSAKIMİLLİ TUZAĞI (2019 / 2022 İptal KPSS)</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Misakımilli'de alınan kararlar arasında hangisi yoktur diye sorulur. <strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: "Milli egemenlik (ulusal irade)" şıkkı her zaman yanlış cevaptır! Misakımilli'de ulusal egemenlik kararı yoktur.</strong></p>
                        </div>
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2018 / 2024 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Mustafa Kemal'in askerlikten istifa ettikten sonra "Sine-i Millete dönerek" katıldığı sivil yapı hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Erzurum Kongresi</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">İstanbul Hükümeti'nin Temsil Heyeti'nin hukuki varlığını resmen tanıdığı olay hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Amasya Görüşmeleri</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2018 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">1919 yılında Türkiye'ye gelen ve Sivas'ta Mustafa Kemal Paşa ile görüşme yapan ABD'li general kimdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: General Harbord</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 İptal KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Mebusan Meclisinin basılması ve İstanbul'un işgaline karşı Mustafa Kemal'in aldığı askeri önlem nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Geyve ve Ulukışla demiryollarının tahrip edilmesi</strong></p>
                        </div>
                    </div>
                </div>
            </section>
"""

with open('unite10.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace main content for unite11
template = re.sub(r'<main class="flex-1 space-y-8 lg:space-y-12">.*?</main>', f'<main class="flex-1 space-y-8 lg:space-y-12">{unite11_content}\n        </main>', template, flags=re.DOTALL)

with open('unite11.html', 'w', encoding='utf-8') as f:
    f.write(template)
    
update_file_sidebar('unite11.html', 11)
