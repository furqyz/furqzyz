import fitz

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    
    red_question_pages = []
    turquoise_question_pages = []
    turquoise_solution_pages = []
    
    for page_idx in range(len(doc)):
        page = doc[page_idx]
        drawings = page.get_drawings()
        
        has_green = False
        has_red = False
        has_turquoise = False
        
        for d in drawings:
            fill = d.get("fill")
            if fill:
                r, g, b = fill
                if r < 0.1 and g > 0.5 and b < 0.3:
                    has_green = True
                elif r > 0.9 and g < 0.1 and b < 0.1:
                    has_red = True
                elif r < 0.1 and g > 0.9 and b > 0.9:
                    has_turquoise = True
                    
        page_num = page_idx + 1
        
        if has_green: # Question Page
            if has_red:
                red_question_pages.append(page_num)
            if has_turquoise:
                turquoise_question_pages.append(page_num)
        else: # Solution Page
            if has_turquoise:
                turquoise_solution_pages.append(page_num)
                
    print("=== SUMMARY OF MARKED QUESTIONS ===")
    print(f"Total wrong question pages (Red): {len(red_question_pages)} pages")
    print(f"  Pages: {red_question_pages}")
    print(f"Total liked question pages (Turquoise): {len(turquoise_question_pages)} pages")
    print(f"  Pages: {turquoise_question_pages}")
    print(f"Total liked solution pages (Turquoise): {len(turquoise_solution_pages)} pages")
    print(f"  Pages: {turquoise_solution_pages}")

if __name__ == "__main__":
    main()
