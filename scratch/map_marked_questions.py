import fitz
import json
import os

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    
    pages_info = []
    
    for page_idx in range(len(doc)):
        page = doc[page_idx]
        drawings = page.get_drawings()
        
        green_shapes = []
        red_shapes = []
        turquoise_shapes = []
        
        for d in drawings:
            fill = d.get("fill")
            rect = d.get("rect")
            if fill:
                r, g, b = fill
                # Green checkmark
                if r < 0.1 and g > 0.5 and b < 0.3:
                    green_shapes.append(rect)
                # Red wrong
                elif r > 0.9 and g < 0.1 and b < 0.1:
                    red_shapes.append(rect)
                # Turquoise highlight
                elif r < 0.1 and g > 0.9 and b > 0.9:
                    turquoise_shapes.append(rect)
                    
        # If it has any of these marks, record it
        if green_shapes or red_shapes or turquoise_shapes:
            page_type = "Question" if len(green_shapes) > 0 else "Solution"
            pages_info.append({
                "page_1indexed": page_idx + 1,
                "type": page_type,
                "green_count": len(green_shapes),
                "red_count": len(red_shapes),
                "turquoise_count": len(turquoise_shapes),
                "red_rects": [[r.x0, r.y0, r.x1, r.y1] for r in red_shapes],
                "turquoise_rects": [[r.x0, r.y0, r.x1, r.y1] for r in turquoise_shapes],
                "green_rects": [[r.x0, r.y0, r.x1, r.y1] for r in green_shapes],
            })
            
    print(f"Total marked pages found: {len(pages_info)}")
    
    # Save this metadata as JSON in the scratch folder
    output_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\scratch\marked_pages_meta.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(pages_info, f, indent=4)
    print(f"Saved metadata to {output_path}")
    
    # Print the grouped sequence of Question vs Solution sections
    print("\nPage Sections Sequence:")
    current_type = None
    start_page = None
    end_page = None
    
    for p in pages_info:
        ptype = p["type"]
        pnum = p["page_1indexed"]
        
        if current_type is None:
            current_type = ptype
            start_page = pnum
            end_page = pnum
        elif ptype == current_type:
            end_page = pnum
        else:
            print(f"  Section {current_type}s: Pages {start_page} to {end_page}")
            current_type = ptype
            start_page = pnum
            end_page = pnum
            
    if current_type is not None:
        print(f"  Section {current_type}s: Pages {start_page} to {end_page}")

if __name__ == "__main__":
    main()
