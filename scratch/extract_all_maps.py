import fitz
import os

pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\tüik.pdf"
dest_dir = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\assets\images\cografya"
os.makedirs(dest_dir, exist_ok=True)

doc = fitz.open(pdf_path)

# Map pages to their output filenames
# Page index is 0-based.
# Format: (page_index, is_top_half, filename)
map_config = [
    # Page 2 (idx 1)
    (1, True, "findik.png"),
    (1, False, "cay.png"),
    # Page 3 (idx 2)
    (2, True, "celtik.png"),
    (2, False, "kivi.png"),
    # Page 4 (idx 3)
    (3, True, "aycicegi.png"),
    (3, False, "kanola.png"),
    # Page 5 (idx 4)
    (4, True, "uzum.png"),
    (4, False, "zeytin.png"),
    # Page 6 (idx 5)
    (5, True, "tutun.png"),
    (5, False, "hashas.png"),
    # Page 7 (idx 6)
    (6, True, "keten.png"),
    (6, False, "incir.png"),
    # Page 8 (idx 7)
    (7, True, "susam.png"),
    (7, False, "gul.png"),
    # Page 9 (idx 8)
    (8, True, "elma.png"),
    (8, False, "soya.png"),
    # Page 10 (idx 9)
    (9, True, "kayisi.png"),
    (9, False, "yerfistigi.png"),
    # Page 11 (idx 10)
    (10, True, "turuncgil.png"),
    (10, False, "muz.png"),
    # Page 12 (idx 11)
    (11, True, "avokado.png"),
    (11, False, "pamuk.png"),
    # Page 13 (idx 12)
    (12, True, "antepfistigi.png"),
    (12, False, "kirmizi_mercimek.png"),
    # Page 14 (idx 13)
    (13, True, "bugday.png"),
    (13, False, "arpa.png"),
    # Page 15 (idx 14)
    (14, True, "nohut.png"),
    (14, False, "yesil_mercimek.png"),
    # Page 16 (idx 15)
    (15, True, "seker_pancari.png"),
    (15, False, "misir.png"),
    # Page 17 (idx 16)
    (16, True, "patates.png"),
    (16, False, "kenevir.png"),
    # Page 18 (idx 17)
    (17, True, "anason.png"),
    (17, False, "aspir.png"),
    # Page 19 (idx 18)
    (18, True, "kuru_fasulye.png"),
    (18, False, "sigir_inek.png"),
    # Page 20 (idx 19)
    (19, True, "manda.png"),
    (19, False, "koyun.png"),
    # Page 21 (idx 20)
    (20, True, "kil_kecisi.png"),
    (20, False, "tiftik_kecisi.png"),
    # Page 22 (idx 21)
    (21, True, "aricilik.png"),
    (21, False, "ipek_bocegi.png"),
    # Page 23 (idx 22)
    (22, True, "kumes.png"),  # Page 23 has only 1 map
]

for page_idx, is_top, filename in map_config:
    page = doc[page_idx]
    rect = page.rect
    
    # Define crop area
    if is_top:
        # Top half
        crop_box = fitz.Rect(0, 0, rect.width, rect.height / 2)
    else:
        # Bottom half
        crop_box = fitz.Rect(0, rect.height / 2, rect.width, rect.height)
        
    # Render with high quality (zoom matrix)
    zoom = 2.0
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=crop_box)
    
    out_path = os.path.join(dest_dir, filename)
    pix.save(out_path)
    print(f"Saved {filename} ({'Top' if is_top else 'Bottom'} of page {page_idx+1})")

print("All maps extracted successfully!")
doc.close()
