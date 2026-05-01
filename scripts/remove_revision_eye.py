import os
import re

html_dirs = [
    r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı\unitler', 
    r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı\turkce',
    r'c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı'
]

# Göz butonunu içeren bloğu hedefleyen regex
target_pattern = r'<!-- Akıllı Revizyon Modu Butonları -->.*?<\/script>'

new_injection = """
    <!-- Odaklanma Modu Butonu -->
    <div class="focus-controls">
        <button id="focus-mode-btn" class="focus-btn" title="Odaklanma Modu (Sadece Notlar)">
            <i class="fas fa-expand"></i>
        </button>
    </div>

    <script>
        (function() {
            const focusBtn = document.getElementById('focus-mode-btn');
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
        })();
    </script>
"""

count = 0
for h_dir in html_dirs:
    if not os.path.exists(h_dir): continue
    for fn in os.listdir(h_dir):
        if fn.endswith('.html'):
            fp = os.path.join(h_dir, fn)
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Göz butonunu içeren bloğu kaldır
            if 'focus-controls' in content:
                content = re.sub(target_pattern, '', content, flags=re.DOTALL)
                
                # Sadece odaklanma butonunu ekle
                if 'id="focus-mode-btn"' not in content:
                    content = content.replace('</body>', new_injection + '\n</body>')
                
                # Dark mode anahtarını 'darkMode' olarak sabitleyelim
                content = content.replace("localStorage.getItem('dark-mode')", "localStorage.getItem('darkMode')")
                content = content.replace("localStorage.setItem('dark-mode',", "localStorage.setItem('darkMode',")
                
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1

print(f'{count} dosyada düzenleme yapıldı.')
