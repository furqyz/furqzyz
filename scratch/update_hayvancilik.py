import re

filepath = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\cografya\hayvancilik.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

mappings = {
    "Büyükbaş Hayvancılık": "tuik_sigir.jpeg",
    "Küçükbaş (Koyun)": "tuik_koyun.jpeg",
    "Kıl Keçisi": "tuik_kil_kecisi.jpeg",
    "Kümes Hayvancılığı": "tuik_kumes.jpeg",
    "Arıcılık": "tuik_aricilik.jpeg",
    "İpek Böcekçiliği": "tuik_ipek_bocegi.jpeg"
}

for title, img_name in mappings.items():
    img_tag = f'\n                    <img src="../assets/images/cografya/{img_name}" alt="{title} Haritası" class="w-full h-auto mt-4 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm hover:scale-[1.02] transition-transform duration-300">\n'
    
    # We want to insert the img_tag right before the `<div class="mt-4 pt-3 border-t` inside the section that has the title.
    # A bit tricky with regex, let's find the section block:
    # Look for: <h3 ...> ... title ... </h3> ... <div class="mt-4 pt-3 border-t
    
    pattern = r"(<h3[^>]*>.*?{}.*?</h3>.*?)(<div class=\"mt-4 pt-3 border-t)".format(re.escape(title))
    
    def replacer(match):
        return match.group(1) + img_tag + "                    " + match.group(2)
        
    content = re.sub(pattern, replacer, content, flags=re.DOTALL)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated hayvancilik.html")
