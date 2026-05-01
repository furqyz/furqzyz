import re

# FIX UNITE2.HTML
with open('unite2.html', 'r', encoding='utf-8') as f:
    unite2_content = f.read()

# Replace the purple block in unite2
unite2_purple_old = """                    <ul class="space-y-4 text-slate-800 dark:text-purple-100 font-medium">
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Orta Asya'da kurulan ilk Müslüman Türk devleti <strong class="text-purple-700 dark:text-purple-400">Karahanlılardır</strong>.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Türk-İslam tarihinde ilk medreseyi (Semerkant Medresesi) açan, ilk burslu öğrencilik sistemini başlatan ve ilk posta teşkilatını kuran devlet <strong class="text-purple-700 dark:text-purple-400">Karahanlılardır</strong>.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Dünya tarihinde "Sultan" unvanını kullanan ilk hükümdar <strong class="text-purple-700 dark:text-purple-400">Gazneli Mahmut'tur</strong>.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Mısır'da kurulan ilk Türk-İslam devleti <strong class="text-purple-700 dark:text-purple-400">Tolunoğulları'dır</strong>. Hicaz (Mekke-Medine) bölgesine egemen olan ilk devlet ise <strong class="text-purple-700 dark:text-purple-400">İhşidilerdir (Akşitler)</strong>.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Türk tarihinde orduda esir alınan veya satın alınan gençlerin asker/yönetici olarak yetiştirildiği "Gulam Sistemini" ilk uygulayan devlet <strong class="text-purple-700 dark:text-purple-400">Karahanlılardır</strong>.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Tarihte yenilmez sanılan Moğolları durduran ve mağlup eden ilk devlet <strong class="text-purple-700 dark:text-purple-400">Memlüklerdir</strong> (Ayn Calud ve Elbistan Savaşları).</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Türk tasavvuf tarihinin ilk edebi eseri Hoca Ahmet Yesevi'nin yazdığı <strong class="text-purple-700 dark:text-purple-400">Divan-ı Hikmet'tir</strong>.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Malazgirt'ten sonra Anadolu'da kurulan ilk Türk-İslam devleti <strong class="text-purple-700 dark:text-purple-400">Saltuklulardır</strong>. Anadolu'da yapılan ilk medrese ise <strong class="text-purple-700 dark:text-purple-400">Danişmentlilere</strong> aittir (Yağıbasan Medresesi).</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Tarihteki ilk Türk denizcisi <strong class="text-purple-700 dark:text-purple-400">Çaka Bey'dir</strong>.</li>"""

unite2_purple_new = """                    <ul class="space-y-4 text-slate-800 dark:text-purple-100 font-medium">
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Orta Asya'da kurulan ilk Müslüman Türk devleti <strong class="text-purple-700 dark:text-purple-400">Karahanlılardır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Türk-İslam tarihinde ilk medreseyi (Semerkant Medresesi) açan, ilk burslu öğrencilik sistemini başlatan ve ilk posta teşkilatını kuran devlet <strong class="text-purple-700 dark:text-purple-400">Karahanlılardır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Dünya tarihinde "Sultan" unvanını kullanan ilk hükümdar <strong class="text-purple-700 dark:text-purple-400">Gazneli Mahmut'tur</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Mısır'da kurulan ilk Türk-İslam devleti <strong class="text-purple-700 dark:text-purple-400">Tolunoğulları'dır</strong>. Hicaz (Mekke-Medine) bölgesine egemen olan ilk devlet ise <strong class="text-purple-700 dark:text-purple-400">İhşidilerdir (Akşitler)</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Türk tarihinde orduda esir alınan veya satın alınan gençlerin asker/yönetici olarak yetiştirildiği "Gulam Sistemini" ilk uygulayan devlet <strong class="text-purple-700 dark:text-purple-400">Karahanlılardır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Tarihte yenilmez sanılan Moğolları durduran ve mağlup eden ilk devlet <strong class="text-purple-700 dark:text-purple-400">Memlüklerdir</strong> (Ayn Calud ve Elbistan Savaşları).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Türk tasavvuf tarihinin ilk edebi eseri Hoca Ahmet Yesevi'nin yazdığı <strong class="text-purple-700 dark:text-purple-400">Divan-ı Hikmet'tir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Malazgirt'ten sonra Anadolu'da kurulan ilk Türk-İslam devleti <strong class="text-purple-700 dark:text-purple-400">Saltuklulardır</strong>. Anadolu'da yapılan ilk medrese ise <strong class="text-purple-700 dark:text-purple-400">Danişmentlilere</strong> aittir (Yağıbasan Medresesi).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Tarihteki ilk Türk denizcisi <strong class="text-purple-700 dark:text-purple-400">Çaka Bey'dir</strong>.</span></li>"""

unite2_content = unite2_content.replace(unite2_purple_old, unite2_purple_new)

with open('unite2.html', 'w', encoding='utf-8') as f:
    f.write(unite2_content)


# FIX INDEX.HTML
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

