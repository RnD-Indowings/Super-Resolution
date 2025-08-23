#!/bin/bash
# ==============================
# Drone Video Enhancement Script (12 unique break/batch files)
# ==============================

FOLDER="/home/udit/Real-ESRGAN-Main"
RIFE_FOLDER="/home/udit/ECCV2022_RIFE_main"

# List of all video_break and batches scripts (12 pairs)
# ==============================
# List of all video_break and batches scripts (12 pairs with full paths)
# ==============================
video_break_list=(
    "/home/zz/Super-Resolution/first_video_break.py"
    "/home/zz/Super-Resolution/second_video_break.py"
    "/home/zz/Super-Resolution/third_video_break.py"
    "/home/zz/Super-Resolution/fourth_video_break.py"
    "/home/zz/Super-Resolution/fifth_video_break.py"
    "/home/zz/Super-Resolution/sixth_video_break.py"
    "/home/zz/Super-Resolution/seventh_video_break.py"
    "/home/zz/Super-Resolution/eighth_video_break.py"
    "/home/zz/Super-Resolution/ninth_video_break.py"
    "/home/zz/Super-Resolution/tenth_video_break.py"
    "/home/zz/Super-Resolution/eleventh_video_break.py"
    "/home/zz/Super-Resolution/twelfth_video_break.py"
)

batches_list=(
    "/home/zz/Super-Resolution/first_batches.py"
    "/home/zz/Super-Resolution/second_batches.py"
    "/home/zz/Super-Resolution/third_batches.py"
    "/home/zz/Super-Resolution/fourth_batches.py"
    "/home/zz/Super-Resolution/fifth_batches.py"
    "/home/zz/Super-Resolution/sixth_batches.py"
    "/home/zz/Super-Resolution/seventh_batches.py"
    "/home/zz/Super-Resolution/eighth_batches.py"
    "/home/zz/Super-Resolution/ninth_batches.py"
    "/home/zz/Super-Resolution/tenth_batches.py"
    "/home/zz/Super-Resolution/eleventh_batches.py"
    "/home/zz/Super-Resolution/twelfth_batches.py"
)


# ==============================
# Step 2 + 3 Function
# ==============================
run_step2_3() {
    local idx=$1
    local break_script=${video_break_list[$idx]}
    local batch_script=${batches_list[$idx]}
    local run_id=$((idx+1))

    gnome-terminal -- bash -c "
        cd $FOLDER || exit
        echo '=== Run $run_id: Step 2 (Break video) ==='
        python3 $break_script

        echo '=== Run $run_id: Step 3 (Super-resolution) ==='
        python3 $batch_script

        echo '=== Run $run_id DONE ==='
        exec bash
    "
}

# ==============================
# Batch Execution (3 at once × 4 times = 12 runs)
# ==============================
run_all_batches() {
    idx=0
    for batch in {1..4}; do
        echo "=== Starting Batch $batch (3 parallel runs) ==="
        for i in {1..3}; do
            run_step2_3 $idx
            idx=$((idx+1))
        done
        echo "=== Waiting before next batch... ==="
        sleep 15   # adjust as needed
    done
}

# ==============================
# Step 4: Stitch all 12 outputs
# ==============================
run_step4() {
    cd $FOLDER || exit
    echo "=== Step 4: Stitching 12 outputs into one video ==="
    python3 video_stitching.py --inputs output_run*
}

# ==============================
# Step 5: FPS Enhancement (RIFE)
# ==============================
run_step5() {
    cd $RIFE_FOLDER || exit
    echo "=== Step 5: FPS Enhancement using RIFE ==="
    python3 inference_video.py --exp=1 --video=$FOLDER/final_stitched/output-all-runs.mp4
}

# ==============================
# MAIN PIPELINE
# ==============================
run_all_batches
run_step4
run_step5

echo "=== ALL DONE ==="
exec bash
