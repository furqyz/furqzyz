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

for filename, content_to_add in additions.items():
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Let's find <section class="exam-memory
    # However, we must ensure we insert it inside the <div class="columns-1 ..."> </div>
    # Actually, exam-memory is usually OUTSIDE the columns div!
    # So we should find the END of the columns div.
    # We can just match the exam-memory and insert right before it, but outside columns. That's fine since we gave it col-span-2 if it were inside. But as a normal block, it's fine.
    
    pattern = r'(\s*<!-- SINAV HAFIZASI|\s*<section class="exam-memory)'
    
    if re.search(pattern, html):
        html = re.sub(pattern, "\n            </div>\n            <div class=\"columns-1 gap-8 space-y-8\">\n" + content_to_add + "\n            </div>\n" + r'\1', html, count=1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Added content to {filename}")
    else:
        print(f"Could not find insert point in {filename}")
