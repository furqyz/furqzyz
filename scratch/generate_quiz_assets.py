import fitz
import os
import json

def get_column_and_y(rect, width=612):
    # Determine column: Left (0) or Right (1)
    x_mid = (rect[0] + rect[2]) / 2
    col = "left" if x_mid < width / 2 else "right"
    return col, rect[1], rect[3]

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    
    output_dir = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\assets\images\cografya\quiz"
    os.makedirs(output_dir, exist_ok=True)
    
    questions = []
    solutions = []
    
    print("Scanning and extracting quiz assets...")
    
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
                    
        page_num = page_idx + 1
        is_question_page = len(green_shapes) > 0
        
        # High resolution matrix
        zoom = 2.0
        mat = fitz.Matrix(zoom, zoom)
        
        if is_question_page:
            # Check for wrong questions (Red) or liked questions (Turquoise)
            marked_cols = set()
            for r in red_shapes:
                col, y0, y1 = get_column_and_y(r)
                marked_cols.add((col, "red"))
            for t in turquoise_shapes:
                col, y0, y1 = get_column_and_y(t)
                marked_cols.add((col, "turquoise"))
                
            if marked_cols:
                # We need a clean render of this page (without drawings)
                # To get a clean render, we can temporarily extract the background image, or we can use get_images()
                # But since get_images() extracts the raw image which might have a different aspect ratio,
                # an even easier way in PyMuPDF is to temporarily delete the drawings before rendering, 
                # or just render the page with fitz.SHOW_ANNOT=False? No, drawings are vector paths, not annotations.
                # Let's temporarily hide/delete the vector paths by cleaning page contents, render, then restore!
                # Actually, PyMuPDF allows us to clean contents.
                # Let's extract the raw image which is 100% clean and has the exact same aspect ratio!
                image_list = page.get_images()
                clean_img_path = None
                if image_list:
                    xref = image_list[0][0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    
                    # Save clean background image temporarily
                    temp_clean_path = os.path.join(output_dir, f"temp_clean_{page_num}.png")
                    with open(temp_clean_path, "wb") as f:
                        f.write(image_bytes)
                    
                    # Open with PyMuPDF to do the cropping on the clean image!
                    clean_doc = fitz.open(temp_clean_path)
                    clean_page = clean_doc[0]
                    
                    # Clean page dimensions might be different from the page view, so we scale coordinates!
                    # Scale factor: clean_page.rect.width / page.rect.width
                    scale_x = clean_page.rect.width / page.rect.width
                    scale_y = clean_page.rect.height / page.rect.height
                    
                    for col, mark_type in marked_cols:
                        # Define column rectangle in page coordinates
                        if col == "left":
                            rect = fitz.Rect(0, 50, page.rect.width / 2, page.rect.height - 20)
                        else:
                            rect = fitz.Rect(page.rect.width / 2, 50, page.rect.width, page.rect.height - 20)
                            
                        # Scale to clean image coordinates
                        scaled_rect = fitz.Rect(rect.x0 * scale_x, rect.y0 * scale_y, rect.x1 * scale_x, rect.y1 * scale_y)
                        
                        # Crop
                        pix = clean_page.get_pixmap(matrix=mat, clip=scaled_rect)
                        img_filename = f"q_{page_num}_{col}.png"
                        img_filepath = os.path.join(output_dir, img_filename)
                        pix.save(img_filepath)
                        
                        questions.append({
                            "id": f"q_{page_num}_{col}",
                            "page": page_num,
                            "column": col,
                            "type": mark_type, # "red" or "turquoise"
                            "image_path": f"assets/images/cografya/quiz/{img_filename}"
                        })
                        print(f"  Extracted clean question: {img_filename} ({mark_type})")
                        
                    clean_doc.close()
                    try:
                        os.remove(temp_clean_path)
                    except:
                        pass
        else:
            # Solutions page: We want to preserve the turquoise highlight!
            # So we render it WITH drawings!
            if turquoise_shapes:
                marked_cols = set()
                for t in turquoise_shapes:
                    col, y0, y1 = get_column_and_y(t)
                    marked_cols.add(col)
                    
                for col in marked_cols:
                    if col == "left":
                        rect = fitz.Rect(0, 30, page.rect.width / 2, page.rect.height - 20)
                    else:
                        rect = fitz.Rect(page.rect.width / 2, 30, page.rect.width, page.rect.height - 20)
                        
                    pix = page.get_pixmap(matrix=mat, clip=rect)
                    img_filename = f"s_{page_num}_{col}.png"
                    img_filepath = os.path.join(output_dir, img_filename)
                    pix.save(img_filepath)
                    
                    solutions.append({
                        "id": f"s_{page_num}_{col}",
                        "page": page_num,
                        "column": col,
                        "image_path": f"assets/images/cografya/quiz/{img_filename}"
                    })
                    print(f"  Extracted solution with highlight: {img_filename}")
                    
    # Save the database index
    db = {
        "questions": questions,
        "solutions": solutions
    }
    db_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\assets\js\quizData.js"
    with open(db_path, "w", encoding="utf-8") as f:
        f.write(f"const quizData = {json.dumps(db, indent=4)};")
    print(f"\nSaved quiz database to {db_path}")
    print(f"Total extracted questions: {len(questions)}")
    print(f"Total extracted solutions: {len(solutions)}")

if __name__ == "__main__":
    main()
