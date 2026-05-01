import os
import re

html_files = ['index.html'] + [f'unitler/unite{i}.html' for i in range(2, 26)]

left_colors = [('purple', 'purple'), ('yellow', 'yellow'), ('orange', 'orange')]
right_colors = [('turquoise', 'cyan'), ('green', 'emerald'), ('red', 'red')]

category_to_tailwind = {
    'purple': 'purple',
    'turquoise': 'cyan',
    'yellow': 'yellow',
    'green': 'emerald',
    'orange': 'orange',
    'red': 'red'
}

for filename in html_files:
    filepath = os.path.join(r"c:\Users\67ded\OneDrive\Masaüstü\tarih özet kanalı", filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    has_grid = 'mt-8"' in content and 'grid-cols-1 xl:grid-cols-2' in content
    
    # We find all sections
    all_sections = re.findall(r'(<section class="category-[a-z]+ note-card[\s\S]*?</section>)', content)
    
    if not all_sections:
        continue
        
    masonry_sections = all_sections[:-2] if has_grid else all_sections
    grid_sections = all_sections[-2:] if has_grid else []
    
    n_masonry = len(masonry_sections)
    half = (n_masonry + 1) // 2
    
    new_content = content
    
    for i, old_section in enumerate(masonry_sections):
        if i < half:
            target_cat, target_tail = left_colors[i % len(left_colors)]
        else:
            target_cat, target_tail = right_colors[(i - half) % len(right_colors)]
            
        match = re.search(r'class="category-([a-z]+)', old_section)
        if not match: continue
        old_cat = match.group(1)
        old_tail = category_to_tailwind.get(old_cat, old_cat)
        
        new_section = old_section
        if old_cat != target_cat:
            new_section = new_section.replace(f'category-{old_cat}', f'category-{target_cat}')
            for weight in ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900']:
                new_section = new_section.replace(f'{old_tail}-{weight}', f'{target_tail}-{weight}')
                
        new_content = new_content.replace(old_section, new_section, 1)

    if grid_sections:
        left_idx = half % len(left_colors)
        right_idx = (n_masonry - half) % len(right_colors)
        
        for i, old_section in enumerate(grid_sections):
            if i == 0:
                target_cat, target_tail = left_colors[left_idx]
            else:
                target_cat, target_tail = right_colors[right_idx]
                
            match = re.search(r'class="category-([a-z]+)', old_section)
            if not match: continue
            old_cat = match.group(1)
            old_tail = category_to_tailwind.get(old_cat, old_cat)
            
            new_section = old_section
            if old_cat != target_cat:
                new_section = new_section.replace(f'category-{old_cat}', f'category-{target_cat}')
                for weight in ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900']:
                    new_section = new_section.replace(f'{old_tail}-{weight}', f'{target_tail}-{weight}')
                    
            new_content = new_content.replace(old_section, new_section, 1)
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
print("Renkler Sütun mantığına göre sol-sağ uyumlu olacak şekilde yeniden hesaplandı.")
