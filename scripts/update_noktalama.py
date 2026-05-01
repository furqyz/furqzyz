import os
import re

file_path = r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı\turkce\noktalama-diger-isaretler.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_sections = '''                <section class="note-card category-indigo p-6 md:p-8 rounded-2xl shadow-sm lg:col-span-2">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-indigo-900 dark:text-indigo-200">
                        <div class="bg-indigo-100 dark:bg-indigo-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-minus text-indigo-600 dark:text-indigo-300"></i>
                        </div>
                        Kısa Çizgi (-)
                    </h3>
                    <ul class="space-y-4 text-sm text-slate-700 dark:text-slate-300">
                        <li class="flex items-start">
                            <i class="fas fa-chevron-right text-indigo-500 mt-1 mr-2"></i>
                            <div>Cümle içindeki ara sözlerin ve ara cümlelerin başına ve sonuna konur.</div>
                        </li>
                        <li class="flex items-start">
                            <i class="fas fa-chevron-right text-indigo-500 mt-1 mr-2"></i>
                            <div>Bir olayın veya durumun başlangıç-bitişini göstermek için tarihlerin ve kelimelerin arasına eklenir.<br><em class="opacity-80 text-xs">Örn: 1914-1918, Türk-Alman ilişkileri</em></div>
                        </li>
                    </ul>
                </section>

                <section class="note-card category-purple p-6 md:p-8 rounded-2xl shadow-sm">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-purple-900 dark:text-purple-200">
                        <div class="bg-purple-100 dark:bg-purple-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-quote-right text-purple-600 dark:text-purple-300"></i>
                        </div>
                        Tırnak İşareti (" ")
                    </h3>
                    <ul class="space-y-4 text-sm text-slate-700 dark:text-slate-300">
                        <li class="flex items-start">
                            <i class="fas fa-check text-purple-500 mt-1 mr-2"></i>
                            <div>Başkalarından yapılan <strong>doğrudan alıntı sözlerin</strong> başına ve sonuna konur.</div>
                        </li>
                        <li class="flex items-start">
                            <i class="fas fa-check text-purple-500 mt-1 mr-2"></i>
                            <div>Metin içinde özellikle vurgulanmak istenen terimler ile kitap ve sanat eseri adları tırnak içine alınır.</div>
                        </li>
                    </ul>
                    <div class="mt-4 bg-purple-50 dark:bg-purple-900/30 p-4 rounded-xl border border-purple-100 dark:border-purple-800/50 text-xs text-purple-800 dark:text-purple-300">
                        <strong>Not (Tek Tırnak):</strong> Tırnak içindeki bir cümlenin içinde tekrar alıntı yapmak veya vurgu yapmak gerekirse Tek Tırnak (' ') kullanılır.
                    </div>
                </section>

                <section class="note-card category-teal p-6 md:p-8 rounded-2xl shadow-sm">
                    <h3 class="text-xl font-extrabold mb-6 flex items-center text-teal-900 dark:text-teal-200">
                        <div class="bg-teal-100 dark:bg-teal-900/50 p-2.5 rounded-xl mr-3 shadow-sm">
                            <i class="fas fa-code text-teal-600 dark:text-teal-300"></i>
                        </div>
                        Yay Ayraç ( )
                    </h3>
                    <p class="text-sm text-slate-700 dark:text-slate-300 mb-4">Cümle içinde bir kelimenin eş anlamlısını veya cümleye ait ek açıklamaları vermek için kullanılır.</p>
                    <div class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-100 dark:border-slate-800 text-xs font-mono mb-4">
                        Mübalağa (abartma) sanatı
                    </div>
                    <div class="bg-teal-50 dark:bg-teal-900/30 p-4 rounded-xl border border-teal-100 dark:border-teal-800/50 text-xs text-teal-800 dark:text-teal-300">
                        <strong>Not (Köşeli Ayraç):</strong> Ayraç içinde tekrar bir açıklama ayracı açmak gerekirse, en dışta Köşeli Ayraç ([ ]) kullanılır.
                    </div>
                </section>

            <!-- SINAV HAFIZASI -->'''

content = content.replace('<!-- SINAV HAFIZASI -->', new_sections)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Noktalama updated.")
