import os
import subprocess
from PIL import Image
from multiprocessing import Pool
from tqdm import tqdm

# === CONFIGURATION ===
input_folder = "/home/nisha-/Real-ESRGAN_old/batch_images_ip"
output_folder = "/home/nisha-/Real-ESRGAN_old/batch_images_old_op"
model_name = "RealESRGAN_x4plus"  # Or x2plus
upscale = 2  # Scale factor used by ESRGAN

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# === Function to crop center region to 1280x1024 ===
def center_crop(img, target_width=1280, target_height=1024):
    width, height = img.size
    left = max((width - target_width) // 2, 0)
    top = max((height - target_height) // 2, 0)
    right = left + target_width
    bottom = top + target_height
    return img.crop((left, top, right, bottom))

# === Step 1: Run Real-ESRGAN once for the whole folder (FP32 by default) ===
print("🚀 Running Real-ESRGAN on entire folder (FP32)...")
subprocess.run([
    "python", "inference_realesrgan.py",
    "-n", model_name,
    "-i", input_folder,
    "--outscale", str(upscale),
    "--output", output_folder
])

# === Step 2: Parallel cropping function ===
def crop_file(filename):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
        path = os.path.join(output_folder, filename)
        if os.path.exists(path):
            try:
                img = Image.open(path)
                cropped = center_crop(img, 1280, 1024)
                cropped.save(path)
            except Exception as e:
                print(f"Error cropping {filename}: {e}")

# === Step 3: Run cropping in parallel with progress bar ===
print("✂️ Cropping all images to 1280x1024 in parallel...")

files = [f for f in os.listdir(output_folder) if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))]

with Pool(processes=os.cpu_count()) as pool:
    list(tqdm(pool.imap_unordered(crop_file, files), total=len(files), desc="Cropping", unit="img"))

print("✅ All done!")
