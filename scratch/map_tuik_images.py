import fitz  # PyMuPDF
import os

pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\tüik.pdf"
output_dir = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\scratch\tuik_images_mapped"
os.makedirs(output_dir, exist_ok=True)

keywords = ['gül', 'pirinç', 'çeltik', 'turunçgil', 'tarım', 'hayvancılık', 'sığır', 'koyun', 'keçi', 'kümes', 'arıcılık', 'arpa', 'buğday', 'mısır', 'pamuk', 'tütün', 'şeker pancarı', 'ayçiçeği', 'zeytin', 'incir', 'üzüm', 'elma', 'fındık', 'çay', 'kenevir', 'haşhaş']

doc = fitz.open(pdf_path)
for page_index in range(len(doc)):
    page = doc.load_page(page_index)
    text = page.get_text().lower()
    
    found_keywords = [kw for kw in keywords if kw in text]
    
    if found_keywords:
        image_list = page.get_images(full=True)
        if image_list:
            print(f"Page {page_index+1} matches {found_keywords} and has {len(image_list)} images.")
            for image_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                # Sadece en büyük/ana haritayı almak için boyut kısıtlaması
                if len(image_bytes) > 50000:  # Genelde haritalar >50KB olur
                    name_prefix = "_".join(found_keywords)
                    image_name = f"{name_prefix}_p{page_index+1}_i{image_index+1}.{image_ext}"
                    with open(os.path.join(output_dir, image_name), "wb") as f:
                        f.write(image_bytes)
                    print(f"  -> Saved {image_name}")

print("Done.")
