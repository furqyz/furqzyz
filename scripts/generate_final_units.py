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
        {"title": "14. Atatürk'un Hayatı", "file": "unite14.html", "icon": "fa-user-tie"},
        {"title": "15. Atatürk Dönemi İç Politika", "file": "unite15.html", "icon": "fa-landmark-flag"},
        {"title": "16. Atatürk İlkeleri", "file": "unite16.html", "icon": "fa-scale-balanced"},
        {"title": "17. Atatürk İnkılapları", "file": "unite17.html", "icon": "fa-lightbulb"},
        {"title": "18. Atatürk Dönemi Türk Dış Politikası", "file": "unite18.html", "icon": "fa-earth-europe"},
        {"title": "19. Cumhuriyet Dönemi Kültür ve Medeniyeti", "file": "unite19.html", "icon": "fa-masks-theater"},
        {"title": "20. Çağdaş Türk ve Dünya Tarihi", "file": "unite20.html", "icon": "fa-earth-americas"},
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
    for i in range(2, 16):
        files.append((f'unitler/unite{i}.html', i))
        
    for filepath, idx in files:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            new_nav = generate_sidebar(idx)
            content = re.sub(r'<nav class="space-y-1.5 max-h-\[60vh\] overflow-y-auto pr-1.5 custom-scrollbar">.*?</nav>', new_nav, content, flags=re.DOTALL)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

