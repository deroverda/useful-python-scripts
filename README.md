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
--
## file_organizer

Description:

This script automatically organizes files in a specified directory by their extension type. It moves files into respective folders based on their extensions (e.g., .txt files into a "Text" folder, .jpg files into an "Images" folder, etc.).
Example:

    The script will sort all .txt files into the "Text" folder, .jpg files into the "Images" folder, .mp4 files into the "Videos" folder, and so on.
    It will create the necessary folders (if they don’t already exist) for each file type.

Just specify the directory you want to organize, and run the script!
