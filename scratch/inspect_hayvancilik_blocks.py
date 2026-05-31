with open("cografya/tuik-hayvancilik.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's find some paragraphs or structures
import re
# Print surrounding text of "Koyun"
start_idx = content.find("<!-- KOYUN -->")
if start_idx != -1:
    print("=== Koyun Block ===")
    print(content[start_idx:start_idx+1000])

start_idx = content.find("<!-- SIĞIR -->")
if start_idx != -1:
    print("\n=== Sığır Block ===")
    print(content[start_idx:start_idx+1000])
