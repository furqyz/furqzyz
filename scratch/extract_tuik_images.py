import os
import fitz  # PyMuPDF
from PIL import Image
import io

pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\tüik.pdf"
output_dir = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\scratch\tuik_images"
os.makedirs(output_dir, exist_ok=True)

try:
    doc = fitz.open(pdf_path)
    img_count = 0
    for page_index in range(len(doc)):
        page = doc.load_page(page_index)
        image_list = page.get_images(full=True)
        
        for image_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_name = f"page{page_index+1}_img{image_index+1}.{image_ext}"
            
            with open(os.path.join(output_dir, image_name), "wb") as f:
                f.write(image_bytes)
            img_count += 1
            
    print(f"Extracted {img_count} images to {output_dir}")
except ImportError:
    print("PyMuPDF (fitz) is not installed. Run: pip install PyMuPDF")
except Exception as e:
    print(f"Error: {e}")
