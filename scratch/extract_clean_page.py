import fitz
import os

def main():
    pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\son 22 coğ.pdf"
    doc = fitz.open(pdf_path)
    
    # Let's inspect Page 24 (index 23)
    page = doc[23]
    
    # Method 1: Extract raw image
    image_list = page.get_images()
    print(f"Page 24 has {len(image_list)} images.")
    
    output_dir = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\scratch"
    os.makedirs(output_dir, exist_ok=True)
    
    if image_list:
        xref = image_list[0][0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        output_path = os.path.join(output_dir, f"clean_page_24.{image_ext}")
        with open(output_path, "wb") as f:
            f.write(image_bytes)
        print(f"Saved clean background image to: {output_path}")
        
        # Copy to artifacts directory so we can inspect it
        dest_dir = r"C:\Users\67ded\.gemini\antigravity\brain\0f0884f0-da21-4d63-a6fb-04db700574dd"
        dest_path = os.path.join(dest_dir, f"clean_page_24.{image_ext}")
        shutil_path = os.path.join(output_dir, f"clean_page_24.{image_ext}")
        
        import shutil
        shutil.copy(shutil_path, dest_path)
        print(f"Copied clean image to artifacts: {dest_path}")

if __name__ == "__main__":
    main()
