import requests
from bs4 import BeautifulSoup
import json

# Target URL
url = "https://laravel.com/"

# HTTP request
response = requests.get(url)

# Check status
print("Status code:", response.status_code)

# Parse HTML
soup = BeautifulSoup(response.content, "html.parser")

# Extract information
title = soup.title.get_text()

description_tag = soup.find("meta", attrs={"name": "description"})
description = description_tag["content"] if description_tag else "No description"

# Extract main links
links = []
for a in soup.find_all("a", href=True):
    links.append({
        "text": a.get_text(strip=True),
        "url": a["href"]
    })

# Create data structure
data = {
    "website": "Laravel",
    "url": url,
    "title": title,
    "description": description,
    "total_links": len(links),
    "links": links[:10]  # only first 10 to keep it manageable
}

# Save to JSON
with open("laravel_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Data saved to laravel_data.json")
