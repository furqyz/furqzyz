import re

def inspect_html(filepath):
    print(f"\n===== Inspecting {filepath} =====")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find all note-cards or lists of products
    cards = re.findall(r'<h3[^>]*>(.*?)</h3>', content, re.DOTALL)
    print("Found titles:")
    for c in cards:
        print("  " + re.sub(r'<[^>]+>', '', c).strip())

inspect_html("cografya/tuik-tarim.html")
inspect_html("cografya/tuik-hayvancilik.html")
