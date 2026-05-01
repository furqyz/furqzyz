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
    ]
    
    upcoming = [
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

files_to_update = ['index.html', 'unite2.html', 'unite3.html', 'unite4.html', 'unite5.html', 'unite6.html', 'unite7.html', 'unite8.html', 'unite9.html']
for idx, f in enumerate(files_to_update):
    update_file_sidebar(f, idx + 1)

unite10_content = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-globe text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">
                        KPSS Tarih Hazırlık
                    </div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">10. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">XX. YÜZYIL BAŞLARINDA OSMANLI DEVLETİ</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Trablusgarp Savaşı, Balkan Savaşları ve I. Dünya Savaşı'nın genel gidişatı ile savaşların kaderini belirleyen kahramanları incelediğimiz ünitedir.</p>
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
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı Devleti'nin Kuzey Afrika'daki son toprak parçası <strong class="text-purple-700 dark:text-purple-400">Trablusgarp'tır</strong> (Uşi Antlaşması ile kaybedilmiştir).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Dünya tarihinde savaş uçağının ilk kullanıldığı savaş <strong class="text-purple-700 dark:text-purple-400">Trablusgarp Savaşı'dır</strong> (İtalya kullanmıştır).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı Devleti'nden ayrılarak bağımsız olan son Balkan devleti <strong class="text-purple-700 dark:text-purple-400">Arnavutluk'tur</strong> (Böylece "Osmanlıcılık" fikri ilk büyük darbeyi almıştır).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı tarihindeki ilk resmî hükûmet darbesi <strong class="text-purple-700 dark:text-purple-400">Babıali Baskını'dır</strong> (1913). İttihat ve Terakki yönetime el koymuştur.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>I. Dünya Savaşı'nda Osmanlı'nın toprak kazandığı ilk ve tek cephe <strong class="text-purple-700 dark:text-purple-400">Kafkas Cephesi'dir</strong> (Rusya'nın çekilmesiyle Muş, Bitlis, Kars, Ardahan, Batum geri alınmıştır).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>I. Dünya Savaşı'nda Osmanlı'nın zaferle kapattığı tek cephe <strong class="text-purple-700 dark:text-purple-400">Çanakkale Cephesi'dir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Mustafa Kemal'in sömürgeciliğe karşı verdiği ilk askerî mücadele <strong class="text-purple-700 dark:text-purple-400">Trablusgarp Savaşı'dır</strong>.</span></li>
                    </ul>
                </section>

                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-crown text-yellow-600 dark:text-yellow-300"></i>
                        </div>
                        Önemli Şahsiyetler, Lakaplar ve Rütbeler
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-yellow-100 font-medium">
                        <div class="bg-yellow-50/50 dark:bg-yellow-900/20 p-4 rounded-2xl">
                            <strong class="text-yellow-800 dark:text-yellow-300 text-lg block mb-3 border-b border-yellow-200 dark:border-yellow-800/50 pb-2"><i class="fas fa-star mr-2"></i>Mustafa Kemal Paşa</strong>
                            <ul class="space-y-2 text-sm">
                                <li><strong class="text-yellow-700 dark:text-yellow-400">Trablusgarp'ta:</strong> "Gazeteci Şerif Bey" kimliğiyle gizlice gitmiş, yerel halkı örgütlemiş ve "Binbaşı" rütbesine yükselmiştir (Derne ve Tobruk'ta başarılıdır).</li>
                                <li><strong class="text-yellow-700 dark:text-yellow-400">Çanakkale'de:</strong> "Ben size taarruzu değil, ölmeyi emrediyorum" diyerek savaşın kaderini değiştirmiş, "Anafartalar Kahramanı" unvanını almış ve "Albay" rütbesine yükselmiştir. Ayrıca savaştığı tepeye "Kemalyeri" adı verilmiştir.</li>
                                <li><strong class="text-yellow-700 dark:text-yellow-400">Kafkasya'da:</strong> Muş ve Bitlis'i Ruslardan geri alarak "Altın Kılıç" madalyası almıştır.</li>
                            </ul>
                        </div>
                        
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Enver Paşa (Edirne Fatihi):</strong> Trablusgarp'a "Kuyumcu Hamdi" adıyla gitmiştir. II. Balkan Savaşı'nda Edirne'yi Bulgarlardan geri alarak bu unvanı kazanmıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Şükrü Paşa (Edirne Müdafii):</strong> I. Balkan Savaşı sırasında Edirne'yi her türlü imkânsızlığa rağmen 160 gün boyunca kahramanca savunan efsanevi komutandır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Nuri Paşa / Killigil (Bakü Fatihi):</strong> Kafkas İslam Ordusu komutanı olarak Bakü'yü Ermeni ve Rus işgalinden kurtaran kahramandır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Rauf Orbay (Hamidiye Kahramanı):</strong> I. Balkan Savaşı sırasındaki deniz başarılarından dolayı bu unvanı almıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Cevat Çobanlı (18 Mart Kahramanı):</strong> Çanakkale Deniz Savaşlarında Nusret Mayın Gemisi'ne mayın hattı emrini vererek düşman donanmasını yok eden kahramandır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Halil Kut Paşa (Kut'ül Amare Kahramanı):</strong> Irak Cephesi'nde İngiliz General Townshend'i esir alan paşadır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Fahrettin Paşa (Çöl Kaplanı / Medine Müdafii):</strong> Hicaz-Yemen Cephesi'nde Medine'yi çekirge yiyerek savunan büyük kahramandır.</li>
                    </div>
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
                        
                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-2">
                            <div class="grid grid-cols-1 gap-3 text-sm">
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Trablusgarp Savaşı (1911-1912):</strong> İtalya'nın sömürge arayışıyla saldırmasıdır. Osmanlı, Şeyh Sunusi gibi yerel aşiret liderlerinin de desteğiyle bölge halkını İtalyanlara karşı direnişe geçirmiştir.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Balkan Savaşları (1912-1913):</strong>
                                    <ul class="list-disc pl-4 mt-1 space-y-1">
                                        <li><strong>I. Balkan:</strong> Sırbistan, Karadağ, Yunanistan ve Bulgaristan'ın saldırmasıdır (Romanya yoktur!). Osmanlı ağır yenilgi alıp Midye-Enez hattının batısını (Edirne dâhil) kaybetmiştir.</li>
                                        <li><strong>II. Balkan:</strong> Bulgaristan'ın çok toprak almasını bahane eden devletlerin (Romanya dâhil) Bulgaristan'a saldırmasıdır. Osmanlı bu fırsatla Edirne ve Kırklareli'yi geri almıştır.</li>
                                    </ul>
                                </div>
                                
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1"><i class="fas fa-key mr-2"></i>I. Dünya Savaşı Cephe Şifreleri:</strong>
                                    <ul class="list-disc pl-4 space-y-1">
                                        <li><strong class="text-cyan-600 dark:text-cyan-400">Taarruz (K-K):</strong> Kafkas, Kanal.</li>
                                        <li><strong class="text-cyan-600 dark:text-cyan-400">Savunma:</strong> Çanakkale, Suriye-Filistin, Irak, Hicaz-Yemen.</li>
                                        <li><strong class="text-cyan-600 dark:text-cyan-400">Yardım (Sonu "Ya" ile bitenler):</strong> Galiçya, Romanya, Makedonya.</li>
                                    </ul>
                                </div>
                                
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">M. Kemal'in Cephe Sırası:</strong> <span class="bg-cyan-200 dark:bg-cyan-800 px-2 rounded text-cyan-900 dark:text-cyan-100 font-bold">ÇıKıS</span> (Çanakkale ➔ Kafkasya ➔ Suriye-Filistin).
                                </div>

                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Tehcir (Sevk ve İskân) Kanunu (1915):</strong> Kafkas Cephesi'nde Ruslarla iş birliği yapan Ermenilerin savaş bölgesinden alınıp Suriye ve Lübnan'a göç ettirilmesi kanunudur.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Gizli Antlaşmalar:</strong> İtilaf devletlerinin Osmanlı'yı paylaştıkları antlaşmalardır. Saint Jean de Maurienne antlaşmasıyla İzmir İtalya'ya bırakılmıştır. Bu gizli antlaşmaları dünyaya Sovyet Rusya ("Sarı Kitap" ile) duyurmuştur.
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
                        Savaşları Bitiren Antlaşmalar
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-emerald-100 font-medium">
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">Uşi Antlaşması (1912):</strong></p>
                            <p class="text-sm">Trablusgarp ve Bingazi İtalya'ya bırakılmıştır. Rodos ve 12 Ada, Balkan Savaşları bitene kadar "geçici olarak" İtalya'ya bırakılmıştır.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">Brest-Litovsk Antlaşması (1918):</strong></p>
                            <p class="text-sm">Kafkas Cephesi'ni kapatan antlaşmadır. Sovyet Rusya savaştan çekilmiş; Kars, Ardahan ve Batum'u Osmanlı'ya geri vermiştir.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">Mac Mahon Antlaşması:</strong></p>
                            <p class="text-sm">İngilizlerin, Hicaz Emiri Şerif Hüseyin'e bağımsız bir Arap devleti vadettiği gizli antlaşmadır. Bu, "Ümmetçilik (İslamcılık)" fikrinin çöktüğünün net kanıtıdır.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl relative overflow-hidden">
                            <div class="absolute right-0 top-0 text-emerald-500/20 dark:text-emerald-500/10 text-6xl -mt-2 -mr-2"><i class="fas fa-file-signature"></i></div>
                            <strong class="text-emerald-800 dark:text-emerald-300 block text-lg mb-2 relative z-10">Mondros Ateşkes Antlaşması (30 Ekim 1918):</strong>
                            <p class="text-sm mb-3 relative z-10">I. Dünya Savaşı'nı bitiren ateşkesi Osmanlı adına Agamemnon Zırhlısı'nda Rauf Orbay imzalamıştır.</p>
                            <ul class="text-sm space-y-2 relative z-10 border-t border-emerald-200/60 dark:border-emerald-800/50 pt-2">
                                <li><strong class="text-emerald-700 dark:text-emerald-400">7. Madde:</strong> İtilaf devletleri güvenliklerini tehdit eden herhangi bir bölgeyi işgal edebilecektir (Anadolu işgallere açık hâle gelmiştir).</li>
                                <li><strong class="text-emerald-700 dark:text-emerald-400">24. Madde:</strong> Vilayet-i Sitte'de (6 Doğu ilinde: Bitlis, Erzurum, Sivas, Van, Elazığ, Diyarbakır) bir karışıklık çıkarsa işgal edilecektir (Amacı "Büyük Ermenistan" devleti kurmaktır).</li>
                            </ul>
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
                            <strong class="text-red-800 dark:text-red-300 block mb-1">İki Edirne Kahramanı Tuzağı:</strong>
                            <p class="text-sm">"Edirne Fatihi" Enver Paşa'dır, "Edirne Müdafii" Şükrü Paşa'dır. ÖSYM bu ikisini şıklarda karıştırmanızı ister, DİKKAT!</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2 bg-white/40 dark:bg-black/10 rounded-r-xl">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Babıali Baskını Tuzağı:</strong>
                            <p class="text-sm">1913 Babıali Baskını bir HÜKÛMET DARBESİDİR. Padişahı (rejimi) değiştirmemiş, İttihat ve Terakki'nin yönetime el koymasını sağlamıştır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2 bg-white/40 dark:bg-black/10 rounded-r-xl">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">12 Ada Tuzağı:</strong>
                            <p class="text-sm">Uşi Antlaşması ile Rodos ve 12 Ada İtalya'ya "geçici" olarak bırakılmış ancak İtalya bu adaları bir daha geri vermemiştir.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2 bg-white/40 dark:bg-black/10 rounded-r-xl">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">İlk İşgaller:</strong>
                            <p class="text-sm">Mondros'tan sonra işgale uğrayan ilk Osmanlı toprağı Musul'dur (İngilizler). Anadolu'da işgale uğrayan ilk yer ise Hatay-Dörtyol'dur (Kara Mehmet Çavuş, Fransızlara karşı ilk kurşunu atmıştır).</p>
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
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">İngiliz General Townshend'in esir alındığı cephe ve bu cephenin kahramanı komutan kimdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Irak Cephesi - Halil (Kut) Paşa</strong></p>
                        </div>
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2021 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Sırbistan, Karadağ, Yunanistan ve Bulgaristan'ın saldırmasıyla başlayan ve Midye-Enez hattının kaybedildiği savaş hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: I. Balkan Savaşı</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2018 / 2024 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">"I. Balkan Savaşı'nda olmayıp, II. Balkan Savaşı'na katılan devlet hangisidir?"<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Romanya</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 İptal KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Osmanlı'nın müttefiklerine yardım için savaştığı (Taarruz veya Savunma olmayan) cephelerden biri hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Galiçya</strong></p>
                        </div>

                        <div class="bg-red-50 hover:bg-red-100 dark:bg-red-900/30 dark:hover:bg-red-900/50 transition-colors p-5 rounded-2xl border border-red-200 dark:border-red-800/50 backdrop-blur-sm relative lg:col-span-2">
                            <div class="absolute -top-3 -left-3 bg-red-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md flex items-center"><i class="fas fa-exclamation-circle mr-1"></i> DİKKAT: SİYASİ ŞAHSİYET ÇELDİRİCİSİ</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-red-200">Mustafa Kemal, I. Dünya Savaşı başladığında <strong>Sofya Askeri Ataşeliği</strong> görevindedir. Savaşın başlamasında (Almanya ile ittifak kurulmasında vb.) başrol oynayan grup ise <strong>İttihat ve Terakki Cemiyeti</strong> olmuştur.</p>
                        </div>
                    </div>
                </div>
            </section>
"""

with open('unite9.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace main content for unite10
template = re.sub(r'<main class="flex-1 space-y-8 lg:space-y-12">.*?</main>', f'<main class="flex-1 space-y-8 lg:space-y-12">{unite10_content}\n        </main>', template, flags=re.DOTALL)

with open('unite10.html', 'w', encoding='utf-8') as f:
    f.write(template)
    
update_file_sidebar('unite10.html', 10)
