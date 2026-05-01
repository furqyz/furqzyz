import os
import re

root_dir = r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı\turkce'

# 1. HTML Content Generation
page_html = '''
            <div class="columns-1 xl:columns-2 gap-8 space-y-8">
                
                <section class="note-card category-indigo p-6 md:p-8 rounded-2xl shadow-sm">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-indigo-900 dark:text-indigo-200">
                        <div class="bg-indigo-100 dark:bg-indigo-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-cubes text-indigo-600 dark:text-indigo-300"></i>
                        </div>
                        Sözcüğün Yapısı
                    </h3>
                    <div class="space-y-4">
                        <div class="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-indigo-700 dark:text-indigo-400 block mb-1">Basit Sözcük:</strong>
                            <p class="text-slate-700 dark:text-slate-300 text-sm">Hiçbir yapım eki almamış sözcüklerdir. İstedikleri kadar çekim eki alabilirler, yapıları bozulmaz.</p>
                            <span class="block mt-2 text-xs font-mono bg-white dark:bg-slate-800 px-2 py-1 rounded border dark:border-slate-700">kedi-m, gez-di, ev-ler-in</span>
                        </div>
                        <div class="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-indigo-700 dark:text-indigo-400 block mb-1">Türemiş Sözcük:</strong>
                            <p class="text-slate-700 dark:text-slate-300 text-sm">Kök ya da gövdeye <strong>en az bir tane yapım eki</strong> getirilerek oluşturulan sözcüklerdir.</p>
                            <span class="block mt-2 text-xs font-mono bg-white dark:bg-slate-800 px-2 py-1 rounded border dark:border-slate-700">ses-siz, yer-gi, göz-le-di</span>
                        </div>
                        <div class="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-indigo-700 dark:text-indigo-400 block mb-1">Birleşik Sözcük:</strong>
                            <p class="text-slate-700 dark:text-slate-300 text-sm">En az iki sözcüğün yeni bir anlamı karşılamak üzere birleşmesidir.</p>
                            <span class="block mt-2 text-xs font-mono bg-white dark:bg-slate-800 px-2 py-1 rounded border dark:border-slate-700">bugün, huzurevi, imambayıldı</span>
                        </div>
                    </div>
                </section>

                <section class="note-card category-purple p-6 md:p-8 rounded-2xl shadow-sm">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-layer-group text-purple-600 dark:text-purple-300"></i>
                        </div>
                        Birleşik Yapılı Fiiller
                    </h3>
                    <ul class="space-y-4 text-sm text-slate-700 dark:text-slate-300">
                        <li class="p-3 bg-slate-50 dark:bg-slate-900/50 rounded-xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-purple-700 dark:text-purple-400">Yardımcı Eylemle Kurulanlar:</strong> İsim + etmek/olmak/kılmak <em>(Örn: hasta olmak, hissetmek)</em>
                        </li>
                        <li class="p-3 bg-slate-50 dark:bg-slate-900/50 rounded-xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-purple-700 dark:text-purple-400">Kurallı Birleşik Fiiller:</strong> İki fiilin birleşmesiyle oluşur.<br>
                            <span class="mt-2 block space-y-1">
                                <span class="block"><i class="fas fa-check text-purple-500 w-4"></i> Yeterlilik: -ebil</span>
                                <span class="block"><i class="fas fa-bolt text-purple-500 w-4"></i> Tezlik: -iver</span>
                                <span class="block"><i class="fas fa-infinity text-purple-500 w-4"></i> Süreklilik: -edur, -ekal, -egel</span>
                                <span class="block"><i class="fas fa-arrow-right text-purple-500 w-4"></i> Yaklaşma: -eyaz</span>
                            </span>
                        </li>
                        <li class="p-3 bg-slate-50 dark:bg-slate-900/50 rounded-xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-purple-700 dark:text-purple-400">Anlamca Kaynaşmış Birleşik Fiiller:</strong> Genellikle deyimlerdir. <em>(Örn: gözden düşmek, kulak vermek, etekleri zil çalmak)</em>
                        </li>
                    </ul>
                </section>

                <section class="note-card category-orange p-6 md:p-8 rounded-2xl shadow-sm">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-orange-900 dark:text-orange-200">
                        <div class="bg-orange-100 dark:bg-orange-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-exclamation-circle text-orange-600 dark:text-orange-300"></i>
                        </div>
                        Ekstra Bilgi & İstisnalar
                    </h3>
                    <div class="p-4 bg-slate-50 dark:bg-slate-900/50 rounded-2xl border border-slate-100 dark:border-slate-800 text-sm text-slate-700 dark:text-slate-300">
                        <p class="font-bold text-orange-600 dark:text-orange-400 mb-2">Yeterlilik Fiilinin Olumsuzu (En Büyük Tuzak!)</p>
                        <p><strong>"Yapabildi"</strong> fiilinin olumsuzu <strong>"yapamadı"</strong> şeklindedir. Aradaki <strong class="text-rose-600 text-lg">a/e</strong> sesi kuralın izidir.</p>
                        <div class="mt-3 flex flex-wrap gap-2 text-xs font-mono">
                            <span class="bg-white dark:bg-slate-800 px-2 py-1 rounded border dark:border-slate-700">Yap-ma-dı (Basit)</span>
                            <span class="bg-orange-100 dark:bg-orange-900/30 text-orange-800 dark:text-orange-300 px-2 py-1 rounded font-bold border border-orange-200 dark:border-orange-800">Yap-a-ma-dı (Birleşik)</span>
                        </div>
                    </div>
                </section>

                <section class="note-card category-red p-6 md:p-8 rounded-2xl shadow-sm text-white" style="background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center">
                        <div class="bg-white/20 p-2.5 rounded-xl mr-3">
                            <i class="fas fa-balance-scale"></i>
                        </div>
                        Kritik Uyarılar
                    </h3>
                    <div class="space-y-4 text-sm leading-relaxed">
                        <div class="bg-white/10 p-4 rounded-2xl border border-white/20">
                            <p class="font-bold text-rose-100 mb-2">"Sözcüğün Yapısı" vs "Fiilin Zamanı"</p>
                            <ul class="space-y-2">
                                <li><i class="fas fa-cube text-emerald-300 w-4"></i> Soruda <strong>"Sözcüğün yapısı"</strong> soruluyorsa: Sadece <strong class="text-white border-b border-white border-dashed pb-0.5">Basit - Türemiş - Birleşik</strong> aramalısınız.</li>
                                <li><i class="fas fa-clock text-rose-300 w-4"></i> Soruda <strong>"Fiilin zaman/çekim yapısı"</strong> soruluyorsa: Sözcüğün kaç tane kip eki aldığına (Basit zamanlı / Birleşik zamanlı) bakılır. Bu ikisini birbirine karıştırmayın!</li>
                            </ul>
                        </div>
                    </div>
                </section>

            </div>

            <!-- SINAV HAFIZASI -->
            <section class="note-card p-8 md:p-12 rounded-3xl shadow-2xl relative overflow-hidden group mt-12 exam-memory">
                <div class="absolute right-0 top-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -mr-16 -mt-16"></div>
                <div class="relative z-10 text-white">
                    <h3 class="text-3xl font-black mb-8 flex items-center tracking-tight">
                        <i class="fas fa-graduation-cap text-4xl mr-4 text-indigo-300"></i> SINAV HAFIZASI & ANALİZ
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-white/10 backdrop-blur p-6 rounded-2xl border border-white/10">
                            <p class="text-indigo-200 font-bold mb-2 flex items-center"><i class="fas fa-trophy mr-2"></i>"Yapısı Bakımından Farklıdır"</p>
                            <p class="text-sm leading-relaxed text-slate-200">
                                ÖSYM'nin en popüler sorusu <strong>"Hangisi yapısı bakımından diğerlerinden farklıdır?"</strong> sorusudur. Şıklara genelde 4 türemiş, 1 basit sözcük koyarlar.
                            </p>
                        </div>
                        <div class="bg-white/10 backdrop-blur p-6 rounded-2xl border border-white/10">
                            <p class="text-indigo-200 font-bold mb-2 flex items-center"><i class="fas fa-ghost mr-2"></i>Yeterlilik Fiilinin Olumsuzu</p>
                            <p class="text-sm leading-relaxed text-slate-200">
                                Çıkmış sorularda altı çizili verilen <strong>"yapamadı"</strong> veya <strong>"göremez"</strong> gibi yeterlilik fiilinin olumsuz (birleşik) hâlleri ile adayları sıkça elemişlerdir. Basit sanılması en kolay tuzaktır.
                            </p>
                        </div>
                    </div>
                </div>
            </section>
    '''

