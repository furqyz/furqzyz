import re

filepath = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\cografya\tarim-urunleri.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Pirinç
pirinc_img = '\n                            <img src="../assets/images/cografya/tuik_celtik.jpeg" alt="Pirinç (Çeltik) Haritası" class="w-full h-auto mt-3 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm hover:scale-[1.02] transition-transform duration-300">'
content = content.replace(
    'akarsu boylarında ekilir.</p>',
    f'akarsu boylarında ekilir.</p>{pirinc_img}'
)

# 2. Turunçgiller
turuncgil_img = '\n                            <img src="../assets/images/cografya/tuik_turuncgiller.jpeg" alt="Turunçgiller Haritası" class="w-full h-auto mt-3 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm hover:scale-[1.02] transition-transform duration-300">'
content = content.replace(
    '(Ege-Manisa kuru üzümde liderdir).</p>',
    f'(Ege-Manisa kuru üzümde liderdir).</p>{turuncgil_img}'
)

# 3. Gül (Eksik olduğu için yeni bir blok ekliyoruz)
gul_block = f'''
                        <!-- Gül ve Kozmetik -->
                        <div class="bg-slate-50 dark:bg-slate-900/50 p-4 rounded-xl border border-slate-100 dark:border-slate-800">
                            <strong class="text-orange-600 dark:text-orange-400 block text-xs uppercase mb-1">Gül (Kozmetik Sanayisi)</strong>
                            <p class="mb-1">Akdeniz iklimi ile Karasal iklimin geçiş alanlarında (Göller Yöresi) yoğunlaşmıştır. Isparta dünya ve Türkiye üretiminde açık ara liderdir, parfüm ve kozmetik sanayisinde kullanılır.</p>
                            <img src="../assets/images/cografya/tuik_gul.jpeg" alt="Gül Haritası" class="w-full h-auto mt-3 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm hover:scale-[1.02] transition-transform duration-300">
                        </div>
'''
content = content.replace(
    '<!-- Pamuk ve Kayısı -->',
    f'{gul_block}\n                        <!-- Pamuk ve Kayısı -->'
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated tarim-urunleri.html")
