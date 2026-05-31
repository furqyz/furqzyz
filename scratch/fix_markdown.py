import os
import re
import glob

def process_file(file_path):
    print(f"Processing: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match ***text*** -> <strong><em>text</em></strong>
    content_fixed = re.sub(r'\*\*\*([^*]+)\*\*\*', r'<strong><em>\1</em></strong>', content)
    # Match **text** -> <strong>text</strong>
    content_fixed = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', content_fixed)

    if content != content_fixed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content_fixed)
        print(f"  Fixed markdown in {file_path}")
    else:
        print(f"  No changes needed in {file_path}")

def main():
    workspace_dir = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane"
    
    # 1. Target all HTML files in the root directory
    root_html_files = glob.glob(os.path.join(workspace_dir, "*.html"))
    for file_path in root_html_files:
        process_file(file_path)
        
    # 2. Target all HTML files in cografya directory
    cografya_dir = os.path.join(workspace_dir, "cografya")
    cografya_html_files = glob.glob(os.path.join(cografya_dir, "*.html"))
    for file_path in cografya_html_files:
        process_file(file_path)

if __name__ == "__main__":
    main()
