import os

html_files = []
for root, dirs, files in os.walk('.'):
    # exclude scripts folder
    if 'scripts' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Root level
    content = content.replace('href="style.css"', 'href="assets/css/style.css"')
    content = content.replace('src="script.js"', 'src="assets/js/script.js"')
    content = content.replace('src="searchIndex.js"', 'src="assets/js/searchIndex.js"')
    content = content.replace('src="test.js"', 'src="assets/js/test.js"')
    content = content.replace('src="testQuestions.js"', 'src="assets/js/testQuestions.js"')
    
    # Subfolder level
    content = content.replace('href="../style.css"', 'href="../assets/css/style.css"')
    content = content.replace('src="../script.js"', 'src="../assets/js/script.js"')
    content = content.replace('src="../searchIndex.js"', 'src="../assets/js/searchIndex.js"')
    content = content.replace('src="../test.js"', 'src="../assets/js/test.js"')
    content = content.replace('src="../testQuestions.js"', 'src="../assets/js/testQuestions.js"')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

os.makedirs('assets/css', exist_ok=True)
os.makedirs('assets/js', exist_ok=True)

if os.path.exists('style.css'):
    os.rename('style.css', 'assets/css/style.css')
    
for js in ['script.js', 'searchIndex.js', 'test.js', 'testQuestions.js']:
    if os.path.exists(js):
        os.rename(js, f'assets/js/{js}')

print('Refactored assets successfully.')
