import os
import re

root_dir = r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı'

def is_turkce(filepath):
    # Check if file is turkce.html or inside turkce folder
    rel = os.path.relpath(filepath, root_dir)
    return 'turkce' in rel.lower()

def get_depth(filepath):
    # Returns relative depth to root_dir
    rel_path = os.path.relpath(filepath, root_dir)
    return rel_path.count(os.sep)

for root, _, files in os.walk(root_dir):
    for filename in files:
        if not filename.endswith('.html'): continue
        filepath = os.path.join(root, filename)
        
        depth = get_depth(filepath)
        prefix = '../' * depth
        
        in_turkce = is_turkce(filepath)
        
        tarih_class = 'px-3 py-2 rounded-lg font-bold text-sm transition-colors '
        turkce_class = 'px-3 py-2 rounded-lg font-bold text-sm transition-colors '
        
        if in_turkce:
            tarih_class += 'text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-700 dark:hover:text-slate-200 font-semibold'
            turkce_class += 'bg-rose-50 dark:bg-rose-900/30 text-rose-600 dark:text-rose-400'
        else:
            tarih_class += 'bg-indigo-50 dark:bg-indigo-900/30 text-indigo-600 dark:text-indigo-400'
            turkce_class += 'text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-700 dark:hover:text-slate-200 font-semibold'

        ring_color = 'rose-500' if in_turkce else 'indigo-500'

        new_html = f'''<div class="flex items-center space-x-4">
                <!-- Dersler Menüsü -->
                <nav class="hidden lg:flex items-center space-x-1 mr-2">
                    <a href="{prefix}index.html" class="{tarih_class}">Tarih</a>
                    <a href="{prefix}turkce.html" class="{turkce_class}">Türkçe</a>
                    <a href="#" class="px-3 py-2 rounded-lg text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-700 dark:hover:text-slate-200 font-semibold text-sm transition-colors">Coğrafya</a>
                    <a href="#" class="px-3 py-2 rounded-lg text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-700 dark:hover:text-slate-200 font-semibold text-sm transition-colors">Vatandaşlık</a>
                </nav>
                
                <!-- Arama Kutusu -->
                <div class="hidden md:flex items-center bg-slate-100 dark:bg-slate-800 rounded-full px-4 py-2 border border-slate-200 dark:border-slate-700 focus-within:ring-2 focus-within:ring-{ring_color} transition-all relative z-50">
                    <i class="fas fa-search text-slate-400"></i>
                    <input type="text" id="searchInput" placeholder="Notlarda ara..." class="bg-transparent border-none outline-none ml-2 text-sm text-slate-800 dark:text-slate-200 placeholder-slate-400 w-48 lg:w-64" autocomplete="off">
                    
                    <!-- Sonuç Kutusu -->
                    <div id="searchResults" class="absolute top-full right-0 mt-3 w-80 bg-white dark:bg-slate-800 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-700 hidden flex-col max-h-[70vh] overflow-y-auto z-50 custom-scrollbar divide-y divide-slate-100 dark:divide-slate-700/50">
                    </div>
                </div>
                
                <button id="dark-mode-toggle"'''

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        pattern = r'<div class="flex items-center space-x-4">(?:\s*<!-- Dersler Menüsü -->)?\s*<nav.*?</nav>.*?<button id="dark-mode-toggle"'
        
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, new_html, content, flags=re.DOTALL)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            print(f"Pattern not found in {filename}")

print("Headers updated successfully.")
