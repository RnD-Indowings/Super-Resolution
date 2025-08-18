import os
import subprocess

input_video = "/home/udit/Real-ESRGAN/30mins.mp4"
output_folder = "/home/udit/Real-ESRGAN/sorted_frames"

# Make output folder
os.makedirs(output_folder, exist_ok=True)

# 50/9 ≈ 5.5556 fps → ~10,000 frames in 30 minutes
fps_fraction = "50/9"

cmd = [
    "ffmpeg",
    "-i", input_video,
    "-vf", f"fps={fps_fraction}",
    os.path.join(output_folder, "frame_%05d.png")
]

subprocess.run(cmd, check=True)
print(f"Frames extracted to '{output_folder}/'")
