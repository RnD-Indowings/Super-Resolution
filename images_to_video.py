import cv2
import os

# Folder containing images
image_folder = "/home/nisha-/image_to_video/thermal_img_ip"
video_name = "/home/nisha-/image_to_video/thermal_img_to_video/output_video.mp4"

print(f"[INFO] Reading images from: {image_folder}")

# Get list of images and sort them
images = sorted([img for img in os.listdir(image_folder) if img.endswith(".jpg")])
print(f"[INFO] Found {len(images)} images.")

if not images:
    raise FileNotFoundError("No .jpg images found in the folder.")

# Read the first image to get dimensions
print(f"[INFO] Reading first image: {images[0]}")
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
print(f"[INFO] Image dimensions: {width}x{height}")

# Create a video writer (30 FPS)
print("[INFO] Initializing video writer...")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(video_name, fourcc, 30, (width, height))

# Write images to video
for idx, image in enumerate(images, start=1):
    img_path = os.path.join(image_folder, image)
    video.write(cv2.imread(img_path))
    print(f"[INFO] Writing frame {idx}/{len(images)}: {image}")

# Release video
video.release()
print(f"[SUCCESS] Video saved as: {video_name}")
