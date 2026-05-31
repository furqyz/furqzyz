import shutil
import os

source_dir = r"C:\Users\67ded\.gemini\antigravity\brain\0f0884f0-da21-4d63-a6fb-04db700574dd"
dest_dir = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\assets\images\cografya"

os.makedirs(dest_dir, exist_ok=True)

# Copy the two new files uploaded in this turn:
shutil.copy(os.path.join(source_dir, "media__1780256818281.png"), os.path.join(dest_dir, "tuik_unesco_map.png"))
shutil.copy(os.path.join(source_dir, "media__1780256830706.png"), os.path.join(dest_dir, "tuik_ramsar_map.png"))
print("New maps copied successfully to assets.")
