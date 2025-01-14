import os

def list_folders(directory):
    """List all folders and subfolders in the given directory recursively."""
    
    try:
        # Walk through the directory and its subdirectories
        for root, dirs, _ in os.walk(directory):
            for dir_name in dirs:
                # Print the folder/subfolder relative path
                print(os.path.relpath(os.path.join(root, dir_name), directory))
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Prompt the user to enter the directory
    directory = input("Enter the directory path: ")
    
    # Check if the directory exists
    if os.path.isdir(directory):
        list_folders(directory)
    else:
        print("Error: The provided directory does not exist.")
