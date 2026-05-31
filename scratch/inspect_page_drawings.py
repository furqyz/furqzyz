import fitz

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    
    # Inspect Page 24 (Questions)
    page_24 = doc[23]
    drawings_24 = page_24.get_drawings()
    print(f"=== Page 24 (Drawings Count: {len(drawings_24)}) ===")
    
    for idx, d in enumerate(drawings_24):
        fill = d.get("fill")
        rect = d.get("rect")
        if fill:
            r, g, b = fill
            color_name = "Other"
            if r < 0.1 and g > 0.9 and b > 0.9:
                color_name = "Turquoise"
            elif r > 0.9 and g < 0.1 and b < 0.1:
                color_name = "Red"
            elif r < 0.1 and g > 0.5 and b < 0.3:
                color_name = "Green (Checkmark)"
            
            print(f"  Shape {idx+1}: Color={color_name} ({r:.3f}, {g:.3f}, {b:.3f}), Rect=[{rect.x0:.1f}, {rect.y0:.1f}, {rect.x1:.1f}, {rect.y1:.1f}]")
            
    # Inspect Page 27 (Solutions)
    page_27 = doc[26]
    drawings_27 = page_27.get_drawings()
    print(f"\n=== Page 27 (Drawings Count: {len(drawings_27)}) ===")
    
    for idx, d in enumerate(drawings_27):
        fill = d.get("fill")
        rect = d.get("rect")
        if fill:
            r, g, b = fill
            color_name = "Other"
            if r < 0.1 and g > 0.9 and b > 0.9:
                color_name = "Turquoise"
            elif r > 0.9 and g < 0.1 and b < 0.1:
                color_name = "Red"
            elif r < 0.1 and g > 0.5 and b < 0.3:
                color_name = "Green (Checkmark)"
                
            print(f"  Shape {idx+1}: Color={color_name} ({r:.3f}, {g:.3f}, {b:.3f}), Rect=[{rect.x0:.1f}, {rect.y0:.1f}, {rect.x1:.1f}, {rect.y1:.1f}]")

if __name__ == "__main__":
    main()
