import re
import requests
from urllib.parse import urlparse

def extract_urls(file_path):
    """Extract all URLs from a file, supporting both Markdown and plain text URLs."""
    url_pattern = r'https?://[^\s)]+'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return re.findall(url_pattern, content)

def check_url_status(url):
    """Check the HTTP status of a URL."""
    try:
        # Check if the URL is valid by parsing it
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc or '..' in parsed_url.netloc:
            raise ValueError(f"Invalid URL format: {url}")

        response = requests.head(url, timeout=10, allow_redirects=True)
        return response.status_code
    except (requests.RequestException, ValueError) as e:
        print(f"Skipping invalid URL: {url} - {e}")
        return None

def main():
    # Replace with the path to your Markdown or .txt file
    file_path = r"C:\root\download\readmee.txt"  # Use raw string or double backslashes for Windows paths

    # Extract URLs
    try:
        urls = extract_urls(file_path)
        print(f"Found {len(urls)} URLs in the file.")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please check the path.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # Check the status of each URL
    results = {}
    for url in urls:
        print(f"Checking: {url}")
        status = check_url_status(url)
        if status is None:
            results[url] = "Error"
        elif status == 200:
            results[url] = "OK"
        else:
            results[url] = f"HTTP {status}"

    # Print results
    print("\nLink Check Results:")
    for url, status in results.items():
        print(f"{url}: {status}")

    # Save results to a file
    try:
        with open("link_check_results.txt", "w", encoding="utf-8") as output_file:
            for url, status in results.items():
                output_file.write(f"{url}: {status}\n")
        print("\nResults saved to 'link_check_results.txt'.")
    except Exception as e:
        print(f"An error occurred while saving results: {e}")

if __name__ == "__main__":
    main()