index_purple_old = """                    <ul class="space-y-4 text-slate-800 dark:text-purple-100 font-medium">
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> "Türk" adı ilk defa Çin, "Türkiye" adı Bizans kaynaklarında geçmiştir.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> İlk Türk boyu İskitler, ilk teşkilatlı devlet Asya Hun'dur.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Onlu Sistem'i bulan ve Türkleri tek bayrakta toplayan Mete Han'dır.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Türk adıyla kurulan ilk devlet I. Göktürk Devleti'dir.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Avrupa'da kurulan ilk Türk devleti Avrupa Hun Devleti'dir.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> İlk Türkoloji Enstitüsü Macarlar tarafından kuruldu.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Orduda ücretli asker alan ve Museviliği kabul eden Hazarlardır.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> İslamiyet'i kabul eden ilk Türk devleti İtil Bulgarlarıdır (Almış Han). İlk Türk boyu ise Karluklardır.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Kendi adına para bastıran ilk Türk hükümdarı Baga Tarkan'dır.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Yerleşik yaşam, minyatür, fresko ve matbaa: Uygurlar.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> İlk siyasetname Orhun Abideleri, ilk yazılı eser Yenisey Kitabeleri'dir.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> İlk tarihçi ve yazar Vezir Tonyukuk'tur.</li>
                    </ul>"""

index_purple_new = """                    <ul class="space-y-4 text-slate-800 dark:text-purple-100 font-medium">
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>"Türk" adı ilk defa <strong class="text-purple-700 dark:text-purple-400">Çin</strong>, "Türkiye" adı <strong class="text-purple-700 dark:text-purple-400">Bizans</strong> kaynaklarında geçmiştir.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>İlk Türk boyu <strong class="text-purple-700 dark:text-purple-400">İskitler</strong>, ilk teşkilatlı devlet <strong class="text-purple-700 dark:text-purple-400">Asya Hun'dur</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Onlu Sistem'i bulan ve Türkleri tek bayrakta toplayan <strong class="text-purple-700 dark:text-purple-400">Mete Han'dır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Türk adıyla kurulan ilk devlet <strong class="text-purple-700 dark:text-purple-400">I. Göktürk Devleti'dir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Avrupa'da kurulan ilk Türk devleti <strong class="text-purple-700 dark:text-purple-400">Avrupa Hun Devleti'dir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>İlk Türkoloji Enstitüsü <strong class="text-purple-700 dark:text-purple-400">Macarlar</strong> tarafından kuruldu.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Orduda ücretli asker alan ve Museviliği kabul eden <strong class="text-purple-700 dark:text-purple-400">Hazarlardır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>İslamiyet'i kabul eden ilk Türk devleti <strong class="text-purple-700 dark:text-purple-400">İtil Bulgarlarıdır</strong> (Almış Han). İlk Türk boyu ise <strong class="text-purple-700 dark:text-purple-400">Karluklardır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Kendi adına para bastıran ilk Türk hükümdarı <strong class="text-purple-700 dark:text-purple-400">Baga Tarkan'dır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Yerleşik yaşam, minyatür, fresko ve matbaa öncüleri <strong class="text-purple-700 dark:text-purple-400">Uygurlardır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>İlk siyasetname <strong class="text-purple-700 dark:text-purple-400">Orhun Abideleri</strong>, ilk yazılı eser <strong class="text-purple-700 dark:text-purple-400">Yenisey Kitabeleri'dir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>İlk tarihçi ve yazar Vezir <strong class="text-purple-700 dark:text-purple-400">Tonyukuk'tur</strong>.</span></li>
                    </ul>"""

index_content = index_content.replace(index_purple_old, index_purple_new)

