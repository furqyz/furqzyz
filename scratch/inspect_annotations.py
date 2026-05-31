import fitz
import os

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    if not os.path.exists(pdf_path):
        print(f"Error: {pdf_path} does not exist.")
        return
        
    doc = fitz.open(pdf_path)
    print(f"PDF opened successfully. Total pages: {len(doc)}")
    
    # Check first 15 pages for annotations
    pages_to_check = min(30, len(doc))
    for page_num in range(pages_to_check):
        page = doc[page_num]
        annots = list(page.annots())
        drawings = page.get_drawings()
        
        # Filter for annotations or colored shapes
        if len(annots) > 0 or len(drawings) > 0:
            print(f"\n--- Page {page_num+1} ---")
            print(f"  Annotations: {len(annots)}")
            for idx, annot in enumerate(annots):
                print(f"    Annot {idx+1}: Type={annot.type}, Rect={annot.rect}, Colors={annot.colors}")
                # Try to get highlighted text if it's a Highlight annot
                # highlight type in PyMuPDF is 8 (or fitz.PDF_ANNOT_HIGHLIGHT)
                if annot.type[0] == 8:
                    # Get highlighted text
                    # We can use the annot's rect to extract text
                    text = page.get_text("text", clip=annot.rect)
                    print(f"      Text: {text.strip()}")
            
            print(f"  Drawings/Shapes: {len(drawings)}")
            # Print unique colors of drawings
            colors = set()
            for draw in drawings:
                fill_color = draw.get("fill")
                stroke_color = draw.get("color")
                if fill_color:
                    colors.add(f"Fill: {fill_color}")
                if stroke_color:
                    colors.add(f"Stroke: {stroke_color}")
            if colors:
                print(f"    Unique Colors in Drawings: {list(colors)[:10]}")

if __name__ == "__main__":
    main()
