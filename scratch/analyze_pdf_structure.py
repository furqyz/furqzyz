import fitz
import os

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    
    print(f"Total pages: {len(doc)}")
    
    # We will scan all pages and collect information about markings
    marked_data = []
    
    for page_idx in range(len(doc)):
        page = doc[page_idx]
        drawings = page.get_drawings()
        
        red_shapes = []
        turquoise_shapes = []
        green_shapes = []
        
        for d in drawings:
            fill = d.get("fill")
            rect = d.get("rect")
            if fill:
                r, g, b = fill
                # Turquoise
                if r < 0.1 and g > 0.9 and b > 0.9:
                    turquoise_shapes.append(rect)
                # Red
                elif r > 0.9 and g < 0.1 and b < 0.1:
                    red_shapes.append(rect)
                # Green
                elif r < 0.1 and g > 0.5 and b < 0.3:
                    green_shapes.append(rect)
                    
        if red_shapes or turquoise_shapes or green_shapes:
            marked_data.append({
                "page_1indexed": page_idx + 1,
                "red_count": len(red_shapes),
                "turquoise_count": len(turquoise_shapes),
                "green_count": len(green_shapes),
                "red_rects": [[r.x0, r.y0, r.x1, r.y1] for r in red_shapes],
                "turquoise_rects": [[r.x0, r.y0, r.x1, r.y1] for r in turquoise_shapes],
                "green_rects": [[r.x0, r.y0, r.x1, r.y1] for r in green_shapes],
            })
            
    print(f"\nAnalyzed {len(marked_data)} pages with markings.")
    
    # Let's print details for the first 15 marked pages to check coordinates
    for idx, p in enumerate(marked_data[:15]):
        print(f"\nPage {p['page_1indexed']}:")
        print(f"  Green checkmarks: {p['green_count']}")
        if p['green_rects']:
            print(f"    Sample: {p['green_rects'][:2]}")
        print(f"  Red marks (Wrong): {p['red_count']}")
        if p['red_rects']:
            print(f"    Sample: {p['red_rects'][:2]}")
        print(f"  Turquoise highlights: {p['turquoise_count']}")
        if p['turquoise_rects']:
            print(f"    Sample: {p['turquoise_rects'][:2]}")

if __name__ == "__main__":
    main()
