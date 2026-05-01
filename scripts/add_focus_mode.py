import os

html_dirs = [
    r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı\unitler', 
    r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı\turkce'
]

script_injection = """
    <!-- Akıllı Revizyon Modu Butonları -->
    <div class="focus-controls">
        <button id="focus-mode-btn" class="focus-btn" title="Odaklanma Modu (Sadece Notlar)">
            <i class="fas fa-expand"></i>
        </button>
        <button id="revision-mode-btn" class="focus-btn" title="Akıllı Revizyon (Sadece Kritikler)">
            <i class="fas fa-eye"></i>
        </button>
    </div>

    <script>
        (function() {
            const focusBtn = document.getElementById('focus-mode-btn');
            const revisionBtn = document.getElementById('revision-mode-btn');
            const body = document.body;

            if (focusBtn) {
                focusBtn.addEventListener('click', function() {
                    body.classList.toggle('focus-mode');
                    focusBtn.classList.toggle('active');
                    const icon = focusBtn.querySelector('i');
                    if (body.classList.contains('focus-mode')) {
                        icon.className = 'fas fa-compress';
                    } else {
                        icon.className = 'fas fa-expand';
                    }
                });
            }

            if (revisionBtn) {
                revisionBtn.addEventListener('click', function() {
                    body.classList.toggle('revision-mode');
                    revisionBtn.classList.toggle('active');
                });
            }
        })();
    </script>
"""

count = 0
for h_dir in html_dirs:
    if not os.path.exists(h_dir):
        continue
    for fn in os.listdir(h_dir):
        if fn.endswith('.html'):
            fp = os.path.join(h_dir, fn)
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'focus-controls' not in content:
                new_content = content.replace('</body>', script_injection + '\n</body>')
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

print(f'{count} dosyaya Akıllı Revizyon eklendi.')
