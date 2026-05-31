import fitz
import os

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    
    highlighted_pages = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        drawings = page.get_drawings()
        
        has_turquoise = False
        has_red = False
        
        for draw in drawings:
            fill = draw.get("fill")
            if fill:
                r, g, b = fill[0], fill[1], fill[2]
                # Turquoise check: very high green and blue, zero red
                if r < 0.1 and g > 0.9 and b > 0.9:
                    has_turquoise = True
                # Red check: very high red, zero green/blue
                elif r > 0.9 and g < 0.1 and b < 0.1:
                    has_red = True
                    
        if has_turquoise or has_red:
            highlighted_pages.append({
                "page": page_num + 1,
                "has_turquoise": has_turquoise,
                "has_red": has_red
            })
            
    print(f"Found {len(highlighted_pages)} marked pages out of {len(doc)} pages.")
    print("\nMarked Pages List:")
    for p in highlighted_pages:
        types = []
        if p["has_turquoise"]: types.append("Turquoise (Cyan)")
        if p["has_red"]: types.append("Red (Wrong)")
        print(f"  Page {p['page']}: {', '.join(types)}")

if __name__ == "__main__":
    main()