template_path = os.path.join(root_dir, 'yapi-sekil-cekim-ekleri.html')
new_page_path = os.path.join(root_dir, 'yapi-sekil-sozcugun-yapisi.html')

with open(template_path, 'r', encoding='utf-8') as f:
    page_content = f.read()

# Replace titles
page_content = re.sub(r'<title>.*?</title>', '<title>Sözcüğün Yapısı: Basit, Türemiş, Birleşik - KPSS Türkçe</title>', page_content)
page_content = re.sub(r'<h2 class="text-3xl md:text-4xl font-black[^>]+>.*?</h2>', '<h2 class="text-3xl md:text-4xl font-black text-slate-900 dark:text-white leading-tight tracking-tight">Sözcüğün Yapısı: Basit, Türemiş, Birleşik</h2>', page_content)

# Replace content
pattern = r'<div class="columns-1 xl:columns-2 gap-8 space-y-8">.*?</section>\s*</div>\s*<!-- SINAV HAFIZASI -->\s*<section.*?</section>'
page_content = re.sub(pattern, page_html.strip(), page_content, flags=re.DOTALL)

with open(new_page_path, 'w', encoding='utf-8') as f:
    f.write(page_content)

# 2. Update Hub Page
hub_path = os.path.join(root_dir, 'yapi-sekil.html')
with open(hub_path, 'r', encoding='utf-8') as f:
    hub_content = f.read()

