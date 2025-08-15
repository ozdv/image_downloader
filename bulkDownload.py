import os
import requests

# Path to your file with URLs
urls_file = "urls.txt"

# Folder to save images
os.makedirs("downloads", exist_ok=True)

# Read URLs from file
with open(urls_file, "r") as f:
    urls = [line.strip() for line in f if line.strip()]

print(f"Found {len(urls)} URLs to download.")

# Download each image
for i, url in enumerate(urls, 1):
    # Optionally replace the fit size here
    url = url.replace("fit=188x188", "fit=1000x750")

    print(f"Downloading {i}/{len(urls)}: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        filename = os.path.join("downloads", f"image_{i:03}.jpg")
        with open(filename, "wb") as f:
            f.write(response.content)
    except Exception as e:
        print(f"❌ Failed to download {url}: {e}")

print("✅ Done! Images saved in 'downloads' folder.")
