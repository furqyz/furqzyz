with open("cografya/tuik-hayvancilik.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = re.findall(r'(<!--.*?-->)', content)
print("Comments found:")
for m in matches:
    # Print clean comment without non-ascii
    clean_m = "".join([c if ord(c) < 128 else '?' for c in m])
    print("  ", clean_m)
