import fitz

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    page = doc[30 - 1] # page 30
    drawings = page.get_drawings()
    
    print("Page 30 drawings:")
    for idx, d in enumerate(drawings):
        fill = d.get("fill")
        rect = d.get("rect")
        if fill:
            r, g, b = fill
            if r < 0.1 and g > 0.9 and b > 0.9:
                print(f"Turquoise rect: {rect}")
                # Print text inside or near rect
                print(f"Text: '{page.get_text('text', clip=rect).strip()}'")

if __name__ == "__main__":
    main()
