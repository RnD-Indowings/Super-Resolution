import cv2
import os

video_path = '/home/nisha-/video_to_image/ir_videos/first.mp4'  # change this!
output_folder = 'frames-thermal'
frame_interval = 1

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("❌ Failed to open video")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(f"Video FPS: {fps}, Total frames: {total_frames}")

frame_count = 0
saved_count = 0

while True:
    success, frame = cap.read()
    if not success:
        print("🔚 Done reading video")
        break

    if frame_count % frame_interval == 0:
        filename = os.path.join(output_folder, f"frame_{saved_count:05d}.jpg")
        cv2.imwrite(filename, frame)
        saved_count += 1

    frame_count += 1

cap.release()
print(f"✅ Saved {saved_count} frames to '{output_folder}'")
