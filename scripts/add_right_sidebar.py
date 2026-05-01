import os
import re

right_sidebar = """
        <!-- Sağ Sidebar (Hap Bilgiler) -->
        <aside class="w-full xl:w-[320px] shrink-0 hidden xl:block">
            <div class="sticky top-28 h-[calc(100vh-8rem)] bg-white/80 dark:bg-slate-800/80 backdrop-blur-xl rounded-3xl shadow-lg shadow-slate-200/50 dark:shadow-none border border-slate-100 dark:border-slate-700 overflow-hidden flex flex-col relative">
                <div class="p-5 border-b border-slate-100 dark:border-slate-700 bg-white/90 dark:bg-slate-800/90 backdrop-blur-md relative z-10">
                    <h3 class="font-black text-slate-800 dark:text-white flex items-center text-lg tracking-tight">
                        <div class="bg-yellow-100 dark:bg-yellow-900/50 p-2 rounded-xl mr-3">
                            <i class="fas fa-bolt text-yellow-500 dark:text-yellow-400 text-sm"></i>
                        </div>
                        HAP BİLGİLER
                    </h3>
                    <p class="text-[10px] text-slate-500 dark:text-slate-400 mt-2 font-bold uppercase tracking-widest pl-12">Sınavda Hayat Kurtarır</p>
                </div>
                
                <div class="flex-1 overflow-hidden relative group">
                    <div class="absolute top-0 inset-x-0 h-12 bg-gradient-to-b from-white dark:from-slate-800 to-transparent z-10 pointer-events-none"></div>
                    <div class="absolute bottom-0 inset-x-0 h-12 bg-gradient-to-t from-white dark:from-slate-800 to-transparent z-10 pointer-events-none"></div>
                    
                    <div id="tickerContainer" class="flex flex-col gap-4 p-4 pb-0 hover:[animation-play-state:paused]">
                        <!-- JS ile dinamik doldurulacak -->
                    </div>
                </div>
            </div>
        </aside>
"""

# HTML replace function
files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]
for filename in files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace main container classes to add right sidebar
    content = content.replace('max-w-[1600px] mx-auto flex flex-col lg:flex-row gap-8 lg:gap-12 p-4 md:p-8 lg:px-12', 'max-w-[1800px] mx-auto flex flex-col xl:flex-row gap-6 lg:gap-8 p-4 md:p-6 lg:px-8')
    content = content.replace('w-full lg:w-72 shrink-0', 'w-full xl:w-72 shrink-0')
    
    # Insert right sidebar before the closing div of the flex container
    if '<!-- Sağ Sidebar (Hap Bilgiler) -->' not in content:
        pattern = r'(</main>\s*)(</div>\s*<!-- Footer -->)'
        content = re.sub(pattern, r'\1' + right_sidebar + r'\n    \2', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("HTML dosyaları güncellendi.")
