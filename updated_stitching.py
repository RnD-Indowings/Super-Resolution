import os
import shutil
import subprocess

# Input folders
frames_folders = [
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output-op1",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output-op2",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output-op3",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output-op4",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output-op5",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output-op6",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output-op7",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output-op8",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output-op9",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output-op10",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output-op11",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output-op12"
]

# Output video path
output_video = "/home/zz/Super-Resolution/Final-Parallel-5.5/all-final-stitched/FINAL-OUTPUT.mp4"

# Temporary folder to hold all frames
temp_dir = "/tmp/stitched_frames"
os.makedirs(temp_dir, exist_ok=True)

# Collect and copy/rename all frames into temp_dir
frame_index = 1
for folder in frames_folders:
    frames = sorted([f for f in os.listdir(folder) if f.endswith('.png')])
    for frame in frames:
        src = os.path.join(folder, frame)
        dst_name = f"frame_{frame_index:05d}_out.png"
        dst = os.path.join(temp_dir, dst_name)
        shutil.copyfile(src, dst)
        frame_index += 1

print(f"✅ All frames collected into {temp_dir}")

# Run ffmpeg
input_fps = "5.5"
cmd = [
    "ffmpeg",
    "-framerate", input_fps,
    "-i", os.path.join(temp_dir, "frame_%05d_out.png"),
    "-r", "5.5",
    "-c:v", "libx264", "-pix_fmt", "yuv420p",
    "-an",
    output_video
]

subprocess.run(cmd, check=True)
print(f"🎉 Final video created at: {output_video}")
