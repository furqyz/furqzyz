with open("cografya/tuik-hayvancilik.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("Kümes Hayvancılığı Özellikleri")
if idx != -1:
    snippet = content[idx:idx+1500]
    # Print the clean code
    clean_snippet = "".join([c if ord(c) < 128 else '?' for c in snippet])
    print(clean_snippet)
