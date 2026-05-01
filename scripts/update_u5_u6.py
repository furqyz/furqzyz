import re

with open('unite5.html', 'r', encoding='utf-8') as f:
    u5_content = f.read()

u5_timeline = """            <!-- DÖNEM PADİŞAHLARI KRONOLOJİSİ -->
            <section class="bg-white dark:bg-slate-800 p-8 md:p-12 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 mt-12">
                <h3 class="text-3xl font-black mb-8 flex items-center text-slate-900 dark:text-white">
                    <div class="bg-slate-100 dark:bg-slate-700 p-3 rounded-2xl mr-4 text-slate-600 dark:text-slate-300">
                        <i class="fas fa-hourglass-half"></i>
                    </div>
                    KURULUŞ DÖNEMİ PADİŞAHLARI (KRONOLOJİK)
                </h3>
                <div class="flex flex-wrap items-center gap-4 text-sm font-medium">
                    <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                        <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">1</div>
                        <span class="text-slate-700 dark:text-slate-300 font-semibold">Osman Bey</span>
                    </div>
                    <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                    <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                        <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">2</div>
                        <span class="text-slate-700 dark:text-slate-300 font-semibold">Orhan Bey</span>
                    </div>
                    <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                    <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                        <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">3</div>
                        <span class="text-slate-700 dark:text-slate-300 font-semibold">I. Murat</span>
                    </div>
                    <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                    <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                        <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">4</div>
                        <span class="text-slate-700 dark:text-slate-300 font-semibold">I. Bayezid (Yıldırım)</span>
                    </div>
                    <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                    <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                        <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">5</div>
                        <span class="text-slate-700 dark:text-slate-300 font-semibold">I. Mehmet (Çelebi)</span>
                    </div>
                    <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                    <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                        <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">6</div>
                        <span class="text-slate-700 dark:text-slate-300 font-semibold">II. Murat</span>
                    </div>
                </div>
            </section>
        </main>"""

u5_content = re.sub(r'</main>', f'{u5_timeline}', u5_content)
with open('unite5.html', 'w', encoding='utf-8') as f:
    f.write(u5_content)


with open('unite6.html', 'r', encoding='utf-8') as f:
    u6_content = f.read()

