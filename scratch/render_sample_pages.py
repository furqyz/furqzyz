import fitz
import os

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    
    output_dir = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\scratch"
    os.makedirs(output_dir, exist_ok=True)
    
    # Render pages 24, 25, 27
    pages_to_render = [24, 25, 27]
    for p in pages_to_render:
        page = doc[p - 1]
        # High resolution (2x zoom) for crisp text
        zoom = 2.0
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        
        output_path = os.path.join(output_dir, f"page_{p}.png")
        pix.save(output_path)
        print(f"Saved: {output_path}")

if __name__ == "__main__":
    main()
