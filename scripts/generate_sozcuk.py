import os
import re

root_dir = r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı\turkce'

pages = [
    {
        'filename': 'sozcuk-turleri-isimler.html',
        'title': 'İsimler (Adlar) ve İsim Tamlamaları',
        'icon': 'fa-tag',
        'color': 'turquoise',
        'html': '''
                <section class="note-card category-turquoise p-6 md:p-8 rounded-2xl shadow-sm">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-teal-900 dark:text-teal-200">
                        <div class="bg-teal-100 dark:bg-teal-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-tag text-teal-600 dark:text-teal-300"></i>
                        </div>
                        İsimler ve Tamlamalar
                    </h3>
                    <div class="space-y-4">
                        <div class="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-teal-700 dark:text-teal-400 block mb-1">İsim (Ad):</strong>
                            <p class="text-slate-700 dark:text-slate-300 text-sm">Varlıkları ve nesneleri karşılayan sözcüklerdir.</p>
                        </div>
                        <div class="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-teal-700 dark:text-teal-400 block mb-2">İsim Tamlamaları:</strong>
                            <p class="text-slate-700 dark:text-slate-300 text-sm mb-3">İki temel unsurdan oluşur: <strong>Tamlayan</strong> (İlgi eki: -ın, -in) ve <strong>Tamlanan</strong> (İyelik eki: -ı, -i).</p>
                            <ul class="space-y-2 text-sm text-slate-700 dark:text-slate-300">
                                <li><i class="fas fa-check-circle text-teal-500 mr-1"></i> <strong class="text-teal-600 dark:text-teal-400">Belirtili:</strong> Hem tamlayan hem tamlanan ek alır. <span class="font-mono text-xs bg-white dark:bg-slate-800 px-1 rounded ml-1">ev-in kapı-s-ı</span></li>
                                <li><i class="fas fa-check-circle text-teal-500 mr-1"></i> <strong class="text-teal-600 dark:text-teal-400">Belirtisiz:</strong> Sadece tamlanan ek alır. <span class="font-mono text-xs bg-white dark:bg-slate-800 px-1 rounded ml-1">ev kedi-s-i</span></li>
                                <li><i class="fas fa-check-circle text-teal-500 mr-1"></i> <strong class="text-teal-600 dark:text-teal-400">Zincirleme:</strong> En az üç isim/zamir iç içe girer. <span class="font-mono text-xs bg-white dark:bg-slate-800 px-1 rounded ml-1">ev-in kapısı-nın kolu</span></li>
                            </ul>
                        </div>
                    </div>
                </section>

                <section class="note-card category-indigo p-6 md:p-8 rounded-2xl shadow-sm">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-indigo-900 dark:text-indigo-200">
                        <div class="bg-indigo-100 dark:bg-indigo-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-info-circle text-indigo-600 dark:text-indigo-300"></i>
                        </div>
                        Ekstra Bilgi & İstisnalar
                    </h3>
                    <ul class="space-y-3 text-sm text-slate-700 dark:text-slate-300">
                        <li class="flex items-start">
                            <i class="fas fa-arrow-right text-indigo-500 mt-1 mr-2"></i>
                            <div>Belirtili isim tamlamalarında tamlayan ile tamlanan <strong>yer değiştirebilir</strong>.<br><em class="opacity-80 text-xs">Örn: Bütün meyhanelerini dolaştım İstanbul'un.</em></div>
                        </li>
                        <li class="flex items-start">
                            <i class="fas fa-arrow-right text-indigo-500 mt-1 mr-2"></i>
                            <div>Belirtili isim tamlamalarında araya <strong>sıfat veya farklı sözcükler</strong> girebilir.<br><em class="opacity-80 text-xs">Örn: devletin <span class="text-rose-500">eski</span> bakanı</em></div>
                        </li>
                    </ul>
                </section>

                <section class="note-card category-red p-6 md:p-8 rounded-2xl shadow-sm text-white lg:col-span-2" style="background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center">
                        <div class="bg-white/20 p-2.5 rounded-xl mr-3">
                            <i class="fas fa-bomb"></i>
                        </div>
                        En Çok Düşülen Zincirleme Tuzağı
                    </h3>
                    <div class="bg-white/10 p-5 rounded-2xl border border-white/20 text-sm leading-relaxed">
                        <p class="mb-4">Araya sıfat giren belirtili isim tamlamalarını sakın zincirleme isim tamlaması sanmayın!</p>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div class="bg-black/20 p-4 rounded-xl border border-white/10">
                                <p class="font-bold text-rose-200 mb-1">Okulun <span class="text-white bg-rose-500/50 px-1 rounded">kırık</span> kapısı</p>
                                <p class="text-xs opacity-90">"Kırık" sıfat olduğu için bu arasına sıfat girmiş bir <strong>Belirtili İsim Tamlamasıdır</strong>.</p>
                            </div>
                            <div class="bg-black/20 p-4 rounded-xl border border-white/10">
                                <p class="font-bold text-emerald-300 mb-1">Okulun <span class="text-white bg-emerald-500/50 px-1 rounded">demir</span> kapısı</p>
                                <p class="text-xs opacity-90">"Demir" isim olduğu için bu bir <strong>Zincirleme İsim Tamlamasıdır</strong>.</p>
                            </div>
                        </div>
                    </div>
                </section>

            <!-- SINAV HAFIZASI -->
            <section class="note-card p-8 md:p-12 rounded-3xl shadow-2xl relative overflow-hidden group mt-12 exam-memory lg:col-span-2">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16"></div>
                <div class="relative z-10 text-white">
                    <h3 class="text-3xl font-black mb-8 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-300"></i> SINAV HAFIZASI & ANALİZ
                    </h3>
                    <div class="bg-white/10 backdrop-blur p-6 rounded-2xl border border-white/10">
                        <p class="text-indigo-200 font-bold mb-2 flex items-center"><i class="fas fa-search mr-2"></i>Karma Dil Bilgisinde Gizlenen Tamlamalar</p>
                        <p class="text-sm leading-relaxed text-slate-200">
                            ÖSYM isim tamlamalarını doğrudan sormak yerine <strong>karma dil bilgisi sorularında metin içine gizlemeyi</strong> sever. Altı çizili tamlamaların türünü (sıfat tamlaması mı, belirtisiz isim mi, zincirleme mi?) sırasıyla bulmanızı isteyen sorular ve <strong>arasına niteleme sıfatı girmiş belirtili isim tamlamaları</strong> çıkmış sorularda sıkça elleyici olmuştur.
                        </p>
                    </div>
                </div>
            </section>
        '''
    },
    {
        'filename': 'sozcuk-turleri-sifatlar.html',
        'title': 'Sıfatlar (Ön Adlar) ve Sıfat Tamlamaları',
        'icon': 'fa-paint-brush',
        'color': 'purple',
        'html': '''
                <section class="note-card category-purple p-6 md:p-8 rounded-2xl shadow-sm">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-paint-brush text-purple-600 dark:text-purple-300"></i>
                        </div>
                        Sıfatlar ve Sıfat Tamlaması
                    </h3>
                    <p class="text-slate-700 dark:text-slate-300 text-sm mb-4">İsimlerin önüne gelerek onları renk, durum, biçim yönünden niteleyen ya da belirten sözcüklerdir.</p>
                    
                    <div class="space-y-4 mt-4">
                        <div class="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-purple-700 dark:text-purple-400 block mb-2">1. Niteleme Sıfatları:</strong>
                            <p class="text-slate-700 dark:text-slate-300 text-sm">İsme sorulan <strong>"Nasıl?"</strong> sorusunun cevabıdır. Küçültme (küçücük el) ve Pekiştirme (masmavi ev) sıfatları da birer niteleme sıfatıdır.</p>
                        </div>
                        <div class="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-purple-700 dark:text-purple-400 block mb-2">2. Belirtme Sıfatları (4'e Ayrılır):</strong>
                            <ul class="space-y-1 text-sm text-slate-700 dark:text-slate-300">
                                <li><strong>İşaret:</strong> bu adam, şu vazo</li>
                                <li><strong>Sayı:</strong> üç kişi (Asıl), birinci (Sıra), beşer (Üleştirme)</li>
                                <li><strong>Belgisiz:</strong> birkaç öğrenci, hiçbir kitap</li>
                                <li><strong>Soru:</strong> nasıl araba, hangi gün</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <section class="note-card category-orange p-6 md:p-8 rounded-2xl shadow-sm">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-compress text-orange-600 dark:text-orange-300"></i>
                        </div>
                        Kurallı Birleşik Sıfat
                    </h3>
                    <div class="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800 text-sm text-slate-700 dark:text-slate-300">
                        <p class="mb-3">Yediiklim notlarına göre sınavda detay olarak gelebilecek bir başlıktır. İki şekilde yapılır:</p>
                        <ul class="space-y-2">
                            <li><i class="fas fa-check text-orange-500 mr-1"></i> Sıfat tamlamasına "-lı/-li" eki getirilir: <strong>kırmızı başlık-lı kız</strong></li>
                            <li><i class="fas fa-check text-orange-500 mr-1"></i> İsimle sıfat yer değiştirip isme iyelik eki getirilir: <strong>başlığı kırmızı kız</strong></li>
                        </ul>
                    </div>
                </section>

                <section class="note-card category-red p-6 md:p-8 rounded-2xl shadow-sm text-white lg:col-span-2" style="background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center">
                        <div class="bg-white/20 p-2.5 rounded-xl mr-3">
                            <i class="fas fa-exclamation-triangle"></i>
                        </div>
                        Kritik Uyarılar
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm leading-relaxed">
                        <div class="bg-white/10 p-4 rounded-2xl border border-white/20">
                            <p class="font-bold text-rose-200 mb-2">Adlaşmış Sıfat</p>
                            <p>Niteleme sıfatlarının yanındaki isim düştüğünde sıfat, adlaşmış sıfat olur.</p>
                            <p class="mt-2 text-xs font-mono">Yaşlı insanlar -> <strong>Yaşlılar</strong></p>
                        </div>
                        <div class="bg-white/10 p-4 rounded-2xl border border-white/20">
                            <p class="font-bold text-rose-200 mb-2">Sıfat - Zamir Ayrımı</p>
                            <p>İsmin önüne gelirse sıfat, ek alıp ismin yerini tutarsa zamir olur!</p>
                            <p class="mt-2 text-xs font-mono">Birkaç kişi geldi -> <strong>Sıfat</strong></p>
                            <p class="mt-1 text-xs font-mono">Birkaçı geldi -> <strong>Zamir</strong></p>
                        </div>
                    </div>
                </section>

            <!-- SINAV HAFIZASI -->
            <section class="note-card p-8 md:p-12 rounded-3xl shadow-2xl relative overflow-hidden group mt-12 exam-memory lg:col-span-2">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16"></div>
                <div class="relative z-10 text-white">
                    <h3 class="text-3xl font-black mb-8 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-300"></i> SINAV HAFIZASI & ANALİZ
                    </h3>
                    <div class="bg-white/10 backdrop-blur p-6 rounded-2xl border border-white/10">
                        <p class="text-indigo-200 font-bold mb-2 flex items-center"><i class="fas fa-star-half-alt mr-2"></i>Hem Niteleme Hem Belirtme Sıfatı</p>
                        <p class="text-sm leading-relaxed text-slate-200">
                            ÖSYM "Hangisinde bir isim hem niteleme hem de belirtme sıfatı almıştır?" kuralını sıkça sorar. Klasik yapı şudur:<br>
                            <strong>Yaşlı bir arkadaş</strong> -> "Yaşlı" niteleme sıfatı, "bir" belirtme (belgisiz) sıfatıdır.
                        </p>
                    </div>
                </div>
            </section>
        '''
    },
    {
        'filename': 'sozcuk-turleri-zamirler.html',
        'title': 'Zamirler (Adıllar)',
        'icon': 'fa-user-secret',
        'color': 'indigo',
        'html': '''
                <section class="note-card category-indigo p-6 md:p-8 rounded-2xl shadow-sm lg:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-indigo-900 dark:text-indigo-200">
                        <div class="bg-indigo-100 dark:bg-indigo-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-user-secret text-indigo-600 dark:text-indigo-300"></i>
                        </div>
                        Zamir Çeşitleri
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="space-y-3">
                            <strong class="text-indigo-700 dark:text-indigo-400 border-b border-indigo-100 dark:border-indigo-900/50 pb-2 block">Sözcük Hâlindeki Zamirler</strong>
                            <ul class="space-y-2 text-sm text-slate-700 dark:text-slate-300">
                                <li><strong>Şahıs:</strong> ben, sen, o, biz, siz, onlar</li>
                                <li><strong>Dönüşlülük:</strong> kendi</li>
                                <li><strong>İşaret:</strong> bu, şu, o, bunlar, şunlar, öteki</li>
                                <li><strong>Belgisiz:</strong> bazıları, tümü, hiçbiri, kimse, şey</li>
                                <li><strong>Soru:</strong> kim, ne, hangisi, nereye</li>
                            </ul>
                        </div>
                        <div class="space-y-3">
                            <strong class="text-indigo-700 dark:text-indigo-400 border-b border-indigo-100 dark:border-indigo-900/50 pb-2 block">Ek Hâlindeki Zamirler</strong>
                            <ul class="space-y-4 text-sm text-slate-700 dark:text-slate-300">
                                <li class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                                    <strong class="text-indigo-600 dark:text-indigo-300">İlgi Zamiri ("-ki"):</strong> İsmin yerine kullanılır ve bitişik yazılır.<br>
                                    <em class="text-xs opacity-80">Örn: Onların arabası kötü sizin-ki güzel.</em>
                                </li>
                                <li class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                                    <strong class="text-indigo-600 dark:text-indigo-300">İyelik Zamiri:</strong> Kime ait olduğunu bildiren iyelik eklerinin ta kendisidir.
                                </li>
                            </ul>
                        </div>
                    </div>
                </section>

                <section class="note-card category-red p-6 md:p-8 rounded-2xl shadow-sm text-white" style="background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center">
                        <div class="bg-white/20 p-2.5 rounded-xl mr-3">
                            <i class="fas fa-balance-scale-right"></i>
                        </div>
                        "O" ve "Onlar" Tuzakları
                    </h3>
                    <div class="bg-white/10 p-4 rounded-2xl border border-white/20 text-sm leading-relaxed">
                        <p class="mb-3">İnsan isminin yerini tutarsa <strong>Şahıs Zamiri</strong>, insan dışı bir varlığın yerini tutarsa <strong>İşaret Zamiri</strong> olur.</p>
                        <p><i class="fas fa-user mr-1 text-rose-200"></i> O, çok başarılı biriydi. (Şahıs)</p>
                        <p class="mt-2"><i class="fas fa-chair mr-1 text-rose-200"></i> O, antika bir saatti. (İşaret)</p>
                    </div>
                </section>

                <section class="note-card category-purple p-6 md:p-8 rounded-2xl shadow-sm text-white" style="background: linear-gradient(135deg, #7c3aed 0%, #5b21b6 100%);">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center">
                        <div class="bg-white/20 p-2.5 rounded-xl mr-3">
                            <i class="fas fa-vector-square"></i>
                        </div>
                        Sıfat mı Zamir mi?
                    </h3>
                    <div class="bg-white/10 p-4 rounded-2xl border border-white/20 text-sm leading-relaxed font-mono text-xs space-y-2">
                        <p class="text-purple-200">İsmin önüne gelirse Sıfat, yerine geçerse Zamir.</p>
                        <p class="mt-2">Bu adam geldi -> <strong class="text-white">İşaret Sıfatı</strong></p>
                        <p>Bunu al -> <strong class="text-white">İşaret Zamiri</strong></p>
                        <hr class="border-white/10 my-2">
                        <p>Birkaç kişi -> <strong class="text-white">Belgisiz Sıfat</strong></p>
                        <p>Birkaçı geldi -> <strong class="text-white">Belgisiz Zamir</strong></p>
                    </div>
                </section>

            <!-- SINAV HAFIZASI -->
            <section class="note-card p-8 md:p-12 rounded-3xl shadow-2xl relative overflow-hidden group mt-12 exam-memory lg:col-span-2">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16"></div>
                <div class="relative z-10 text-white">
                    <h3 class="text-3xl font-black mb-6 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-300"></i> SINAV HAFIZASI
                    </h3>
                    <div class="bg-white/10 backdrop-blur p-6 rounded-2xl border border-white/10">
                        <p class="text-sm leading-relaxed text-slate-200">
                            ÖSYM altı çizili kelimelerde sıfat tamlaması içindeki bir kelimeyi zamirle karıştırmanız için tuzak kurar. Ayrıca metinlerde geçen <strong>"şey"</strong> kelimesinin HER ZAMAN <strong>belgisiz zamir</strong> olduğunu bilmek size ciddi hız kazandırır.
                        </p>
                    </div>
                </div>
            </section>
        '''
    },
    {
        'filename': 'sozcuk-turleri-zarflar.html',
        'title': 'Zarflar (Belirteçler)',
        'icon': 'fa-bolt',
        'color': 'orange',
        'html': '''
                <section class="note-card category-orange p-6 md:p-8 rounded-2xl shadow-sm lg:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-bolt text-orange-600 dark:text-orange-300"></i>
                        </div>
                        Zarf Çeşitleri
                    </h3>
                    <p class="text-slate-700 dark:text-slate-300 text-sm mb-6">Fiilleri, fiilimsileri, sıfatları veya zarfları niteleyen sözcüklerdir.</p>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                        <div class="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-orange-600 dark:text-orange-400">Durum (Hâl):</strong> "Nasıl?" <br><em class="opacity-70 text-xs">doğru söylüyor, koşarak geldi</em>
                        </div>
                        <div class="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-orange-600 dark:text-orange-400">Zaman:</strong> "Ne zaman?" <br><em class="opacity-70 text-xs">şimdi çalışıyorum, dün gece geldi</em>
                        </div>
                        <div class="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-orange-600 dark:text-orange-400">Yer-Yön:</strong> "Nere?" <br><em class="opacity-70 text-xs">aşağı indi, ileri git</em>
                        </div>
                        <div class="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-orange-600 dark:text-orange-400">Miktar:</strong> "Ne kadar?" <br><em class="opacity-70 text-xs">çok çalıştı, fazla yoruldum</em>
                        </div>
                    </div>
                </section>

                <section class="note-card category-red p-6 md:p-8 rounded-2xl shadow-sm text-white" style="background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center">
                        <div class="bg-white/20 p-2.5 rounded-xl mr-3">
                            <i class="fas fa-skull-crossbones"></i>
                        </div>
                        En Tehlikeli Zarf Kuralı
                    </h3>
                    <div class="bg-white/10 p-4 rounded-2xl border border-white/20 text-sm leading-relaxed">
                        <p class="mb-3">Yer-yön bildiren sözcükler (içeri, dışarı, aşağı) <strong>kesinlikle çekim eki almazlar</strong>. Ek alırlarsa isim olurlar!</p>
                        <p class="font-mono text-xs"><i class="fas fa-check text-emerald-300"></i> Aşağı indi -> <strong>Yer-Yön Zarfı</strong></p>
                        <p class="mt-2 font-mono text-xs"><i class="fas fa-times text-rose-300"></i> Aşağı<span class="text-rose-300 font-bold">ya</span> indi -> <strong>İsim</strong></p>
                    </div>
                </section>

                <section class="note-card category-purple p-6 md:p-8 rounded-2xl shadow-sm">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-question-circle text-purple-600 dark:text-purple-300"></i>
                        </div>
                        "Ne" Sözcüğüne Dikkat
                    </h3>
                    <div class="space-y-2 text-sm text-slate-700 dark:text-slate-300 bg-slate-50 dark:bg-slate-900/50 p-4 rounded-2xl border border-slate-100 dark:border-slate-800">
                        <p><strong>Neden/Niçin</strong> anlamındaysa: Zarf (Ne ağlarsın?)</p>
                        <p><strong>İsmin yerini</strong> tutarsa: Zamir (Bana ne aldın?)</p>
                        <p><strong>İsmin önüne</strong> gelirse: Sıfat (Ne gün geleceksin?)</p>
                    </div>
                </section>

            <!-- SINAV HAFIZASI -->
            <section class="note-card p-8 md:p-12 rounded-3xl shadow-2xl relative overflow-hidden group mt-12 exam-memory lg:col-span-2">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16"></div>
                <div class="relative z-10 text-white">
                    <h3 class="text-3xl font-black mb-6 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-300"></i> SINAV HAFIZASI
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-white/10 backdrop-blur p-6 rounded-2xl border border-white/10">
                            <p class="font-bold text-indigo-200 mb-2">Sıfat / Zarf Ayrımı</p>
                            <p class="text-sm">İsme sorulan "Nasıl" sıfatı, fiile sorulan "Nasıl" zarfı buldurur (Güzel araba -> Sıfat, Güzel konuştu -> Zarf).</p>
                        </div>
                        <div class="bg-white/10 backdrop-blur p-6 rounded-2xl border border-white/10">
                            <p class="font-bold text-indigo-200 mb-2">Derecelendirme Zarfı</p>
                            <p class="text-sm">"En" ve "daha" sözcükleri sıfatları derecelendiren <strong>miktar zarflarıdır</strong>. Şıklarda ararken gözden kaçması için gizlenirler.</p>
                        </div>
                    </div>
                </div>
            </section>
        '''
    },
    {
        'filename': 'sozcuk-turleri-edat-baglac.html',
        'title': 'Edat, Bağlaç ve Ünlem',
        'icon': 'fa-link',
        'color': 'teal',
        'html': '''
                <section class="note-card category-teal p-6 md:p-8 rounded-2xl shadow-sm lg:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-teal-900 dark:text-teal-200">
                        <div class="bg-teal-100 dark:bg-teal-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-link text-teal-600 dark:text-teal-300"></i>
                        </div>
                        Edat, Bağlaç ve Ünlem
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="space-y-3">
                            <div class="bg-slate-50 dark:bg-slate-900/50 p-4 rounded-2xl border border-slate-100 dark:border-slate-800">
                                <strong class="text-teal-700 dark:text-teal-400 block mb-1">Edat (İlgeç):</strong>
                                <p class="text-sm text-slate-700 dark:text-slate-300 mb-2">Tek başlarına anlamı yoktur. Sözcüklere benzetme, amaç, neden katar.</p>
                                <p class="text-xs font-mono text-teal-600 dark:text-teal-500">gibi, için, kadar, göre, rağmen, üzere, değil, mi</p>
                            </div>
                            <div class="bg-slate-50 dark:bg-slate-900/50 p-4 rounded-2xl border border-slate-100 dark:border-slate-800">
                                <strong class="text-teal-700 dark:text-teal-400 block mb-1">Bağlaç:</strong>
                                <p class="text-sm text-slate-700 dark:text-slate-300 mb-2">Eş görevli sözcükleri bağlar. Cümlenin ögesi olmaz.</p>
                                <p class="text-xs font-mono text-teal-600 dark:text-teal-500">ve, veya, ya da, ama, fakat, lakin, çünkü, ne...ne</p>
                            </div>
                        </div>
                        <div class="space-y-4">
                            <div class="bg-emerald-50 dark:bg-emerald-900/30 p-4 rounded-2xl border border-emerald-100 dark:border-emerald-800">
                                <strong class="text-emerald-700 dark:text-emerald-400 block mb-2">"İle" Taktiği:</strong>
                                <p class="text-sm text-slate-700 dark:text-slate-300">Yerine "ve" getirebiliyorsanız <strong>Bağlaç</strong>, getiremiyorsanız <strong>Edat</strong>tır.</p>
                            </div>
                            <div class="bg-emerald-50 dark:bg-emerald-900/30 p-4 rounded-2xl border border-emerald-100 dark:border-emerald-800">
                                <strong class="text-emerald-700 dark:text-emerald-400 block mb-2">"Yalnız / Ancak" Taktiği:</strong>
                                <p class="text-sm text-slate-700 dark:text-slate-300">"Sadece" anlamındaysa <strong>Edat</strong>, "ama/fakat" anlamındaysa <strong>Bağlaç</strong>tır.</p>
                            </div>
                        </div>
                    </div>
                </section>

                <section class="note-card category-red p-6 md:p-8 rounded-2xl shadow-sm text-white lg:col-span-2" style="background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center">
                        <div class="bg-white/20 p-2.5 rounded-xl mr-3">
                            <i class="fas fa-exclamation-triangle"></i>
                        </div>
                        Kritik Uyarılar
                    </h3>
                    <div class="bg-white/10 p-5 rounded-2xl border border-white/20 text-sm leading-relaxed space-y-3">
                        <p><strong>Doğru, karşı, beri, sonra</strong> kelimelerinin edat olabilmesi için mutlaka kendinden önceki isimle durum ekleri (-e, -den) alarak birleşmesi gerekir (<strong>-e doğru, -den beri</strong>). Tek başlarına edat olmazlar.</p>
                        <p class="text-rose-200">"Değil" olumsuzluk edatı, "Mi" soru edatıdır.</p>
                    </div>
                </section>

            <!-- SINAV HAFIZASI -->
            <section class="note-card p-8 md:p-12 rounded-3xl shadow-2xl relative overflow-hidden group mt-12 exam-memory lg:col-span-2">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16"></div>
                <div class="relative z-10 text-white">
                    <h3 class="text-3xl font-black mb-4 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-300"></i> SINAV HAFIZASI
                    </h3>
                    <p class="text-sm leading-relaxed text-slate-200 mb-4">
                        ÖSYM karma sözcük türü sorularında en çok "ile"nin, "yalnız"ın ve "ancak" kelimesinin türünü sorarak adayları eler. Ayrıca sorularda geçen kavramlara dikkat:
                    </p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="bg-white/10 p-4 rounded-xl"><strong class="text-indigo-200">Edat Öbeği:</strong> Edatın önceki kelimeyle kurduğu grup (senin için).</div>
                        <div class="bg-white/10 p-4 rounded-xl"><strong class="text-indigo-200">Bağlama Grubu:</strong> Bağlacın iki ismi bağladığı grup (Ahmet ve Ayşe).</div>
                    </div>
                </div>
            </section>
        '''
    },
    {
        'filename': 'sozcuk-turleri-fiiller.html',
        'title': 'Fiillerde Kip, Çekim ve Anlam Özellikleri',
        'icon': 'fa-running',
        'color': 'rose',
        'html': '''
                <section class="note-card category-rose p-6 md:p-8 rounded-2xl shadow-sm lg:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-rose-900 dark:text-rose-200">
                        <div class="bg-rose-100 dark:bg-rose-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-running text-rose-600 dark:text-rose-300"></i>
                        </div>
                        Fiillerde Kip ve Çekim
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="space-y-4">
                            <div class="bg-slate-50 dark:bg-slate-900/50 p-4 rounded-2xl border border-slate-100 dark:border-slate-800">
                                <strong class="text-rose-700 dark:text-rose-400 block mb-2"><i class="fas fa-clock mr-1"></i> Haber (Bildirme) Kipleri</strong>
                                <p class="text-xs text-slate-500 mb-2">Kesin zaman bildirirler.</p>
                                <ul class="text-sm text-slate-700 dark:text-slate-300 space-y-1">
                                    <li>Görülen Geçmiş: <strong>-di</strong></li>
                                    <li>Duyulan Geçmiş: <strong>-miş</strong></li>
                                    <li>Şimdiki: <strong>-yor, -makta</strong></li>
                                    <li>Gelecek: <strong>-ecek</strong></li>
                                    <li>Geniş Zaman: <strong>-r, -ar, -er</strong></li>
                                </ul>
                            </div>
                            <div class="bg-slate-50 dark:bg-slate-900/50 p-4 rounded-2xl border border-slate-100 dark:border-slate-800">
                                <strong class="text-rose-700 dark:text-rose-400 block mb-2"><i class="fas fa-lightbulb mr-1"></i> Dilek (Tasarı) Kipleri</strong>
                                <p class="text-xs text-slate-500 mb-2">Zaman anlamı taşımazlar.</p>
                                <ul class="text-sm text-slate-700 dark:text-slate-300 space-y-1">
                                    <li>Gereklilik: <strong>-malı</strong></li>
                                    <li>Şart: <strong>-sa</strong></li>
                                    <li>İstek: <strong>-e, -a</strong></li>
                                    <li>Emir: <strong>(Eki yoktur)</strong></li>
                                </ul>
                            </div>
                        </div>
                        <div class="space-y-4">
                            <div class="bg-rose-50 dark:bg-rose-900/20 p-4 rounded-2xl border border-rose-100 dark:border-rose-900/50">
                                <strong class="text-rose-700 dark:text-rose-400 block mb-2">Fiillerde Çekim</strong>
                                <p class="text-sm mb-2"><strong class="text-slate-900 dark:text-white">Basit Çekimli:</strong> Sadece bir tane kip eki alanlar (gel-ecek-sin).</p>
                                <p class="text-sm"><strong class="text-slate-900 dark:text-white">Birleşik Çekimli:</strong> İki tane kip eki alanlar. Hikâye (-di), Rivayet (-miş) ve Şart (-sa) birleşik çekimi (gel-ecek-ti).</p>
                            </div>
                            <div class="bg-rose-50 dark:bg-rose-900/20 p-4 rounded-2xl border border-rose-100 dark:border-rose-900/50">
                                <strong class="text-rose-700 dark:text-rose-400 block mb-2">Anlamına Göre Fiiller</strong>
                                <ul class="text-sm space-y-2">
                                    <li><strong>İş (Kılış):</strong> Nesne alır (onu çöz).</li>
                                    <li><strong>Durum:</strong> Nesne almaz (onu uyu X).</li>
                                    <li><strong>Oluş:</strong> Nesne almaz, zamanla kendiliğinden değişim (sararmak).</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </section>

                <section class="note-card category-red p-6 md:p-8 rounded-2xl shadow-sm text-white lg:col-span-2" style="background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center">
                        <div class="bg-white/20 p-2.5 rounded-xl mr-3">
                            <i class="fas fa-exchange-alt"></i>
                        </div>
                        Anlam (Zaman) Kayması
                    </h3>
                    <div class="bg-white/10 p-5 rounded-2xl border border-white/20 text-sm leading-relaxed">
                        <p class="mb-3">Bir kip ekinin, başka bir kip kastedilerek kullanılmasıdır.</p>
                        <p class="font-mono text-xs text-rose-200">Dersler haftaya başlıyor. (Gelecek hafta olduğu için "başlayacak" olmalıydı)</p>
                        <p class="mt-4 font-bold text-lg text-emerald-300"><i class="fas fa-exclamation-circle"></i> Anlam kayması KESİNLİKLE anlatım bozukluğu DEĞİLDİR!</p>
                    </div>
                </section>

            <!-- SINAV HAFIZASI -->
            <section class="note-card p-8 md:p-12 rounded-3xl shadow-2xl relative overflow-hidden group mt-12 exam-memory lg:col-span-2">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16"></div>
                <div class="relative z-10 text-white">
                    <h3 class="text-3xl font-black mb-6 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-300"></i> SINAV HAFIZASI
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-white/10 backdrop-blur p-6 rounded-2xl border border-white/10">
                            <p class="font-bold text-indigo-200 mb-2">İstek Kipi Tuzağı</p>
                            <p class="text-sm">Adaylar genelde İstek Kipi olan "-e, -a" ekini gözden kaçırır. <strong>gideyim, yapalım</strong> kelimelerinde dilek kipi vardır.</p>
                        </div>
                        <div class="bg-white/10 backdrop-blur p-6 rounded-2xl border border-white/10">
                            <p class="font-bold text-indigo-200 mb-2">Nesne-Yüklem İlişkisi Oyunu</p>
                            <p class="text-sm">"Hangisi nesne-yüklem ilişkisine göre farklıdır?" gibi görünse de aslında "Hangisi iş, durum, oluş fiilidir?" ayrımını yoklayan sorular çıkar.</p>
                        </div>
                    </div>
                </div>
            </section>
        '''
    },
    {
        'filename': 'sozcuk-turleri-fiilimsiler.html',
        'title': 'Fiilimsiler (Eylemsiler)',
        'icon': 'fa-paperclip',
        'color': 'emerald',
        'html': '''
                <section class="note-card category-emerald p-6 md:p-8 rounded-2xl shadow-sm lg:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-emerald-900 dark:text-emerald-200">
                        <div class="bg-emerald-100 dark:bg-emerald-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-paperclip text-emerald-600 dark:text-emerald-300"></i>
                        </div>
                        Fiilimsi Türleri
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <div class="p-5 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-emerald-700 dark:text-emerald-400 block mb-2 text-lg">İsim-Fiil</strong>
                            <p class="text-xs text-slate-500 mb-3 font-mono font-bold bg-emerald-100 dark:bg-emerald-900/50 px-2 py-1 rounded inline-block">ma - y - ış - mak</p>
                            <p class="text-sm text-slate-700 dark:text-slate-300">Seninle konuşmaya geldim, şiir okuyuşunu beğendik.</p>
                        </div>
                        <div class="p-5 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-emerald-700 dark:text-emerald-400 block mb-2 text-lg">Sıfat-Fiil (Ortaç)</strong>
                            <p class="text-xs text-slate-500 mb-3 font-mono font-bold bg-emerald-100 dark:bg-emerald-900/50 px-2 py-1 rounded inline-block">anası mezar dikecekmiş</p>
                            <p class="text-sm text-slate-700 dark:text-slate-300">Yürüy-en merdiven, koşar adım, görünmez kaza.</p>
                        </div>
                        <div class="p-5 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-emerald-700 dark:text-emerald-400 block mb-2 text-lg">Zarf-Fiil (Ulaç)</strong>
                            <p class="text-xs text-slate-500 mb-3 font-mono font-bold bg-emerald-100 dark:bg-emerald-900/50 px-2 py-1 rounded inline-block">ıp, erek, ınca, ken, madan...</p>
                            <p class="text-sm text-slate-700 dark:text-slate-300">Binip gitti, hiç düşünmeden yanıtladı, koşa koşa geldi.</p>
                        </div>
                    </div>
                </section>

                <section class="note-card category-red p-6 md:p-8 rounded-2xl shadow-sm text-white lg:col-span-2" style="background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center">
                        <div class="bg-white/20 p-2.5 rounded-xl mr-3">
                            <i class="fas fa-ghost"></i>
                        </div>
                        Kalıcı İsim Tuzağı
                    </h3>
                    <div class="bg-white/10 p-5 rounded-2xl border border-white/20 text-sm leading-relaxed">
                        <p class="mb-4">Fiilimsi eklerini aldığı hâlde zamanla bir nesnenin/kavramın kalıcı adı olanlar fiilimsi SAYILMAZ: <strong>Dolmuş, dondurma, çakmak, döner, sarma</strong>.</p>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div class="bg-black/20 p-4 rounded-xl border border-white/10">
                                <p class="text-rose-200">"Danışma"da bekleyen kız... -> <strong class="text-white">Kalıcı İsim</strong></p>
                            </div>
                            <div class="bg-black/20 p-4 rounded-xl border border-white/10">
                                <p class="text-emerald-300">Bu konuyu "danışma"ya geldim... -> <strong class="text-white">İsim-Fiil</strong></p>
                            </div>
                        </div>
                    </div>
                </section>

            <!-- SINAV HAFIZASI -->
            <section class="note-card p-8 md:p-12 rounded-3xl shadow-2xl relative overflow-hidden group mt-12 exam-memory lg:col-span-2">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16"></div>
                <div class="relative z-10 text-white">
                    <h3 class="text-3xl font-black mb-4 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-300"></i> SINAV HAFIZASI
                    </h3>
                    <p class="text-sm leading-relaxed text-slate-200">
                        ÖSYM genellikle altı çizili sözcükler verip <strong>"Hangisi fiilimsi değildir?"</strong> diye sorar. Şıkların arasına yerleştirdikleri <strong>"yemek"</strong> veya <strong>"geçmiş"</strong> gibi kelimeler en çok düşülen kalıcı isim tuzaklarıdır.
                    </p>
                </div>
            </section>
        '''
    },
    {
        'filename': 'sozcuk-turleri-fiilde-cati.html',
        'title': 'Fiilde Çatı',
        'icon': 'fa-home',
        'color': 'amber',
        'html': '''
                <section class="note-card category-amber p-6 md:p-8 rounded-2xl shadow-sm lg:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-amber-900 dark:text-amber-200">
                        <div class="bg-amber-100 dark:bg-amber-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-home text-amber-600 dark:text-amber-300"></i>
                        </div>
                        Çatı Özellikleri
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div>
                            <h4 class="font-bold text-lg text-amber-700 dark:text-amber-400 mb-4 border-b border-amber-100 dark:border-amber-900/50 pb-2">Özne - Yüklem İlişkisi</h4>
                            <ul class="space-y-4 text-sm text-slate-700 dark:text-slate-300">
                                <li class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                                    <strong class="text-amber-600 dark:text-amber-400">Etken:</strong> İşi yapan bellidir. (Seni hep sevdim)
                                </li>
                                <li class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                                    <strong class="text-amber-600 dark:text-amber-400">Edilgen:</strong> İşi yapan belli değildir, <strong>-l, -n</strong> eki alır. (Adam görüldü)
                                </li>
                                <li class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                                    <strong class="text-amber-600 dark:text-amber-400">Dönüşlü:</strong> İşi yapan bellidir ve etkilenen de kendisidir. <strong>-l, -n</strong> eki alır. (Çok sevindi)
                                </li>
                                <li class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                                    <strong class="text-amber-600 dark:text-amber-400">İşteş:</strong> Karşılıklı veya birlikte yapılır. <strong>-ş</strong> eki alır. (selamlaştı)
                                </li>
                            </ul>
                        </div>
                        <div>
                            <h4 class="font-bold text-lg text-amber-700 dark:text-amber-400 mb-4 border-b border-amber-100 dark:border-amber-900/50 pb-2">Nesne - Yüklem İlişkisi</h4>
                            <ul class="space-y-4 text-sm text-slate-700 dark:text-slate-300">
                                <li class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                                    <strong class="text-amber-600 dark:text-amber-400">Geçişli:</strong> Nesne alabilir. (Neyi, kimi?)
                                </li>
                                <li class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                                    <strong class="text-amber-600 dark:text-amber-400">Geçişsiz:</strong> Nesne alamaz.
                                </li>
                                <li class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                                    <strong class="text-amber-600 dark:text-amber-400">Oldurgan:</strong> Geçişsiz fiili <strong>-r, -t, -tır</strong> ile geçişli yapmak. (piş- -> piş-ir-)
                                </li>
                                <li class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                                    <strong class="text-amber-600 dark:text-amber-400">Ettirgen:</strong> Zaten geçişli olan fiilin geçişliliğini artırmak, işi başkasına yaptırmak. (yap- -> yap-tır-)
                                </li>
                            </ul>
                        </div>
                    </div>
                </section>

                <section class="note-card category-red p-6 md:p-8 rounded-2xl shadow-sm text-white lg:col-span-2" style="background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center">
                        <div class="bg-white/20 p-2.5 rounded-xl mr-3">
                            <i class="fas fa-exclamation-circle"></i>
                        </div>
                        Altın Kural
                    </h3>
                    <p class="text-lg font-bold">Yüklemi isim olan cümlelerde kesinlikle çatı özelliği ARANMAZ!</p>
                </section>

            <!-- SINAV HAFIZASI -->
            <section class="note-card p-8 md:p-12 rounded-3xl shadow-2xl relative overflow-hidden group mt-12 exam-memory lg:col-span-2">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16"></div>
                <div class="relative z-10 text-white">
                    <h3 class="text-3xl font-black mb-4 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-300"></i> SINAV HAFIZASI
                    </h3>
                    <p class="text-sm leading-relaxed text-slate-200 mb-4">
                        ÖSYM çatı sorularında sıkça "Hangisinde çatı özelliği aranmaz?" diyerek yüklemin isim mi fiil mi olduğuna bakıp bakmadığınızı test eder.
                    </p>
                    <div class="bg-white/10 backdrop-blur p-4 rounded-xl border border-white/10 text-sm">
                        Edilgen ve Dönüşlü çatıların her ikisinin de <strong>-l, -n</strong> eki alması sınavın en klasik tuzağıdır. İşi kimin yaptığına (gerçek özne var mı?) bakarak bu tuzağı aşabilirsiniz.
                    </div>
                </div>
            </section>
        '''
    }
]

