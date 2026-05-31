import os
import re
import json

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', raw_html)
    return ' '.join(cleantext.split())

def build_search_index():
    index_data = []
    files = [('index.html', 1)] + [(f'unitler/unite{i}.html', i) for i in range(2, 26)]
    
    for filepath, idx in files:
        full_path = os.path.join(root_dir, filepath)
        if not os.path.exists(full_path):
            continue
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract title
        unit_title = f"Ünite {idx}"
        title_match = re.search(r'<h2[^>]*>(.*?)</h2>', content, re.DOTALL)
        if title_match:
            unit_title = clean_html(title_match.group(1))

        # Extract sections
        sections = re.finditer(r'<section[^>]*class="[^"]*note-card[^"]*"[^>]*>(.*?)</section>', content, re.DOTALL)
        for s in sections:
            sec_content = s.group(1)
            h3_match = re.search(r'<h3[^>]*>(.*?)</h3>', sec_content, re.DOTALL)
            sec_title = clean_html(h3_match.group(1)) if h3_match else unit_title
            text_content = clean_html(sec_content)
            
            index_data.append({
                "unit": unit_title,
                "title": sec_title,
                "content": text_content,
                "url": filepath, # 'index.html' or 'unitler/unite2.html'
                "unit_id": idx
            })

    js_content = f"const searchIndex = {json.dumps(index_data, ensure_ascii=False)};\n"
    out_path = os.path.join(root_dir, 'assets', 'js', 'searchIndex.js')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js_content)

def build_search_index_turkce():
    index_data = []
    
    files = [('turkce.html', 'KPSS Türkçe')]
    turkce_dir = os.path.join(root_dir, 'turkce')
    
    if os.path.exists(turkce_dir):
        for filename in os.listdir(turkce_dir):
            if filename.endswith('.html'):
                files.append((f'turkce/{filename}', filename.replace('.html', '')))
            
    for filepath, default_title in files:
        full_path = os.path.join(root_dir, filepath)
        if not os.path.exists(full_path):
            continue
            
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract title
        unit_title = default_title
        title_match = re.search(r'<h2[^>]*>(.*?)</h2>', content, re.DOTALL)
        if title_match:
            unit_title = clean_html(title_match.group(1))

        # Extract sections
        sections = re.finditer(r'<section[^>]*class="[^"]*note-card[^"]*"[^>]*>(.*?)</section>', content, re.DOTALL)
        for s in sections:
            sec_content = s.group(1)
            h3_match = re.search(r'<h3[^>]*>(.*?)</h3>', sec_content, re.DOTALL)
            sec_title = clean_html(h3_match.group(1)) if h3_match else unit_title
            text_content = clean_html(sec_content)
            
            index_data.append({
                "unit": unit_title,
                "title": sec_title,
                "content": text_content,
                "url": filepath, # 'turkce.html' or 'turkce/ses-bilgisi.html'
                "subject": "Türkçe"
            })

    js_content = f"const searchIndex = {json.dumps(index_data, ensure_ascii=False)};\n"
    out_path = os.path.join(root_dir, 'assets', 'js', 'searchIndex_turkce.js')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js_content)

def build_search_index_cografya():
    index_data = []
    
    files = [('cografya.html', 'KPSS Coğrafya')]
    cografya_dir = os.path.join(root_dir, 'cografya')
    
    if os.path.exists(cografya_dir):
        for filename in os.listdir(cografya_dir):
            if filename.endswith('.html'):
                files.append((f'cografya/{filename}', filename.replace('.html', '')))
            
    for filepath, default_title in files:
        full_path = os.path.join(root_dir, filepath)
        if not os.path.exists(full_path):
            continue
            
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract title
        unit_title = default_title
        title_match = re.search(r'<h2[^>]*>(.*?)</h2>', content, re.DOTALL)
        if title_match:
            unit_title = clean_html(title_match.group(1))

        # Extract sections
        sections = re.finditer(r'<section[^>]*class="[^"]*note-card[^"]*"[^>]*>(.*?)</section>', content, re.DOTALL)
        for s in sections:
            sec_content = s.group(1)
            h3_match = re.search(r'<h3[^>]*>(.*?)</h3>', sec_content, re.DOTALL)
            sec_title = clean_html(h3_match.group(1)) if h3_match else unit_title
            text_content = clean_html(sec_content)
            
            index_data.append({
                "unit": unit_title,
                "title": sec_title,
                "content": text_content,
                "url": filepath,
                "subject": "Coğrafya"
            })

    js_content = f"const searchIndex = {json.dumps(index_data, ensure_ascii=False)};\n"
    out_path = os.path.join(root_dir, 'assets', 'js', 'searchIndex_cografya.js')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js_content)

build_search_index()
build_search_index_turkce()
build_search_index_cografya()
print("All search indices built successfully.")
