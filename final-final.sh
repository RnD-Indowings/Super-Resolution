#!/bin/bash
# ==============================
# Drone Video Enhancement Script (12 unique break/batch files)
# ==============================

FOLDER="/home/zz/Super-Resolution"
RIFE_FOLDER="/home/zz/ECCV2022_RIFE"

# List of all video_break and batches scripts (12 pairs)
video_break_list=(
    "/home/zz/Super-Resolution/final_video_breaking.py"
    "/home/zz/Super-Resolution/two_final_video_breaking.py"
    "/home/zz/Super-Resolution/three_final_video_breaking.py"
    "/home/zz/Super-Resolution/four_final_video_breaking.py"
    "/home/zz/Super-Resolution/five_final_video_breaking.py"
    "/home/zz/Super-Resolution/six_final_video_breaking.py"
    "/home/zz/Super-Resolution/seven_final_video_breaking.py"
    "/home/zz/Super-Resolution/eight_final_video_breaking.py"
    "/home/zz/Super-Resolution/nine_final_video_breaking.py"
    "/home/zz/Super-Resolution/ten_final_video_breaking.py"
    "/home/zz/Super-Resolution/eleven_final_video_breaking.py"
    "/home/zz/Super-Resolution/twelve_final_video_breaking.py"
)

batches_list=(
    "/home/zz/Super-Resolution/final_batches.py"
    "/home/zz/Super-Resolution/two_final_batches.py"
    "/home/zz/Super-Resolution/three_final_batches.py"
    "/home/zz/Super-Resolution/four_final_batches.py"
    "/home/zz/Super-Resolution/five_final_batches.py"
    "/home/zz/Super-Resolution/six_final_batches.py"
    "/home/zz/Super-Resolution/seven_final_batches.py"
    "/home/zz/Super-Resolution/eight_final_batches.py"
    "/home/zz/Super-Resolution/nine_final_batches.py"
    "/home/zz/Super-Resolution/ten_final_batches.py"
    "/home/zz/Super-Resolution/eleven_final_batches.py"
    "/home/zz/Super-Resolution/twelve_final_batches.py"
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
        touch $FOLDER/done_$run_id
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
        sleep 1   # adjust as needed
    done
    #waiting for all 12 terminals done and then execute other processes(4-5)
    echo "=== Waiting for all 12 runs to finish... ==="
    while [ $(ls $FOLDER/done_* 2>/dev/null | wc -l) -lt 12]; do
        sleep 5
    done
    echo " === All 12 runs finished! ==="
}

# ==============================
# Step 4: Stitch all 12 outputs
# ==============================
run_step4() {
    cd $FOLDER || exit
    echo "=== Step 4: Stitching 12 outputs into one video ==="
    python3 /home/zz/Super-Resolution/final-video-stitching.py
}

# ==============================
# Step 5: FPS Enhancement (RIFE)
# ==============================
run_step5() {
    cd $RIFE_FOLDER || exit
    echo "=== Step 5: FPS Enhancement using RIFE ==="
    python3 inference_video.py --exp=1 --video=/home/zz/Super-Resolution/all-final-stitched/FINAL-OUTPUT.mp4
}

# ==============================
# MAIN PIPELINE
# ==============================
run_all_batches
run_step4
run_step5

echo "=== ALL DONE ==="
exec bash
