#!/bin/bash
# ==============================
# Drone Video Enhancement Script (12 unique break/batch files)
# ==============================

FOLDER="/home/udit/Real-ESRGAN-Main"
RIFE_FOLDER="/home/udit/ECCV2022_RIFE_main"

# List of all video_break and batches scripts (12 pairs)
video_break_list=(
    "first_video_break.py" "second_video_break.py" "third_video_break.py"
    "fourth_video_break.py" "fifth_video_break.py" "sixth_video_break.py"
    "seventh_video_break.py" "eighth_video_break.py" "ninth_video_break.py"
    "tenth_video_break.py" "eleventh_video_break.py" "twelfth_video_break.py"
)

batches_list=(
    "first_batches.py" "second_batches.py" "third_batches.py"
    "fourth_batches.py" "fifth_batches.py" "sixth_batches.py"
    "seventh_batches.py" "eighth_batches.py" "ninth_batches.py"
    "tenth_batches.py" "eleventh_batches.py" "twelfth_batches.py"
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
