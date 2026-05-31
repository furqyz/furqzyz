import fitz

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\coğrafya.pdf"
    doc = fitz.open(pdf_path)
    
    pages_with_text = 0
    total_text_length = 0
    
    print("Checking text presence in coğrafya.pdf...")
    for page_num in range(min(50, len(doc))):
        text = doc[page_num].get_text().strip()
        if text:
            pages_with_text += 1
            total_text_length += len(text)
            
    print(f"\nSummary (first 50 pages):")
    print(f"  Total pages checked: {min(50, len(doc))}")
    print(f"  Pages containing selectable text: {pages_with_text}")
    print(f"  Total text characters: {total_text_length}")

if __name__ == "__main__":
    main()