# Create all 8 files using yazim-kurallari-buyuk-harf.html as template
template_path = os.path.join(root_dir, 'yapi-sekil-kok-ve-yapim.html') # A valid inner page
with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

pattern = r'<div class="columns-1 xl:columns-2 gap-8 space-y-8">.*?</section>\s*</div>\s*<!-- SINAV HAFIZASI -->\s*<section.*?</section>'

for page in pages:
    content = template_content
    # Update titles
    content = re.sub(r'<title>.*?</title>', f'<title>{page["title"]} - KPSS Türkçe</title>', content)
    content = re.sub(r'<h2 class="text-3xl md:text-4xl font-black[^>]+>.*?</h2>', f'<h2 class="text-3xl md:text-4xl font-black text-slate-900 dark:text-white leading-tight tracking-tight">{page["title"]}</h2>', content)
    # Replace backlink
    content = content.replace('href="yapi-sekil.html"', 'href="sozcuk-turleri.html"')
    content = content.replace('Sözcükte Yapı Ana Menüye Dön', 'Sözcük Türleri Ana Menüye Dön')
    
    # Check if we need to replace columns container
    if 'lg:col-span-2' in page['html']:
        # if using grid col-span, maybe we change wrapper to grid instead of columns-1 xl:columns-2 space-y-8
        page_html = f'<div class="grid grid-cols-1 lg:grid-cols-2 gap-8">\n{page["html"]}\n</div>'
    else:
        page_html = f'<div class="columns-1 xl:columns-2 gap-8 space-y-8">\n{page["html"]}\n</div>'
        
    content = re.sub(pattern, page_html, content, flags=re.DOTALL)
    
    with open(os.path.join(root_dir, page['filename']), 'w', encoding='utf-8') as f:
        f.write(content)

