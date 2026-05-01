import os
import re

root_dir = r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı\turkce'

analyses = {
    'ses-bilgisi.html': {
        'en_cok': [
            "Ünsüz Benzeşmesi (Sertleşmesi) ve Ünsüz Yumuşaması",
            "Ünlü Düşmesi",
            "Ünlü Daralması",
            "Ünsüz Düşmesi"
        ],
        'favori_soru': "ÖSYM, son yıllarda tek bir ses olayını nadiren sorar. Sınavların vazgeçilmez kalıbı, bir paragraf veya şiir verip \"Bu parçada aşağıdaki ses olaylarından hangisi yoktur?\" diye sormaktır. Bu soru tipiyle tek soruda tüm ses bilgisi hâkimiyetinizi ölçer.",
        'detaylar': [
            ("Ünlü Düşmesinde Kelime Avı", "ÖSYM artık \"akıl-ı -> aklı\" gibi basit çekim ekli düşmeleri sormayı bıraktı. Bunun yerine sözcüğün yapım eki alırken ünlü kaybettiği \"türetilirken ünlü düşmesi\" örneklerini paragrafa saklar. Çıkmış sorulardaki en tehlikeli gizli düşmeler şunlardır: ayrıntı (ayır-ıntı), kıvrım (kıvır-ım), benzeyen (beniz-e-yen), oynuyor (oyun-a-yor)."),
            ("Ünlü Daralmasındaki \"-yor\" İlizyonu", "Sınavın en büyük çeldiricilerinden biridir. Şıklarda \"ünlü daralması\" ararken her \"-yor\" eki alan kelimeye atlamanızı beklerler. \"Geliyor\" veya \"seviyor\" kelimelerinde daralma yoktur; oradaki \"i\" sadece koruyucu/yardımcı ünlüdür. Gerçek daralma için eylemin son harfinin mutlaka \"a\" veya \"e\" olması gerekir (başla-yor -> başlıyor)."),
            ("Gizli Daralma Bekçileri", "İçinde \"-yor\" eki geçmediği hâlde daralma barındıran üç sihirli kelime ÖSYM'nin kurtarıcılarıdır: \"diye\" (de-y-e), \"niye\" (ne-y-e) ve \"yiyecek\" (ye-y-ecek). Bunları metne ustaca yerleştirip adayların gözünden kaçmasını umarlar."),
            ("\"Gülücük\" Tuzağı", "Soru bankalarında ve çıkmış dil bilgisi testlerinde adaylar \"-cık, -cik\" ekini görünce refleks olarak \"ünlü türemesi\" (dar-a-cık gibi) der. Ancak gülücük ve öpücük kelimeleri, \"gülüş-cük\" ve \"öpüş-cük\"ten geldiği için ünlü türemesi değil, ünsüz düşmesidir."),
            ("Sinsi Ünsüz Düşmeleri", "\"Ufacık\" (ufak-cık) gibi bilinen örneklerin yanı sıra, \"kaldırım\" (kalk-dırım) kelimesini ünsüz düşmesi olarak çıkmış sorularda kullanıp birçok adayı elemişlerdir.")
        ],
        'uyarilar': [
            "\"Gülücük\" ve \"öpücük\" kelimelerinde ünlü türemesi kesinlikle yoktur, ünsüz düşmesi vardır.",
            "Cümlede \"diye\", \"diyen\" veya \"niye\" kelimelerini gördüğün an hiç düşünmeden \"Ünlü Daralması vardır\" diyebilirsin.",
            "Ünsüz türemesi ararken \"hisseden\" (his-s-etmek) veya \"hakkı\" (hak-k-ı) gibi Arapça kökenli kelimelere odaklan."
        ]
    },
    'yazim-kurallari.html': {
        'en_cok': [
            "Birleşik Sözcüklerin Yazımı (Anlam kayması, somut yer bildirmeyen alt/üst kelimeleri)",
            "Büyük Harflerin Kullanımı (Coğrafi yerler, kurum-kuruluş adları, unvanlar)",
            "Bitişik/Ayrı Yazılan Kelimeler (\"Şey\", ikilemeler, belgisiz sözcükler)",
            "Kısaltmaların ve Sayıların Yazımı"
        ],
        'favori_soru': "Paragraf içinde numaralanmış kelimeler vererek, karma kural bilgisini tek soruda test ettiği \"Bu parçada numaralanmış sözlerden hangisinin yazımı yanlıştır?\" kalıbı.",
        'detaylar': [
            ("Anlam Kayması İlizyonu (Bitişik/Ayrı)", "Kelimelerden her ikisi veya ikincisi gerçek anlamını yitirmişse kelime bitişik yazılır. ÖSYM 2022 sınavında bu kuralı efsanevi bir tuzakla sormuştur: Keçiboynuzu bitki adıysa bitişik yazılır; ancak sorudaki \"hayvan boynuzu\" gerçek anlamında kullanıldığı için ayrı yazılması gerekirken bitişik verilerek adaylar elenmiştir."),
            ("Somut Yer Bildirmeyen Alt/Üst Tuzağı", "\"Alt, üst, üzeri\" sözcükleri somut bir yer (mekân) bildirmiyorsa kesinlikle bitişik yazılır. Çıkmış sorularda olağanüstü (2020'de \"olağan üstü\" yazılarak soruldu), akşamüstü ve bilinçaltı kelimeleri en popüler çeldiricilerdir."),
            ("Büyük Harflerde \"Cins İsim\" Kamuflajı", "Özel isme dâhil olmayan il, ilçe, belde, köy vb. sözcükler küçük harfle başlar. ÖSYM, \"Trabzon'un Araklı ilçesi\" veya \"Osmanlı tarihi\" (2018 sorusu) gibi kullanımlarda cins ismin ilk harfini bilerek büyük yazıp gözden kaçmanızı bekler. Özel ada dâhil olan coğrafi yerler her kelimesi büyük harfle başlayacak şekilde yazılır."),
            ("İkilemeler ve \"Bir\" Karmaşası", "İkilemeler her zaman ayrı yazılır ve aralarına hiçbir noktalama işareti konmaz. ÖSYM 2014'te yanyana, 2020'de renkrenk yazarak kuralı ihlal etmiştir. Ayrıca \"birtakım\" kelimesi bazı anlamındaysa bitişik, sayı anlamındaysa ayrı yazılır; 2018'de \"bir takım cihazlar\" şeklinde ayrı yazılarak tuzak kurulmuştur. \"Şey\" kelimesi daima ayrı yazılır.")
        ],
        'uyarilar': [
            "Kurum, kuruluş, kurul ve iş yeri adlarına gelen ekler KESİNLİKLE kesme işaretiyle ayrılmaz. (Örn: Türk Dil Kurumuna, Bakanlar Kurulunun)",
            "Kısaltmalara getirilen eklerde kelimenin uzun okunuşuna değil, kısaltmanın son harfinin okunuşuna bakılır. (KYK'nin, RTÜK'e doğrudur. Ölçü birimlerinde nokta kullanılmaz: kg'dan)",
            "\"İç, dış, sıra\" sözcükleriyle oluşturulan birleşik kelimeler ve terimler ayrı yazılır. (Yurt içi, hafta sonu, peşi sıra)"
        ]
    },
    'noktalama.html': {
        'en_cok': [
            "Virgülün Kullanılmadığı Yerler (Zarf-fiiller, şart ekleri ve tamlamalar arası)",
            "Virgül ile Noktalı Virgül Ayrımı (Öge gruplandırmaları)",
            "Kesme İşaretinin İstisnaları (Kurum/kuruluş adları, yapım eklerinden sonraki durum)",
            "İki Nokta (Açıklama ve örnekleme farkı)"
        ],
        'favori_soru': "ÖSYM'nin en klasik formatı paragraf içinde yay ayraç ( ) ile boşluklar bırakıp \"Bu parçada boş bırakılan yerlere sırasıyla hangileri getirilmelidir?\" diye sormasıdır. Diğer bir favorisi ise metin içindeki beş virgülün altını çizip \"Hangisinin kullanımı yanlıştır?\" sorusudur.",
        'detaylar': [
            ("Tek Zarf-Fiil ve Şart Kipi Tuzağı", "ÖSYM'nin en çok elediği kural budur. Cümle içinde -ip, -erek, -meden, -dıkça, -ınca gibi zarf-fiil eklerinden veya -sa/-se şart kipinden sonra okurken doğal bir duraksama olur; ÖSYM tam bu duraksama noktasına virgül koyarak sizi avlamaya çalışır. Ancak kural nettir: Metin içinde tek bir zarf-fiil veya şart eki varsa asla virgül konmaz."),
            ("Virgül ile Noktalı Virgül Çatışması", "Noktalı virgül (;) ÖSYM sorularında ancak ve ancak \"cümlede halihazırda en az bir virgül varsa\" doğru cevap olabilir. ÖSYM virgül barındırmayan basit sıralı cümlelerin arasına noktalı virgül koyarak hata yapmanızı bekler."),
            ("Ayrılmayan Tamlamalar ve Bağlaçlar", "İsim ve sıfat tamlamalarında tamlayan ile tamlanan arasına kesinlikle hiçbir noktalama işareti giremez. Aynı şekilde \"ve, veya, yahut\" veya \"ne... ne\" gibi bağlaçlardan önce veya sonra virgül konmaz."),
            ("Bölünemeyen \"Kurumlar\" ve \"Yapım Ekleri\"", "1. Kurum, kuruluş ve iş yeri adlarına gelen ekler asla ayrılmaz. 2. Özel isme bir yapım eki geldiğinde (Türkçe, Konyalı) kesme kullanılmaz; daha tehlikelisi, yapım ekinden sonra gelen çekim ekleri de ayrılmaz (Türkçenin, Konyalıdan)."),
            ("İki Noktadan (:) Sonraki Harfin Büyüklüğü", "Kural şudur: İki noktadan sonra gelen kısım tam bir cümle niteliğindeyse büyük harfle başlar, sadece örnekler sıralanıyorsa küçük harfle başlar.")
        ],
        'uyarilar': [
            "Metin içinde \"tek\" bir zarf-fiil eki almış kelimeden veya \"-sa/-se\" şart ekinden sonra KESİNLİKLE virgül kullanılmaz.",
            "Kurum, kuruluş, kurul ve birleşim adlarına gelen ekler KESİNLİKLE kesme işaretiyle ayrılmaz.",
            "Cümlede bağlaç varsa ya da isim/sıfat tamlaması bölünüyorsa araya virgül KESİNLİKLE girmez."
        ]
    },
    'yapi-sekil.html': {
        'en_cok': [
            "Kök Türü Bulma (İsim kökü mü, Fiil kökü mü?)",
            "İyelik Eki ile Belirtme (Yükleme) Hâl Ekinin Ayrımı",
            "Yapım Eklerinin Görevi (İsimden fiil, fiilden isim vb.)",
            "Sözcüğün Yapısı (Basit, Türemiş, Birleşik)"
        ],
        'favori_soru': "ÖSYM bu konuda iki kalıptan vazgeçmez. Birincisi beş kelimenin altını çizip doğrudan \"Hangisi kökünün türü bakımından farklıdır?\" diye sormaktır. İkincisi ise bir kelime verip özellikleri hakkında \"Hangisi yanlıştır?\" diyerek tek soruda tüm ek/kök bilginizi taramaktır.",
        'detaylar': [
            ("Sinsi İsim Kökleri", "\"Kök türü\" sorularında ÖSYM eylem gibi görünen ama aslında isim olan kökleri şıklara gizler. Sınavlarda en çok can yakan kelimeler şunlardır: yaşayan (kökü \"yaş\" ismidir), başladı (kökü \"baş\" ismidir), kanadı (kökü \"kan\" ismidir), yolladı (kökü \"yol\" ismidir)."),
            ("Yansıma Sözcüklerin Kökü", "2023 sınavında parıldayan kelimesinin kökü sorularak birçok aday elenmiştir. Doğadaki yansıma seslerin (parıl, gürül, şırıl, tıkır vb.) tamamı isim kökü kabul edilir."),
            ("İyelik Eki vs. Belirtme Hâl Eki Çatışması", "İkisi de kelime sonuna \"-ı, -i, -u, -ü\" olarak gelir. ÖSYM bunu her yıl mutlaka sorar. Kelimenin başına \"onun / onların\" getirebiliyorsanız o ek iyelik ekidir, getiremiyor ve sadece \"neyi/kimi\" sorusuna cevap alıyorsanız belirtme hâl ekidir."),
            ("\"Diye\" Kelimesindeki Yapı İllüzyonu", "Adaylar metin içinde \"diye\" sözcüğünü görünce basit bir kelime sanır. Oysa ÖSYM 2017 çıkmış sorusunda bunu test etmiş ve avlamıştır; \"diye\" sözcüğü \"de-y-e\" şeklinde zarf-fiil eki alarak türediği için yapıca türemiş bir sözcüktür."),
            ("Yapım Ekini Yanlış Adlandırma", "ÖSYM 2016'da kurbağalama kelimesini verip şıklara \"fiilden fiil yapım eki almıştır\" yazarak bir tuzak kurmuştur. \"Kurbağa\" isim olduğu için isimden isim yapım eki almıştır.")
        ],
        'uyarilar': [
            "\"Yaşayan\", \"başlıyor\", \"kanayan\", \"yolladı\" kelimelerinin kökü eylem değil, KESİNLİKLE isim köküdür.",
            "\"Diye\" ve \"niye\" sözcükleri zarf-fiil/yönelme eki aldıkları için KESİNLİKLE türemiş sözcüklerdir.",
            "Yansıma sözcüklerin (parıl, gürül, pat vb.) tümü istisnasız İSİM KÖKÜ kabul edilir."
        ]
    },
    'sozcuk-turleri.html': {
        'en_cok': [
            "Karma Sözcük Türleri (Altı çizili 5 kelimenin türünü sırasıyla bulma)",
            "Edat ve Bağlaç Ayrımı (Özellikle \"ile, yalnız, ancak\" kelimeleri)",
            "Niteleme Sıfatı ile Durum Zarfı Çatışması",
            "Belgisiz Sıfat ve Belgisiz Zamir Ayrımı"
        ],
        'favori_soru': "ÖSYM son 10 yılda tek bir sözcük türünü nadiren sormuştur. Klasikleşen şablonu, bir paragraf verip 5 farklı kelimenin altını çizmek ve \"Bu parçadaki altı çizili sözcüklerin türleri sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?\" diye sormaktır.",
        'detaylar': [
            ("\"İle\", \"Yalnız\" ve \"Ancak\" Kapanı", "Sınavın en tehlikeli ve en çok sorulan kelimeleridir. ÖSYM defalarca yoklamıştır. \"İle\" sözcüğünün yerine \"ve\" koyabiliyorsanız bağlaç, koyamıyorsanız edattır. \"Yalnız\" ve \"ancak\" sözcükleri ise \"sadece\" anlamındaysa edat, \"ama/fakat\" anlamındaysa bağlaçtır."),
            ("İkilemelerin İki Yüzü", "ÖSYM ikilemeleri cümle içinde verip görevini sormayı çok sever. 2011'de “pırıl pırıl parlıyordu” (zarf) ile “kucak kucak papatyalar” (sıfat) ifadelerini aynı soruda şıklara yerleştirerek eleyici bir tuzak kurmuştur."),
            ("Zaman Zarfı İllüzyonu", "2018 sınavında \"gece\" kelimesini “Gece yanan bir ateşin…” şeklinde kullanıp zarf olarak sormuştur. Eğer ne zaman yapıldığını bildiriyorsa zaman zarfı; kavramın adı olarak kullanılmışsa (Örn: Geceyi hiç sevmem) isimdir."),
            ("İşaret Zamiri ile İşaret Sıfatının Savaşı", "2022'de “bu cümbüşün içinde” diyerek ismin önüne getirdiği için işaret sıfatı yaparken; 2018'de “böyledir bu.” diyerek ismin yerine geçirdiği için işaret zamiri olarak sormuştur."),
            ("Gizli Zarflar", "\"Ne\" sözcüğünün \"niçin\" anlamında kullanılması her zaman soru zarfıdır. Ayrıca \"en, daha, çok\" gibi miktar zarfları bazen bir fiili değil, bir sıfatı derecelendirmek için kullanılır.")
        ],
        'uyarilar': [
            "İçeri, dışarı, aşağı, yukarı gibi yer-yön kelimeleri KESİNLİKLE ek almazlar; ek aldıkları an (içeriye) zarf olmaktan çıkıp isim olurlar.",
            "Bir kelimenin \"Nasıl\" sorusuna verdiği cevap isme yönelikse Niteleme Sıfatı, fiile/fiilimsiye yönelikse Durum Zarfıdır.",
            "\"O\" ve \"Onlar\" sözcükleri insan isminin yerini tutuyorsa Şahıs Zamiri, cansız bir varlığın yerini tutuyorsa İşaret Zamiridir."
        ]
    },
    'cumlenin-ogeleri.html': {
        'en_cok': [
            "Öge Dizilişini (Sırasını) Bulma",
            "Parçalanmaması Gereken Söz Öbekleri (Tamlamalar ve Fiilimsi grupları)",
            "Özne ve Belirtisiz Nesne Çatışması (\"Ne?\" sorusu)",
            "Cümle Dışı Unsurlar (Ara sözler, ünlemler, bağlaçlar)"
        ],
        'favori_soru': "ÖSYM'nin bu konudaki banko soru kalıbı, upuzun ve karmaşık bir cümle verip \"Bu cümlenin ögeleri sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?\" diye sormaktır. Diğer bir sevdiği kalıp ise eğik çizgilerle (/) ayrılmış cümleler verip hata buldurmaktır.",
        'detaylar': [
            ("Bölünmeyen Devasa Bloklar", "ÖSYM'nin en çok can yaktığı yer burasıdır. İsim tamlamaları, sıfat tamlamaları, birleşik fiiller ve deyimler kesinlikle parçalanamaz. Çıkmış bir soruda \"Yüksek duvarların ortasındaki büyük kapının önünden geçen yol\" ifadesinin tamamı bölünmeden tek bir \"Özne\" olarak kabul edilmiştir."),
            ("Gizli İsim Yüklemleri", "Adaylar genellikle yüklemi sonda duran tek bir fiil olarak arar. Ancak ÖSYM çıkmış sorularda yüklemi sıklıkla ek fiil almış uzun bir isim tamlaması olarak verir. Örneğin, \"sürecin en önemli adımıdır\" ifadesi tek başına yüklemdir, bölünemez."),
            ("\"Ne\" Sorusunun Kapanı", "Yükleme sorulan \"Ne\" sorusu hem Özneyi hem de Belirtisiz Nesneyi buldurur. ÖSYM, nesneyi başa veya özneye yakın bir yere koyarak sizi avlamaya çalışır. Altın kural: Yüklemden sonra daima önce özne bulunur."),
            ("Cümle Dışı Unsur (CDU) Kamuflajı", "Hitaplar, ünlemler, bağlaçlar (\"fakat, ama, ki\") ve ara sözler hiçbir soruya cevap vermez ve öge tablosuna dâhil edilmez. ÖSYM bu kelimelere \"Zarf Tümleci\" demenizi umar.")
        ],
        'uyarilar': [
            "İsim tamlamaları, sıfat tamlamaları, deyimler ve birleşik fiiller ögelere ayırırken KESİNLİKLE bölünmez, tek bir öge olarak alınır.",
            "Bir cümleyi çözümlerken şaşmaz kural şudur: Önce YÜKLEM, sonra ÖZNE bulunur; diğer sorular daima bu ikiliden sonra sorulur.",
            "\"Nere\" sorusuna cevap veren içeri, dışarı, aşağı, yukarı gibi kelimeler ek almamışsa Zarf Tümleci, ek almışsa Dolaylı Tümleç olur."
        ]
    }
}

