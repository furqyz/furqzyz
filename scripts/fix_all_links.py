import os

dirs = [
    r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı\unitler',
    r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı\turkce',
    r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı'
]

# Tüm olası anasayfa.html varyasyonlarını düzelt
replacements = [
    # Alt klasörlerden ana dizine giden linkler
    ('href="../anasayfa.html"', 'href="../index.html"'),
    ("href='../anasayfa.html'", "href='../index.html'"),
    # Ana dizindeki linkler
    ('href="anasayfa.html"', 'href="index.html"'),
    ("href='anasayfa.html'", "href='index.html'"),
    # JS window.location varyasyonları
    ("window.location.href = '../anasayfa.html'", "window.location.href = '../index.html'"),
    ("window.location.href = 'anasayfa.html'", "window.location.href = 'index.html'"),
    ("window.location='../anasayfa.html'", "window.location='../index.html'"),
    ("window.location='anasayfa.html'", "window.location='index.html'"),
    # tarih.html: Ana dizinde index.html iken alt klasörden gelen tarih.html linki
    ('href="../index.html"', 'href="../tarih.html"'),  # Bu satır dikkatli! Sadece tarih.html klasörlerinden
]

# Alt klasörlerdeki dosyalar (unitler, turkce) için
# ../index.html -> ../index.html (anasayfa - doğru)
# BU YÜZDENden yukarıda yanlış yazdım, düzeltelim

alt_klasor_replacements = [
    ('href="../anasayfa.html"', 'href="../index.html"'),
    ("href='../anasayfa.html'", "href='../index.html'"),
    ("window.location.href = '../anasayfa.html'", "window.location.href = '../index.html'"),
    ("window.location='../anasayfa.html'", "window.location='../index.html'"),
]

root_replacements = [
    ('href="anasayfa.html"', 'href="index.html"'),
    ("href='anasayfa.html'", "href='index.html'"),
    ("window.location.href = 'anasayfa.html'", "window.location.href = 'index.html'"),
    ("window.location='anasayfa.html'", "window.location='index.html'"),
]

count = 0

# Alt klasörler
for d in [r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı\unitler',
           r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı\turkce']:
    if not os.path.exists(d):
        continue
    for fn in os.listdir(d):
        if not fn.endswith('.html'):
            continue
        fp = os.path.join(d, fn)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        for old, new in alt_klasor_replacements:
            content = content.replace(old, new)
        if content != original:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            print(f'Fixed: {fn}')

# Root klasör (anasayfa.html -> index.html)
root = r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı'
for fn in os.listdir(root):
    if not fn.endswith('.html'):
        continue
    fp = os.path.join(root, fn)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for old, new in root_replacements:
        content = content.replace(old, new)
    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Fixed (root): {fn}')

print(f'\nToplam {count} dosya duzeltildi.')
