import os
import subprocess

frames_folder = "/home/udit/Real-ESRGAN/four_fps"
output_video = "new_op_4fps.mp4"

# Match the FPS you used during extraction
input_fps = "4"  # ~5.555 fps

cmd = [
    "ffmpeg",
    "-framerate", input_fps,                       # Real input FPS
    "-i", os.path.join(frames_folder, "frame_%05d_out.jpg"),
    "-r", "4",                                    # Smooth 30fps output
    "-c:v", "libx264", "-pix_fmt", "yuv420p",
    "-an",
    output_video
]

subprocess.run(cmd, check=True)
print(f"✅ Video stitched (no audio, correct speed) and saved as '{output_video}'")
