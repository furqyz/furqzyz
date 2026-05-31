import fitz
import os

pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\tüik.pdf"
doc = fitz.open(pdf_path)
print(f"Number of pages: {len(doc)}")

for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    print(f"\n--- Page {i+1} ---")
    lines = text.split('\n')
    # Print first few non-empty lines
    printed = 0
    for line in lines:
        cleaned = line.strip()
        if cleaned:
            print(f"  {cleaned}")
            printed += 1
            if printed >= 10:
                break
