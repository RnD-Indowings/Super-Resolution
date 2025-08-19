import cv2

# Input video paths
video1_path = "/home/nisha-/video_to_image/video_ir1.mp4"
video2_path = "/home/nisha-/video_to_image/video_ir2.mp4"
video2_path = "/home/nisha-/video_to_image/video_ir3.mp4"
video2_path = "/home/nisha-/video_to_image/video_ir4.mp4"
video2_path = "/home/nisha-/video_to_image/video_ir5.mp4"
video2_path = "/home/nisha-/video_to_image/video_ir6.mp4"
output_path = "/home/nisha-/video_to_image/stitched_video_six.mp4"

# Open video files
cap1 = cv2.VideoCapture(video1_path)
cap2 = cv2.VideoCapture(video2_path)

# Get video properties from first video
fps = int(cap1.get(cv2.CAP_PROP_FPS))
width = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define VideoWriter with same resolution and FPS
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Function to write frames from a video
def write_video(cap):
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

# Write first video
write_video(cap1)
# Write second video
write_video(cap2)

# Release everything
cap1.release()
cap2.release()
out.release()

print("✅ Videos stitched and saved as", output_path)