# Create Hub Page `sozcuk-turleri.html`
hub_template_path = os.path.join(root_dir, 'yapi-sekil.html')
with open(hub_template_path, 'r', encoding='utf-8') as f:
    hub_content = f.read()

hub_content = re.sub(r'<title>.*?</title>', '<title>Sözcük Türleri - KPSS Türkçe</title>', hub_content)
hub_content = re.sub(r'<h2 class="text-3xl md:text-4xl font-black[^>]+>.*?</h2>', '<h2 class="text-3xl md:text-4xl font-black text-slate-900 dark:text-white leading-tight tracking-tight">Sözcük Türleri</h2>', hub_content)

cards_html = ""
for page in pages:
    cards_html += f'''
                <a href="{page['filename']}" class="group bg-white dark:bg-slate-800 rounded-3xl p-8 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-xl hover:-translate-y-2 transition-all duration-300 relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-{page['color']}-500/5 dark:bg-{page['color']}-500/10 rounded-bl-[100px] -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
                    <div class="w-16 h-16 bg-{page['color']}-100 dark:bg-{page['color']}-900/40 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform relative z-10">
                        <i class="fas {page['icon']} text-{page['color']}-600 dark:text-{page['color']}-400 text-2xl font-bold"></i>
                    </div>
                    <h3 class="font-extrabold text-slate-900 dark:text-white text-2xl mb-3 relative z-10">{page['title']}</h3>
                    <div class="inline-flex items-center text-{page['color']}-600 dark:text-{page['color']}-400 font-bold relative z-10 mt-4">
                        <span>Konuya Çalış</span>
                        <i class="fas fa-arrow-right ml-2 group-hover:translate-x-2 transition-transform"></i>
                    </div>
                </a>'''