u6_main = """<main class="flex-1 space-y-8 lg:space-y-12">
            <header class="space-y-4 bg-white dark:bg-slate-800 p-8 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 relative overflow-hidden">
                <div class="absolute right-0 bottom-0 opacity-5 dark:opacity-10 pointer-events-none transform translate-x-1/4 translate-y-1/4">
                    <i class="fas fa-chess-rook text-[20rem]"></i>
                </div>
                <div class="relative z-10">
                    <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-2 shadow-inner">
                        KPSS Tarih Hazırlık
                    </div>
                    <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight uppercase tracking-tight">6. ÜNİTE:<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400">OSMANLI DEVLETİ YÜKSELME DÖNEMİ (1453 - 1595)</span></h2>
                    <p class="text-slate-500 dark:text-slate-400 mt-4 text-lg max-w-2xl">Bu ünitede Fatih Sultan Mehmet, II. Bayezid, Yavuz Sultan Selim, Kanuni Sultan Süleyman, II. Selim ve III. Murat dönemlerinde Osmanlı'nın bir cihan devletine dönüşmesi incelenmektedir.</p>
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
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı Devleti'nin doğuda en geniş sınırlara ulaştığı antlaşma III. Murat dönemindeki 1590 tarihli <strong class="text-purple-700 dark:text-purple-400">Ferhat Paşa Antlaşması'dır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı tarihinde bir iç sorunken dış sorun hâline gelen ilk olay <strong class="text-purple-700 dark:text-purple-400">Cem Sultan Olayı'dır</strong> (II. Bayezid Dönemi).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Anadolu'da çıkan ilk "Celâlî İsyanı" (Bozoklu Celal isyanı) <strong class="text-purple-700 dark:text-purple-400">Yavuz Sultan Selim</strong> döneminde Yozgat'ta çıkmıştır.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Karadeniz'in kesin olarak Türk gölü hâline gelmesi <strong class="text-purple-700 dark:text-purple-400">Kırım'ın Fethi</strong> ile (Fatih dönemi); Akdeniz'in kesin olarak Türk gölü hâline gelmesi ise <strong class="text-purple-700 dark:text-purple-400">Preveze Deniz Zaferi</strong> ile (Kanuni dönemi) olmuştur.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Dünya tarihinin bilinen en kısa süren ova savaşı <strong class="text-purple-700 dark:text-purple-400">Mohaç Meydan Muharebesi'dir</strong> (2 saatte Macaristan alınmıştır - Kanuni dönemi).</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Halifelik makamı ilk defa <strong class="text-purple-700 dark:text-purple-400">Yavuz Sultan Selim</strong> döneminde Ridaniye Savaşı ile Osmanlı'ya geçmiştir.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Anadolu Türk siyasi birliği kesin olarak <strong class="text-purple-700 dark:text-purple-400">Yavuz Sultan Selim</strong> döneminde Turnadağ Savaşı ile Dulkadiroğulları beyliğinin alınmasıyla sağlanmıştır.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı donanması tarihinde ilk defa <strong class="text-purple-700 dark:text-purple-400">İnebahtı Deniz Savaşı'nda</strong> (1571) Haçlılar tarafından yakılmıştır.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Ordunun başında sefere çıkma geleneğini terk eden ve İstanbul'da ölen ilk padişah <strong class="text-purple-700 dark:text-purple-400">II. Selim'dir</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Osmanlı Devleti'nin İran (Safevi) ile imzaladığı ilk resmî antlaşma 1555 <strong class="text-purple-700 dark:text-purple-400">Amasya Antlaşması'dır</strong>.</span></li>
                        <li class="flex items-start"><i class="fas fa-caret-right mt-1 mr-2 text-purple-400"></i> <span>Divan-ı Hümayun'a padişah yerine sadrazamın başkanlık etmesi uygulaması ilk kez <strong class="text-purple-700 dark:text-purple-400">Fatih Sultan Mehmet</strong> döneminde başlamıştır.</span></li>
                    </ul>
                </section>

                <!-- SARI BÖLÜM -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-crown text-yellow-600 dark:text-yellow-300"></i>
                        </div>
                        Önemli Padişahlar ve Şahsiyetler
                    </h3>
                    <ul class="space-y-4 text-slate-800 dark:text-yellow-100 font-medium">
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Fatih Sultan Mehmet (II. Mehmet):</strong> "Avni" mahlasıyla şiirler yazmıştır. Hz. Muhammed'in hadisine nail olmuş, Roma'nın varisi olduğu için "Kayser-i Rum" unvanını kullanmıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">II. Bayezid:</strong> Kardeşi Cem Sultan'ın isyanı yüzünden dış politikada pasif kalmış, bu yüzden dönemi "Yükselme içinde duraklama dönemi" olarak adlandırılmıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Yavuz Sultan Selim (I. Selim):</strong> "Sekiz yıla seksen yıllık iş sığdıran padişah"tır. Doğu siyasetine yönelmesinde İdris-i Bitlisi'nin Heşt Behişt adlı eseri etkili olmuştur. Kutsal toprakları alarak "Hâdimü'l Haremeyn" (Mekke ve Medine'nin Hizmetkârı) unvanını almıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Kanuni Sultan Süleyman (I. Süleyman):</strong> Osmanlı'nın en uzun süre tahtta kalan padişahıdır (46 yıl). "Muhibbi" mahlasıyla şiirler yazmıştır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Sokullu Mehmet Paşa:</strong> Kanuni, II. Selim ve III. Murat dönemlerinde sadrazamlık yapan, sunduğu büyük kanal projeleriyle döneme damgasını vuran devlet adamıdır.</li>
                        <li class="bg-white/40 dark:bg-black/10 p-3 rounded-xl"><strong class="text-yellow-800 dark:text-yellow-300 block text-lg mb-1">Barbaros Hayreddin Paşa:</strong> Preveze Deniz Zaferi'ni kazanan ünlü kaptan-ı deryadır.</li>
                    </ul>
                </section>

                <!-- TURKUAZ BÖLÜM -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-khanda text-cyan-600 dark:text-cyan-300"></i>
                        </div>
                        Kavramlar, İsyanlar ve Savaşlar
                    </h3>
                    <div class="space-y-6 text-slate-800 dark:text-cyan-100 font-medium">
                        
                        <div class="bg-cyan-50/50 dark:bg-cyan-900/20 p-4 rounded-2xl">
                            <strong class="text-cyan-800 dark:text-cyan-300 text-lg block mb-2"><i class="fas fa-quote-left mr-2"></i>Tarihi Sözler</strong>
                            <div class="space-y-3">
                                <p class="text-sm border-l-2 border-cyan-300 pl-3"><strong class="text-cyan-700 dark:text-cyan-400">Sokullu Mehmet Paşa:</strong> İnebahtı bozgunu sonrasında Venedik elçisine; "Biz Kıbrıs'ı almakla sizin kolunuzu kestik, siz İnebahtı'nda bizi yenmekle sakalımızı tıraş ettiniz. Kesilen kol yerine gelmez ama tıraş edilen sakal daha gür çıkar." demiştir.</p>
                            </div>
                        </div>

                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-4">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-3"><i class="fas fa-fire mr-2"></i>Önemli İsyanlar</p>
                            <div class="flex flex-col gap-2 text-sm">
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Şahkulu İsyanı (1511):</strong> II. Bayezid döneminde Safevilerin kışkırtmasıyla çıkan Şii nitelikli büyük isyandır.
                                </div>
                                <div class="bg-white dark:bg-slate-800 px-4 py-3 rounded-lg shadow-sm border border-cyan-100 dark:border-cyan-800">
                                    <strong class="text-cyan-700 dark:text-cyan-400 block mb-1">Kanuni Dönemi İç İsyanları:</strong> Canberdi Gazali ve Ahmet Paşa (Siyasi); Baba Zünnun ve Kalenderoğlu isyanları (Ekonomik/Dini) yaşanmıştır.
                                </div>
                            </div>
                        </div>

                        <div class="border-t border-cyan-200 dark:border-cyan-800/50 pt-4">
                            <p class="font-bold text-cyan-800 dark:text-cyan-300 mb-3"><i class="fas fa-crosshairs mr-2"></i>Önemli Seferler ve Savaşlar</p>
                            <div class="grid grid-cols-1 gap-2 text-sm">
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Kıbrıs'ın Fethi (1571):</strong> II. Selim döneminde Doğu Akdeniz'in güvenliğini sağlamak için alınmış, ancak buna tepki gösteren Haçlılar İnebahtı'da donanmamızı yakmıştır.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Cerbe Deniz Savaşı (1560):</strong> Kanuni döneminde Haçlılara karşı kazanılan ve Kuzey Afrika'daki Türk egemenliğini pekiştiren deniz savaşıdır.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Hint Deniz Seferleri:</strong> Kanuni döneminde Portekizlilere karşı yapılmış ancak Osmanlı gemilerinin okyanus şartlarına uygun olmaması nedeniyle başarısız olunmuştur.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Zigetvar Seferi (1566):</strong> Kanuni Sultan Süleyman'ın hayatını kaybettiği son seferidir.
                                </div>
                                <div class="bg-cyan-50/80 dark:bg-cyan-900/40 p-3 rounded-xl border border-cyan-100 dark:border-cyan-800/50">
                                    <strong class="text-cyan-800 dark:text-cyan-300 block mb-1">Çaldıran (1514) ve Ridaniye (1517):</strong> Yavuz Sultan Selim'in Safevileri mağlup ettiği savaş Çaldıran; Memlükleri yıkıp Halifeliği ve Baharat Yolu'nu aldığı savaş Ridaniye'dir.
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
                        Antlaşmalar ve Ayrıcalıklar
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-emerald-100 font-medium">
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">1533 İstanbul (İbrahim Paşa) Antlaşması:</strong></p>
                            <p class="text-sm">Avusturya Arşidükü'nün protokolde Osmanlı Sadrazamı'na eşit sayıldığı antlaşmadır. Bu durum Osmanlı'nın Avrupa'da siyasi üstünlüğü ele geçirdiğinin kanıtıdır.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">1555 Amasya Antlaşması:</strong></p>
                            <p class="text-sm">Kanuni döneminde Osmanlı ile Safeviler (İran) arasında imzalanan ilk resmî barış antlaşmasıdır.</p>
                        </div>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 rounded-2xl">
                            <p class="mb-1"><strong class="text-emerald-800 dark:text-emerald-300">1569 Fransa Kapitülasyonları:</strong></p>
                            <p class="text-sm">Hristiyan birliğini parçalamak ve sarsılan Akdeniz ticaretini yeniden canlandırmak amacıyla Fransa'ya verilen ayrıcalıklardır.</p>
                        </div>
                    </div>
                </section>

                <!-- TURUNCU BÖLÜM -->
                <section class="category-orange note-card p-6 md:p-8 rounded-3xl">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-project-diagram text-orange-600 dark:text-orange-300"></i>
                        </div>
                        Önemli Politikalar ve Projeler
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-orange-100 font-medium">
                        <div class="bg-white/60 dark:bg-black/10 p-4 rounded-xl border border-orange-200 dark:border-orange-800/40">
                            <strong class="text-orange-800 dark:text-orange-300 text-lg block mb-1">Fatih'in Ortodoks Politikası:</strong>
                            <p class="text-sm">Ortodoks kilisesinin himaye edilmesi; Hristiyan birliğinin (Haçlı İttifakı) oluşmasını engellemek içindir.</p>
                        </div>
                        
                        <div class="border-l-4 border-orange-400 pl-4 py-2 mt-4 bg-orange-50/50 dark:bg-orange-900/20 rounded-r-xl">
                            <strong class="text-orange-800 dark:text-orange-300 block mb-2"><i class="fas fa-hard-hat mr-2"></i>SOKULLU MEHMET PAŞA'NIN PROJELERİ:</strong>
                            <ul class="space-y-2 text-sm">
                                <li><strong class="text-orange-700 dark:text-orange-400">Don - Volga Projesi:</strong> İki nehri birleştirerek Rusların güneye inmesini engellemek ve İpek Yolu'nu canlandırmak amaçlanmıştır.</li>
                                <li><strong class="text-orange-700 dark:text-orange-400">Süveyş Kanalı Projesi:</strong> Kızıldeniz ile Akdeniz'i birleştirip Baharat Yolu'nu tekrar işlerlik kazandırmak amaçlanmıştır.</li>
                                <li><strong class="text-orange-700 dark:text-orange-400">Marmara - Karadeniz Projesi:</strong> Kereste ihtiyacını gidermek ve donanmaya alternatif yol açmak için tasarlanmıştır.</li>
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
                        Kritik Uyarılar ve Analizler
                    </h3>
                    <div class="space-y-4 text-slate-800 dark:text-red-100 font-medium">
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Trabzon Rum İmparatorluğu'nun Yıkılması (1461):</strong>
                            <p class="text-sm">Fatih'in bu fethiyle, Bizans'ı yeniden diriltme umutları tamamen sona ermiştir.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Fatih'in Alamadığı İki Yer:</strong>
                            <p class="text-sm">Fatih'in kuşatıp da alamadığı Sırbistan'daki Belgrat ve Ege'deki Rodos'u fetheden padişah Kanuni Sultan Süleyman'dır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Müsadere ve Kanunname-i Ali Osman:</strong>
                            <p class="text-sm">Fatih'in örfi hukuku yazılı hâle getirdiği kanunnamedir. Merkezî otoriteyi güçlü tutmak ve "Nizam-ı Alem" için kardeş katli, müsadere (haksız kazanca el koyma), cülus bahşişi uygulamaları yasallaşmıştır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Mısır Seferinin Ekonomik Etkisi:</strong>
                            <p class="text-sm">Yavuz Sultan Selim Baharat Yolu'nu ele almıştır. Ancak Avrupa'da Coğrafi Keşifler gerçekleştiği için Osmanlı bu ticaret yolundan beklediği yüksek ekonomik verimi alamamıştır.</p>
                        </div>
                        <div class="border-l-4 border-red-400 pl-4 py-2">
                            <strong class="text-red-800 dark:text-red-300 block mb-1">Divan Başkanlığının Değişmesi:</strong>
                            <p class="text-sm">Fatih döneminde Divana Sadrazamın başkanlık etmeye başlamasıyla Divan, padişahın son sözü söylediği bir "danışma organına" dönüşmüştür.</p>
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
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Fatih'in Ortodoks Kilisesine yönelik izlediği hoşgörü politikasının amacı nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Müslüman olmayan uyrukların devlete olan bağlılığını ve güvenini sağlamak</strong></p>
                        </div>
                        
                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2020 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Fatih Kanunnamesi'nde devletin parçalanmasına meydan verilmemesi için yasallaştırılan kural nedir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Nizam-ı Alem (Kardeş Katli)</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2021 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Kanuni'nin mektubundaki unvanlarından yola çıkarak hangisi söylenemez?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Hristiyan dünyasını hâkimiyeti altına aldığı (Hepsini ele geçirmemiştir)</strong></p>
                        </div>

                        <div class="bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80 transition-colors p-5 rounded-2xl border border-indigo-100 dark:border-indigo-800/50 backdrop-blur-sm relative">
                            <div class="absolute -top-3 -left-3 bg-indigo-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md">2021 KPSS</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-slate-300">Memlük Devleti yıkılarak Suriye, Filistin, Mısır'ın alınması ve Baharat Yolu denetiminin ele geçirilmesi hangi padişah dönemidir?<br><strong class="text-indigo-600 dark:text-indigo-400 mt-2 block text-base">Cevap: Yavuz Sultan Selim</strong></p>
                        </div>

                        <div class="bg-red-50 hover:bg-red-100 dark:bg-red-900/30 dark:hover:bg-red-900/50 transition-colors p-5 rounded-2xl border border-red-200 dark:border-red-800/50 backdrop-blur-sm relative lg:col-span-2">
                            <div class="absolute -top-3 -left-3 bg-red-600 text-white font-black text-xs px-3 py-1.5 rounded-lg shadow-md flex items-center"><i class="fas fa-exclamation-circle mr-1"></i> DİKKAT: İSYAN TUZAĞI</div>
                            <p class="text-sm font-medium leading-relaxed mt-2 text-slate-700 dark:text-red-200">Sorularda "Şahkulu İsyanı" <strong class="text-red-700 dark:text-red-400">Yavuz döneminde DEĞİL, II. Bayezid dönemindedir.</strong> "Celali İsyanları"nın ilki ise Yavuz dönemindedir. Bu ayrım KPSS'de hayat kurtarır.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- DÖNEM PADİŞAHLARI KRONOLOJİSİ -->
            <section class="bg-white dark:bg-slate-800 p-8 md:p-12 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700 mt-12">
                <h3 class="text-3xl font-black mb-8 flex items-center text-slate-900 dark:text-white">
                    <div class="bg-slate-100 dark:bg-slate-700 p-3 rounded-2xl mr-4 text-slate-600 dark:text-slate-300">
                        <i class="fas fa-hourglass-half"></i>
                    </div>
                    YÜKSELME DÖNEMİ PADİŞAHLARI (KRONOLOJİK)
                </h3>
                <div class="flex flex-wrap items-center gap-4 text-sm font-medium">
                    <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                        <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">1</div>
                        <span class="text-slate-700 dark:text-slate-300 font-semibold">Fatih Sultan Mehmet</span>
                    </div>
                    <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                    <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                        <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">2</div>
                        <span class="text-slate-700 dark:text-slate-300 font-semibold">II. Bayezid</span>
                    </div>
                    <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                    <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                        <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">3</div>
                        <span class="text-slate-700 dark:text-slate-300 font-semibold">Yavuz Sultan Selim</span>
                    </div>
                    <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                    <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                        <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">4</div>
                        <span class="text-slate-700 dark:text-slate-300 font-semibold">Kanuni Sultan Süleyman</span>
                    </div>
                    <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                    <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                        <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">5</div>
                        <span class="text-slate-700 dark:text-slate-300 font-semibold">II. Selim</span>
                    </div>
                    <i class="fas fa-chevron-right text-slate-300 dark:text-slate-600"></i>
                    <div class="flex items-center bg-slate-50 dark:bg-slate-900/50 pr-4 rounded-full border border-slate-200 dark:border-slate-700">
                        <div class="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold mr-3 shadow-inner">6</div>
                        <span class="text-slate-700 dark:text-slate-300 font-semibold">III. Murat</span>
                    </div>
                </div>
            </section>
        </main>"""

u6_content = re.sub(r'<main class="flex-1 space-y-8 lg:space-y-12">.*?</main>', f'{u6_main}', u6_content, flags=re.DOTALL)
with open('unite6.html', 'w', encoding='utf-8') as f:
    f.write(u6_content)
