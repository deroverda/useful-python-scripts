import os
import shutil

def organize_files(directory):
    """Organizes files in the given directory by their extensions."""
    
    # Define the folder names for different file types
    file_types = {
        'Text': ['.txt', '.md', '.csv', '.log'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Documents': ['.pdf', '.docx', '.xlsx', '.pptx'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Archives': ['.zip', '.tar', '.rar', '.gz']
    }
    
    # Create directories if they don't exist
    for folder in file_types:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Loop through all files in the directory and organize them
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(directory, folder)
                    shutil.move(file_path, os.path.join(destination_folder, filename))
                    print(f"Moved: {filename} -> {folder}")
                    break

if __name__ == "__main__":
    # Replace with the directory you want to organize
    directory = r"C:\root\download"  # Use your own directory path
    organize_files(directory)
