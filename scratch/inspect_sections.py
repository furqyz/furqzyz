import re
import os

with open('cografya/tuik-verileri.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all section tags and their inner content
sections = re.findall(r'(<section\s+id="([^"]+)"[^>]*>(.*?)</section>)', html, re.DOTALL)
print(f"Total sections found: {len(sections)}")
for idx, (full_block, sid, inner) in enumerate(sections):
    h3_match = re.search(r'<h3[^>]*>(.*?)</h3>', inner, re.DOTALL)
    h3_text = re.sub('<.*?>', '', h3_match.group(1)).strip() if h3_match else "No h3"
    print(f"{idx+1}. ID: {sid} | Title: {h3_text} | Size: {len(full_block)} bytes")
