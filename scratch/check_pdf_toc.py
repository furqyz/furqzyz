import fitz

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    
    toc = doc.get_toc()
    print(f"Table of Contents (total items: {len(toc)}):")
    for item in toc[:30]:
        print(f"  Level {item[0]}: {item[1]} -> Page {item[2]}")

if __name__ == "__main__":
    main()
