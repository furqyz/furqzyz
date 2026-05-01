import os
import re

html_files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]

for filename in html_files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<!-- Hızlı Filtre Paneli -->' not in content:
        continue

    # Sorun: </nav> kapanışından sonra filtre paneli geliyor ama nav'ı saran div kapanmadan önce geliyor.
    # Beklenen yapı:
    #   </nav>
    #   </div>   <-- nav'ı saran bg-white kartı kapanır
    # 
    # Sonra filtre paneli kendi kartında gelir:
    #   <!-- Hızlı Filtre Paneli -->
    #   <div class="bg-white ...">
    
    # Şu an filtre paneli </div> kapanışından ÖNCE geliyor (nav kartı hâlâ açık)
    # Bunu düzelt: nav kartının kapanış </div>'ini bul, filtre panelinin önüne koy
    
    # Mevcut hatalı yapı:
    # </nav>\n\n                <!-- Hızlı Filtre Paneli -->
    # Doğru yapı:
    # </nav>\n                </div>\n\n                <!-- Hızlı Filtre Paneli -->
    
    bad_pattern = r'(</nav>)\s*\n(\s*)(<!-- Hızlı Filtre Paneli -->)'
    
    def fix_nav_close(m):
        return m.group(1) + '\n' + m.group(2) + '</div>\n\n' + m.group(2) + m.group(3)
    
    new_content = re.sub(bad_pattern, fix_nav_close, content)
    
    # Ayrıca filtre paneli kapanışındaki fazladan </div> varsa temizle
    # Kapanış yapısı: </div> </div> </div> </aside>
    # Doğru olması gereken: </div> </div> </aside>
    # </div>\n                </div>\n            </div>\n        </aside>
    # bunu: </div>\n            </div>\n        </aside> yapmalıyız
    
    new_content = new_content.replace(
        '                </div>\n                </div>\n            </div>\n        </aside>',
        '                </div>\n            </div>\n        </aside>'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
print("Sidebar kart yapısı düzeltildi - nav kartı artık doğru şekilde kapanıyor.")
