import fitz
import sys
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\tüik.pdf"
doc = fitz.open(pdf_path)

toc = doc.get_toc()
for item in toc:
    print(f"Level {item[0]}: {item[1]} (Page {item[2]})")
