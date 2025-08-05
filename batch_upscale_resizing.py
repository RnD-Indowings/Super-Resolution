import os
import cv2
import torch
from PIL import Image
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

# -----------------------------
# Configuration
input_dir = './input_images/data'
output_dir = './output_images_1280x720'
os.makedirs(output_dir, exist_ok=True)

# -----------------------------
# Load Real-ESRGAN x4 model
model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64,
                num_block=23, num_grow_ch=32, scale=4)

upsampler = RealESRGANer(
    scale=4,
    model_path='weights/RealESRGAN_x4plus.pth',
    model=model,
    tile=0,
    tile_pad=10,
    pre_pad=0,
    half=False  # use True if your GPU supports float16
)

# -----------------------------
# Process all images in input_dir
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_dir, filename)
        print(f'Upscaling {filename}...')

        img = cv2.imread(input_path, cv2.IMREAD_COLOR)
        if img is None:
            print(f'Skipped: {filename} (Not a valid image)')
            continue

        try:
            output, _ = upsampler.enhance(img, outscale=1)

            # Resize to 1280x720 using OpenCV
            resized = cv2.resize(output, (1280, 720), interpolation=cv2.INTER_AREA)

            output_name = os.path.splitext(filename)[0] + '_1280x720.jpg'
            output_path = os.path.join(output_dir, output_name)

            cv2.imwrite(output_path, resized)
        except Exception as e:
            print(f'❌ Failed: {filename} - {e}')

print('\n✅ Done. All images saved to:', output_dir)
