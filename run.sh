#!/bin/bash
# ==============================
# Drone Video Enhancement Script
# ==============================

echo "=== Step 1: Stitching video ==="
python3 starting_video_stitch.py

echo "=== Step 2: Breaking video into frames ==="
python3 video_break.py

echo "=== Step 3: Super-resolution on frames ==="
python3 batches.py

echo "=== Step 4: Re-stitching super-res frames ==="
python3 video_stitching.py

echo "=== Step 5: FPS enhancement using RIFE ==="
cd "$ECCV2022_RIFE_main" || exit
python3 inference_video.py --exp=1 --video=/home/udit/Real-ESRGAN-Main/videos-5.5-stitched/final_stitched/output-op-stitched.mp4
echo "=== DONE ==="
