from PIL import Image
import os

# Function to check if the directory exists and contains image files
def directory_existence_checker(directory):
    if os.path.isdir(directory):
        return directory
    else:
        print("[-] Provide a valid directory path containing images")
        sys.exit(1)

# Get the directory path from the user
directory_path = input("Enter the directory path containing images (please use backslash when typing in directory path): ")

# Check if the directory exists
directory_path = directory_existence_checker(directory_path)

# List all the image files in the directory
image_files = [f for f in os.listdir(directory_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

# Sort the images by filename (optional, adjust if you need a different order)
image_files.sort()

# Ensure there are images in the directory
if not image_files:
    print("[-] No image files found in the specified directory.")
    sys.exit(1)

# Create a list to hold Image objects
images = []

# Open each image and append it to the images list
for image_file in image_files:
    image_path = os.path.join(directory_path, image_file)
    try:
        with Image.open(image_path) as img:
            # Convert all images to RGB (PDFs require RGB mode)
            images.append(img.convert('RGB'))
    except Exception as e:
        print(f"[-] Error opening image {image_file}: {e}")
        continue

# Define the output PDF file path (same directory as images)
output_pdf_path = os.path.join(directory_path, "merged_images.pdf")

# Save the images as a single PDF
if images:
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
    print(f"[+] Images have been merged and saved as {output_pdf_path}")
else:
    print("[-] No valid images to convert.")
