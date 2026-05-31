import re

with open("cografya/tuik-hayvancilik.html", "r", encoding="utf-8") as f:
    content = f.read()

# For Kumes
kumes_pattern = r'(Kümes\s+Hayvancılığı\s+Özellikleri.*?</ul>\s*)(<div\s+class="pt-4\s+border-t[^>]*>)'
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
    print("Successfully injected Kümes map!")
else:
    print("Could NOT find block for Kümes")

# Save modified tuik-hayvancilik.html
with open("cografya/tuik-hayvancilik.html", "w", encoding="utf-8") as f:
    f.write(content)
