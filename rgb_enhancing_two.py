import os
import subprocess
from PIL import Image, ImageOps

# === CONFIGURATION ===
input_folder = "/home/nisha-/Real-ESRGAN/butter_ip"
output_folder = "/home/nisha-/Real-ESRGAN/butter_op"
model_name = "RealESRGAN_x4plus"  # Ensure this model is downloaded
upscale = 2  # Can be 2 or 4

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# === Resize to 1280x720 with aspect-ratio-preserving padding ===
def resize_to_1280x720(img):
    return ImageOps.pad(img, (1280, 720), method=Image.LANCZOS, color=(0, 0, 0))

# === Main Processing ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
        input_path = os.path.join(input_folder, filename)

        # Run ESRGAN CLI
        result = subprocess.run([
            "python", "inference_realesrgan.py",
            "-n", model_name,
            "-i", input_path,
            "--outscale", str(upscale),
            "--output", output_folder
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"❌ ESRGAN failed on {filename}: {result.stderr}")
            continue

        print(f"[✓] Upscaled: {filename}")

        # Determine expected output file name
        name, ext = os.path.splitext(filename)
        output_file = f"{name}_out{ext}"
        output_path = os.path.join(output_folder, output_file)

        if os.path.exists(output_path):
            try:
                img = Image.open(output_path).convert("RGB")
                resized = resize_to_1280x720(img)
                resized.save(output_path)
                print(f"[✓] Resized to 1280x720 & saved: {output_file}")
            except Exception as e:
                print(f"⚠️ Error processing {output_file}: {e}")
        else:
            print(f"❌ Output not found: {output_path}")
