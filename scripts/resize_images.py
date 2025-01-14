from PIL import Image
import os

def resize_images(directory, target_width, target_height):
    """Resize all images in the given directory to the specified width and height."""
    
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Only process image files
        if os.path.isfile(file_path) and filename.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif')):
            try:
                with Image.open(file_path) as img:
                    # Resize the image to the target width and height
                    resized_img = img.resize((target_width, target_height))
                    
                    # Create a new filename with '_resized' added
                    base_name, ext = os.path.splitext(filename)
                    new_filename = f"{base_name}_resized{ext}"
                    new_file_path = os.path.join(directory, new_filename)
                    
                    # Save the resized image with the new filename
                    resized_img.save(new_file_path)
                    print(f"Resized: {filename} to {target_width}x{target_height} and saved as {new_filename}")
            
            except Exception as e:
                print(f"Failed to resize {filename}: {e}")

if __name__ == "__main__":
    # Prompt the user to enter the directory, target width, and target height
    directory = input("Enter the directory path where the images are stored: ")
    target_width = int(input("Enter the target width (in pixels): "))
    target_height = int(input("Enter the target height (in pixels): "))
    
    # Check if the directory exists
    if os.path.isdir(directory):
        resize_images(directory, target_width, target_height)
    else:
        print("Error: The provided directory does not exist.")
