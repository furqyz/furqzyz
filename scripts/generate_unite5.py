import re

def generate_sidebar(active_index):
    items = [
        {"title": "1. İslamiyet Öncesi Türk Tarihi", "file": "index.html", "icon": "fa-landmark"},
        {"title": "2. İlk Türk İslam Devletleri", "file": "unite2.html", "icon": "fa-mosque"},
        {"title": "3. Anadolu (Türkiye) Selçuklu Devleti", "file": "unite3.html", "icon": "fa-chess-knight"},
        {"title": "4. Osmanlı Devleti Kültür ve Medeniyeti", "file": "unite4.html", "icon": "fa-landmark-dome"},
        {"title": "5. Osmanlı Devleti Kuruluş Dönemi (1299 - 1453)", "file": "unite5.html", "icon": "fa-campground"},
    ]
    
    upcoming = [
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
update_file_sidebar('unite4.html', 4)

unite5_content = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-campground text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">
                        KPSS Tarih Hazırlık
                    </div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">5. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">OSMANLI DEVLETİ KURULUŞ DÖNEMİ (1299 - 1453)</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Bu ünitede Osmanlı Devleti'nin doğuşu, beylikten devlete geçiş süreci, Balkanlar'daki ilk fetihleri ve iskan ile istimalet politikaları incelenmektedir.</p>
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
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>İlk vergi (Baç), ilk kadı ataması (Dursun Fakih), ilk bakır para (Mangır) ve ilk tımar dağıtımı <strong class="text-purple-700 dark:text-purple-400">Osman Bey</strong> dönemindedir.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>İlk saray (Bursa Sarayı), ilk medrese (İznik), ilk müderris (Davud-u Kayseri), ilk düzenli ordu (Yaya ve Müsellem), ilk gümüş para (Akçe) ve ilk Divan teşkilatı <strong class="text-purple-700 dark:text-purple-400">Orhan Bey</strong> döneminde kurulmuştur.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı'nın Rumeli'de aldığı ilk toprak parçası, Bizans'taki taht kavgalarında Kantakuzen'e yardım edilmesi karşılığı alınan <strong class="text-purple-700 dark:text-purple-400">Çimpe Kalesi'dir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Devşirme sisteminin temeli olan "Pençik" sistemini hayata geçiren, ilk defa maliye teşkilatını ve Kapıkulu Ocağı'nı kuran padişah <strong class="text-purple-700 dark:text-purple-400">I. Murat'tır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı tarihinde savaş meydanında şehit düşen ilk ve tek padişah <strong class="text-purple-700 dark:text-purple-400">I. Murat'tır</strong> (I. Kosova Savaşı). Top ilk defa bu savaşta (korkutma amaçlı) kullanılmıştır.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>İstanbul'u kuşatan ilk Osmanlı padişahı <strong class="text-purple-700 dark:text-purple-400">Yıldırım Bayezid'dir</strong> (I. Bayezid). Kuşatmaya yardımcı olması için Anadolu Hisarı'nı (Güzelcehisar) yaptırmıştır.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Kuruluş dönemindeki ilk dinî ve sosyal nitelikli toplumsal ayaklanma I. Mehmet (Çelebi) döneminde çıkan <strong class="text-purple-700 dark:text-purple-400">Şeyh Bedrettin isyanıdır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Enderun mektebi, ilk defa devlet adamı yetiştirmek için <strong class="text-purple-700 dark:text-purple-400">II. Murat</strong> döneminde Edirne Sarayı'nda açılmıştır.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Kendi isteğiyle tahttan inen ilk padişah <strong class="text-purple-700 dark:text-purple-400">II. Murat'tır</strong>.</span></li>
                    </ul>
                </section>

                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-user-crown text-yellow-600 dark:text-yellow-300"></i>
                        </div>
                        Önemli Şahsiyetler ve Eserler
                    </h3>
                    <ul class="space-y-4 text-slate-800 dark:text-yellow-100 font-medium">
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Yahşi Fakih:</strong> Osmanlı hakkında bilgi veren "Yahşi Fakih Menakıbnamesi"nin yazarıdır (Ancak bu eser günümüze ulaşmamıştır).</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Ahmedi:</strong> Günümüzde elimizde olan ve Osmanlı Devleti'nin kuruluşu ile ilgili bilgi veren kaynaklardan en eskisi olan "İskendername" eserinin yazarıdır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Süleyman Paşa:</strong> Rumeli'ye geçişte çok önemli rol oynayan ve tarihe "Gelibolu Fatihi" olarak geçen Orhan Bey'in oğludur.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Hacı İlbey:</strong> Sırpsındığı Savaşı'nda gece baskınıyla Haçlı ordusunu mağlup eden ünlü Osmanlı komutanıdır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Yıldırım Bayezid (I. Bayezid):</strong> Niğbolu zaferinden sonra Abbasi Halifesi tarafından kendisine "Sultan-ı İklim-i Rum" (Anadolu'nun Sultanı) unvanı verilen padişahtır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">I. Mehmet (Çelebi):</strong> Ankara Savaşı sonrası yaşanan 11 yıllık Fetret Devri'ne son vererek devletin dağılmasını önlemiş ve "Osmanlı'nın İkinci Kurucusu" unvanını almıştır.</li>
                    </ul>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-khanda text-cyan-600 dark:text-cyan-300"></i>
                        </div>
                        Kavramlar, Politikalar ve Savaşlar
                    </h3>
                    <div class="space-y-6 text-slate-800 dark:text-cyan-100 font-medium">
                        
                        <div class="bg-cyan-50/50 dark:bg-cyan-900/20 p-4 rounded-2xl">
                            <strong class="text-cyan-800 dark:text-cyan-300 text-lg block mb-2"><i class="fas fa-shield-alt mr-2"></i>Savaş Şifresi: <span class="bg-cyan-200 dark:bg-cyan-800 px-2 py-0.5 rounded text-cyan-900 dark:text-cyan-100">SINAV II</span></strong>
                            <p class="text-sm">Kuruluş dönemi Osmanlı-Haçlı Savaşları kronolojik olarak Sırpsındığı, I. Kosova, Niğbolu, (A harfi Ankara Savaşıdır ancak Haçlılarla değil Timur iledir!), Varna, II. Kosova şeklinde kodlanır.</p>
                        </div>

                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-4">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-3"><i class="fas fa-crosshairs mr-2"></i>Önemli Olaylar ve Savaşlar</p>
                            <div class="flex flex-col gap-2 text-sm">
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Sazlıdere Savaşı (1363):</strong> I. Murat döneminde Edirne'nin fethedildiği ve başkentin Edirne'ye taşındığı savaştır.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Çalı Bey Savaşı (1416):</strong> I. Mehmet döneminde Venedik ile yapılan ilk deniz savaşıdır. Osmanlı donanması henüz yetersiz olduğu için savaş kaybedilmiştir.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Düzmece Mustafa İsyanı:</strong> I. Mehmet döneminde başlayan ve II. Murat döneminde de devam eden, Timur'un kışkırtmasıyla ortaya çıkan saltanat (taht) kavgasıdır.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Ploşnik Bozgunu (1387):</strong> I. Murat döneminde Osmanlı öncü birliğinin Sırplar tarafından pusuya düşürülüp bozguna uğratıldığı olaydır.
                                </div>
                            </div>
                        </div>

                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-4">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-3"><i class="fas fa-globe-europe mr-2"></i>Devlet Politikaları</p>
                            <div class="grid grid-cols-1 gap-2 text-sm">
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">İskân Politikası:</strong> Fethedilen bölgelerin Türkleşmesini ve İslamlaşmasını sağlayarak egemenliği kalıcı hâle getirmek için uygulanan "şenlendirme / yerleştirme" politikasıdır.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">İstimalet Politikası:</strong> Fethedilen bölgelerdeki gayrimüslim halka hoşgörü, din ve vicdan hürriyeti tanıyarak adaletle yaklaşma politikasıdır.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Müdara:</strong> Kuruluş yıllarında Bizans tekfurlarına karşı uygulanan, "görünüşte dostça geçinme / idare etme" politikasıdır.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Kılıç Hakkı:</strong> Fethedilen bölgenin yönetiminin, fethi özendirmek amacıyla zaman zaman fetheden komutanlara dirlik olarak verilmesidir.
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
                        <p class="mb-2"><strong class="text-emerald-800 dark:text-emerald-300">Edirne - Segedin Antlaşması (1444):</strong></p>
                        <p class="text-sm">Osmanlı Devleti (II. Murat) ile Macarlar arasında imzalanmıştır. İki tarafın 10 yıl savaşmayacağı karara bağlanmıştır. Bu antlaşma, Osmanlı'nın Balkanlarda imzaladığı ilk büyük ve olumsuz şartlar içeren barış antlaşmasıdır.</p>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-puzzle-piece text-orange-600 dark:text-orange-300"></i>
                        </div>
                        Beyliklerin Alınması ve Gruplar
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-orange-100 font-medium">
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Karesioğulları:</strong>
                            <p class="text-sm">Balıkesir ve Çanakkale çevresinde Orhan Bey döneminde alınmıştır. Osmanlı'ya katılan ilk beyliktir. Bu sayede Osmanlı ilk kez donanma gücüne sahip olmuş, Rumeli'ye geçiş kolaylaşmıştır.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Germiyanoğulları ve Hamitoğulları:</strong>
                            <p class="text-sm">I. Murat döneminde Germiyanoğullarından "çeyiz ve vasiyet" yoluyla, Hamitoğullarından ise "para (satın alma)" yoluyla toprak sınırları genişletilmiştir.</p>
                        </div>
                        <div class="border-l-4 border-orange-400 pl-4 py-2 mt-4 bg-orange-50/50 dark:bg-orange-900/20 rounded-r-xl">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Kuruluşa Destek Verenler:</strong>
                            <p class="text-sm">Gaziyan-ı Rum (Anadolu Gazileri), Abdalan-ı Rum (Dervişler), Bacıyan-ı Rum (Anadolu Kadınları) ve Ahiyân-ı Rum (Ahiler) gibi zümreler devlete büyük destek sağlamıştır.</p>
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
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Balkanların Kesin Türk Yurdu Olması:</strong>
                            <p class="text-sm">II. Murat dönemindeki II. Kosova Savaşı zaferiyle Balkanlar kesin olarak Türk yurdu hâline gelmiştir. Bu durum, Anadolu'yu kesin Türk yurdu yapan Miryokefalon Savaşı ile aynı özelliği gösterir.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Fetret Devri'nde Toprak Kaybedilmemesi:</strong>
                            <p class="text-sm">1402 Ankara Savaşı'ndan sonraki Fetret Devri'nde Anadolu'da beylikler yeniden kurulmuş ancak Balkanlarda büyük bir isyan/toprak kaybı yaşanmamıştır. Bunun temel nedeni İstimalet ve İskân politikalarıdır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Ankara Savaşı'nın Doğurduğu Kriz:</strong>
                            <p class="text-sm">Timur ile yapılan Ankara Savaşı (1402) kaybedilince İstanbul'un fethi 50 yıl gecikmiş, Anadolu tahrip edilmiş ve Türk siyasi birliği bozulmuştur.</p>
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
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Fethi özendirmek için fethedilen bölgenin yönetiminin fetheden komutanlara bırakılması politikasına ne denir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Kılıç Hakkı</strong></p>
                        </div>
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2018 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Balkanlardaki ahalinin Osmanlı yönetimini kabullenmesinde hoşgörü etkilidir. Ancak şıklardaki yanlış/çeldirici ifade hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Gayrimüslimlerin avarızdan muaf tutulması (Gayrimüslimler de avarız öder)</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Mihaloğulları ve Evrenosoğulları gibi uç beylerinin sisteme dahil edilmesi ve sınırlarının genişletilmesi neyin göstergesidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Devletin merkezî yapısının güçlendirilmeye çalışıldığı</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Edirne ve Filibe'nin alınması sonucu Macar Kralı Layoş öncülüğünde kurulan Haçlı birliğinin bozguna uğratıldığı savaş hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Sırpsındığı Savaşı (1364)</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2023 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">1396 yılında Niğbolu Zaferi dolayısıyla Abbasi Halifesi tarafından "Sultan-ı İklim-i Rum" unvanı verilen padişah kimdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Yıldırım Bayezid</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2024 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Yıldırım Bayezid'in Anadolu beyliklerinin isyanı üzerine giderek onları Osmanlı toprağı hâline getirmesi ve siyasi birliği sağlamasının sonuçlarından BİRİ DEĞİLDİR çeldiricisi nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Rumeli'de toprak kayıplarının yaşanması (Toprak kaybı yaşanmamıştır)</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2025 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Devletin göçe tabi tuttuğu ailelere arazi tahsis etmesi ve vergi almaması (İskân Esasları) uygulamasının temel amacı nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Fethedilen yerde kalıcı hâle gelmek</strong></p>
                        </div>
                    </div>
                </div>
            </section>
"""

with open('unite4.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace main content for unite5
template = re.sub(r'<main class="flex-1 space-y-8 lg:space-y-12">.*?</main>', f'<main class="flex-1 space-y-8 lg:space-y-12">{unite5_content}\n        </main>', template, flags=re.DOTALL)

# Remove the ÖSYM Kelime Tuzağı from the template
template = re.sub(r'<!-- ÖSYM KELİME TUZAĞI \(Geniş Kart\) -->.*?</div>\s*</div>', '', template, flags=re.DOTALL)

with open('unite5.html', 'w', encoding='utf-8') as f:
    f.write(template)
    
update_file_sidebar('unite5.html', 5)
