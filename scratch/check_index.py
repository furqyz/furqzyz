import json
with open(r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\assets\js\searchIndex_cografya.js", "r", encoding="utf-8") as f:
    content = f.read()

# It starts with "const searchIndex = ["
json_str = content[content.find('['): content.rfind(';')]
data = json.loads(json_str)
for item in data:
    if 'unesco' in item.get('title', '').lower() or 'unesco' in item.get('content', '').lower():
        print(f"FOUND: {item['title']} in {item['url']}")
        
    if 'ramsar' in item.get('title', '').lower() or 'ramsar' in item.get('content', '').lower():
        print(f"FOUND: {item['title']} in {item['url']}")
