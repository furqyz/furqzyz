import os
import re

html_files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]

OLD_MODAL = '''    <!-- Hızlı Filtre Modal -->
    <div id="filterModal" class="fixed inset-0 z-[100] hidden">
        <div class="absolute inset-0 bg-black/60 backdrop-blur-sm" onclick="closeFilterPanel()"></div>
        <div class="absolute right-0 top-0 h-full w-full max-w-2xl bg-white dark:bg-slate-900 shadow-2xl flex flex-col transform transition-transform duration-300 translate-x-full" id="filterPanel">
            <!-- Modal Header -->
            <div class="flex items-center justify-between p-6 border-b border-slate-100 dark:border-slate-800 shrink-0">
                <div class="flex items-center space-x-3">
                    <div id="filterIcon" class="w-10 h-10 rounded-xl flex items-center justify-center text-white text-lg"></div>
                    <div>
                        <h2 id="filterTitle" class="text-xl font-black text-slate-900 dark:text-white"></h2>
                        <p id="filterCount" class="text-xs text-slate-500 dark:text-slate-400 mt-0.5"></p>
                    </div>
                </div>
                <button onclick="closeFilterPanel()" class="w-9 h-9 flex items-center justify-center rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors text-slate-500 dark:text-slate-400">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <!-- Search inside modal -->
            <div class="px-6 py-4 border-b border-slate-100 dark:border-slate-800 shrink-0">
                <div class="flex items-center bg-slate-100 dark:bg-slate-800 rounded-xl px-4 py-2.5">
                    <i class="fas fa-search text-slate-400 text-sm"></i>
                    <input type="text" id="filterSearch" placeholder="Bu listede ara..." class="bg-transparent outline-none border-none ml-3 text-sm text-slate-800 dark:text-slate-200 placeholder-slate-400 w-full" oninput="filterModalSearch(this.value)">
                </div>
            </div>
            <!-- Results -->
            <div id="filterResults" class="flex-1 overflow-y-auto p-6 space-y-3">
            </div>
        </div>
    </div>'''

NEW_MODAL = '''    <!-- Hızlı Filtre Modal -->
    <div id="filterModal" class="fixed inset-0 z-[100] hidden flex items-center justify-center p-4">
        <div class="absolute inset-0 bg-slate-900/70 backdrop-blur-md" onclick="closeFilterPanel()"></div>
        <div class="relative w-full max-w-3xl bg-white dark:bg-slate-900 rounded-3xl shadow-2xl flex flex-col transform transition-all duration-300 scale-95 opacity-0 max-h-[85vh]" id="filterPanel">
            <!-- Dekoratif gradient şerit -->
            <div id="filterHeaderGradient" class="h-1.5 w-full rounded-t-3xl"></div>
            <!-- Modal Header -->
            <div class="flex items-center justify-between px-8 py-5 shrink-0">
                <div class="flex items-center space-x-4">
                    <div id="filterIcon" class="w-12 h-12 rounded-2xl flex items-center justify-center text-white text-xl shadow-lg"></div>
                    <div>
                        <h2 id="filterTitle" class="text-2xl font-black text-slate-900 dark:text-white tracking-tight"></h2>
                        <p id="filterCount" class="text-xs text-slate-400 dark:text-slate-500 mt-0.5 font-semibold uppercase tracking-widest"></p>
                    </div>
                </div>
                <button onclick="closeFilterPanel()" class="w-10 h-10 flex items-center justify-center rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors text-slate-400 dark:text-slate-500 hover:text-slate-600 dark:hover:text-slate-300">
                    <i class="fas fa-times text-lg"></i>
                </button>
            </div>
            <!-- Search inside modal -->
            <div class="px-8 pb-4 shrink-0">
                <div class="flex items-center bg-slate-100 dark:bg-slate-800 rounded-2xl px-4 py-3 border border-slate-200 dark:border-slate-700 focus-within:ring-2 focus-within:ring-indigo-400 transition-all">
                    <i class="fas fa-search text-slate-400 text-sm"></i>
                    <input type="text" id="filterSearch" placeholder="Bu listede ara..." class="bg-transparent outline-none border-none ml-3 text-sm text-slate-700 dark:text-slate-200 placeholder-slate-400 w-full font-medium" oninput="filterModalSearch(this.value)">
                </div>
            </div>
            <!-- Divider -->
            <div class="border-t border-slate-100 dark:border-slate-800 mx-8"></div>
            <!-- Results -->
            <div id="filterResults" class="flex-1 overflow-y-auto px-8 py-5 space-y-4">
            </div>
        </div>
    </div>'''

for filename in html_files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(OLD_MODAL, NEW_MODAL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Modal tasarımı güncellendi - artık ortada açılıyor ve daha premium görünüyor.")
