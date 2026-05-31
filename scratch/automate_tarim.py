import re

# Read tuik-tarim.html
with open("cografya/tuik-tarim.html", "r", encoding="utf-8") as f:
    tarim_content = f.read()

# Define mappings from data-name to filename and nice title
tarim_mappings = {
    "zeytin": ("zeytin.png", "Zeytin"),
    "haşhaş": ("hashas.png", "Haşhaş"),
    "susam": ("susam.png", "Susam"),
    "kolza kanola": ("kanola.png", "Kolza (Kanola)"),
    "ayçiçeği": ("aycicegi.png", "Ayçiçeği"),
    "yer fıstığı": ("yerfistigi.png", "Yer Fıstığı"),
    "pamuk": ("pamuk.png", "Pamuk"),
    "soya": ("soya.png", "Soya Fasulyesi"),
    "şeker pancarı": ("seker_pancari.png", "Şeker Pancarı"),
    "kenevir": ("kenevir.png", "Kenevir"),
    "tütün": ("tutun.png", "Tütün"),
    "keten": ("keten.png", "Keten"),
    "fındık": ("findik.png", "Fındık"),
    "çay": ("cay.png", "Çay"),
    "kivi": ("kivi.png", "Kivi"),
    "avokado": ("avokado.png", "Avokado"),
    "muz": ("muz.png", "Muz"),
    "turunçgiller": ("turuncgil.png", "Turunçgiller"),
    "kayısı": ("kayisi.png", "Kayısı"),
    "incir": ("incir.png", "İncir"),
    "üzüm": ("uzum.png", "Üzüm"),
    "elma": ("elma.png", "Elma"),
    "antep fıstığı": ("antepfistigi.png", "Antep Fıstığı"),
    "arpa": ("arpa.png", "Arpa"),
    "buğday": ("bugday.png", "Buğday"),
    "mısır": ("misir.png", "Mısır"),
    "nohut": ("nohut.png", "Nohut"),
    "kuru fasulye": ("kuru_fasulye.png", "Kuru Fasulye"),
    "yeşil mercimek": ("yesil_mercimek.png", "Yeşil Mercimek"),
    "kırmızı mercimek": ("kirmizi_mercimek.png", "Kırmızı Mercimek"),
    "patates": ("patates.png", "Patates"),
    "çeltik": ("celtik.png", "Çeltik"),
    "anason": ("anason.png", "Anason"),
    "aspir": ("aspir.png", "Aspir")
}

# We will search for each card using regex
# Example: <div data-category="yagli" data-name="zeytin" class="tarim-card ...">
# We want to insert the map HTML block right before the footer:
# <div class="mt-5 pt-4 border-t border-slate-200/40 dark:border-slate-700/40 flex items-center justify-between">

modified_count = 0
for name, (img_file, title) in tarim_mappings.items():
    # Find the card block starting with data-name="name"
    # We will search for a block containing data-name="name" and having a footer div.
    # To do this safely, we can replace the text using regex.
    pattern = rf'(<div\s+data-category="[^"]*"\s+data-name="{name}"\s+class="tarim-card[^>]*>.*?)(<div\s+class="mt-5\s+pt-4\s+border-t[^>]*>)'
    
    # Check if we can find a match
    match = re.search(pattern, tarim_content, re.DOTALL)
    if match:
        # We will insert the map block
        map_html = f"""
                            <!-- Harita Görseli -->
                            <div class="mt-4 bg-white dark:bg-slate-850 p-1.5 rounded-xl border border-slate-200/60 dark:border-slate-700/50 flex justify-center items-center overflow-hidden">
                                <img src="../assets/images/cografya/{img_file}" alt="{title} Üretim Haritası" class="max-w-full h-auto rounded-lg shadow-sm hover:scale-[1.03] transition-transform duration-300 cursor-zoom-in" onclick="openMapModal(this.src, '{title} Üretim Haritası')">
                            </div>
                        """
        # Reconstruct the block
        replacement = match.group(1) + map_html + match.group(2)
        tarim_content = tarim_content.replace(match.group(0), replacement)
        modified_count += 1
        print(f"Injected map for: {name}")
    else:
        print(f"Could NOT find card for: {name}")

print(f"Total tarim cards modified: {modified_count}")

# Save modified tuik-tarim.html
with open("cografya/tuik-tarim.html", "w", encoding="utf-8") as f:
    f.write(tarim_content)
