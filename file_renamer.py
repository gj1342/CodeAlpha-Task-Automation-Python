import os

# Define the root directory path
root_directory = r"D:\SCHOOL WORKS\3RD YEAR\CAPSTONE\KOMUNIKA AI TRAINING\FSLAR - SMALL PROTOTYPE\QUESTIONS\QUESTIONS\how"

# Iterate over all items in the root directory
for folder_name in os.listdir(root_directory):
    # Construct full folder path
    folder_path = os.path.join(root_directory, folder_name)
    
    # Check if the item is a directory and matches the naming pattern "realtime_video_"
    if os.path.isdir(folder_path) and folder_name.startswith("realtime_video_"):
        # Replace "realtime_video" with "color_kp" in the folder name
        new_folder_name = folder_name.replace("realtime_video", "how_kp")
        
        # Construct new full folder path
        new_folder_path = os.path.join(root_directory, new_folder_name)
        
        # Rename the folder
        os.rename(folder_path, new_folder_path)

print("Folder renaming completed.")
