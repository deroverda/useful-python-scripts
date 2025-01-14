import requests as rq
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = input("Enter Link: ")  # input link by user

# Check if the URL starts with http or https
if not url.startswith("http"):
    url = "https://" + url

# Fetch the page data
data = rq.get(url)

# Parse the HTML
soup = BeautifulSoup(data.text, "html.parser")

# Initialize an empty list for the links
links = []

# Loop through all <a> tags and extract href attributes
for link in soup.find_all("a", href=True):
    href = link.get("href")
    # Join relative URLs with the base URL to create absolute URLs
    absolute_url = urljoin(url, href)
    links.append(absolute_url)

# Save all links to a file (each link on a new line) with utf-8 encoding
with open("myLinks.txt", 'w', encoding='utf-8') as saved:
    for link in links:
        saved.write(link + "\n")

print(f"All links saved to 'myLinks.txt'")
