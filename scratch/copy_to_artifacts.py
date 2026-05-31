import shutil
import os

def main():
    src_dir = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\scratch"
    dest_dir = r"C:\Users\67ded\.gemini\antigravity\brain\0f0884f0-da21-4d63-a6fb-04db700574dd"
    
    os.makedirs(dest_dir, exist_ok=True)
    
    for p in [24, 25, 27]:
        src_path = os.path.join(src_dir, f"page_{p}.png")
        dest_path = os.path.join(dest_dir, f"page_{p}.png")
        
        if os.path.exists(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copied: {src_path} -> {dest_path}")
        else:
            print(f"Src not found: {src_path}")

if __name__ == "__main__":
    main()
