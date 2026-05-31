import re

with open("cografya/tuik-hayvancilik.html", "r", encoding="utf-8") as f:
    content = f.read()

# Mappings for hayvancilik
# Format: (comment_or_marker_text, img_file, title)
hayvancilik_configs = [
    ("<!-- KOYUN -->", "koyun.png", "Koyun"),
    ("<!-- KIL KEÇİSİ -->", "kil_kecisi.png", "Kıl Keçisi"),
    ("<!-- TİFTİK KEÇİSİ -->", "tiftik_kecisi.png", "Tiftik Keçisi"),
    ("<!-- SIĞIR -->", "sigir_inek.png", "Sığır"),
    ("<!-- MANDA -->", "manda.png", "Manda"),
    ("<!-- ARICILIK -->", "aricilik.png", "Arıcılık"),
    ("<!-- İPEK BÖCEKÇİLİĞİ -->", "ipek_bocegi.png", "İpek Böcekçiliği"),
]

modified_count = 0

# Process all standard comments
for marker, img_file, title in hayvancilik_configs:
    # Find the block starting with the marker comment and ending before the footer
    pattern = rf'({re.escape(marker)}.*?)(<div\s+class="mt-6\s+pt-4\s+border-t[^>]*>)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        map_html = f"""
                            <!-- Harita Görseli -->
                            <div class="mt-4 bg-white dark:bg-slate-850 p-1.5 rounded-xl border border-slate-200/60 dark:border-slate-700/50 flex justify-center items-center overflow-hidden">
                                <img src="../assets/images/cografya/{img_file}" alt="{title} Dağılış Haritası" class="max-w-full h-auto rounded-lg shadow-sm hover:scale-[1.03] transition-transform duration-300 cursor-zoom-in" onclick="openMapModal(this.src, '{title} Dağılış Haritası')">
                            </div>
                        """
        replacement = match.group(1) + map_html + match.group(2)
        content = content.replace(match.group(0), replacement)
        modified_count += 1
        print(f"Injected map for hayvancilik: {title}")
    else:
        print(f"Could NOT find block for marker: {marker}")

# For Kumes, we can search for "Kümes Hayvancılığı Özellikleri" and find the next footer
kumes_pattern = r'(Kümes\s+Hayvancılığı\s+Özellikleri.*?</ul>\s*)(<div\s+class="mt-6\s+pt-4\s+border-t[^>]*>)'
kumes_match = re.search(kumes_pattern, content, re.DOTALL)
if kumes_match:
    map_html = """
                            <!-- Harita Görseli -->
                            <div class="mt-4 bg-white dark:bg-slate-850 p-1.5 rounded-xl border border-slate-200/60 dark:border-slate-700/50 flex justify-center items-center overflow-hidden">
                                <img src="../assets/images/cografya/kumes.png" alt="Kümes Hayvancılığı Haritası" class="max-w-full h-auto rounded-lg shadow-sm hover:scale-[1.03] transition-transform duration-300 cursor-zoom-in" onclick="openMapModal(this.src, 'Kümes Hayvancılığı Haritası')">
                            </div>
                        """
    replacement = kumes_match.group(1) + map_html + kumes_match.group(2)
    content = content.replace(kumes_match.group(0), replacement)
    modified_count += 1
    print("Injected map for hayvancilik: Kümes Hayvancılığı")
else:
    print("Could NOT find block for Kümes")

# Save modified tuik-hayvancilik.html
with open("cografya/tuik-hayvancilik.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Total hayvancilik modifications: {modified_count}")
