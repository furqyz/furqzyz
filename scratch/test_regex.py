import re
import os

filepath = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\cografya\tuik-koruma.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's try the script's regex
regex = r'<section[^>]*class="[^"]*note-card[^"]*"[^>]*>(.*?)</section>'
matches = list(re.finditer(regex, content, re.DOTALL))
print(f"Regex matches: {len(matches)}")

# Let's see what is inside the file
print("Checking for note-card classes in file:")
for line in content.split('\n'):
    if 'note-card' in line:
        print(line[:120])