def build_html(data):
    encok_li = "".join([f'<li class="flex items-start"><i class="fas fa-check-circle text-rose-400 mt-1 mr-2"></i> {item}</li>' for item in data['en_cok']])
    
    detay_divs = ""
    for title, content in data['detaylar']:
        detay_divs += f'''
                                <div class="p-4 rounded-2xl bg-slate-50 dark:bg-slate-900/50 border border-slate-100 dark:border-slate-800">
                                    <strong class="block text-indigo-600 dark:text-indigo-400 mb-1">{title}</strong>
                                    <p class="text-sm text-slate-700 dark:text-slate-300 leading-relaxed">{content}</p>
                                </div>'''

    uyari_li = "".join([f'<li class="flex items-start"><i class="fas fa-arrow-right mt-1 mr-3 text-rose-300"></i><span>{item}</span></li>' for item in data['uyarilar']])

    return f'''
            <!-- ÇIKMIŞ ANALİZLERİ -->
            <section class="mt-12 space-y-8 animate-fade-in">
                <div class="flex items-center space-x-4 mb-8">
                    <div class="h-px flex-1 bg-slate-200 dark:bg-slate-700"></div>
                    <h2 class="text-2xl md:text-3xl font-black text-slate-800 dark:text-white tracking-tight flex items-center">
                        <i class="fas fa-chart-line text-rose-500 mr-3"></i> Çıkmış Soru Analizleri
                    </h2>
                    <div class="h-px flex-1 bg-slate-200 dark:bg-slate-700"></div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    <!-- Sol Kolon: İstatistikler ve Soru Tipi -->
                    <div class="space-y-6 lg:col-span-1">
                        <div class="bg-white dark:bg-slate-800 p-6 rounded-3xl border border-slate-100 dark:border-slate-700 shadow-sm relative overflow-hidden">
                            <div class="absolute top-0 right-0 w-24 h-24 bg-rose-500/10 rounded-bl-full -mr-4 -mt-4"></div>
                            <h4 class="font-black text-slate-800 dark:text-white text-lg mb-4 flex items-center">
                                <i class="fas fa-fire text-rose-500 mr-2"></i> En Çok Sorulanlar
                            </h4>
                            <ul class="space-y-3 text-sm text-slate-600 dark:text-slate-400 font-medium relative z-10">
                                {encok_li}
                            </ul>
                        </div>
                        
                        <div class="bg-gradient-to-br from-indigo-500 to-purple-600 p-6 rounded-3xl shadow-lg text-white">
                            <h4 class="font-black text-white text-lg mb-3 flex items-center">
                                <i class="fas fa-crosshairs text-indigo-200 mr-2"></i> Favori Soru Tipi
                            </h4>
                            <p class="text-sm text-indigo-50 leading-relaxed font-medium">{data['favori_soru']}</p>
                        </div>
                    </div>

                    <!-- Sağ Kolon: Detaylı Analizler -->
                    <div class="lg:col-span-2 space-y-6">
                        <div class="bg-white dark:bg-slate-800 p-6 md:p-8 rounded-3xl border border-slate-100 dark:border-slate-700 shadow-sm">
                            <h4 class="font-black text-slate-800 dark:text-white text-xl mb-6 flex items-center">
                                <i class="fas fa-microscope text-indigo-500 mr-3"></i> Detaylı Sınav Analizi
                            </h4>
                            <div class="space-y-4">
                                {detay_divs}
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Kritik Uyarı Paneli -->
                <div class="note-card bg-rose-600 p-8 rounded-3xl shadow-xl shadow-rose-200 dark:shadow-none text-white relative overflow-hidden mt-6">
                    <div class="absolute right-0 top-0 w-64 h-64 bg-white/10 rounded-full blur-3xl -mr-16 -mt-16"></div>
                    <h3 class="text-2xl font-black mb-6 flex items-center relative z-10">
                        <i class="fas fa-exclamation-triangle text-3xl mr-4"></i> Bunu Bilmeden Sınava Girme!
                    </h3>
                    <ul class="space-y-4 relative z-10 text-rose-50 font-medium">
                        {uyari_li}
                    </ul>
                </div>
            </section>
'''

for filename, data in analyses.items():
    filepath = os.path.join(root_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if '<!-- ÇIKMIŞ ANALİZLERİ -->' in content:
        print(f"Already processed: {filename}")
        continue
        
    # We want to insert this right before </main> or after the main grid
    # A safe place is right before </main>
    # In some pages, </main> might be followed by </div>.
    
    new_html = build_html(data)
    content = content.replace('</main>', new_html + '\n        </main>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Analyses added successfully.")
