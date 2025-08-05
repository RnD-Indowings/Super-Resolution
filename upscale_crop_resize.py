import os
import subprocess
from PIL import Image

# === CONFIGURATION ===
input_folder = "/home/nisha-/Real-ESRGAN/ir_input"
output_folder = "/home/nisha-/Real-ESRGAN/ir_output"
model_name = "RealESRGAN_x4plus"  # Or x2plus depending on what you have
upscale = 2  # Scale factor used by ESRGAN

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# === Function to crop center region to 1280x720 ===
def center_crop(img, target_width=1280, target_height=720):
    width, height = img.size
    left = max((width - target_width) // 2, 0)
    top = max((height - target_height) // 2, 0)
    right = left + target_width
    bottom = top + target_height
    return img.crop((left, top, right, bottom))

# === Main Processing Loop ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
        input_path = os.path.join(input_folder, filename)

        # Step 1: Run Real-ESRGAN
        subprocess.run([
            "python", "inference_realesrgan.py",
            "-n", model_name,
            "-i", input_path,
            "--outscale", str(upscale),
            "--output", output_folder
        ])

        print(f"Upscaled: {filename}")

        # Step 2: Crop the _out file to 1280x720
        name, ext = os.path.splitext(filename)
        output_file = f"{name}_out{ext}"
        output_path = os.path.join(output_folder, output_file)

        if os.path.exists(output_path):
            try:
                img = Image.open(output_path)
                cropped = center_crop(img, 1280, 720)
                cropped.save(output_path)
                print(f"Cropped to 1280x720: {output_file}")
            except Exception as e:
                print(f"Error cropping {output_file}: {e}")
        else:
            print(f"❌ Output not found: {output_path}")
