import re

with open("cografya/tuik-tarim.html", "r", encoding="utf-8") as f:
    content = f.read()

# Target mappings specifically for the missing ones:
# Format: (data_name, img_file, title)
missing_mappings = [
    ("gül", "gul.png", "Gül"),
    ("pirinç çeltik", "celtik.png", "Pirinç (Çeltik)"),
    ("turunçgiller narenciye", "turuncgil.png", "Turunçgiller")
]

modified_count = 0
for name, img_file, title in missing_mappings:
    # Pattern to match the card header and footer
    pattern = rf'(<div\s+data-category="[^"]*"\s+data-name="{name}"\s+class="tarim-card[^>]*>.*?)(<div\s+class="mt-5\s+pt-4\s+border-t[^>]*>)'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        map_html = f"""
                            <!-- Harita Görseli -->
                            <div class="mt-4 bg-white dark:bg-slate-850 p-1.5 rounded-xl border border-slate-200/60 dark:border-slate-700/50 flex justify-center items-center overflow-hidden">
                                <img src="../assets/images/cografya/{img_file}" alt="{title} Üretim Haritası" class="max-w-full h-auto rounded-lg shadow-sm hover:scale-[1.03] transition-transform duration-300 cursor-zoom-in" onclick="openMapModal(this.src, '{title} Üretim Haritası')">
                            </div>
                        """
        replacement = match.group(1) + map_html + match.group(2)
        content = content.replace(match.group(0), replacement)
        modified_count += 1
        print(f"Successfully injected map for: {name}")
    else:
        print(f"Could NOT find card for: {name}")

# Save the updated file
with open("cografya/tuik-tarim.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Total missing cards injected: {modified_count}")