# Define U16, U17, U18, U19, U20
u16 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-scale-balanced text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">16. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">ATATÜRK İLKELERİ</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Türkiye Cumhuriyeti'nin temellerini oluşturan altı temel ilkenin anahtar kelimeleri ve ilgili inkılaplarla birlikte tam analizi.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- MOR BÖLÜM -->
                <section class="category-purple note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-person-booth text-purple-600 dark:text-purple-300"></i></div>
                        Cumhuriyetçilik
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-purple-100 font-medium text-sm">
                        <p>Ulusal egemenlik, millet iradesi, seçim, meclis ve çok partili hayatı esas alır.</p>
                        <div class="bg-purple-50 dark:bg-purple-900/30 p-3 rounded-xl border border-purple-100 dark:border-purple-800/50">
                            <strong class="text-purple-800 dark:text-purple-300 block mb-1">Anahtar Kelimeler:</strong>
                            <p>Ulusal egemenlik, milli irade, seçim, meclis, parti, oy.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-3 rounded-xl">
                            <strong class="text-purple-800 dark:text-purple-300 block mb-1">İlgili İnkılaplar:</strong>
                            <p>TBMM'nin açılması, Saltanatın ve Halifeliğin kaldırılması, Kadınlara siyasi hakların verilmesi, Ordunun siyasetten ayrılması.</p>
                        </div>
                    </div>
                </section>

                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-flag text-yellow-600 dark:text-yellow-300"></i></div>
                        Milliyetçilik
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-yellow-100 font-medium text-sm">
                        <p>Ulusal bağımsızlığı, Türk kültürünü, birlik ve beraberliği esas alır. Irkçı değildir, birleştiricidir.</p>
                        <div class="bg-yellow-50 dark:bg-yellow-900/30 p-3 rounded-xl border border-yellow-100 dark:border-yellow-800/50">
                            <strong class="text-yellow-800 dark:text-yellow-300 block mb-1">Anahtar Kelimeler:</strong>
                            <p>Ulusal bağımsızlık, milli benlik, ortak dil, ortak tarih, milli bilinç.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-3 rounded-xl">
                            <strong class="text-yellow-800 dark:text-yellow-300 block mb-1">İlgili İnkılaplar:</strong>
                            <p>Türk Tarih ve Türk Dil kurumlarının açılması, <strong>Kabotaj Kanunu</strong> (denizlerin millileşmesi), Yabancı okulların MEB'e bağlanması, Merkez Bankasının kurulması, Reji İdaresinin millileştirilmesi.</p>
                        </div>
                    </div>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-users text-cyan-600 dark:text-cyan-300"></i></div>
                        Halkçılık
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-cyan-100 font-medium text-sm">
                        <p>Eşitliği, sosyal adaleti ve ayrıcalıkların reddini esas alır. Cumhuriyetçilik ve Milliyetçiliğin "doğal bir sonucudur".</p>
                        <div class="bg-cyan-50 dark:bg-cyan-900/30 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Anahtar Kelimeler:</strong>
                            <p>Eşitlik, sosyal devlet, sınıf ayrımının reddi, dayanışma, imtiyazsız toplum.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-3 rounded-xl">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">İlgili İnkılaplar:</strong>
                            <p><strong>Aşar (Öşür) vergisinin kaldırılması</strong> (köylü rahatlatıldı - en net örneğidir!), Medeni Kanun (kadın-erkek eşitliği), Soyadı Kanunu, Unvan ve lakapların kaldırılması, Millet Mekteplerinin açılması (ücretsiz eğitim).</p>
                        </div>
                    </div>
                </section>

                <!-- YEŞİL BÖLÜM -->
                <section class="category-green note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-emerald-900 dark:text-emerald-200">
                        <div class="bg-emerald-100 dark:bg-emerald-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-scale-unbalanced text-emerald-600 dark:text-emerald-300"></i></div>
                        Laiklik
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-emerald-100 font-medium text-sm">
                        <p>Din ve devlet işlerinin ayrılmasını, akılcılığı ve bilimselliği esas alır.</p>
                        <div class="bg-emerald-50 dark:bg-emerald-900/30 p-3 rounded-xl border border-emerald-200 dark:border-emerald-800/50">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-1">Anahtar Kelimeler:</strong>
                            <p>Akılcılık, bilimsellik, din ve vicdan özgürlüğü, hurafe ve dogma karşıtlığı.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-3 rounded-xl">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-1">İlgili İnkılaplar:</strong>
                            <p>Saltanat ve Halifeliğin kaldırılması, Tevhid-i Tedrisat Kanunu, Şeriye ve Evkaf Vekâletinin kaldırılması, Tekke ve zaviyelerin kapatılması, 1928'de "Devletin dini İslam'dır" maddesinin anayasadan çıkarılması.</p>
                        </div>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-industry text-orange-600 dark:text-orange-300"></i></div>
                        Devletçilik
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-orange-100 font-medium text-sm">
                        <p>İdeolojik bir tercih değil, Türkiye'nin o günkü şartlarında (1929 Krizi sonrası) özel sektörde sermaye olmaması nedeniyle <strong>"zorunluluktan"</strong> doğmuştur.</p>
                        <div class="bg-orange-50 dark:bg-orange-900/30 p-3 rounded-xl border border-orange-100 dark:border-orange-800/50">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Anahtar Kelimeler:</strong>
                            <p>Ekonomi, yatırım, banka, kalkınma planı, karma ekonomi, kamulaştırma, fabrika.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-3 rounded-xl">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">İlgili İnkılaplar:</strong>
                            <p>I. Beş Yıllık Sanayi Planı, Sümerbank, Etibank, MTA'nın kurulması, Çubuk Barajı.</p>
                        </div>
                    </div>
                </section>

                <!-- KIRMIZI BÖLÜM -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-arrows-rotate text-red-600 dark:text-red-300"></i></div>
                        İnkılapçılık
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-red-100 font-medium text-sm">
                        <p>Sürekli değişimi, yeniliği, Batılılaşmayı ve dinamizmi savunan ilkedir. Bütün inkılaplar bu ilkenin çatısı altındadır.</p>
                        <div class="bg-red-50 dark:bg-red-900/30 p-3 rounded-xl border border-red-100 dark:border-red-800/50">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Anahtar Kelimeler:</strong>
                            <p>Çağdaşlaşma, Batılılaşma, muasır medeniyet, sürekli değişim, dinamizm.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-3 rounded-xl">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">İlgili İnkılaplar:</strong>
                            <p>Takvim, saat, ölçü, tartı, rakam ve hafta tatili değişiklikleri, Harf İnkılabı, Kılık-Kıyafet Kanunu.</p>
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
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2024 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">"Türk Parasını Koruma Kanunu" doğrudan hangi ilkeyle ilişkilidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Milliyetçilik</strong></p>
                        </div>
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Atatürk'ün "Türk milleti bin yıldan fazladır bu topraklarda yaşama hakkına sahiptir... Biz kudreti ve görkemi bütün dünyada tanınan bir milletiz." sözü hangi ilkeyle ilgilidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Milliyetçilik</strong></p>
                        </div>

                        <div class="bg-red-50 hover:bg-white dark:bg-red-900/30 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-red-200 dark:border-red-800/50 backdrop-blur-sm relative md:col-span-2">
                            <div class="absolute -top-3 -left-3 bg-red-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md flex items-center"><i class="fas fa-exclamation-circle mr-1"></i> İLKE KRONOLOJİ TUZAĞI (2022 KPSS)</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Kurtuluş Savaşı'nın sonuna kadar geçen (1920-1923) sürede TBMM'nin uyguladığı ilkeler sorulmuş; *Milliyetçilik* ve *Halkçılık* kabul edilirken, <strong>Devletçilik ilkesi kabul edilmemiştir</strong> (Devletçilik 1929 Krizi'nden sonra uygulanmaya başlanmıştır).</p>
                        </div>

                    </div>
                </div>
            </section>
"""

u17 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-lightbulb text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">17. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">ATATÜRK İNKILAPLARI</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Siyasi, hukuki, eğitim, toplumsal ve ekonomik alanda Türkiye'nin çağdaşlaşma sürecindeki tüm adımlar.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- MOR BÖLÜM -->
                <section class="category-purple note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-gavel text-purple-600 dark:text-purple-300"></i></div>
                        Siyasi İnkılaplar ve Hukuk
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-purple-100 font-medium text-sm">
                        <ul class="space-y-3">
                            <li><strong class="text-purple-800 dark:text-purple-300 block">Saltanatın Kaldırılması (1 Kasım 1922):</strong> I. TBMM'nin yaptığı <strong>ilk ve tek inkılaptır</strong>. Lozan öncesi ikilik çıkmasını engellemek için yapılmıştır.</li>
                            <li><strong class="text-purple-800 dark:text-purple-300 block">Ankara'nın Başkent Olması (13 Ekim 1923):</strong> İsmet İnönü'nün yasa teklifiyle gerçekleşmiştir.</li>
                            <li><strong class="text-purple-800 dark:text-purple-300 block">Cumhuriyetin İlanı (29 Ekim 1923):</strong> Rejim ve devlet başkanlığı sorunu çözülmüş, "Kabine Sistemine" geçilmiştir.</li>
                            <li><strong class="text-purple-800 dark:text-purple-300 block">Halifeliğin Kaldırılması (3 Mart 1924):</strong> Ümmetçilik fikri tamamen bitmiştir. Aynı gün: Şeriye Vekâleti ve Erkân-ı Harbiye kaldırıldı, Tevhid-i Tedrisat kabul edildi, hanedan sürgün edildi.</li>
                        </ul>
                        
                        <div class="bg-purple-50 dark:bg-purple-900/30 p-3 rounded-xl border border-purple-100 dark:border-purple-800/50">
                            <strong class="text-purple-800 dark:text-purple-300 block mb-1">Türk Medeni Kanunu (1926):</strong>
                            <p>İsviçre'den alınmıştır. Hukukta ikilik bitmiştir.</p>
                            <div class="mt-2 bg-red-50 dark:bg-red-900/30 p-2 rounded border border-red-200 dark:border-red-800/50">
                                <strong class="text-red-700 dark:text-red-400 block mb-1 text-xs"><i class="fas fa-exclamation-triangle"></i> DİKKAT (SİYASİ HAK TUZAĞI)</strong>
                                <p class="text-xs text-red-900 dark:text-red-200">Medeni Kanun ile kadına miras, boşanma, şahitlik gibi haklar verilmiş ancak <strong>SİYASİ HAK (Seçme ve Seçilme) KESİNLİKLE YOKTUR!</strong></p>
                            </div>
                        </div>

                        <div class="bg-white/60 dark:bg-black/20 p-3 rounded-xl border border-purple-100 dark:border-purple-800/30">
                            <strong class="text-purple-800 dark:text-purple-300 block mb-1">Kadınlara Siyasi Hakların Verilmesi (BMW Şifresi):</strong>
                            <p><strong>B</strong>elediye (1930), <strong>M</strong>uhtar (1933 - İlk kadın muhtar Gül Esin), <strong>W</strong>ekil/Milletvekili (1934 - 18 kadın vekil seçildi).</p>
                        </div>
                    </div>
                </section>

                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-book-open-reader text-yellow-600 dark:text-yellow-300"></i></div>
                        Eğitim ve Kültür İnkılapları
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-yellow-100 font-medium text-sm">
                        <ul class="space-y-3">
                            <li><strong class="text-yellow-800 dark:text-yellow-300 block">Tevhid-i Tedrisat Kanunu (1924):</strong> Vasıf Çınar'ın teklifiyle kabul edilmiştir. Tüm okullar MEB'e bağlanmış, eğitimde ikilik bitmiştir.</li>
                            <li><strong class="text-yellow-800 dark:text-yellow-300 block">Harf Devrimi (1 Kasım 1928):</strong> Okuma yazma oranını artırmak için yapılmıştır. Yeni harflerle basılan ilk dergi <em>Belleten</em>, ilk gazete <em>Mardin</em> gazetesidir.</li>
                            <li><strong class="text-yellow-800 dark:text-yellow-300 block">Millet Mektepleri (1928):</strong> Yeni alfabeyi halka öğretmek için açılmıştır (Mustafa Kemal'e "Başöğretmen" unvanı verilmiştir).</li>
                            <li><strong class="text-yellow-800 dark:text-yellow-300 block">Halkevleri (1932):</strong> İnkılapları halka benimsetmek için açılmıştır. Yayın organı <strong>"Ülkü"</strong> dergisidir.</li>
                            <li><strong class="text-yellow-800 dark:text-yellow-300 block">Üniversite Reformu (1933):</strong> İsviçreli uzman <strong>Albert Malche</strong>'nin raporuyla Darülfünun kapatılmış, yerine İstanbul Üniversitesi açılmıştır.</li>
                        </ul>
                    </div>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-people-group text-cyan-600 dark:text-cyan-300"></i></div>
                        Toplumsal Alanda Yapılan İnkılaplar
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-slate-800 dark:text-cyan-100 font-medium text-sm">
                        <div class="bg-cyan-50 dark:bg-cyan-900/30 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Şapka Kanunu (1925):</strong>
                            <p>Atatürk bu kanunu Kastamonu'da tanıtmıştır.</p>
                        </div>
                        <div class="bg-cyan-50 dark:bg-cyan-900/30 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Tekke ve Zaviyelerin Kapatılması (1925):</strong>
                            <p>Şeyh Sait isyanının etkisi büyüktür. "Şeyh, derviş, mürit" gibi unvanlar yasaklanmıştır.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Batı ile Uyum İnkılapları:</strong>
                            <p>Takvim, Saat, Ölçü/Tartı ve Hafta Tatili değişikliklerinin <strong>temel amacı, uluslararası ticari ilişkileri kolaylaştırmaktır</strong>.</p>
                        </div>
                        <div class="bg-cyan-50 dark:bg-cyan-900/30 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Soyadı Kanunu (1934):</strong>
                            <p>Ağa, hafız, molla, paşa gibi ayrıcalık belirten unvanlar kaldırılarak toplumsal eşitlik sağlanmıştır.</p>
                        </div>
                    </div>
                </section>

                <!-- YEŞİL BÖLÜM -->
                <section class="category-green note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-emerald-900 dark:text-emerald-200">
                        <div class="bg-emerald-100 dark:bg-emerald-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-coins text-emerald-600 dark:text-emerald-300"></i></div>
                        Ekonomi Alanında Yapılan İnkılaplar
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-slate-800 dark:text-emerald-100 font-medium text-sm">
                        <div class="bg-emerald-50 dark:bg-emerald-900/30 p-4 rounded-xl border border-emerald-100 dark:border-emerald-800/50">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-1">İzmir İktisat Kongresi (1923):</strong>
                            <p>"Misak-ı İktisadi" (Ekonomi Andı) kabul edilmiştir. Temel hedef tam bağımsız, milli bir ekonomidir.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/30 p-4 rounded-xl border border-emerald-100 dark:border-emerald-800/50">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-1">Kabotaj Kanunu (1 Temmuz 1926):</strong>
                            <p>Türk kara sularında gemi işletme hakkı Türklere verilmiştir (Milliyetçilik).</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl border border-emerald-100 dark:border-emerald-800/50">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-1">Teşvik-i Sanayi Kanunu (1927):</strong>
                            <p>Özel sektörü teşvik için çıkarılmış ancak <strong>1929 Dünya Ekonomik Krizi</strong> ve sermaye yetersizliği yüzünden <strong>başarısız olmuştur</strong>.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/30 p-4 rounded-xl border border-emerald-100 dark:border-emerald-800/50">
                            <strong class="text-emerald-800 dark:text-emerald-300 block mb-1">I. Beş Yıllık Sanayi Planı (1933):</strong>
                            <p>Teşviki sanayi tutmayınca Devletçiliğe geçilmiş, Rusya'dan destek alınarak başarıyla uygulanmıştır.</p>
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
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2021 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Cumhuriyet Dönemi'nde hukuk alanında yapılan Medeni Kanun gibi yeniliklerin temel amacı nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Ülkede tek hukuk sistemine geçilmesi (ikiliğin bitirilmesi)</strong></p>
                        </div>
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2019 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">1923'te toplanan İzmir İktisat Kongresi'nin sanayi ile ilgili en önemli kararı nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Ham maddesi yurt içinden temin edilen sanayi dalları kurulmalıdır</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2018 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Saltanat ve halifeliğin kaldırılmasının ortak nedeni nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Rejimin cumhuriyet olmasını (ulusal egemenliği) sağlamak</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Kadınların aşağıdaki görev ve mesleklerden hangisinde diğerlerinden daha önce yer almaya başladığı sorulmuştur?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Belediye Başkanı (1930)</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2016 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Batı tiyatrosu anlayışıyla eser sergileyen "Darülbedayi"nin, Cumhuriyet Dönemi'nde dönüştüğü kurum nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: İstanbul Şehir Tiyatrosu</strong></p>
                        </div>

                    </div>
                </div>
            </section>
"""

u18 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-earth-europe text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">18. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">ATATÜRK DÖNEMİ TÜRK DIŞ POLİTİKASI</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Lozan'dan kalan sorunların çözülmesi ve yaklaşan II. Dünya Savaşı tehlikesine karşı kurulan ittifaklar dönemi.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- KIRMIZI BÖLÜM -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-file-contract text-red-600 dark:text-red-300"></i></div>
                        Lozan'dan Kalan ve Çözülen Sorunlar
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-red-100 font-medium text-sm">
                        <div class="bg-red-50 dark:bg-red-900/30 p-4 rounded-xl border border-red-100 dark:border-red-800/50">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Yabancı Okullar (1924):</strong>
                            <p>Fransa ve Papalık ile kriz yaşanmıştır. Türkiye "Bu bizim iç meselemizdir" diyerek okulları MEB'e bağlamış, dış müdahaleye izin vermemiştir.</p>
                        </div>
                        <div class="bg-red-50 dark:bg-red-900/30 p-4 rounded-xl border border-red-100 dark:border-red-800/50">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Musul (Irak Sınırı) Sorunu (1926):</strong>
                            <p>İngiltere ile yaşanmıştır. Şeyh Sait isyanı yüzünden ordu müdahale edemeyince <strong>1926 Ankara Antlaşması</strong> ile Musul, İngiliz mandasındaki Irak'a bırakılmıştır (Misakımilliden verilen 3. tavizdir).</p>
                        </div>
                        <div class="bg-red-50 dark:bg-red-900/30 p-4 rounded-xl border border-red-100 dark:border-red-800/50">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Bozkurt - Lotus Olayı (1926):</strong>
                            <p>Türk gemisi Bozkurt ile Fransız gemisi Lotus çarpışmıştır. Türkiye'yi Lahey'de Adalet Bakanı <strong>Mahmut Esat (Bozkurt)</strong> başarıyla savunmuştur.</p>
                        </div>
                        <div class="bg-red-50 dark:bg-red-900/30 p-4 rounded-xl border border-red-100 dark:border-red-800/50">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Nüfus Mübadelesi / Etabli Sorunu (1930):</strong>
                            <p>Yunanistan ile yaşanmıştır. Batı Trakya Türkleri ile İstanbul Rumları "yerleşik (etapli)" kabul edilmiş, diğerleri değiştirilmiştir. Bu olaydan sonra ilişkiler düzelmiştir.</p>
                        </div>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-shield-cat text-orange-600 dark:text-orange-300"></i></div>
                        Tehditlere Karşı Alınan Önlemler ve İttifaklar
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-orange-100 font-medium text-sm">
                        <div class="bg-orange-50 dark:bg-orange-900/30 p-4 rounded-xl border border-orange-100 dark:border-orange-800/50">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Milletler Cemiyeti'ne Giriş (1932):</strong>
                            <p>İspanya'nın daveti ve Yunanistan'ın desteği ile üye olmuştur.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl border border-orange-100 dark:border-orange-800/30">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Balkan Antantı (1934):</strong>
                            <p>İtalya ve Almanya'nın saldırganlığına karşı Batı sınırları için <strong class="bg-orange-200 dark:bg-orange-800 px-1 rounded text-orange-900 dark:text-orange-100">TAYYAR</strong> (Türkiye, Yunanistan, Yugoslavya, Romanya) arasında imzalandı. Bulgaristan ve Arnavutluk yoktur.</p>
                        </div>
                        <div class="bg-orange-50 dark:bg-orange-900/30 p-4 rounded-xl border border-orange-100 dark:border-orange-800/50">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Montrö Boğazlar Sözleşmesi (1936):</strong>
                            <p>Uluslararası komisyon kaldırılarak Boğazların yönetimi ve savunması <strong>tamamen Türkiye'ye</strong> geçmiştir.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl border border-orange-100 dark:border-orange-800/30">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Sadabat Paktı (1937):</strong>
                            <p>İtalya'nın saldırganlığına karşı Doğu sınırları için <strong class="bg-orange-200 dark:bg-orange-800 px-1 rounded text-orange-900 dark:text-orange-100">ATİ</strong> (Afganistan, Türkiye, İran, Irak) arasında imzalandı. Suriye Hatay sorunu nedeniyle katılmadı.</p>
                        </div>
                        <div class="bg-orange-50 dark:bg-orange-900/30 p-4 rounded-xl border border-orange-100 dark:border-orange-800/50">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Hatay Sorunu:</strong>
                            <p>Milletler Cemiyeti <strong>Sandler Raporu</strong>'nu hazırladı. 1938'de Hatay Cumhuriyeti kuruldu (İlk C.Başkanı <strong>Tayfur Sökmen</strong>), 1939'da anavatana katıldı. Atatürk <em>Asım Us</em> takma adıyla gazetede yazılar yazmıştır.</p>
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
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2024 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Lozan'da çözülemeyen tek sorun olan Türkiye ile İngiltere arasındaki sınır sorunu nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Irak Sınırı (Musul sorunu)</strong></p>
                        </div>
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2016 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Musul sorununun çözümü için 1924'te toplanan Haliç Konferansı'nda Türkiye'yi temsil eden devlet adamı kimdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Ali Fethi Okyar</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2021 / 2022 İptal KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Balkan Antantı'nın (1934) kurulmasındaki dış etkenler nelerdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: İtalya'nın Akdeniz'de yayılmacılığı, Almanya'nın silahlanması ve Bulgaristan'ın sınırlarını genişletme politikası</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2024 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">1930'lu yıllardan itibaren Türkiye ile Yunanistan arasında dostluk ilişkilerini başlatan gelişme nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Türk-Yunan Nüfus Mübadelesine İlişkin Sözleşme (Etapli sorununun çözülmesi)</strong></p>
                        </div>

                    </div>
                </div>
            </section>
"""

u19 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-masks-theater text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">19. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">CUMHURİYET DÖNEMİ KÜLTÜR</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Cumhuriyetin ilk yıllarında mimari, müzik, resim ve kadınların imza attığı önemli ilkler.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-palette text-cyan-600 dark:text-cyan-300"></i></div>
                        Sanat ve İlkler
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-slate-800 dark:text-cyan-100 font-medium text-sm">
                        
                        <div class="bg-cyan-50 dark:bg-cyan-900/30 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-2 text-lg">Mimari ve Heykel:</strong>
                            <ul class="space-y-2">
                                <li>İlk kadın heykelini yaptıran padişah <strong>Abdülaziz'dir</strong>.</li>
                                <li>Ankara Zafer ve Samsun Atatürk Anıtı'nı <strong>Heinrich Krippel</strong>; Taksim Cumhuriyet Anıtı'nı <strong>Pietro Canonica</strong> yapmıştır.</li>
                                <li>Anıtkabir'in mimarları <strong>Emin Halid Onat ve Orhan Arda</strong>'dır.</li>
                            </ul>
                        </div>
                        
                        <div class="bg-cyan-50 dark:bg-cyan-900/30 p-4 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-2 text-lg">Müzik ve Resim:</strong>
                            <ul class="space-y-2">
                                <li>10. Yıl Marşı: <strong>Cemal Reşit Rey</strong>.</li>
                                <li>İstiklal Marşı bestesi: <strong>Osman Zeki Üngör</strong>.</li>
                                <li>İlk Türk operası "Özsoy": <strong>Adnan Saygun</strong> (Bu gruba <em>Türk Beşleri</em> denir).</li>
                                <li>"Zeybekler Tablosu" ve "Hatay'ın Anavatana Özlemi" tabloları <strong>İbrahim Çallı</strong>'ya aittir.</li>
                            </ul>
                        </div>

                        <div class="bg-white/60 dark:bg-black/20 p-4 rounded-xl border border-cyan-200 dark:border-cyan-800/50 md:col-span-2">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-2 text-lg">Kadınların İlkleri:</strong>
                            <div class="flex flex-wrap gap-2">
                                <span class="bg-cyan-100 dark:bg-cyan-900/50 px-2.5 py-1 rounded-lg">Tiyatrocu: <strong>Afife Jale</strong></span>
                                <span class="bg-cyan-100 dark:bg-cyan-900/50 px-2.5 py-1 rounded-lg">Savaş Pilotu: <strong>Sabiha Gökçen</strong></span>
                                <span class="bg-cyan-100 dark:bg-cyan-900/50 px-2.5 py-1 rounded-lg">Muhtar: <strong>Gül Esin</strong></span>
                                <span class="bg-cyan-100 dark:bg-cyan-900/50 px-2.5 py-1 rounded-lg">Hekim: <strong>Safiye Ali</strong></span>
                                <span class="bg-cyan-100 dark:bg-cyan-900/50 px-2.5 py-1 rounded-lg">Dünya Güzeli: <strong>Keriman Halis</strong></span>
                            </div>
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
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2018 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Atatürk Dönemi'nde açılan kurumlardan biri <em>değildir</em> diye sorulmuştur.<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Sanayi-i Nefise Mektebi</strong> (Bu kurum 1883'te Osman Hamdi Bey tarafından Osmanlı döneminde açılmış, Atatürk döneminde Güzel Sanatlar Akademisi'ne dönüştürülmüştür).</p>
                        </div>
                        
                        <div class="bg-red-50 hover:bg-white dark:bg-red-900/30 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-red-200 dark:border-red-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-red-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md flex items-center"><i class="fas fa-exclamation-circle mr-1"></i> GENEL ÖSYM TUZAĞI</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">"Ülkemizde ilkleri gerçekleştiren kadınlar" daima soru potansiyeli taşır. Sadiye Hanım'ın ilk kadın belediye başkanı, Gül Esin'in ilk kadın muhtar, Sabiha Gökçen'in ilk kadın savaş pilotu olduğu eşleştirmeleri şıklarda çok sık kullanılır.</p>
                        </div>

                    </div>
                </div>
            </section>
"""

u20 = """
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-earth-americas text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">KPSS Tarih Hazırlık</div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">20. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">ÇAĞDAŞ TÜRK VE DÜNYA TARİHİ</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">ÖSYM'nin son yıllarda en çok soru seçtiği güncel olaylar zinciri: Dünya Savaşları, Soğuk Savaş ve Küreselleşen Dünya.</p>
                </div>
            </header>

            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                <!-- KIRMIZI BÖLÜM -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-biohazard text-red-600 dark:text-red-300"></i></div>
                        İki Savaş Arası Dönem (1918 - 1939)
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-red-100 font-medium text-sm">
                        <div class="bg-red-50 dark:bg-red-900/30 p-3 rounded-xl border border-red-100 dark:border-red-800/50">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">SSCB ve Türkistan:</strong>
                            <p>Lenin 1917 Bolşevik İhtilali'ni yaptı. Ekonomiyi düzeltmek için NEP'i ilan etti. Türkistan'da Ruslara karşı <strong>"Basmacı Hareketi"</strong> başladı (Korbaşı Ergaş, Zeki Velidi Togan ve şehit düşen <strong>Enver Paşa</strong> önderlik etti).</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-3 rounded-xl">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Japonya (Meiji Restorasyonu):</strong>
                            <p>Mutsuhito önderliğinde "Güçlü ordu, zengin ülke" parolasıyla yapıldı. <strong class="text-red-600 dark:text-red-400 block mt-1"><i class="fas fa-exclamation-triangle"></i> DİKKAT TUZAK!</strong> Meiji restorasyonunda Latin harflerine geçiş veya kılık-kıyafet devrimi KESİNLİKLE YOKTUR!</p>
                        </div>
                        <div class="bg-red-50 dark:bg-red-900/30 p-3 rounded-xl border border-red-100 dark:border-red-800/50">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">1929 Dünya Ekonomik Krizi (Kara Perşembe):</strong>
                            <p>ABD borsası çöktü. Edebiyattaki yansıması John Steinbeck'in <strong>"Gazap Üzümleri"</strong> eseridir. Türkiye "Kliring Sistemi"ni ve Milli İktisat ve Tasarruf Cemiyeti'ni kurarak <strong>Devletçilik</strong> ilkesine geçti.</p>
                        </div>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-fighter-jet text-orange-600 dark:text-orange-300"></i></div>
                        II. Dünya Savaşı (1939 - 1945)
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-orange-100 font-medium text-sm">
                        <p>ABD, Japonya'nın "Pearl Harbor" baskını üzerine savaşa girdi. Japonya'ya atom bombası atılmasıyla bitti.</p>
                        <div class="bg-orange-50 dark:bg-orange-900/30 p-3 rounded-xl border border-orange-100 dark:border-orange-800/50">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Türkiye'nin Durumu (İnönü Dönemi):</strong>
                            <p>"Aktif Tarafsızlık" izlenmiştir. Alman tehdidine karşı "Çakmak Hattı" kuruldu. Türkiye BM kurucu üyesi olabilmek için kâğıt üzerinde Almanya ve Japonya'ya savaş ilan etmiştir.</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-3 rounded-xl">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-1">Savaş Yıllarında İç Politika:</strong>
                            <p>Ekonomik sıkıntılara karşı <strong>Milli Korunma Kanunu</strong>, Varlık Vergisi ve Toprak Mahsulleri Vergisi çıkarıldı. 1940'ta köyleri kalkındırmak için <strong>Köy Enstitüleri</strong> (Hasan Ali Yücel ve İsmail Hakkı Tonguç) açıldı.</p>
                        </div>
                    </div>
                </section>

                <!-- MOR BÖLÜM -->
                <section class="category-purple note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-snowflake text-purple-600 dark:text-purple-300"></i></div>
                        Soğuk Savaş Dönemi (1947 - 1990)
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-purple-100 font-medium text-sm">
                        <div class="flex gap-2">
                            <div class="bg-blue-50 dark:bg-blue-900/20 p-3 rounded-xl flex-1 border border-blue-100 dark:border-blue-800/30">
                                <strong class="text-blue-800 dark:text-blue-300 block mb-1">ABD (Batı Bloku):</strong>
                                <p>Truman Doktrini, Marshall Planı, <strong>NATO</strong></p>
                            </div>
                            <div class="bg-red-50 dark:bg-red-900/20 p-3 rounded-xl flex-1 border border-red-100 dark:border-red-800/30">
                                <strong class="text-red-800 dark:text-red-300 block mb-1">SSCB (Doğu Bloku):</strong>
                                <p>Cominform, Comecon, <strong>Varşova Paktı</strong></p>
                            </div>
                        </div>
                        <div class="bg-purple-50 dark:bg-purple-900/30 p-3 rounded-xl border border-purple-100 dark:border-purple-800/50">
                            <strong class="text-purple-800 dark:text-purple-300 block mb-1">Türkiye'nin NATO'ya Girişi:</strong>
                            <p>ABD desteğini almak ve NATO'ya girebilmek için 1950'de <strong>Kore Savaşı'na asker göndermiştir</strong> (NATO'ya 1952'de kabul edildi).</p>
                        </div>
                        <div class="bg-white/60 dark:bg-black/20 p-3 rounded-xl">
                            <strong class="text-purple-800 dark:text-purple-300 block mb-1">Demokrat Parti Dönemi (1950 - 1960):</strong>
                            <p>Celal Bayar Cumhurbaşkanı, Adnan Menderes Başbakan olmuştur. Ezan tekrar Arapça okunmaya başlanmış, Atatürk'ü Koruma Kanunu çıkarılmıştır. ODTÜ ve Atatürk Üniversitesi açılmıştır.</p>
                        </div>
                    </div>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-handshake-angle text-cyan-600 dark:text-cyan-300"></i></div>
                        Yumuşama (Detente) Dönemi ve Krizler
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-cyan-100 font-medium text-sm">
                        <ul class="space-y-3">
                            <li><strong class="text-cyan-800 dark:text-cyan-300 block">Küba Füze Krizi (1962):</strong> SSCB'nin Küba'ya, ABD'nin de Türkiye'ye (Jüpiter füzeleri) füze yerleştirmesiyle çıkan Nükleer savaşın eşiğinden dönülen krizdir.</li>
                            <li><strong class="text-cyan-800 dark:text-cyan-300 block">Vietnam Savaşı:</strong> Efsanevi boksör <strong>Muhammed Ali</strong> "Vietnamlılar bana hiçbir kötülük yapmadılar" diyerek askere gitmeyi reddetmiştir.</li>
                            <li><strong class="text-cyan-800 dark:text-cyan-300 block">Kıbrıs Sorunu:</strong> Rumların EOKA terör örgütüne karşı Türkler TMT'yi kurmuştur. Türkiye müdahale etmek istemiş ancak ABD'den gelen <strong>"Johnson Mektubu"</strong> ile engellenmiştir. Sonunda <strong>1974 Kıbrıs Barış Harekâtı</strong> "Ayşe tatile çıksın" parolasıyla yapılmıştır.</li>
                            <li><strong class="text-cyan-800 dark:text-cyan-300 block">Ermeni Terörü (ASALA):</strong> Türk diplomatlarına suikastlar düzenleyen örgüttür.</li>
                        </ul>
                    </div>
                </section>
                
                <!-- YEŞİL BÖLÜM -->
                <section class="category-green note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-emerald-900 dark:text-emerald-200">
                        <div class="bg-emerald-100 dark:bg-emerald-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-network-wired text-emerald-600 dark:text-emerald-300"></i></div>
                        Küreselleşen Dünya (1990 - 2026)
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-emerald-100 font-medium text-sm">
                        <ul class="space-y-3">
                            <li><strong class="text-emerald-800 dark:text-emerald-300 block">SSCB'nin Dağılması:</strong> 1991'de Orta Asya Türk Cumhuriyetleri bağımsız olmuştur. Bu ülkelerle iş birliği için <strong>TİKA</strong> kurulmuştur.</li>
                            <li><strong class="text-emerald-800 dark:text-emerald-300 block">Bosna Savaşı:</strong> Srebrenitsa Katliamı. Bosna direnişinin lideri "Bilge Kral" lakaplı <strong>Aliya İzzetbegoviç</strong>'tir. Savaş 1995 Dayton Antlaşması ile bitmiştir.</li>
                            <li><strong class="text-emerald-800 dark:text-emerald-300 block">Avrupa Birliği (AB) Süreci:</strong> Türkiye 1999 Helsinki Zirvesi'nde resmen "Aday Ülke" statüsü almıştır.</li>
                        </ul>
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
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2024 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Soğuk Savaş Dönemi'ni başlatan gelişme nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: İkinci Dünya Savaşı'nın sona ermesi</strong></p>
                        </div>
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2023 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">NATO'nun 1952'de Türkiye'yi kabul etmesinde etkili olan olay nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Türkiye'nin Kore Savaşı'na asker göndermesi</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Demokrat Parti'nin kurulmasına giden süreçte, CHP grubuna verilen önerge nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Dörtlü Takrir</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">ABD Başkanı Johnson'ın 1964'te İsmet İnönü'ye yazdığı mektubun amacı nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Kıbrıs Sorunu'na Türkiye'nin müdahalesini engellemek</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">ABD'nin 1975-1978 yılları arasında Türkiye'ye silah ambargosu uygulamasının sebebi nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Kıbrıs Barış Harekâtı</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2019 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Demokrat Parti Dönemi'nde kurulan yükseköğretim kurumu nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: ODTÜ</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2019 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">SSCB'nin ekonomik alanda Batı Blokuna karşı kurduğu birlik nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: COMECON</strong></p>
                        </div>

                    </div>
                </div>
            </section>
"""

create_unit_file(16, u16)
create_unit_file(17, u17)
create_unit_file(18, u18)
create_unit_file(19, u19)
create_unit_file(20, u20)

update_existing_sidebars()

print("Units 16-20 generated successfully. Final 20 units completed.")
