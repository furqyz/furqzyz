import fitz

pdf_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\tüik.pdf"
doc = fitz.open(pdf_path)

# Let's check page 2 dimensions
page = doc[1]  # 0-indexed, so page 2
rect = page.rect
print(f"Page 2 Dimensions: width={rect.width}, height={rect.height}")

# Render it to check resolution
pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom for high quality
print(f"Rendered Page 2 Pixmap: width={pix.width}, height={pix.height}")
pix.save("scratch/page2.png")
print("Saved page2.png to scratch")
