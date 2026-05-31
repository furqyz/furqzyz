from PIL import Image
import os

def crop_and_save(filename, box, output_name):
    folder = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\scratch\temp_rendered"
    output_folder = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\assets\images\cografya\quiz"
    os.makedirs(output_folder, exist_ok=True)
    
    filepath = os.path.join(folder, filename)
    if os.path.exists(filepath):
        img = Image.open(filepath)
        cropped = img.crop(box)
        output_path = os.path.join(output_folder, output_name)
        cropped.save(output_path)
        print(f"Cropped and saved to {output_path}")
    else:
        print(f"File not found: {filepath}")

def main():
    # Page 25: Question 6 Map (saruhan menteşe masifi)
    # Box in 1224x1872 image
    crop_and_save("page_25.jpg", (40, 180, 580, 480), "map_q6.png")
    
    # Page 47: Question 1 Map (black sea highlighted)
    # Box in 1224x2010 image
    crop_and_save("page_47.jpg", (40, 200, 580, 520), "map_q1_47.png")
    
    # Page 87: Question 5 Map (geothermal points)
    # Box in 1224x1969 image
    crop_and_save("page_87.jpg", (630, 980, 1180, 1260), "map_q5_87.png")
    
    # Page 114: Question 5 Map (mining towns)
    # Box in 1224x1988 image
    crop_and_save("page_114.jpg", (630, 920, 1180, 1200), "map_q5_114.png")
    
    # Page 115: Question 9 Map (uranium/thorium)
    # Box in 1224x1854 image
    crop_and_save("page_115.jpg", (40, 1480, 580, 1750), "map_q9_115.png")

if __name__ == "__main__":
    main()
