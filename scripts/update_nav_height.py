import glob

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('max-h-[85vh]', 'max-h-[85vh]')
    
    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file}')

import glob

for file in glob.glob('*.py'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('max-h-[85vh]', 'max-h-[85vh]')
    
    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file}')
