# Useful Python Scripts
A collection of Python scripts for various useful tasks.

## url_checker

**Description:**

This Python script extracts all URLs from a file, supporting both Markdown-style links and plain text URLs, checks their HTTP status, and generates a report with the results. The script performs the following tasks:

- **Extracts URLs:** It reads a file (either `.txt` or `.md`), using a regular expression to find all URLs. It supports URLs in both Markdown link format (e.g., `[link](http://example.com)`) and plain text URLs.
- **Checks URL Status:** It verifies the HTTP status of each URL, handling any errors or invalid URLs by skipping them and logging the issue.
- **Generates a Report:** It creates a summary of the URL statuses, marking each URL with "OK" if the HTTP status is 200, or the appropriate HTTP error code for others. Invalid URLs are marked with an "Error".
- **Saves the Results:** The script writes the results to a text file (`link_check_results.txt`) for future reference.

This script is useful for validating URLs in both Markdown and plain text files, ensuring that all links are functional and accessible.

---

## file_organizer

**Description:**

This script automatically organizes files in a specified directory by their extension type. It moves files into respective folders based on their extensions (e.g., `.txt` files into a "Text" folder, `.jpg` files into an "Images" folder, etc.).

**Example:**

The script will sort all `.txt` files into the "Text" folder, `.jpg` files into the "Images" folder, `.mp4` files into the "Videos" folder, and so on. It will create the necessary folders (if they don’t already exist) for each file type.

Just specify the directory you want to organize, and run the script!

---

## resize_images

**Description:**

This Python script resizes all image files in a specified directory to the user-defined width and height. It saves the resized images with the same name, but adds a "_resized" suffix before the file extension. The new images are saved in the same directory as the original images, leaving the original files unchanged.

---

## directory_tree

**Description:**

This Python script lists all the folders and subfolders within a given directory. It uses the `os.walk()` method to recursively traverse the directory, printing the relative path of each folder/subfolder. The user is prompted to enter the directory path, and the script checks for any errors or invalid directory paths.

---

## **duplicate_file_finder**

**Description:**

This Python script helps you find and manage duplicate files in a directory and its subdirectories by comparing file content rather than file names. It works by calculating a hash (defaulting to SHA256) for each file and then compares these hashes to identify duplicates. The script will print the paths of any duplicate files it finds, helping you clean up unnecessary copies and free up disk space.

**How the Script Works:**

- **Hash Calculation:** For each file in the specified directory, the script calculates a hash (SHA256 by default). It reads the file in chunks for efficiency, especially with large files.
- **Directory Traversal:** It recursively walks through the given directory and its subdirectories to find all files.
- **Duplicate Detection:** It compares the calculated hashes of the files. If two files have the same hash, they are considered duplicates.
- **Display Results:** The script outputs a list of duplicates, showing the original file and its duplicates.

**Example Use Case:**

If you have multiple copies of the same files, such as images or documents scattered across folders, this script will help you identify and list those duplicates so you can remove them, freeing up valuable disk space.

**Key Features:**

- **Cross-Directory Search:** The script scans a directory and its subdirectories.
- **Content-Based Comparison:** It finds duplicates by comparing file content, not just file names.
- **Efficient Hashing:** It uses hashing (SHA256 by default) to compare files without needing to load them entirely into memory.

---


## **images2pdf**

**Description:**

This Python script allows you to merge all images in a specified directory into a single PDF file. It automatically processes various image formats (like PNG, JPG, BMP, GIF), converts them to a uniform RGB format, and combines them into one PDF document. The resulting PDF is saved in the same directory as the images, making it easy to create a PDF from a batch of images.

**How the Script Works:**

- **Directory Input:** The script prompts the user to specify the directory containing the images to be merged.
- **Image File Listing:** It scans the directory for image files (PNG, JPG, JPEG, BMP, GIF) and sorts them by filename.
- **Image Conversion:** Each image is opened and converted to the RGB color mode, as required for creating PDFs.
- **PDF Creation:** The images are saved as a single PDF file in the same directory, with each image placed on a separate page.
- **Error Handling:** The script handles any errors related to opening or reading images, ensuring that the process continues smoothly even if some files cannot be processed.

**Example Use Case:**

If you have a collection of scanned images or photos that you want to compile into a single PDF document, this script will automate the process, saving you the time and effort of doing it manually. It's useful for creating digital albums, portfolios, or document compilations.

**Key Features:**

- **Batch Image Processing:** Converts and merges all images in a specified directory.
- **Flexible Image Formats:** Supports common image formats like PNG, JPG, BMP, and GIF.
- **Single PDF Output:** Generates one PDF that contains all the images, with each image on a separate page.
- **Automatic Directory Handling:** Saves the output PDF in the same directory as the images.

---

# **fetch_all_links_from_webpage**

# **Description:**

# This Python script extracts all hyperlinks (<a> tags) from a given webpage, saves them to a file, 
# and handles both absolute and relative URLs. The script performs the following tasks:

# - **Extracts Links:** It retrieves all hyperlinks (<a> tags with href attributes) from the provided webpage URL.
# - **Handles Relative URLs:** For any relative links (e.g., /about), it automatically converts them into absolute URLs based on the provided webpage URL.
# - **Saves the Links:** All the extracted links are saved to a file (myLinks.txt), with each URL written on a new line.
# - **Supports Unicode:** The script ensures that all URLs, including those with special characters (e.g., emojis or Unicode symbols), are written to the file using UTF-8 encoding to prevent encoding errors.

# This script is helpful for extracting and saving all hyperlinks from a webpage, allowing you to analyze or collect the links for further use.

---

# **wifi_password_extractor**

# **Description:**

# This Python script extracts saved Wi-Fi profiles (SSIDs) and their associated passwords from a Windows system. It performs the following tasks:

# - **Extracts Wi-Fi Profiles:** It retrieves all saved Wi-Fi profiles (SSIDs) from the system using the `netsh wlan show profiles` command.
# - **Fetches Passwords:** For each profile, the script runs the `netsh wlan show profile <profile> key=clear` command to fetch the Wi-Fi password (if available).
# - **Handles Open Networks:** If the Wi-Fi network does not have a password (i.e., it’s an open network), the script records "THE WIFI IS OPEN".
# - **Saves Results:** The script saves the SSID and corresponding password (or the message "THE WIFI IS OPEN") to a text file (`passwords.txt`).
# - **Error Handling:** It uses try/except blocks to skip any profiles that cause errors (e.g., inaccessible profiles) to prevent the script from crashing.

# This script is useful for retrieving saved Wi-Fi passwords from a Windows system, especially for auditing or managing multiple networks.



