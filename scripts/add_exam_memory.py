import re

u12_exam = """
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
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2017 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">I. TBMM'nin "olağanüstü yetkilere sahip bir meclis" olduğuna kanıt nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Yasama, yürütme ve yargı yetkisini elinde bulundurması (Güçler Birliği)</strong></p>
                        </div>
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2024 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Kastamonu İstiklal Mahkemesi'nin asker kaçaklarına ceza vermesi neye kanıttır?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: TBMM'nin yargı gücünü kullandığına</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 İptal KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">TBMM'nin kendisine karşı çıkan ayaklanmaları bastırmak için aldığı önlemler nelerdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Hıyanet-i Vataniye Kanunu ve İstiklal Mahkemeleri</strong></p>
                        </div>

                    </div>
                </div>
            </section>
"""

u13_exam = """
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
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2017 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Askerî ve siyasi konuları içeren, Sevr'i reddeden ve TBMM'yi tanıyan ilk antlaşma hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Gümrü Antlaşması</strong></p>
                        </div>
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Batı Cephesi'ne cephane taşımak için oluşturulan "İstiklal Yolu" güzergâhı neresidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: İnebolu, Kastamonu, Çankırı, Ankara</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 İptal KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Kütahya-Eskişehir Muharebeleri sonrasında ortaya çıkan gelişmeler nelerdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Sakarya'nın doğusuna çekilme ve mecliste sert eleştiriler yapılması</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2015 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Lozan'a gidecek heyete İsmet İnönü'nün başkanlık edebilmesi için istifa eden Dışişleri Bakanı kimdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Yusuf Kemal Tengirşenk</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">"Üç dört yüzyıllık hesaplaşmaların" (kapitülasyonlar vb.) çözümlenmesi olarak bahsedilen antlaşma hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Lozan Barış Antlaşması</strong></p>
                        </div>

                    </div>
                </div>
            </section>
"""

u14_exam = """
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
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2018 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Atatürk'ün "Siz orada yalnız düşmanı değil, milletin makûs talihini de yendiniz" telgrafını kime çekmiştir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: İsmet İnönü (II. İnönü Savaşı)</strong></p>
                        </div>
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2018 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Atatürk'ün bizzat yönettiği ve "Rum Sındığı" olarak adlandırdığı savaş hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Başkomutanlık Meydan Muharebesi</strong></p>
                        </div>

                        <div class="bg-red-50 hover:bg-white dark:bg-red-900/30 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-red-200 dark:border-red-800/50 backdrop-blur-sm relative lg:col-span-3">
                            <div class="absolute -top-3 -left-3 bg-red-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md flex items-center"><i class="fas fa-exclamation-circle mr-1"></i> ÖSYM NUTUK TUZAĞI</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Sorularda "Hangisi Atatürk'ün Nutuk adlı eserinde yer alır/almaz?" kalıbı sıkça kullanılır. Şıklara konulan <strong>Soyadı Kanunu, Harf İnkılabı, Serbest Cumhuriyet Fırkası</strong> gibi 1927 yılından SONRA yaşanan olaylar Nutuk'ta asla yer almaz.</p>
                        </div>

                    </div>
                </div>
            </section>
"""

u15_exam = """
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
                        
                        <div class="bg-red-50 hover:bg-white dark:bg-red-900/30 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-red-200 dark:border-red-800/50 backdrop-blur-sm relative lg:col-span-2">
                            <div class="absolute -top-3 -left-3 bg-red-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md flex items-center"><i class="fas fa-exclamation-circle mr-1"></i> İÇ POLİTİKA KRONOLOJİ TUZAĞI (2022 İPTAL KPSS)</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Çok partili hayata geçişle ilgili soruda "Serbest Cumhuriyet Fırkasının, Takrir-i Sükûn Dönemi'nde kurulduğu" şıkkı <strong>yanlış cevap (çeldirici)</strong> olarak verilmiştir. (Takrir-i Sükûn 1925-1929 yılları arasıdır, SCF ise 1930'da kurulmuştur).</p>
                        </div>
                        
                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2018 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Saltanat ve halifeliğin kaldırılmasının ortak nedeni nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Rejimin cumhuriyet olmasını (ulusal egemenliği) sağlamak</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2019 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Büyük Taarruz'un ardından gerçekleşen en büyük siyasi gelişme nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Saltanatın kaldırılması</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2021 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">Hukuk alanında yapılan Medeni Kanun gibi yeniliklerin temel amacı nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Ülkede tek hukuk sistemine geçilmesi (hukukta ikiliğin bitirilmesi)</strong></p>
                        </div>

                        <div class="bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2019 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-800 dark:text-slate-200">1923 İzmir İktisat Kongresi'nin sanayi ile ilgili en önemli kararı nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: "Ham maddesi yurt içinden temin edilen sanayi dalları kurulmalıdır"</strong></p>
                        </div>

                    </div>
                </div>
            </section>
"""

exams = {
    'unitler/unite12.html': u12_exam,
    'unitler/unite13.html': u13_exam,
    'unitler/unite14.html': u14_exam,
    'unitler/unite15.html': u15_exam
}

for filepath, exam_html in exams.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # insert before </main>
    if "SINAV HAFIZASI BÖLÜMÜ" not in content:
        content = content.replace('        </main>', f'{exam_html}\n        </main>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Exam memories added to units 12, 13, 14, 15.")
