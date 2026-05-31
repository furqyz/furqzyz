with open("cografya/tuik-hayvancilik.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# Search for <!-- ARICILIK --> or <!-- İPEK BÖCEĞİ -->
for term in ["ARICILIK", "İPEK BÖCEKÇİLİĞİ", "KÜMES"]:
    idx = content.find(term)
    if idx != -1:
        snippet = content[idx-100:idx+800]
        # Replace non-cp1254 chars
        clean_snippet = "".join([c if ord(c) < 128 else '?' for c in snippet])
        print(f"=== {term} ===")
        print(clean_snippet)