index_exam_old = """                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        <!-- Yıllar Kartları -->
                        <div class="bg-white/10 hover:bg-white/20 transition-colors p-5 rounded-2xl border border-white/20 backdrop-blur-sm">
                            <div class="inline-block bg-yellow-400 text-indigo-900 font-black text-xs px-2 py-1 rounded mb-2">2015 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed">Demir madeninin bulunduğu dağı eriterek çıkış destanı: <strong class="text-white">Ergenekon (Göktürkler)</strong>.</p>
                        </div>
                        <div class="bg-white/10 hover:bg-white/20 transition-colors p-5 rounded-2xl border border-white/20 backdrop-blur-sm">
                            <div class="inline-block bg-yellow-400 text-indigo-900 font-black text-xs px-2 py-1 rounded mb-2">2017 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed">I. Göktürk'ün en parlak dönemi: <strong class="text-white">Mukan Kağan</strong>. (Sülale: Aşina).</p>
                        </div>
                        <div class="bg-white/10 hover:bg-white/20 transition-colors p-5 rounded-2xl border border-white/20 backdrop-blur-sm">
                            <div class="inline-block bg-yellow-400 text-indigo-900 font-black text-xs px-2 py-1 rounded mb-2">2018 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed">Veraset sistemi: "Kut" yüzünden <strong class="text-white">"hükümdar önceden belirlenir" yargısı söylenemez.</strong></p>
                        </div>
                        <div class="bg-white/10 hover:bg-white/20 transition-colors p-5 rounded-2xl border border-white/20 backdrop-blur-sm">
                            <div class="inline-block bg-yellow-400 text-indigo-900 font-black text-xs px-2 py-1 rounded mb-2">2019 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed">"Güneş bayrağımız, gökyüzü çadırımız" sözü: <strong class="text-white">Cihan Hâkimiyeti mefkûresi.</strong></p>
                        </div>
                        <div class="bg-white/10 hover:bg-white/20 transition-colors p-5 rounded-2xl border border-white/20 backdrop-blur-sm">
                            <div class="inline-block bg-yellow-400 text-indigo-900 font-black text-xs px-2 py-1 rounded mb-2">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed">Ayukı = Hükümet demektir. Yargıç anlamına gelen kavram ise <strong class="text-white">Yargucu'dur.</strong></p>
                        </div>
                        <div class="bg-white/10 hover:bg-white/20 transition-colors p-5 rounded-2xl border border-white/20 backdrop-blur-sm">
                            <div class="inline-block bg-yellow-400 text-indigo-900 font-black text-xs px-2 py-1 rounded mb-2">2022 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed">Ahiret inancının en somut göstergesi: <strong class="text-white">Kurgan (Mezar)</strong> kavramıdır.</p>
                        </div>
                        
                        <!-- Destanlar (Geniş Kart) -->
                        <div class="md:col-span-2 lg:col-span-3 bg-gradient-to-r from-yellow-400/20 to-orange-500/20 p-6 rounded-2xl border border-yellow-400/30 backdrop-blur-md">
                            <p class="font-black text-yellow-300 mb-3 flex items-center"><i class="fas fa-scroll mr-2"></i> DESTAN EŞLEŞTİRMELERİ KISA YOL</p>
                            <p class="text-sm font-medium leading-relaxed flex flex-wrap gap-x-6 gap-y-2">
                                <span><strong class="text-white">İskitler:</strong> Alper Tunga, Şu</span>
                                <span><strong class="text-white">Asya Hun:</strong> Oğuz Kağan</span>
                                <span><strong class="text-white">Göktürk:</strong> Ergenekon, Bozkurt</span>
                                <span><strong class="text-white">Uygur:</strong> Türeyiş, Göç</span>
                            </p>
                        </div>
                    </div>"""

index_exam_new = """                    <p class="text-sm text-slate-500 dark:text-slate-400 mb-6 uppercase tracking-widest font-bold">Çıkmış Bilgi Soruları</p>
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2015 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Demir madeninin bulunduğu dağı eriterek çıkış destanı hangisidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Ergenekon (Göktürkler)</strong></p>
                        </div>
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2017 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">I. Göktürk'ün en parlak dönemini yaşatan Aşina sülalesine mensup lider kimdir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Mukan Kağan</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2018 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Eski Türk veraset sisteminde "Kut" anlayışından dolayı hangisi söylenemez?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Hükümdarın önceden belli olması</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2019 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">"Güneş bayrağımız, gökyüzü çadırımız" sözü hangi kavrama işaret eder?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Cihan Hâkimiyeti Mefkûresi</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Eski Türklerde "Ayukı" Hükümet demektir. Yargıç anlamına gelen kavram nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Yargucu</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Eski Türklerde ahiret inancının en somut göstergesi hangi yapıdır?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Kurgan (Mezar)</strong></p>
                        </div>
                        
                        <!-- Destanlar (Geniş Kart) -->
                        <div class="md:col-span-2 lg:col-span-3 bg-indigo-50/80 dark:bg-indigo-900/30 p-6 rounded-2xl border border-indigo-200 dark:border-indigo-800/50 flex items-start mt-2">
                            <i class="fas fa-scroll text-indigo-500 mt-1 mr-4 text-3xl"></i>
                            <div>
                                <p class="font-black text-indigo-800 dark:text-indigo-300 mb-2">DESTAN EŞLEŞTİRMELERİ KISA YOL</p>
                                <p class="text-sm font-medium text-slate-700 dark:text-slate-300 leading-relaxed flex flex-wrap gap-x-6 gap-y-2">
                                    <span><strong class="text-indigo-700 dark:text-indigo-400">İskitler:</strong> Alper Tunga, Şu</span>
                                    <span><strong class="text-indigo-700 dark:text-indigo-400">Asya Hun:</strong> Oğuz Kağan</span>
                                    <span><strong class="text-indigo-700 dark:text-indigo-400">Göktürk:</strong> Ergenekon, Bozkurt</span>
                                    <span><strong class="text-indigo-700 dark:text-indigo-400">Uygur:</strong> Türeyiş, Göç</span>
                                </p>
                            </div>
                        </div>
                    </div>"""

index_content = index_content.replace(index_exam_old, index_exam_new)

# Oh wait, for `index.html` there is also an old layout for Sınav Hafızası that I should make sure matches:
# Wait, checking `index_content.find('<i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-300"></i>')`
# I should change `text-indigo-300` to `text-indigo-600 dark:text-indigo-400` as in unit 2!
index_content = index_content.replace('<i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-300"></i>', '<i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-600 dark:text-indigo-400"></i>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)
