import os
import re
import glob
import shutil

# Create directory
if not os.path.exists('unitler'):
    os.makedirs('unitler')

# Move files
for i in range(2, 12):
    file = f'unite{i}.html'
    if os.path.exists(file):
        shutil.move(file, f'unitler/{file}')

# Update index.html
if os.path.exists('index.html'):
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update links from index.html to unite*.html
    content = re.sub(r'href="unite(\d+)\.html"', r'href="unitler/unite\1.html"', content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

# Update unite*.html inside unitler/
for file in glob.glob('unitler/unite*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update link to index.html
    content = content.replace('href="index.html"', 'href="../index.html"')
    
    # 2. Update css and js paths
    content = content.replace('href="style.css"', 'href="../style.css"')
    content = content.replace('src="script.js"', 'src="../script.js"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Refactoring complete.")
