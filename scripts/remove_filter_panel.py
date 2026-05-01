import os
import re

html_files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]

for filename in html_files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Sidebar'daki Hızlı Filtre kartını kaldır
    content = re.sub(
        r'\s*<!-- Hızlı Filtre Paneli -->.*?</div>\s*(?=</div>\s*</aside>)',
        '',
        content,
        flags=re.DOTALL
    )

    # 2. Modal HTML'i kaldır
    content = re.sub(
        r'\s*<!-- Hızlı Filtre Modal -->.*?</div>\s*(?=</body>)',
        '',
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Hızlı Filtre bölümü ve modalı tüm sayfalardan kaldırıldı.")
