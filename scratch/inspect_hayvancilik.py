import re

with open("cografya/tuik-hayvancilik.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for animal cards
# Usually cards look like: <div data-category="..." or similar or just standard card structures.
# Let's print out text around cards
cards = re.findall(r'<h4[^>]*>(.*?)</h4>', content, re.DOTALL)
print("Animal Headings:")
for c in cards:
    print("  " + re.sub(r'<[^>]+>', '', c).strip())
