import os

html_files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]

SIDEBAR_INJECT = '''
                <!-- Hızlı Filtre Paneli -->
                <div class="bg-white dark:bg-slate-800 rounded-2xl shadow-sm border border-slate-100 dark:border-slate-700 p-4">
                    <h2 class="text-xs font-bold text-slate-400 dark:text-slate-500 uppercase tracking-widest px-3 mb-4 flex items-center">
                        <i class="fas fa-filter mr-2"></i> HIZLI FİLTRE
                    </h2>
                    <div class="space-y-1.5">
                        <button onclick="openFilterPanel('ilkler')" class="filter-btn w-full flex items-center space-x-3 px-3 py-2.5 rounded-xl transition-all group hover:bg-purple-50 dark:hover:bg-purple-900/30 text-left">
                            <span class="w-2.5 h-2.5 rounded-full bg-purple-500 shrink-0"></span>
                            <span class="text-[13px] font-semibold text-slate-600 dark:text-slate-300 group-hover:text-purple-700 dark:group-hover:text-purple-300">İlkler & Kesin Yargılar</span>
                        </button>
                        <button onclick="openFilterPanel('anlasma')" class="filter-btn w-full flex items-center space-x-3 px-3 py-2.5 rounded-xl transition-all group hover:bg-emerald-50 dark:hover:bg-emerald-900/30 text-left">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 shrink-0"></span>
                            <span class="text-[13px] font-semibold text-slate-600 dark:text-slate-300 group-hover:text-emerald-700 dark:group-hover:text-emerald-300">Antlaşmalar</span>
                        </button>
                        <button onclick="openFilterPanel('savas')" class="filter-btn w-full flex items-center space-x-3 px-3 py-2.5 rounded-xl transition-all group hover:bg-cyan-50 dark:hover:bg-cyan-900/30 text-left">
                            <span class="w-2.5 h-2.5 rounded-full bg-cyan-500 shrink-0"></span>
                            <span class="text-[13px] font-semibold text-slate-600 dark:text-slate-300 group-hover:text-cyan-700 dark:group-hover:text-cyan-300">Savaşlar</span>
                        </button>
                        <button onclick="openFilterPanel('sozler')" class="filter-btn w-full flex items-center space-x-3 px-3 py-2.5 rounded-xl transition-all group hover:bg-yellow-50 dark:hover:bg-yellow-900/30 text-left">
                            <span class="w-2.5 h-2.5 rounded-full bg-yellow-500 shrink-0"></span>
                            <span class="text-[13px] font-semibold text-slate-600 dark:text-slate-300 group-hover:text-yellow-700 dark:group-hover:text-yellow-300">Sözler</span>
                        </button>
                        <button onclick="openFilterPanel('isimler')" class="filter-btn w-full flex items-center space-x-3 px-3 py-2.5 rounded-xl transition-all group hover:bg-orange-50 dark:hover:bg-orange-900/30 text-left">
                            <span class="w-2.5 h-2.5 rounded-full bg-orange-500 shrink-0"></span>
                            <span class="text-[13px] font-semibold text-slate-600 dark:text-slate-300 group-hover:text-orange-700 dark:group-hover:text-orange-300">İsimler</span>
                        </button>
                        <button onclick="openFilterPanel('devlet')" class="filter-btn w-full flex items-center space-x-3 px-3 py-2.5 rounded-xl transition-all group hover:bg-indigo-50 dark:hover:bg-indigo-900/30 text-left">
                            <span class="w-2.5 h-2.5 rounded-full bg-indigo-500 shrink-0"></span>
                            <span class="text-[13px] font-semibold text-slate-600 dark:text-slate-300 group-hover:text-indigo-700 dark:group-hover:text-indigo-300">Devlet & Boylar</span>
                        </button>
                        <button onclick="openFilterPanel('kelimeler')" class="filter-btn w-full flex items-center space-x-3 px-3 py-2.5 rounded-xl transition-all group hover:bg-rose-50 dark:hover:bg-rose-900/30 text-left">
                            <span class="w-2.5 h-2.5 rounded-full bg-rose-500 shrink-0"></span>
                            <span class="text-[13px] font-semibold text-slate-600 dark:text-slate-300 group-hover:text-rose-700 dark:group-hover:text-rose-300">Kelimeler</span>
                        </button>
                    </div>
                </div>'''

MODAL_HTML = '''
    <!-- Hızlı Filtre Modal -->
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

for filename in html_files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Sidebar'a ekle - nav kapanışından hemen sonra, aside kapanışından önce
    if 'openFilterPanel' not in content:
        content = content.replace('                </div>\n            </div>\n        </aside>', 
                                  SIDEBAR_INJECT + '\n                </div>\n            </div>\n        </aside>', 1)

    # 2. Modal HTML'i body kapanışından önce ekle
    if 'filterModal' not in content:
        content = content.replace('</body>', MODAL_HTML + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Hızlı Filtre paneli ve modalı tüm sayfalara eklendi.")
