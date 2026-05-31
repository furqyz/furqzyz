import os
import re

root_dir = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane"

html_files = []
for root, dirs, files in os.walk(root_dir):
    if "cografya_pages" in root or "furkan" in root or "scratch" in root or ".gemini" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the inline script that attaches to 'dark-mode-toggle'
    content = re.sub(r"document\.getElementById\('dark-mode-toggle'\)\.addEventListener\('click',\s*\(\)\s*=>\s*\{.*?\}\);", "", content, flags=re.DOTALL)
    
    # 2. Let's fix the dark mode text colors to make them brighter
    content = content.replace("dark:text-slate-500", "dark:text-slate-300")
    content = content.replace("dark:text-slate-400", "dark:text-slate-200")
    content = content.replace("dark:text-gray-500", "dark:text-gray-300")
    content = content.replace("dark:text-gray-400", "dark:text-gray-200")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated HTML files for theme inline script and text color contrast.")
