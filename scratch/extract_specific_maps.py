import fitz
import os

pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\tüik.pdf"
output_dir = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\assets\images\cografya"
os.makedirs(output_dir, exist_ok=True)

# Format: page_index (0-based) : [(image_index (0-based), 'file_name')]
target_images = {
    2: [(0, 'tuik_celtik.jpg')],
    7: [(1, 'tuik_gul.jpg')],
    10: [(0, 'tuik_turuncgiller.jpg')],
    18: [(1, 'tuik_sigir.jpg')],
    19: [(1, 'tuik_koyun.jpg')],
    20: [(0, 'tuik_kil_kecisi.jpg'), (1, 'tuik_tiftik_kecisi.jpg')],
    21: [(0, 'tuik_aricilik.jpg'), (1, 'tuik_ipek_bocegi.jpg')],
    22: [(0, 'tuik_kumes.jpg')]
}

doc = fitz.open(pdf_path)

for page_idx, images in target_images.items():
    page = doc.load_page(page_idx)
    image_list = page.get_images(full=True)
    
    # Filter only large images (maps)
    large_images = []
    for img in image_list:
        xref = img[0]
        base_image = doc.extract_image(xref)
        if len(base_image["image"]) > 30000:  # > 30KB
            large_images.append(base_image)
            
    # Now map the indices
    for img_idx, filename in images:
        if img_idx < len(large_images):
            img_data = large_images[img_idx]["image"]
            ext = large_images[img_idx]["ext"]
            final_name = filename.replace('.jpg', f'.{ext}')
            
            with open(os.path.join(output_dir, final_name), 'wb') as f:
                f.write(img_data)
            print(f"Saved {final_name}")
        else:
            print(f"Warning: Could not find image index {img_idx} on page {page_idx+1}")

print("Maps extraction completed successfully!")
