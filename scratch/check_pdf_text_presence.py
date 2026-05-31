import fitz

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    
    pages_with_text = 0
    total_text_length = 0
    
    print("Checking text presence in son 22 coğ.pdf...")
    for page_num in range(len(doc)):
        text = doc[page_num].get_text().strip()
        if text:
            pages_with_text += 1
            total_text_length += len(text)
            if pages_with_text <= 5:
                print(f"Page {page_num+1} has text (length {len(text)}):")
                print(text[:150] + "...")
                
    print(f"\nSummary:")
    print(f"  Total pages: {len(doc)}")
    print(f"  Pages containing selectable text: {pages_with_text}")
    print(f"  Total text characters: {total_text_length}")

if __name__ == "__main__":
    main()
