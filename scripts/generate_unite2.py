import re

with open('unite2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Header
content = re.sub(
    r'<h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">.*?</h2>\s*<p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">.*?</p>',
    '''<h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">2. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">İLK TÜRK - İSLAM DEVLETLERİ VE BEYLİKLERİ</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Bu ünitede Orta Asya ve Anadolu'da kurulan ilk Türk-İslam devletleri, önemli şahsiyetleri ve kültürel mirası incelenmektedir.</p>''',
    content, flags=re.DOTALL
)

new_grid_content = '''
                <!-- MOR BÖLÜM -->
                <section class="category-purple note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-star text-purple-600 dark:text-purple-300"></i>
                        </div>
                        İlkler, Sonlar ve Kesin Yargılar
                    </h3>
                    <ul class="space-y-4 text-slate-800 dark:text-purple-100 font-medium">
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Orta Asya'da kurulan ilk Müslüman Türk devleti <strong class="text-purple-700 dark:text-purple-400">Karahanlılardır</strong>.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Türk-İslam tarihinde ilk medreseyi (Semerkant Medresesi) açan, ilk burslu öğrencilik sistemini başlatan ve ilk posta teşkilatını kuran devlet <strong class="text-purple-700 dark:text-purple-400">Karahanlılardır</strong>.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Dünya tarihinde "Sultan" unvanını kullanan ilk hükümdar <strong class="text-purple-700 dark:text-purple-400">Gazneli Mahmut'tur</strong>.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Mısır'da kurulan ilk Türk-İslam devleti <strong class="text-purple-700 dark:text-purple-400">Tolunoğulları'dır</strong>. Hicaz (Mekke-Medine) bölgesine egemen olan ilk devlet ise <strong class="text-purple-700 dark:text-purple-400">İhşidilerdir (Akşitler)</strong>.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Türk tarihinde orduda esir alınan veya satın alınan gençlerin asker/yönetici olarak yetiştirildiği "Gulam Sistemini" ilk uygulayan devlet <strong class="text-purple-700 dark:text-purple-400">Karahanlılardır</strong>.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Tarihte yenilmez sanılan Moğolları durduran ve mağlup eden ilk devlet <strong class="text-purple-700 dark:text-purple-400">Memlüklerdir</strong> (Ayn Calud ve Elbistan Savaşları).</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Türk tasavvuf tarihinin ilk edebi eseri Hoca Ahmet Yesevi'nin yazdığı <strong class="text-purple-700 dark:text-purple-400">Divan-ı Hikmet'tir</strong>.</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Malazgirt'ten sonra Anadolu'da kurulan ilk Türk-İslam devleti <strong class="text-purple-700 dark:text-purple-400">Saltuklulardır</strong>. Anadolu'da yapılan ilk medrese ise <strong class="text-purple-700 dark:text-purple-400">Danişmentlilere</strong> aittir (Yağıbasan Medresesi).</li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> Tarihteki ilk Türk denizcisi <strong class="text-purple-700 dark:text-purple-400">Çaka Bey'dir</strong>.</li>
                        
                        <div class="mt-4 p-4 bg-purple-50 dark:bg-purple-900/30 rounded-2xl border border-purple-100 dark:border-purple-800/50">
                            <p class="font-bold text-purple-800 dark:text-purple-300 mb-2 border-b border-purple-200 dark:border-purple-800/50 pb-2"><i class="fas fa-book mr-2"></i>İlk Edebi Eserler</p>
                            <ul class="space-y-2 text-sm mt-2">
                                <li><strong class="text-purple-700 dark:text-purple-400">İlk Siyasetname:</strong> Yusuf Has Hacip - <em>Kutadgu Bilig</em> (Mutluluk Veren Bilgi)</li>
                                <li><strong class="text-purple-700 dark:text-purple-400">İlk Türkçe Ansiklopedik Sözlük:</strong> Kaşgarlı Mahmut - <em>Divânu Lügati't-Türk</em></li>
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
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Satuk Buğra Han:</strong> Karahanlılar döneminde İslamiyet'i resmî olarak kabul eden ve "Abdülkerim", "El-Mücahit / El-Gazi" unvanlarını alan liderdir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Gazneli Mahmut:</strong> Hindistan'a İslam'ı yaymak ve zenginliklerini ele geçirmek için tam 17 sefer düzenleyen, Abbasi halifesini kurtaran sultandır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Tuğrul Bey:</strong> Büyük Selçuklu Devleti'nin resmî kurucusudur. Halife tarafından "Doğu'nun ve Batı'nın Sultanı" unvanıyla ödüllendirilmiştir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Sultan Alparslan:</strong> Hristiyanlar için çok kutsal sayılan Ani Kalesini aldığı için "Ebul Feth" (Fetihlerin Babası), Malazgirt Savaşı zaferi sonrası ise "İslam Ülkelerinin Sultanı" unvanını almıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Nizamülmülk:</strong> Büyük Selçuklu'nun en ünlü veziridir. Nizamiye Medreselerini kurmuş ve İkta sistemini sistemli hâle getirmiştir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Selahaddin Eyyubi:</strong> Hıttin Savaşı ile Kudüs'ü Haçlıların elinden geri alan liderdir.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">El-Cezeri:</strong> Robotik ve sibernetik biliminin kurucusu kabul edilen ünlü bilim insanıdır. Artuklular döneminde yaşamıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Çaka Bey:</strong> İzmir'de donanmayı kurarak Türk Deniz Kuvvetleri'nin temellerini atan ilk Türk denizcisidir.</li>
                    </ul>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-book-open text-cyan-600 dark:text-cyan-300"></i>
                        </div>
                        Kavramlar, Tarihi Sözler ve Savaşlar
                    </h3>
                    <div class="space-y-6 text-slate-800 dark:text-cyan-100 font-medium">
                        
                        <div class="bg-cyan-50/50 dark:bg-cyan-900/20 p-4 rounded-2xl">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-2 flex items-center"><i class="fas fa-city mr-2"></i>Şehirlerin Unvanları</p>
                            <div class="flex flex-wrap gap-2 text-sm">
                                <span class="bg-white dark:bg-slate-800 px-3 py-1 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong>Semerkant:</strong> Şehirlerin Şahı</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-1 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong>Buhara:</strong> İslam'ın Roması</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-1 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong>Kaşgar:</strong> Işıldayan İnci</span>
                            </div>
                        </div>

                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-4">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-3"><i class="fas fa-crosshairs mr-2"></i>Önemli Olaylar ve Savaşlar</p>
                            <div class="flex flex-col gap-2 text-sm">
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Talas Savaşı (751):</strong> Çinliler ile Müslüman Araplar (Abbasiler) arasında yapılmıştır. Karluk Türklerinin desteğiyle Çin mağlup olmuştur. Türkler kitleler hâlinde İslamiyet'e girmiş; kâğıt, matbaa, pusula ve barut Çin dışına taşınmıştır.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-2.5 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400">Dandanakan Savaşı (1040):</strong> Büyük Selçuklu Devleti'nin resmen kurulduğu, Gaznelilerin ise yıkılış sürecine girdiği savaştır.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-2.5 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400">Pasinler Savaşı (1048):</strong> Büyük Selçuklu ile Bizans arasındaki ilk büyük savaştır ve Selçuklu kazanmıştır.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-2.5 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400">Malazgirt Savaşı (1071):</strong> Anadolu'nun kapılarının Türklere açıldığı ve tarihe "Yurt Açan" olarak geçen büyük zaferdir.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-2.5 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400">Katvan Savaşı (1141):</strong> Büyük Selçuklu Devleti'nin, Karahitaylara mağlup olarak yıkılış sürecine girdiği savaştır.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-2.5 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400">Otrar Faciası:</strong> Cengiz Han'ın Harzemşahlar üzerine yaptığı ve Orta Asya'da Moğol istilasının başlamasına neden olan büyük katliamdır.
                                </div>
                            </div>
                        </div>

                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-4">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-3"><i class="fas fa-archway mr-2"></i>Mimari Kavramlar</p>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-sm">
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong class="text-cyan-700 dark:text-cyan-400 block mb-0.5">Bimaristan / Darüşşifa</strong> Hastane</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong class="text-cyan-700 dark:text-cyan-400 block mb-0.5">Ribat</strong> Kervansaray / Sınır Karakolu</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong class="text-cyan-700 dark:text-cyan-400 block mb-0.5">Külliye</strong> Merkezinde cami olan yapılar topluluğu</span>
                                <span class="bg-white dark:bg-slate-800 px-3 py-2 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800"><strong class="text-cyan-700 dark:text-cyan-400 block mb-0.5">Kümbet</strong> Çadır şeklindeki anıt mezar</span>
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
                    <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl text-slate-800 dark:text-emerald-100 font-medium flex items-start">
                        <i class="fas fa-info-circle text-emerald-500 mt-1 mr-3 text-xl"></i>
                        <p class="text-sm"><strong>Uyarı:</strong> Bu dönemde Büyük Selçuklu ile Bizans ve Haçlılar arasındaki mücadeleler daha çok meydan muharebeleri şeklinde cereyan etmiştir.</p>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-users-cog text-orange-600 dark:text-orange-300"></i>
                        </div>
                        Divanlar, Meclisler ve Görevliler
                    </h3>
                    <div class="space-y-6 text-slate-800 dark:text-orange-100 font-medium">
                        
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg">Divan-ı Saltanat (Divan-ı Ala):</strong>
                            <p class="mt-1 text-sm">Büyük Selçuklularda devlet işlerinin görüşüldüğü en büyük divandır (Bakanlar Kurulu).</p>
                        </div>

                        <div class="bg-orange-50/50 dark:bg-orange-900/20 p-5 rounded-2xl border border-orange-100 dark:border-orange-800/50">
                            <p class="font-bold text-orange-800 dark:text-orange-300 mb-3 border-b border-orange-200 dark:border-orange-800/50 pb-2"><i class="fas fa-sitemap mr-2"></i>Alt Divanlar ve Görevlileri</p>
                            <ul class="space-y-3 text-sm mt-2">
                                <li class="flex items-start">
                                    <i class="fas fa-coins text-orange-400 mt-1 w-5"></i>
                                    <div><strong class="text-orange-700 dark:text-orange-400">Divan-ı İstifa:</strong> Mali işlere bakar. Görevlisi: <em class="text-slate-600 dark:text-slate-400">Müstevfi</em></div>
                                </li>
                                <li class="flex items-start">
                                    <i class="fas fa-khanda text-orange-400 mt-1 w-5"></i>
                                    <div><strong class="text-orange-700 dark:text-orange-400">Divan-ı Arz (Ceyşül Arz):</strong> Askeri işlere bakar. Görevlisi: <em class="text-slate-600 dark:text-slate-400">Emir-i Arz</em></div>
                                </li>
                                <li class="flex items-start">
                                    <i class="fas fa-feather-alt text-orange-400 mt-1 w-5"></i>
                                    <div><strong class="text-orange-700 dark:text-orange-400">Divan-ı İnşa (Tuğra):</strong> Resmî yazışmalara bakar. Görevlisi: <em class="text-slate-600 dark:text-slate-400">Tuğrai</em></div>
                                </li>
                                <li class="flex items-start">
                                    <i class="fas fa-search text-orange-400 mt-1 w-5"></i>
                                    <div><strong class="text-orange-700 dark:text-orange-400">Divan-ı İşraf:</strong> İdari ve mali denetim yapar. Görevlisi: <em class="text-slate-600 dark:text-slate-400">Müşrif</em></div>
                                </li>
                                <li class="flex items-start border-t border-orange-200 dark:border-orange-800/50 pt-3 mt-3">
                                    <i class="fas fa-balance-scale text-orange-600 dark:text-orange-400 mt-0.5 w-5"></i>
                                    <div><strong class="text-orange-800 dark:text-orange-300">Divan-ı Mezalim:</strong> Sultanın başkanlık ettiği, ağır siyasi suçların görüşüldüğü en üst mahkemedir.</div>
                                </li>
                            </ul>
                        </div>

                        <div class="bg-white dark:bg-slate-800 p-4 rounded-xl shadow-sm border border-orange-100 dark:border-orange-800">
                            <p class="font-bold text-orange-800 dark:text-orange-300 mb-3 border-b border-orange-100 dark:border-orange-800 pb-2"><i class="fas fa-chess-rook mr-2"></i>Saray Görevlileri</p>
                            <ul class="text-sm space-y-2 grid grid-cols-1 sm:grid-cols-2 gap-x-4">
                                <li><strong class="text-orange-700 dark:text-orange-400">Hacip:</strong> Sultan ile halk arasındaki yetkili aracı</li>
                                <li><strong class="text-orange-700 dark:text-orange-400">Candar:</strong> Saray koruması</li>
                                <li><strong class="text-orange-700 dark:text-orange-400">Alemdar:</strong> Bayrak taşıyan</li>
                                <li><strong class="text-orange-700 dark:text-orange-400">Camedar:</strong> Kıyafet sorumlusu</li>
                                <li><strong class="text-orange-700 dark:text-orange-400">Çaşnigir:</strong> Yemek sorumlusu</li>
                                <li><strong class="text-orange-700 dark:text-orange-400">Emir-i Ahur:</strong> Atların sorumlusu</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- KIRMIZI BÖLÜM -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-exclamation-triangle text-red-600 dark:text-red-300"></i>
                        </div>
                        Kritik Öneme Sahip Eserler, Uyarılar ve Analizler
                    </h3>
                    <div class="space-y-6 text-slate-800 dark:text-red-100 font-medium">
                        
                        <div>
                            <p class="font-bold text-red-800 dark:text-red-300 mb-3 border-b border-red-200 dark:border-red-800/50 pb-2"><i class="fas fa-book-open mr-2"></i>TÜRK-İSLAM ESERLERİ VE YAZARLARI</p>
                            <ul class="space-y-2 text-sm">
                                <li><strong class="text-red-700 dark:text-red-400">Atabetü'l Hakayık (Gerçeklerin Eşiği):</strong> Edip Ahmet Yükneki yazmıştır.</li>
                                <li><strong class="text-red-700 dark:text-red-400">Divan-ı Hikmet:</strong> Hoca Ahmet Yesevi (Piri Türkistan) yazmıştır.</li>
                                <li><strong class="text-red-700 dark:text-red-400">Şehname:</strong> Firdevsi tarafından yazılıp Gazneli Mahmut'a sunulmuştur. İskit lideri Alper Tunga'dan "Afrasiyap" olarak bahseder.</li>
                                <li><strong class="text-red-700 dark:text-red-400">Tarihi Yemin:</strong> Utbi tarafından yazılmıştır (Gaznelileri anlatır).</li>
                                <li><strong class="text-red-700 dark:text-red-400">Muhakemetü'l Lügateyn:</strong> Ali Şir Nevai yazmıştır. (Türkçenin Farsça ve Hintçeden zengin olduğunu kanıtlamak için).</li>
                                <li><strong class="text-red-700 dark:text-red-400">Rubai:</strong> Büyük Selçuklu döneminde Ömer Hayyam yazmıştır.</li>
                            </ul>
                        </div>

                        <div>
                            <p class="font-bold text-red-800 dark:text-red-300 mb-3 border-b border-red-200 dark:border-red-800/50 pb-2 flex items-center justify-between">
                                <span><i class="fas fa-map-marked mr-2"></i>MALAZGİRT SONRASI İLK TÜRK BEYLİKLERİ</span>
                                <span class="bg-red-100 dark:bg-red-900/50 text-red-700 dark:text-red-300 text-xs px-2 py-1 rounded font-bold">Şifre: DSMAÇ</span>
                            </p>
                            <ul class="space-y-2 text-sm">
                                <li><strong class="text-red-700 dark:text-red-400">Danişmentliler (Sivas/Tokat):</strong> En güçlüleridir. Anadolu'daki ilk medrese olan Yağıbasan Medresesi onlara aittir.</li>
                                <li><strong class="text-red-700 dark:text-red-400">Saltuklar (Erzurum):</strong> Anadolu'daki ilk Türk-İslam devletidir. Kale Camii, Üç Kümbetler ve Mama Hatun Türbesi en önemli eserleridir.</li>
                                <li><strong class="text-red-700 dark:text-red-400">Mengücekler (Divriği/Erzincan):</strong> UNESCO korumasındaki Divriği Ulu Camii onlara aittir.</li>
                                <li><strong class="text-red-700 dark:text-red-400">Artuklular (Diyarbakır/Mardin):</strong> Ünlü bilim insanı El-Cezeri burada yaşamıştır. Malabadi Köprüsü en önemli eserleridir.</li>
                                <li><strong class="text-red-700 dark:text-red-400">Çaka Beyliği (İzmir):</strong> İlk denizci beyliktir.</li>
                            </ul>
                        </div>

                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">İkta Sistemi vs Gulam Sistemi:</strong>
                            <p class="text-sm"><strong>İkta:</strong> Toprağa dayalıdır, atlı asker (Cebelü) yetiştirir, hazineden para çıkmaz. <br><strong>Gulam:</strong> Devşirme sistemidir, saray muhafızı (Hassa Ordusu) yetiştirir, maaşlıdır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Memlüklerdeki Farklı Veraset:</strong>
                            <p class="text-sm">Eski Türklerdeki "Kut" inancı yoktur. "Her başarılı komutanın sultan olma hakkı vardır."</p>
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
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">ÖSYM, Kaşgarlı Mahmut'un Divânu Lügati't-Türk adlı eserinde "Türk'ün kanadı" olarak nitelendirdiği savaş aracını sormuştur.<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: At</strong></p>
                        </div>
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2015 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Timur döneminde "Şehirlerin Şahı" unvanını alan stratejik şehir soruldu.<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Semerkant</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2018 / 2020</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">ÖSYM "Has Arazi"yi çeldirici/cevap olarak sorar. Geliri doğrudan doğruya hükümdar ve ailesine ayrılan topraklara <strong class="text-indigo-600 dark:text-indigo-400">Has Arazi</strong> denir (Vakıf veya İkta arazisi değildir).</p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Türk-İslam devletlerinde ülke yönetimi hakkında yöneticilere öğüt veren eserlerin genel adı soruldu.<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Siyasetname</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2021 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Karahanlılar dönemi'nde "Hakaniye Lehçesi" ile yazılan, dört karakter üzerinden devlet yönetimi anlatan eser soruldu.<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Kutadgu Bilig</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2022 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Ermeni ve Gürcülerin şefkatli tutumunu övdüğü, Ani'yi fethederek "Ebul Feth" unvanı alan lider soruldu.<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Sultan Alparslan</strong></p>
                        </div>
                        
                        <!-- Tuzağa Dikkat Kartı -->
                        <div class="md:col-span-2 lg:col-span-3 bg-indigo-50/80 dark:bg-indigo-900/30 p-6 rounded-2xl border border-indigo-200 dark:border-indigo-800/50 flex items-start mt-2">
                            <i class="fas fa-lightbulb text-indigo-500 mt-1 mr-4 text-3xl"></i>
                            <div>
                                <p class="font-black text-indigo-800 dark:text-indigo-300 mb-2">MİMARİ TUZAĞI!</p>
                                <p class="text-sm font-medium text-slate-700 dark:text-slate-300 leading-relaxed">
                                    "Kümbet" sosyal bir yapı değildir; İslam öncesi kurgan kültürünün İslami sentezi olan, devlet adamlarına özel çadır tipli anıt mezarlardır.
                                </p>
                            </div>
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
                    İLK TÜRK - İSLAM DEVLETLERİ KÜNYESİ
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 text-sm font-medium">
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">1. Karahanlılar</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Kurucusu Bilge Kül Kadır Han'dır. Orta Asya'da kurulan ilk Müslüman Türk devletidir. Resmî dilleri Türkçedir (milliyetçi yapı).</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">2. Gazneliler</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Kurucusu Alp Tegin'dir. "Sultan" unvanını ilk kullanan devlet olmuşlardır. Hindistan'a 17 sefer düzenlemişlerdir.</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">3. Büyük Selçuklu</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Kurucusu Tuğrul Bey'dir. Dandanakan ile kurulup, Malazgirt ile Anadolu'nun kapılarını Türklere açan büyük cihan devletidir.</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">4. Tolunoğulları</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Kurucusu Tolunoğlu Ahmet'tir. Mısır'da kurulan ilk Türk-İslam devletidir. Hastanelerine Bimaristan denir.</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">5. Akşitler (İhşidiler)</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Kurucusu Muhammed bin Togaç'tır. Hicaz bölgesine (Mekke-Medine) egemen olan ilk Türk devletidir.</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">6. Eyyubiler</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Kurucusu Selahaddin Eyyubi'dir. Hıttin Savaşı ile Kudüs'ü Haçlılardan kurtarmışlardır.</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">7. Memlükler</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Kurucusu Aybek'tir. Moğolları yenebilen ilk devlettir. Kut inancı yoktur.</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">8. Harzemşahlar</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">İl Arslan tarafından kurulmuştur. Kendilerini B. Selçuklu'nun mirasçısı görmüşlerdir. Otrar Faciası'nı yaşamışlardır.</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">9. Timur İmparatorluğu</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Timur kurmuştur. Altınorda Devleti'ni yıkarak Rusların güneye inmesine sebep olmuşlardır. Bilimde çok ileridirler (Ali Kuşçu, Uluğ Bey).</p>
                    </div>
                    <div class="p-4 bg-slate-50 hover:bg-slate-100 dark:bg-slate-900/50 dark:hover:bg-slate-700/50 rounded-2xl border border-slate-200 dark:border-slate-700 transition-colors">
                        <div class="font-bold text-indigo-600 dark:text-indigo-400 mb-1">10. Babür İmparatorluğu</div>
                        <p class="text-slate-600 dark:text-slate-300 text-xs">Babür Şah tarafından Hindistan'da kurulmuştur. En önemli eserleri Tac Mahal'dir.</p>
                    </div>
                </div>
            </section>
'''

content = re.sub(
    r'<!-- MOR BÖLÜM -->.*?</main>',
    new_grid_content + '\n        </main>',
    content, flags=re.DOTALL
)

with open('unite2.html', 'w', encoding='utf-8') as f:
    f.write(content)
