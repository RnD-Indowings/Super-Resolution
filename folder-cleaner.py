import os

# 🔧 Replace these paths with your target folders
folders_to_clear = [
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output1",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output2",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output3",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output4",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output5",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output6",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output7",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output8",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output9",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output10",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output11",
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output12",
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
    "/home/zz/Super-Resolution/Final-Parallel-5.5/output-op12",

]

def clear_files_in_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
        print(f"✔ Folder cleared: {folder_path}\n")
    except Exception as e:
        print(f"❌ Error in '{folder_path}': {e}\n")

# 🔁 Run the cleanup on all specified folders
for folder in folders_to_clear:
    clear_files_in_folder(folder)
