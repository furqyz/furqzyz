import os
import re

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def inject_script_into_file(filepath, script_tag):
    full_path = os.path.join(root_dir, filepath)
    if not os.path.exists(full_path):
        print(f"File not found: {filepath}")
        return
        
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if script.js is already included (either as assets/js/script.js or ../assets/js/script.js)
    if 'script.js' in content:
        # print(f"Script already exists in {filepath}")
        return
        
    # Find the closing </body> tag
    if '</body>' in content:
        new_content = content.replace('</body>', f'    {script_tag}\n</body>')
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected script into {filepath}")
    else:
        print(f"Could not find </body> in {filepath}")

# 1. Landing pages
inject_script_into_file('tarih.html', '<script src="assets/js/script.js"></script>')
inject_script_into_file('cografya.html', '<script src="assets/js/script.js"></script>')
inject_script_into_file('turkce.html', '<script src="assets/js/script.js"></script>')

# 2. Turkish subdirectory files
turkce_dir = os.path.join(root_dir, 'turkce')
if os.path.exists(turkce_dir):
    for filename in os.listdir(turkce_dir):
        if filename.endswith('.html'):
            inject_script_into_file(f'turkce/{filename}', '<script src="../assets/js/script.js"></script>')

# 3. Geography subdirectory files
cografya_dir = os.path.join(root_dir, 'cografya')
if os.path.exists(cografya_dir):
    for filename in os.listdir(cografya_dir):
        if filename.endswith('.html'):
            inject_script_into_file(f'cografya/{filename}', '<script src="../assets/js/script.js"></script>')

print("Injection script finished.")
