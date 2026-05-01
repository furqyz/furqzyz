import os
import re

html_files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]

for filename in html_files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. "TARİH ÜNİTELERİ" başlığını tıklanabilir yap
    old_nav_header = '''<h2 class="text-xs font-bold text-slate-400 dark:text-slate-500 uppercase tracking-widest px-3 mb-4 flex items-center">
                        <i class="fas fa-layer-group mr-2"></i> TARİH ÜNİTELERİ
                    </h2>
                    <nav class="space-y-1.5 max-h-[60vh] overflow-y-auto pr-1.5 custom-scrollbar">'''
    
    new_nav_header = '''<button onclick="toggleSidebarSection('unitNav', this)" class="w-full text-xs font-bold text-slate-400 dark:text-slate-500 uppercase tracking-widest px-3 mb-2 flex items-center justify-between hover:text-slate-600 dark:hover:text-slate-300 transition-colors">
                        <span class="flex items-center"><i class="fas fa-layer-group mr-2"></i> TARİH ÜNİTELERİ</span>
                        <i class="fas fa-chevron-down transition-transform duration-300" id="unitNav-chevron"></i>
                    </button>
                    <nav id="unitNav" class="space-y-1.5 max-h-[60vh] overflow-y-auto pr-1.5 custom-scrollbar hidden">'''
    
    content = content.replace(old_nav_header, new_nav_header)

    # 2. "HIZLI FİLTRE" başlığını tıklanabilir yap
    old_filter_header = '''<h2 class="text-xs font-bold text-slate-400 dark:text-slate-500 uppercase tracking-widest px-3 mb-4 flex items-center">
                        <i class="fas fa-filter mr-2"></i> HIZLI FİLTRE
                    </h2>
                    <div class="space-y-1.5">'''
    
    new_filter_header = '''<button onclick="toggleSidebarSection('filterNav', this)" class="w-full text-xs font-bold text-slate-400 dark:text-slate-500 uppercase tracking-widest px-3 mb-2 flex items-center justify-between hover:text-slate-600 dark:hover:text-slate-300 transition-colors">
                        <span class="flex items-center"><i class="fas fa-filter mr-2"></i> HIZLI FİLTRE</span>
                        <i class="fas fa-chevron-down transition-transform duration-300" id="filterNav-chevron"></i>
                    </button>
                    <div id="filterNav" class="space-y-1.5 hidden">'''
    
    content = content.replace(old_filter_header, new_filter_header)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Sidebar bölümleri aç/kapat özelliği eklendi.")
