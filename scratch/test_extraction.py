import re
import os
def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', raw_html)
    return ' '.join(cleantext.split())

filepath = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\cografya\tuik-koruma.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract title
title_match = re.search(r'<h2[^>]*>(.*?)</h2>', content, re.DOTALL)
unit_title = clean_html(title_match.group(1)) if title_match else "Default Title"

# Extract sections
sections = re.finditer(r'<section[^>]*class="[^"]*note-card[^"]*"[^>]*>(.*?)</section>', content, re.DOTALL)
for s in sections:
    sec_content = s.group(1)
    h3_match = re.search(r'<h3[^>]*>(.*?)</h3>', sec_content, re.DOTALL)
    sec_title = clean_html(h3_match.group(1)) if h3_match else unit_title
    print(f"TITLE: {sec_title}")
    text_content = clean_html(sec_content)
    print(f"CONTENT LEN: {len(text_content)}")
    if 'UNESCO' in text_content.upper():
        print("FOUND UNESCO IN TEXT")
