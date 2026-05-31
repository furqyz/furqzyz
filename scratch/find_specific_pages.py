import fitz

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    
    # We want to search for page containing solution to Question 10 of page 72
    # The question text contains "nüfus projeksiyonu"
    for page_idx in range(len(doc)):
        text = doc[page_idx].get_text()
        if "projeksiyon" in text or "projeksiyonu" in text:
            print(f"Found 'projeksiyon' on page {page_idx + 1}")
            
if __name__ == "__main__":
    main()
