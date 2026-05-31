import fitz
import os

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    
    # Combined target pages to render
    question_pages = [24, 25, 30, 31, 32, 37, 42, 47, 62, 68, 72, 76, 79, 80, 83, 84, 87, 92, 96, 101, 108, 109, 110, 114, 115, 118, 119, 122, 128, 133, 142]
    solution_pages = [27, 29, 35, 36, 39, 81, 89, 90, 91, 94, 95, 98, 103, 112, 116, 117, 120, 121, 125, 135, 136, 139, 140]
    
    target_pages = sorted(list(set(question_pages + solution_pages)))
    
    out_dir = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\scratch\temp_rendered"
    os.makedirs(out_dir, exist_ok=True)
    
    print(f"Rendering {len(target_pages)} target pages...")
    
    for pnum in target_pages:
        # 0-indexed page in fitz
        page = doc[pnum - 1]
        
        # 2x zoom for high readability
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))
        out_path = os.path.join(out_dir, f"page_{pnum}.jpg")
        
        # Save as JPEG with good quality
        pix.save(out_path)
        print(f"Rendered and saved: page_{pnum}.jpg")
        
    print("Done rendering all target pages!")

if __name__ == "__main__":
    main()
