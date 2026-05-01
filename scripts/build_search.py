import os
import re
import json

def update_html_files():
    search_html = """                <!-- Arama Kutusu -->
                <div class="hidden md:flex items-center bg-slate-100 dark:bg-slate-800 rounded-full px-4 py-2 border border-slate-200 dark:border-slate-700 focus-within:ring-2 focus-within:ring-indigo-500 transition-all relative z-50">
                    <i class="fas fa-search text-slate-400"></i>
                    <input type="text" id="searchInput" placeholder="Notlarda ara..." class="bg-transparent border-none outline-none ml-2 text-sm text-slate-800 dark:text-slate-200 placeholder-slate-400 w-48 lg:w-64" autocomplete="off">
                    
                    <!-- Sonuç Kutusu -->
                    <div id="searchResults" class="absolute top-full right-0 mt-3 w-80 bg-white dark:bg-slate-800 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-700 hidden flex-col max-h-[70vh] overflow-y-auto z-50 custom-scrollbar divide-y divide-slate-100 dark:divide-slate-700/50">
                    </div>
                </div>"""

    old_search = r'<!-- Arama Kutusu \(Görsel\) -->\s*<div class="hidden md:flex items-center bg-slate-100 dark:bg-slate-800 rounded-full px-4 py-2 border border-slate-200 dark:border-slate-700 focus-within:ring-2 focus-within:ring-indigo-500 transition-all">\s*<i class="fas fa-search text-slate-400"></i>\s*<input type="text" placeholder="Notlarda ara\.\.\." class="bg-transparent border-none outline-none ml-2 text-sm text-slate-800 dark:text-slate-200 placeholder-slate-400 w-48 lg:w-64">\s*</div>'
    
    files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]
    
    for filepath in files:
        if not os.path.exists(filepath):
            continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = re.sub(old_search, search_html, content)
        
        # also make sure <script src="searchIndex.js"></script> is included
        # actually, I'll just load searchIndex.js in script.js to avoid modifying HTML more
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', raw_html)
    return ' '.join(cleantext.split())

def build_search_index():
    index_data = []
    files = [('index.html', 1)] + [(f'unitler/unite{i}.html', i) for i in range(2, 26)]
    
    for filepath, idx in files:
        if not os.path.exists(filepath):
            continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract title
        unit_title = f"Ünite {idx}"
        title_match = re.search(r'<h2 class="text-4xl[^>]*>(.*?)</h2>', content, re.DOTALL)
        if title_match:
            unit_title = clean_html(title_match.group(1))

        # Extract sections
        sections = re.finditer(r'<section class=".*?note-card[^>]*>(.*?)</section>', content, re.DOTALL)
        for s in sections:
            sec_content = s.group(1)
            h3_match = re.search(r'<h3[^>]*>(.*?)</h3>', sec_content, re.DOTALL)
            sec_title = clean_html(h3_match.group(1)) if h3_match else unit_title
            text_content = clean_html(sec_content)
            
            # Use unit relative URL correctly
            url = f"unite{idx}.html" if idx > 1 else "index.html"
            
            index_data.append({
                "unit": unit_title,
                "title": sec_title,
                "content": text_content,
                "url": url,
                "unit_id": idx
            })

    # Write as a javascript file so it can be easily included or fetched
    js_content = f"const searchIndex = {json.dumps(index_data, ensure_ascii=False)};"
    with open('searchIndex.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

update_html_files()
build_search_index()
print("Search index built and HTML files updated.")
