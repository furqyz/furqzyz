import os

modal_html = """
    <!-- Harita Detay Modalı -->
    <div id="mapModal" class="fixed inset-0 z-[100] bg-slate-900/80 backdrop-blur-sm hidden flex items-center justify-center p-4 transition-all duration-300" onclick="closeMapModal()">
        <div class="bg-white dark:bg-slate-800 rounded-3xl max-w-4xl w-full p-4 md:p-6 border border-slate-200 dark:border-slate-700 shadow-2xl relative" onclick="event.stopPropagation()">
            <button onclick="closeMapModal()" class="absolute top-4 right-4 bg-slate-100 dark:bg-slate-900 hover:bg-slate-200 dark:hover:bg-slate-800 text-slate-500 dark:text-slate-400 p-2.5 rounded-full transition-colors z-50 cursor-pointer">
                <i class="fas fa-times text-lg"></i>
            </button>
            <h3 id="modalTitle" class="text-lg font-extrabold text-slate-900 dark:text-white mb-4 pr-10">Harita Detayı</h3>
            <div class="bg-slate-50 dark:bg-slate-900 p-2 rounded-2xl border border-slate-200/50 dark:border-slate-800 flex justify-center items-center max-h-[80vh] overflow-hidden">
                <img id="modalImage" src="" alt="Harita Detayı" class="max-w-full max-h-[70vh] h-auto object-contain rounded-xl">
            </div>
        </div>
    </div>

    <script>
        function openMapModal(src, title) {
            document.getElementById('modalImage').src = src;
            document.getElementById('modalTitle').innerText = title;
            const modal = document.getElementById('mapModal');
            modal.classList.remove('hidden');
            document.body.style.overflow = 'hidden';
        }
        
        function closeMapModal() {
            const modal = document.getElementById('mapModal');
            modal.classList.add('hidden');
            document.body.style.overflow = '';
        }
        
        // Escape tuşu ile kapatma
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') closeMapModal();
        });
    </script>
</body>
</html>
"""

files = ["cografya/tuik-tarim.html", "cografya/tuik-hayvancilik.html"]

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if modal is already injected to prevent double injection
    if 'id="mapModal"' in content:
        print(f"Modal already present in {fpath}")
        continue
        
    if "</body>" in content:
        content = content.replace("</body>\n</html>", modal_html)
        content = content.replace("</body></html>", modal_html)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully injected map detail modal into {fpath}")
    else:
        print(f"Could not find </body> in {fpath}")
