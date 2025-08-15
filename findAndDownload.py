#!/usr/bin/env python3
"""
HTML Image Extractor and Downloader

This script parses web pages to find image URLs and downloads them automatically.
It's specifically designed for Vatican Media photo pages but can be customized for other sites.

Input: new_urls.txt - Text file with one webpage URL per line
Output: Images saved in downloads/ folder with original filenames

Usage:
    python findAndDownload.py

Requirements:
    - requests library
    - new_urls.txt file with webpage URLs

Features:
    - Extracts image URLs from HTML content using regex patterns
    - Handles Vatican Media photo URL structure
    - Comprehensive error handling and progress reporting

Author: ozdv
"""

import os
import requests
import re

# Path to your file with URLs
urls_file = "new_urls.txt"

# Name of folder to save images
folder_name = "downloads"

# Folder to save images
os.makedirs(folder_name, exist_ok=True)

# Image pattern to find the image URL
image_pattern = r'https://photo\.vaticanmedia\.va/\d+-large_default/\d+\.jpg'

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
        
        image_matches = re.findall(image_pattern, html_content)
        
        if image_matches:
            image_url = image_matches[0]
            print(f"  Found image URL: {image_url}")
            
            # Download the actual image
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            
            # Extract filename from the image URL
            image_filename = image_url.split('/')[-1]
            filename = os.path.join(folder_name, image_filename)
            
            with open(filename, "wb") as f:
                f.write(image_response.content)
            print(f"  ✅ Downloaded: {image_filename}")
        else:
            print(f"  ❌ No image URL found in {url}")
            
    except Exception as e:
        print(f"❌ Failed to process {url}: {e}")

print("✅ Done! Images saved in specified folder.")