card_html = '''                <a href="yapi-sekil-sozcugun-yapisi.html" class="group bg-white dark:bg-slate-800 rounded-3xl p-8 border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-xl hover:-translate-y-2 transition-all duration-300 relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-indigo-500/5 dark:bg-indigo-500/10 rounded-bl-[100px] -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
                    <div class="w-16 h-16 bg-indigo-100 dark:bg-indigo-900/40 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform relative z-10">
                        <i class="fas fa-link text-indigo-600 dark:text-indigo-400 text-2xl font-bold"></i>
                    </div>
                    <h3 class="font-extrabold text-slate-900 dark:text-white text-2xl mb-3 relative z-10">Sözcüğün Yapısı: Basit, Türemiş, Birleşik</h3>
                    <div class="inline-flex items-center text-indigo-600 dark:text-indigo-400 font-bold relative z-10 mt-4">
                        <span>Konuya Çalış</span>
                        <i class="fas fa-arrow-right ml-2 group-hover:translate-x-2 transition-transform"></i>
                    </div>
                </a>'''

# Insert the card
target_hub = r'(<a href="yapi-sekil-cekim-ekleri\.html".*?</a>)\s*</div>'
hub_content = re.sub(target_hub, r'\1\n' + card_html + '\n            </div>', hub_content, flags=re.DOTALL)
with open(hub_path, 'w', encoding='utf-8') as f:
    f.write(hub_content)


# 3. Update all sidebars!
script_path = os.path.join(os.path.dirname(root_dir), 'fix_all_sidebars.py')
with open(script_path, 'r', encoding='utf-8') as f:
    sidebar_script = f.read()

sidebar_script = sidebar_script.replace(
    "('yapi-sekil-cekim-ekleri.html', 'İsim ve Fiil Çekim Ekleri')",
    "('yapi-sekil-cekim-ekleri.html', 'İsim ve Fiil Çekim Ekleri'),\n            ('yapi-sekil-sozcugun-yapisi.html', 'Sözcüğün Yapısı: Basit, Türemiş, Birleşik')"
)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(sidebar_script)
