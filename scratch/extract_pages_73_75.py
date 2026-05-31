import fitz

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    
    # We render pages 73, 74, 75
    for p_num in [73, 74, 75]:
        page = doc[p_num - 1]
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        pix.save(f"c:\\Users\\67ded\\OneDrive\\Masaüstü\\Özethane\\scratch\\page_{p_num}.jpg")
        print(f"Rendered page {p_num} to scratch/page_{p_num}.jpg")

if __name__ == "__main__":
    main()
