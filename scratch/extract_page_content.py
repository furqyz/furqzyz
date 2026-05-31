import fitz
import os

def inspect_page(doc, page_num):
    print(f"\n==================================================")
    print(f"INSPECTING PAGE {page_num}")
    print(f"==================================================")
    
    page = doc[page_num - 1]
    text = page.get_text("blocks") # Returns list of tuples: (x0, y0, x1, y1, "text", block_no, block_type)
    
    print("\n--- Text Blocks ---")
    for block in text:
        x0, y0, x1, y1, txt, block_no, block_type = block
        cleaned_txt = txt.replace("\n", " ").strip()
        if cleaned_txt:
            print(f"Block {block_no} [{x0:.1f}, {y0:.1f}, {x1:.1f}, {y1:.1f}]: {cleaned_txt}")
            
    print("\n--- Highlights & Drawings ---")
    drawings = page.get_drawings()
    for idx, draw in enumerate(drawings):
        fill = draw.get("fill")
        rect = draw.get("rect")
        if fill:
            r, g, b = fill
            color_name = "Other"
            if r < 0.1 and g > 0.9 and b > 0.9:
                color_name = "Turquoise"
            elif r > 0.9 and g < 0.1 and b < 0.1:
                color_name = "Red"
            
            if color_name in ["Turquoise", "Red"]:
                # Get the text inside or near this rect
                clip_rect = fitz.Rect(rect)
                text_under = page.get_text("text", clip=clip_rect).replace("\n", " ").strip()
                print(f"Shape {idx+1}: Color={color_name}, Rect=[{rect.x0:.1f}, {rect.y0:.1f}, {rect.x1:.1f}, {rect.y1:.1f}], Text='{text_under}'")

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    inspect_page(doc, 24)
    inspect_page(doc, 27)

if __name__ == "__main__":
    main()
