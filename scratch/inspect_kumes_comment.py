with open("cografya/tuik-hayvancilik.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = re.findall(r'(<!--.*?KÜMES.*?-->)', content, re.IGNORECASE)
print("Kümes comment matches:", matches)
