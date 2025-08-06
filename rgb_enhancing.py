import os
import subprocess
from PIL import Image

# === CONFIGURATION ===
input_folder = "/home/nisha-/Real-ESRGAN/butterfly_dataset_ip"
output_folder = "/home/nisha-/Real-ESRGAN/butterfly_dataset_op"
model_name = "RealESRGAN_x4plus"  # Ensure this model is downloaded
upscale = 2  # Can be 2 or 4

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

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
                img = Image.open(output_path).convert("RGB")  # Ensure RGB
                resized = img.resize((640, 480), Image.LANCZOS)  # Resize to 640x480
                resized.save(output_path)
                print(f"[✓] Resized to 640x480 & saved: {output_file}")
            except Exception as e:
                print(f"⚠️ Error processing {output_file}: {e}")
        else:
            print(f"❌ Output not found: {output_path}")
