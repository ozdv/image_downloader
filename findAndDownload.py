import os
import requests
import re

# Path to your file with URLs
urls_file = "new_urls.txt"

# Folder to save images
os.makedirs("downloads", exist_ok=True)

# Read URLs from file
with open(urls_file, "r") as f:
    urls = [line.strip() for line in f if line.strip()]

print(f"Found {len(urls)} URLs to download.")

# Download each image
for i, url in enumerate(urls, 1):
    print(f"Processing {i}/{len(urls)}: {url}")
    
    try:
        # First, get the HTML page to extract the image URL
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        
        # Extract the image URL using regex
        # Look for the pattern that matches the image URL structure
        image_pattern = r'https://photo\.vaticanmedia\.va/\d+-large_default/\d+\.jpg'
        image_matches = re.findall(image_pattern, html_content)
        
        if image_matches:
            image_url = image_matches[0]
            print(f"  Found image URL: {image_url}")
            
            # Download the actual image
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            
            # Extract filename from the image URL
            image_filename = image_url.split('/')[-1]
            filename = os.path.join("downloads", image_filename)
            
            with open(filename, "wb") as f:
                f.write(image_response.content)
            print(f"  ✅ Downloaded: {image_filename}")
        else:
            print(f"  ❌ No image URL found in {url}")
            
    except Exception as e:
        print(f"❌ Failed to process {url}: {e}")

print("✅ Done! Images saved in 'downloads' folder.")