hub_content = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 gap-6">.*?</div>', f'<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">\n{cards_html}\n</div>', hub_content, flags=re.DOTALL)

with open(os.path.join(root_dir, 'sozcuk-turleri.html'), 'w', encoding='utf-8') as f:
    f.write(hub_content)

# Update fix_all_sidebars.py script
fix_script = os.path.join(os.path.dirname(root_dir), 'fix_all_sidebars.py')
with open(fix_script, 'r', encoding='utf-8') as f:
    fix_code = f.read()

# We need to add Unit 5 to the menu_structure and remove it from flat_links!
new_unit = '''    {
        'id': 'sozcukTurleriSub',
        'title': '5. Sözcük Türleri',
        'icon': 'fa-tags',
        'links': [
            ('sozcuk-turleri-isimler.html', 'İsimler (Adlar) ve İsim Tamlamaları'),
            ('sozcuk-turleri-sifatlar.html', 'Sıfatlar (Ön Adlar) ve Sıfat Tamlamaları'),
            ('sozcuk-turleri-zamirler.html', 'Zamirler (Adıllar)'),
            ('sozcuk-turleri-zarflar.html', 'Zarflar (Belirteçler)'),
            ('sozcuk-turleri-edat-baglac.html', 'Edat, Bağlaç ve Ünlem'),
            ('sozcuk-turleri-fiiller.html', 'Fiillerde Kip, Çekim ve Anlam Özellikleri'),
            ('sozcuk-turleri-fiilimsiler.html', 'Fiilimsiler (Eylemsiler)'),
            ('sozcuk-turleri-fiilde-cati.html', 'Fiilde Çatı')
        ]
    }'''

fix_code = fix_code.replace("    }\n]\n\nflat_links", "    },\n" + new_unit + "\n]\n\nflat_links")
fix_code = fix_code.replace("('sozcuk-turleri.html', '5. Sözcük Türleri', 'fa-tags'),\n    ", "")
fix_code = fix_code.replace("'yapi-sekil': 'yapiSekilSub'", "'yapi-sekil': 'yapiSekilSub',\n        'sozcuk-turleri': 'sozcukTurleriSub'")

with open(fix_script, 'w', encoding='utf-8') as f:
    f.write(fix_code)

print("Unit 5 generated and sidebar script updated.")
