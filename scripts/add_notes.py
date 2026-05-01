import os
import re

additions = {
    "index.html": """
                <!-- EKLENEN KRİTİK KAVRAMLAR -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-thumbtack text-red-600 dark:text-red-300"></i></div>
                        Kritik Eklemeler ve Sınav İpuçları
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-slate-800 dark:text-red-100 font-medium text-sm">
                        <div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-xl border border-red-200 dark:border-red-800">
                            <strong class="text-red-800 dark:text-red-300 block mb-2">Tüz Kavramı:</strong> Devlet ile vatandaşın karşılıklı görevlerini bildiren <strong>yazısız sözleşmeye</strong> "Tüz" adı verilmiştir.
                        </div>
                        <div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-xl border border-red-200 dark:border-red-800">
                            <strong class="text-red-800 dark:text-red-300 block mb-2">Hükümet Terimleri:</strong> Hükümet'e <strong>"Ayuki"</strong>, Vezir'e ise <strong>"Aygucı (Üge)"</strong> denilirdi. ÖSYM kavram eşleştirmelerinde sıkça kullanır.
                        </div>
                        <div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-xl border border-red-200 dark:border-red-800">
                            <strong class="text-red-800 dark:text-red-300 block mb-2">Kutluk (İlteriş) Kağan:</strong> II. Göktürk devletini kuran Kutluk Kağan'a, devleti toparlayan anlamına gelen <strong>"İlteriş"</strong> unvanı verilmiştir.
                        </div>
                    </div>
                </section>""",
    "unitler/unite2.html": """
                <!-- EKLENEN KRİTİK KAVRAMLAR -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-microscope text-yellow-600 dark:text-yellow-300"></i></div>
                        Bilim İnsanları ve Sağlık (Sınavın Favorisi)
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-slate-800 dark:text-yellow-100 font-medium text-sm">
                        <div class="bg-yellow-50 dark:bg-yellow-900/20 p-4 rounded-xl border border-yellow-200 dark:border-yellow-800">
                            <ul class="space-y-3">
                                <li><strong>Farabi:</strong> <em>Muallim-i Sani</em> (İkinci Öğretmen). Birleşmiş Milletler fikrini ilk defa ortaya atmıştır.</li>
                                <li><strong>Gazali:</strong> <em>Hüccet-ül İslam</em> (İslam'ın ispatlayıcısı).</li>
                            </ul>
                        </div>
                        <div class="bg-yellow-50 dark:bg-yellow-900/20 p-4 rounded-xl border border-yellow-200 dark:border-yellow-800">
                            <ul class="space-y-3">
                                <li><strong>Biruni:</strong> <em>El-Üstad</em> veya <em>Aliboron</em>. Gazneli Mahmut onun için "Sarayımın en kıymetli hazinesi" demiştir.</li>
                                <li><strong>İbni Sina:</strong> <em>Avicenna</em>. El-Kanun Fit Tıbb adlı eseri yüzyıllarca Avrupa'da okutulmuştur.</li>
                            </ul>
                        </div>
                        <div class="bg-yellow-100 dark:bg-yellow-900/40 p-4 rounded-xl border border-yellow-300 dark:border-yellow-700 md:col-span-2">
                            <strong class="text-yellow-900 dark:text-yellow-200 block mb-1">Maristan / Bimaristan:</strong> İlk Türk-İslam devletlerinde (Özellikle Tolunoğulları ve Karahanlılarda) hastanelere ve akıl hastalarının tedavi edildiği yerlere verilen isimdir.
                        </div>
                    </div>
                </section>""",
    "unitler/unite3.html": """
                <!-- EKLENEN KRİTİK KAVRAMLAR -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-fire text-cyan-600 dark:text-cyan-300"></i></div>
                        Kritik İsyan ve Divan Kavramı
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-slate-800 dark:text-cyan-100 font-medium text-sm">
                        <div class="bg-cyan-50 dark:bg-cyan-900/20 p-4 rounded-xl border border-cyan-200 dark:border-cyan-800">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-2">Baba İshak (Babailer) İsyanı (1240):</strong> Türk tarihindeki ilk dinî ve sosyal nitelikli isyandır. Bu isyan Anadolu Selçuklu Devleti'ni çok yıpratmış ve devleti <strong>1243 Kösedağ Savaşı'nda Moğollara (İlhanlılara) karşı zayıf düşürmüştür</strong>.
                        </div>
                        <div class="bg-cyan-50 dark:bg-cyan-900/20 p-4 rounded-xl border border-cyan-200 dark:border-cyan-800">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-2">Divan-ı Pervane:</strong> İkta topraklarının kayıtlarını tutan ve dağıtan divandır, başındaki görevliye <strong>"Pervaneci"</strong> denir. Sadece Anadolu Selçuklularına has bir kurumdur.
                        </div>
                    </div>
                </section>""",
    "unitler/unite4.html": """
                <!-- EKLENEN KRİTİK KAVRAMLAR -->
                <section class="category-purple note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-users-cog text-purple-600 dark:text-purple-300"></i></div>
                        Yönetici Sınıf, Sistemler ve Ekonomi
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 text-slate-800 dark:text-purple-100 font-medium text-sm">
                        <div class="bg-purple-50 dark:bg-purple-900/20 p-4 rounded-xl border border-purple-200 dark:border-purple-800">
                            <strong class="text-purple-800 dark:text-purple-300 block mb-2">Yönetici Sınıf Ayrımı:</strong>
                            <ul class="space-y-2">
                                <li><strong>Seyfiye (Kılıç Ehli):</strong> Askerî/idari (Sadrazam, Yeniçeri Ağası).</li>
                                <li><strong>İlmiye (Eğitim/Hukuk):</strong> Din/hukuk (Şeyhülislam, Kadı, Kazasker).</li>
                                <li><strong>Kalemiye (Yazışma):</strong> Bürokrasi/maliye (Defterdar, Nişancı).</li>
                            </ul>
                        </div>
                        <div class="bg-purple-50 dark:bg-purple-900/20 p-4 rounded-xl border border-purple-200 dark:border-purple-800">
                            <strong class="text-purple-800 dark:text-purple-300 block mb-2">Pençik ve Devşirme Ayrımı:</strong>
                            Savaş esirlerinin beşte birinin asker yapıldığı "Pençik Sistemi" <strong>I. Murat</strong> döneminde; Hristiyan çocuklarının toplanıp yetiştirildiği "Devşirme Sistemi" ise <strong>Çelebi Mehmet ve II. Murat</strong> döneminde sistemleşmiştir.
                        </div>
                        <div class="bg-purple-50 dark:bg-purple-900/20 p-4 rounded-xl border border-purple-200 dark:border-purple-800 lg:col-span-1 md:col-span-2">
                            <strong class="text-purple-800 dark:text-purple-300 block mb-2">Kapan ve Bedesten:</strong>
                            Tek bir cins malın toptan satıldığı (Un kapanı gibi) yerlere <strong>Kapan</strong>; değerli kumaş ve mücevherlerin satıldığı, kapalı çarşıların temeli olan yerlere <strong>Bedesten</strong> denir.
                        </div>
                    </div>
                </section>""",
    "unitler/unite5.html": """
                <!-- EKLENEN KRİTİK KAVRAMLAR -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-swords text-red-600 dark:text-red-300"></i></div>
                        Kritik Savaşlar ve İsyanlar
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-slate-800 dark:text-red-100 font-medium text-sm">
                        <div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-xl border border-red-200 dark:border-red-800">
                            <strong class="text-red-800 dark:text-red-300 block mb-2">Pelekanon (Maltepe) Savaşı (1329):</strong> Orhan Bey döneminde Bizans ile yapılan ve İznik'in alınmasına zemin hazırlayan çok önemli bir savaştır.
                        </div>
                        <div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-xl border border-red-200 dark:border-red-800">
                            <strong class="text-red-800 dark:text-red-300 block mb-2">Buçuktepe İsyanı ve Edirne-Segedin:</strong> II. Murat döneminde Haçlılarla imzalanan barış antlaşması <em>Edirne-Segedin</em> (1444)'dir. II. Murat'ın tahtı küçük yaştaki oğlu II. Mehmet'e (Fatih) bırakması üzerine Osmanlı tarihindeki <strong>ilk Yeniçeri isyanı olan Buçuktepe İsyanı</strong> çıkmıştır.
                        </div>
                    </div>
                </section>""",
    "unitler/unite6.html": """
                <!-- EKLENEN KRİTİK KAVRAMLAR -->
                <section class="category-yellow note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-yellow-900 dark:text-yellow-200">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-crown text-yellow-600 dark:text-yellow-300"></i></div>
                        Yükselme Dönemi Ekstra Bilgiler
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-slate-800 dark:text-yellow-100 font-medium text-sm">
                        <div class="bg-yellow-50 dark:bg-yellow-900/20 p-4 rounded-xl border border-yellow-200 dark:border-yellow-800">
                            <strong class="text-yellow-800 dark:text-yellow-300 block mb-2">Fatih Sultan Mehmet Eklemeleri:</strong>
                            <ul class="space-y-2">
                                <li>İstanbul'un fethinden sonra <strong>"Kayser-i Rum"</strong> (Roma İmparatoru) unvanını almıştır.</li>
                                <li>Örfi hukuku yazılı hâle getirdiği <strong>"Kanunname-i Ali Osman"</strong>ı yayınlamış; kardeş katlini ve müsadereyi yasal hâle getirmiştir.</li>
                                <li>Devletin uzun süre yönetim merkezi olacak <strong>Topkapı Sarayı'nı</strong> ve <strong>Sahn-ı Seman Medreseleri'ni</strong> kurdurmuştur.</li>
                            </ul>
                        </div>
                        <div class="bg-yellow-50 dark:bg-yellow-900/20 p-4 rounded-xl border border-yellow-200 dark:border-yellow-800">
                            <strong class="text-yellow-800 dark:text-yellow-300 block mb-2">Yavuz ve Kanuni Eklemeleri:</strong>
                            <ul class="space-y-2">
                                <li>1515 <strong>Turnadağ Savaşı</strong> ile Dulkadiroğulları beyliğini yıkmış, Anadolu Türk siyasi birliğini <strong>KESİN OLARAK</strong> sağlamıştır.</li>
                                <li>Mercidabık ve Ridaniye ile Memlükleri yıkmış; <strong>Halifelik makamı</strong> Osmanlı'ya geçerek Teokratik yapı güçlenmiştir.</li>
                                <li>Kanuni, <strong>Mohaç Meydan Muharebesi</strong> (2 saat) ile Macaristan'ı himaye altına almıştır.</li>
                            </ul>
                        </div>
                    </div>
                </section>""",
    "unitler/unite10.html": """
                <!-- EKLENEN KRİTİK KAVRAMLAR -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-book text-red-600 dark:text-red-300"></i></div>
                        Sarı Kitap ve Gizli Antlaşmalar
                    </h3>
                    <div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-xl border border-red-200 dark:border-red-800 text-slate-800 dark:text-red-100 font-medium text-sm">
                        I. Dünya Savaşı yıllarında İtilaf Devletlerinin kendi aralarında yaptığı ve Osmanlı'yı paylaştıkları "Gizli Antlaşmaları" (Sykes-Picot, Mac Mahon vb.) dünya kamuoyuna <strong>"Sarı Kitap" adı verilen belgeyle ilk duyuran devlet Sovyet Rusya'dır</strong> (Bolşevik İhtilali sonrası savaştan çekildikleri için ifşa etmişlerdir).
                    </div>
                </section>""",
    "unitler/unite15.html": """
                <!-- EKLENEN KRİTİK KAVRAMLAR -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-bomb text-red-600 dark:text-red-300"></i></div>
                        Nasturi Ayaklanması
                    </h3>
                    <div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-xl border border-red-200 dark:border-red-800 text-slate-800 dark:text-red-100 font-medium text-sm">
                        <strong>Nasturi Ayaklanması (1924):</strong> İngilizlerin Musul'u Türkiye'ye bırakmamak ve Türk ordusunu yıpratmak amacıyla Hakkâri bölgesinde kışkırttığı azınlık ayaklanmasıdır. Şeyh Sait isyanından bir yıl önce yaşanmıştır.
                    </div>
                </section>""",
    "unitler/unite17.html": """
                <!-- EKLENEN KRİTİK KAVRAMLAR -->
                <section class="category-turquoise note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-cyan-900 dark:text-cyan-200">
                        <div class="bg-cyan-100 dark:bg-cyan-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-university text-cyan-600 dark:text-cyan-300"></i></div>
                        Eğitim ve Sanat İnkılapları
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-slate-800 dark:text-cyan-100 font-medium text-sm">
                        <div class="bg-cyan-50 dark:bg-cyan-900/20 p-4 rounded-xl border border-cyan-200 dark:border-cyan-800">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-2">Albert Malche Raporu:</strong> 1933 yılında İsviçreli profesör Albert Malche'nin hazırladığı rapor doğrultusunda <strong>Darülfünun</strong> kapatılmış, yerine <strong>İstanbul Üniversitesi</strong> açılmıştır.
                        </div>
                        <div class="bg-cyan-50 dark:bg-cyan-900/20 p-4 rounded-xl border border-cyan-200 dark:border-cyan-800">
                            <strong class="text-cyan-800 dark:text-cyan-300 block mb-2">Güzel Sanatlar:</strong> Osmanlı'dan kalan Sanayi-i Nefise Mektebi, 1928'de <strong>Güzel Sanatlar Akademisi'ne</strong> dönüştürülmüştür.
                        </div>
                    </div>
                </section>""",
    "unitler/unite22.html": """
                <!-- EKLENEN KRİTİK KAVRAMLAR -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-handshake-slash text-red-600 dark:text-red-300"></i></div>
                        Yatıştırma Politikası
                    </h3>
                    <div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-xl border border-red-200 dark:border-red-800 text-slate-800 dark:text-red-100 font-medium text-sm">
                        <strong>Yatıştırma Politikası:</strong> II. Dünya Savaşı öncesinde İngiltere Başbakanı <strong>Chamberlain'in</strong>, Almanya'nın (Hitler'in) yayılmacı politikasını engellemek için tavizler vererek uyguladığı politikanın adıdır.
                    </div>
                </section>""",
    "unitler/unite24.html": """
                <!-- EKLENEN KRİTİK KAVRAMLAR -->
                <section class="category-red note-card p-6 md:p-8 rounded-3xl xl:col-span-2">
                    <h3 class="text-xl font-extrabold mb-4 flex items-center text-red-900 dark:text-red-200">
                        <div class="bg-red-100 dark:bg-red-900/50 p-2.5 rounded-xl mr-3 shadow-sm"><i class="fas fa-skull-crossbones text-red-600 dark:text-red-300"></i></div>
                        Enosis ve Akritas Planı
                    </h3>
                    <div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-xl border border-red-200 dark:border-red-800 text-slate-800 dark:text-red-100 font-medium text-sm">
                        Kıbrıs Rumlarının Kıbrıs'ı Yunanistan'a bağlama idealine <strong>"Enosis"</strong>, bu amaca ulaşmak için Türkleri adadan yok etmeyi planladıkları vahşi plana ise <strong>"Akritas Planı"</strong> denir.
                    </div>
                </section>"""
}

# Apply additions right before the "SINAV HAFIZASI" section or at the end of the columns container.
# The container is: <div class="columns-1 xl:columns-2 gap-8 space-y-8">
for filename, content_to_add in additions.items():
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We want to insert the content right before </div>\n            <!-- SINAV HAFIZASI BÖLÜMÜ -->
    # or find the end of the columns div.
    pattern = r'(?=</?div>\s*<!-- SINAV HAFIZASI BÖLÜMÜ -->)'
    
    if re.search(pattern, html):
        html = re.sub(pattern, content_to_add + "\n            ", html, count=1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Added content to {filename}")
    else:
        print(f"Could not find insert point in {filename}")
