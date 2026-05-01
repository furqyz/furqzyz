import re
import glob

pattern = re.compile(r'\s*<div class=\"p-5 bg-gradient-to-br from-indigo-50 to-blue-50.*?</div>\s*</div>', re.DOTALL)

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub('', content)
    
    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file}')
