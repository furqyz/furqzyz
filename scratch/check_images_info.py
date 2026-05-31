from PIL import Image
import os

def check_sizes():
    folder = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\scratch\temp_rendered"
    for filename in ["page_25.jpg", "page_47.jpg", "page_87.jpg", "page_114.jpg", "page_115.jpg"]:
        filepath = os.path.join(folder, filename)
        if os.path.exists(filepath):
            img = Image.open(filepath)
            print(f"{filename}: width={img.width}, height={img.height}")

if __name__ == "__main__":
    check_sizes()
