import re

def generate_sidebar(active_index):
    items = [
        {"title": "1. İslamiyet Öncesi Türk Tarihi", "file": "index.html", "icon": "fa-landmark"},
        {"title": "2. İlk Türk İslam Devletleri", "file": "unite2.html", "icon": "fa-mosque"},
        {"title": "3. Anadolu (Türkiye) Selçuklu Devleti", "file": "unite3.html", "icon": "fa-chess-knight"},
    ]
    
    upcoming = [
        "4. Osmanlı Devleti Kültür ve Medeniyeti",
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
    
    # regex replace everything between <nav ...> and </nav>
    content = re.sub(r'<nav class="space-y-1.5 max-h-\[60vh\] overflow-y-auto pr-1.5 custom-scrollbar">.*?</nav>', new_nav, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

update_file_sidebar('index.html', 1)
update_file_sidebar('unite2.html', 2)

unite3_content = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-horse-head text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">
                        KPSS Tarih Hazırlık
                    </div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">3. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">ANADOLU (TÜRKİYE) SELÇUKLU DEVLETİ VE II. BEYLİKLER</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Bu ünitede Türkiye Selçuklu Devleti'nin siyasi ve kültürel gelişimi, Ahilik teşkilatı ve İkinci Beylikler Dönemi incelenmektedir.</p>
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
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Türkiye Selçuklu Devleti, Kutalmışoğlu Süleyman Şah tarafından Bizans’taki taht kavgalarından yararlanılarak başkenti <strong class="text-purple-700 dark:text-purple-400">İznik</strong> olmak üzere kurulmuştur.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Anadolu'dan "Türkiye" diye ilk defa <strong class="text-purple-700 dark:text-purple-400">I. Mesut</strong> Dönemi'nde bahsedilmiştir.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Devletin ilk madeni parası (bakır) <strong class="text-purple-700 dark:text-purple-400">I. Mesut</strong> döneminde, ilk altın parası ise <strong class="text-purple-700 dark:text-purple-400">II. Kılıçarslan</strong> döneminde basılmıştır.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Anadolu'nun kesin olarak "Türk yurdu" hâline gelmesi, Bizans'a karşı kazanılan 1176 <strong class="text-purple-700 dark:text-purple-400">Miryokefalon Savaşı</strong> (Yurttutan) ile gerçekleşmiştir.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Türkiye Selçuklularına en parlak dönemini yaşatan hükümdar <strong class="text-purple-700 dark:text-purple-400">I. Alaaddin Keykubat'tır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Türk tarihinde denizaşırı ilk sefer, Karadeniz'in kuzeyindeki Suğdak Limanı'nın (Kırım) alınmasıyla yapılmıştır (<strong class="text-purple-700 dark:text-purple-400">I. Alaaddin Keykubat</strong>).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Dünya tarihinde ilk kez devlet sigortacılığı sistemini (tüccarların zararını devletin karşılaması) uygulayan devlet <strong class="text-purple-700 dark:text-purple-400">Türkiye Selçuklularıdır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı Devleti'ne katılan ilk beylik <strong class="text-purple-700 dark:text-purple-400">Karesioğulları</strong>, katılan son beylik ise <strong class="text-purple-700 dark:text-purple-400">Dulkadiroğulları'dır</strong>.</span></li>
                        
                        <div class="mt-4 p-4 bg-purple-50 dark:bg-purple-900/30 rounded-2xl border border-purple-100 dark:border-purple-800/50">
                            <p class="font-bold text-purple-800 dark:text-purple-300 mb-2 border-b border-purple-200 dark:border-purple-800/50 pb-2"><i class="fas fa-building mr-2"></i>İlk Mimari Eserler</p>
                            <ul class="space-y-2 text-sm mt-2">
                                <li><strong class="text-purple-700 dark:text-purple-400">İlk Hastane:</strong> Kayseri Gevher Nesibe Darüşşifası</li>
                                <li><strong class="text-purple-700 dark:text-purple-400">İlk Medrese:</strong> Kayseri Kocahasan Medresesi</li>
                                <li><strong class="text-purple-700 dark:text-purple-400">İlk Cami:</strong> Konya Alaaddin Camii</li>
                                <li><strong class="text-purple-700 dark:text-purple-400">İlk Kervansaray:</strong> Aksaray Alay Han</li>
                            </ul>
                        </div>
                    </ul>
                </section>

                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-user-crown text-yellow-600 dark:text-yellow-300"></i>
                        </div>
                        Önemli Şahsiyetler
                    </h3>
                    <ul class="space-y-4 text-slate-800 dark:text-yellow-100 font-medium">
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">I. Kılıçarslan:</strong> I. Haçlı Seferi sırasında başkent İznik'i kaybetmiş ve devletin merkezini Konya'ya taşımak zorunda kalmıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">II. Kılıçarslan:</strong> Miryokefalon Savaşı'nı kazanmış, ölmeden önce eski Türk geleneğine uyarak ülkeyi 11 oğlu arasında paylaştırmıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">I. Alaaddin Keykubat:</strong> Devlete en parlak dönemini yaşatan, Alaiye (Alanya) ve Suğdak'ı alan, Moğol tehlikesine karşı surları güçlendiren büyük sultandır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Ahi Evran:</strong> Ahilik (esnaf ve zanaatkâr) teşkilatının kurucusudur. "Letaif-i Hikmet" adlı eseri yazmıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Fatma Bacı:</strong> Ahi Evran'ın eşidir. Dünyanın ilk kadın sivil toplum örgütü sayılan "Bacıyan-ı Rum"u (Anadolu Kadınları) kurmuştur.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Manevi ve Edebi Şahsiyetler:</strong> Mevlâna (Kebir ve Mesnevi), Hacı Bektaş Veli (Makâlât), Yunus Emre (Risaletü'n Nushiyye), Aşık Paşa (Garipname), Gülşehri (Mantıku't Tayr).</li>
                    </ul>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-book-open text-cyan-600 dark:text-cyan-300"></i>
                        </div>
                        Kavramlar ve Savaşlar
                    </h3>
                    <div class="space-y-6 text-slate-800 dark:text-cyan-100 font-medium">
                        
                        <div class="bg-cyan-50/50 dark:bg-cyan-900/20 p-4 rounded-2xl">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-2 flex items-center"><i class="fas fa-store mr-2"></i>Ahilik Kavramları</p>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-sm">
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong class="text-cyan-700 dark:text-cyan-400 block mb-0.5">Narh Kesmek</strong> Üretilen malın fiyatını belirlemektir.</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong class="text-cyan-700 dark:text-cyan-400 block mb-0.5">Gedik</strong> Dükkân açma izni / hakkıdır.</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong class="text-cyan-700 dark:text-cyan-400 block mb-0.5">İcazetname</strong> Mesleki eğitimi bitirene verilen diplomadır.</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong class="text-cyan-700 dark:text-cyan-400 block mb-0.5">Fütüvvetname</strong> Ahilik teşkilatının yazılı olmayan ahlak ve meslek kurallarıdır.</span>
                            </div>
                        </div>

                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-4">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-3"><i class="fas fa-crosshairs mr-2"></i>Önemli Olaylar ve Savaşlar</p>
                            <div class="flex flex-col gap-2 text-sm">
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Yassıçimen Savaşı (1230):</strong> I. Alaaddin Keykubat döneminde Harzemşahların yenilerek yıkılış sürecine girdiği savaştır. Bu savaşın kazanılması, Doğu Anadolu'da Moğollarla aradaki tampon bölgenin kalkmasına ve Moğol istilasının hızlanmasına neden olmuştur.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Baba İshak (Babailer) İsyanı (1240):</strong> Türkiye Selçuklu tarihindeki ilk dinî ve sosyal nitelikli büyük Türkmen isyanıdır. Devlet isyanı zorlukla bastırmış, bu zayıflığı gören Moğollar Anadolu'ya saldırma cesareti bulmuştur.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Kösedağ Savaşı (1243):</strong> İlhanlılar (Moğollar) ile yapılmış ve kaybedilmiştir. Sonuçlarında; devlet dağılma sürecine girmiş, Anadolu Türk siyasi birliği bozulmuş, Moğol tahribatı yaşanmış ve Anadolu'da "İkinci Türk Beylikleri" dönemi başlamıştır.
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
                    <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl text-slate-800 dark:text-emerald-100 font-medium">
                        <p class="mb-2"><strong class="text-emerald-800 dark:text-emerald-300">Uluslararası Ticaret Antlaşmaları:</strong></p>
                        <p class="text-sm">I. Gıyaseddin Keyhüsrev ve I. İzzeddin Keykavus dönemlerinde Kıbrıs Krallığı ve Venedikliler ile tarihteki ilk ticari gümrük antlaşmaları yapılmıştır.</p>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-users-cog text-orange-600 dark:text-orange-300"></i>
                        </div>
                        Divanlar, Görevliler ve Unvanlar
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-orange-100 font-medium">
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Divan-ı Pervane:</strong>
                            <p class="text-sm">İkta topraklarının kayıtlarını tutan ve dağıtımını yapan divandır. Sorumlusuna <em class="text-slate-600 dark:text-slate-400">Pervaneci</em> denir.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Divan-ı Berid:</strong>
                            <p class="text-sm">Posta ve haberleşme teşkilatıdır.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Reisül Bahr veya Meliküs Sevahil:</strong>
                            <p class="text-sm">Denizaşırı seferler yapan donanma komutanlarına verilen unvanlardır (Denizlerin Reisi / Sahillerin Meliki).</p>
                        </div>
                        <div class="border-l-4 border-orange-400 pl-4 py-2 mt-4 bg-orange-50/50 dark:bg-orange-900/20 rounded-r-xl">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Farsça Unvanlar:</strong>
                            <p class="text-sm">Selçuklu hükümdarları padişah veya sultan anlamında Keyhüsrev, Keykavus, Keykubat gibi Farsça unvanlar kullanmışlardır. Bu, Fars kültürünün ve edebiyatının devlet yönetimindeki etkisini gösterir.</p>
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
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Ahilik Teşkilatı ve Dini Yapı:</strong>
                            <p class="text-sm">Ahilik teşkilatına kesinlikle gayrimüslimler alınmamıştır. (Daha sonra Osmanlı'da kurulacak olan Lonca teşkilatına ise gayrimüslimler alınacaktır.) Ahilik sadece bir esnaf örgütü değil, mesleki eğitimin verildiği, gerektiğinde "cihata katılan" silahlı bir yapıdır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Mimari Eser Bulma Şifresi:</strong>
                            <p class="text-sm">Sorularda bir eserin isminde "Paşa, Çelebi, Haseki, Ağa, Sultan, Yeşil" kelimeleri geçiyorsa o eser istisnalar hariç Osmanlı Devleti'ne aittir. İsminde "Çifte" veya "Alaaddin" kelimeleriyle başlayan eserler ise genellikle Anadolu Selçuklu Devleti'ne aittir.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Ticaret Stratejisi:</strong>
                            <p class="text-sm">Alanya, Sinop, Antalya, Suğdak gibi liman şehirlerinin fethi, kervansarayların inşası, gümrük vergilerinin indirilmesi ve devlet sigortacılığı sisteminin başlatılması tamamen "Anadolu'yu uluslararası bir ticaret merkezi yapmak" amacına yöneliktir.</p>
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
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2016 / 2021</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Zengin liman kentlerinin alınması (Sinop, Antalya), düşük gümrük tarifeleri uygulanması ve tüccarların mallarının devlet güvencesine alınması neyin göstergesidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Ticareti Geliştirme Politikası</strong></p>
                        </div>
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">I. Haçlı Seferi'nde İznik'in elden çıkması üzerine başkentin İznik'ten Konya'ya taşınması kimin döneminde gerçekleşmiştir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: I. Kılıçarslan</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">ÖSYM, mimari eserler ile beylikleri eşleştirmiştir. Divriği Ulu Camii ve Yağıbasan Medresesi hangi beyliklere aittir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Mengücekler ve Danişmentliler</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2023 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">I. Alaeddin Keykubat döneminde Alanya'nın alınıp tersane inşa edilmesi devletin hangi alanda faaliyete giriştiğini gösterir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Akdeniz'de Denizcilik</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2024 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Ülkeyi 11 oğlu arasında paylaştıran ve Miryokefalon Savaşı'nı kazanarak Anadolu'yu kesin Türk yurdu yapan lider kimdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: II. Kılıçarslan</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2025 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">İbn Batuta'nın "Türkmenlerin en ulu sultanı" olarak nitelendirdiği ve Alanya'yı fetheden sultan kimdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: I. Alaeddin Keykubad</strong></p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- DEVLETLER KÜNYESİ (FULL WIDTH) -->
            <section class="bg-white dark:bg-slate-800 p-8 md:p-12 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 mt-12">
                <h3 class="text-3xl font-black mb-8 flex items-center text-slate-900 dark:text-white">
                    <div class="bg-slate-100 dark:bg-slate-700 p-3 rounded-2xl mr-4 text-slate-600 dark:text-slate-300">
                        <i class="fas fa-monument"></i>
                    </div>
                    KÖSEDAĞ SAVAŞI SONRASI KURULAN II. TÜRK BEYLİKLERİ
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 text-sm font-medium">
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">1. Osmanoğulları</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Söğüt-Domaniç civarında kurulmuştur. Merkezi otoritesi en güçlü olan ve cihan imparatorluğuna dönüşen beyliktir.</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">2. Karamanoğulları</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Konya-Karaman'da kurulmuştur. Osmanlı'yı en çok uğraştıran beyliktir. 1277'de Türkçeyi resmî dil ilan etmişlerdir.</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">3. Karesioğulları</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Balıkesir-Çanakkale'de kurulmuştur. Donanması vardır. Osmanlı Devleti'ne katılan İLK beylik olmuştur.</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">4. Dulkadiroğulları</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Maraş'ta kurulmuştur. Osmanlı Devleti'ne katılan SON beyliktir (1515 Turnadağ Savaşı).</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">5. Hamitoğulları</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Isparta-Antalya yöresinde kurulmuştur. Osmanlı'nın para ile (satın alma yoluyla) sınırlarına kattığı beyliktir.</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">6. Germiyanoğulları</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Kütahya'da kurulmuştur. Osmanlı'ya çeyiz ve vasiyet yoluyla katılmışlardır.</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">7. Aydınoğulları</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Aydın yöresinde kurulmuştur. Güçlü bir donanma ile Ege Adaları'na seferler yapmışlardır.</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">8. Diğer Denizci Beylikler</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Menteşeoğulları (Muğla), Candaroğulları (Sinop-Kastamonu), Saruhanoğulları (Manisa) denizcilikle uğraşmıştır.</p>
                    </div>
                </div>
            </section>
"""

with open('unite2.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace main content for unite3
template = re.sub(r'<main class="flex-1 space-y-8 lg:space-y-12">.*?</main>', f'<main class="flex-1 space-y-8 lg:space-y-12">{unite3_content}\n        </main>', template, flags=re.DOTALL)

# Set correct sidebar
new_nav = generate_sidebar(3)
template = re.sub(r'<nav class="space-y-1.5 max-h-\[60vh\] overflow-y-auto pr-1.5 custom-scrollbar">.*?</nav>', new_nav, template, flags=re.DOTALL)

with open('unite3.html', 'w', encoding='utf-8') as f:
    f.write(template)

