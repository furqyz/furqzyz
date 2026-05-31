import fitz
import sys

pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\tüik.pdf"
doc = fitz.open(pdf_path)

with open(r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\scratch\pdf_text.txt", "w", encoding="utf-8") as f:
    for page_index in range(len(doc)):
        page = doc.load_page(page_index)
        text = page.get_text()
        f.write(f"\n--- PAGE {page_index+1} ---\n")
        f.write(text)
