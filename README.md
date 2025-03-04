# Folder Renaming Script

This Python script renames folders within a specified root directory. It specifically targets folders that start with "realtime_video_" and renames them to "how_kp_".

## Description

The script iterates through all items in the provided `root_directory`. For each item, it checks if it is a directory and if its name starts with "realtime_video_". If both conditions are met, the script renames the folder by replacing "realtime_video" with "how_kp".

## Prerequisites

-   Python 3.x
-   The `os` module (included in standard Python library)

## Usage

1.  **Set the Root Directory:**
    -   Modify the `root_directory` variable in the script to the path of the directory containing the folders you want to rename.
    -   Ensure the path is a raw string (prefixed with `r`) to avoid issues with backslashes.

    ```python
    root_directory = r"D:\SCHOOL WORKS\3RD YEAR\CAPSTONE\KOMUNIKA AI TRAINING\FSLAR - SMALL PROTOTYPE\QUESTIONS\QUESTIONS\how"
    ```

2.  **Run the Script:**
    -   Save the script as a `.py` file (e.g., `rename_folders.py`).
    -   Open your terminal or command prompt.
    -   Navigate to the directory where you saved the script.
    -   Run the script using Python:

        ```bash
        python rename_folders.py
        ```

3.  **Verify the Changes:**
    -   After the script completes, verify that the folders have been renamed correctly in the specified root directory.

## Code Explanation

```python
import os

# Define the root directory path
root_directory = r"D:\SCHOOL WORKS\3RD YEAR\CAPSTONE\KOMUNIKA AI TRAINING\FSLAR - SMALL PROTOTYPE\QUESTIONS\QUESTIONS\how"

# Iterate over all items in the root directory
for folder_name in os.listdir(root_directory):
    # Construct full folder path
    folder_path = os.path.join(root_directory, folder_name)

    # Check if the item is a directory and matches the naming pattern "realtime_video_"
    if os.path.isdir(folder_path) and folder_name.startswith("realtime_video_"):
        # Replace "realtime_video" with "how_kp" in the folder name
        new_folder_name = folder_name.replace("realtime_video", "how_kp")

        # Construct new full folder path
        new_folder_path = os.path.join(root_directory, new_folder_name)

        # Rename the folder
        os.rename(folder_path, new_folder_path)

print("Folder renaming completed.")
