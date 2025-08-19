#!/bin/bash
# ==============================
# Drone Video Enhancement Script
# ==============================

# ---- CONFIG ----
FOLDER1="/home/udit/Real-ESRGAN-Main"
FOLDER2="/home/udit/Real-ESRGAN-Main"

# ---- PIPELINE FULL (Step 2 → 5) ----
pipeline_full="

echo '=== Step 2: Breaking video into frames ==='
python3 video_break.py

echo '=== Step 3: Super-resolution on frames ==='
python3 batches.py

echo '=== Step 4: Re-stitching super-res frames ==='
python3 video_stitching.py

echo '=== Step 5: FPS enhancement using RIFE ==='
cd ../ECCV2022_RIFE_main || exit
python3 inference_video.py --exp=1 --video=/home/udit/Real-ESRGAN-Main/parallel_5.5/final_stitched1/output-op-stitched.mp4

echo '=== DONE (FULL) ==='
exec bash
"

# ---- PIPELINE SHORT (Step 2 → 5 only) ----
pipeline_short="

echo '=== Step 2: Breaking video into frames ==='
python3 two_video_break.py

echo '=== Step 3: Super-resolution on frames ==='
python3 two_batches.py

echo '=== Step 4: Re-stitching super-res frames ==='
python3 two_video_stitching.py

echo '=== Step 5: FPS enhancement using RIFE ==='
cd ../ECCV2022_RIFE_main || exit
python3 inference_video.py --exp=1 --video=/home/udit/Real-ESRGAN-Main/parallel_5.5/final_stitched2/output-op-stitched.mp4

echo '=== DONE (SHORT) ==='
exec bash
"

# ---- EXECUTION ----
gnome-terminal -- bash -c "cd $FOLDER1 && $pipeline_full"
gnome-terminal -- bash -c "cd $FOLDER2 && $pipeline_short"
