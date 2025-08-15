# Image Downloader

A collection of Python scripts for downloading images from various sources. This repository contains two main tools for different image downloading scenarios.

## Features

- **bulkDownload.py**: Direct image URL downloader with size customization
- **findAndDownload.py**: Web page parser that extracts and downloads images from HTML content
- Automatic folder creation and error handling
- Progress tracking and status reporting

## Requirements

- Python 3.7+
- Required packages: `requests`, `beautifulsoup4`

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ozdv/image_downloader.git
   cd image_downloader
   ```

2. **Create and activate virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

### bulkDownload.py

Downloads images directly from a list of image URLs. Useful when you have direct links to image files.

**Input:** `urls.txt` - Text file with one image URL per line

**Features:**

- Automatically resizes images (default: 1000x750)
- Sequential file naming (image_001.jpg, image_002.jpg, etc.)
- Error handling for failed downloads

**Example urls.txt:**

```
https://example.com/image1.jpg?fit=188x188
https://example.com/image2.jpg?fit=188x188
https://example.com/image3.jpg?fit=188x188
```

**Run:**

```bash
python bulkDownload.py
```

**Output:** Images saved in `downloads/` folder

### findAndDownload.py

Parses web pages to find and download images. Useful when you have page URLs and need to extract image links.

**Input:** `new_urls.txt` - Text file with one webpage URL per line

**Features:**

- Extracts image URLs from HTML content using regex patterns
- Specifically designed for Vatican Media photo URLs
- Maintains original image filenames
- Comprehensive error handling

**Example new_urls.txt:**

```
https://www.vatican.va/news_services/press/photo/2023/01/example1.html
https://www.vatican.va/news_services/press/photo/2023/01/example2.html
```

**Run:**

```bash
python findAndDownload.py
```

**Output:** Images saved in `downloads/` folder

## File Structure

```
image_downloader/
├── bulkDownload.py          # Direct image downloader
├── findAndDownload.py       # HTML parser and image extractor
├── urls.txt                 # Direct image URLs (for bulkDownload.py)
├── new_urls.txt            # Webpage URLs (for findAndDownload.py)
├── downloads/               # Output folder (created automatically)
├── .gitignore              # Git ignore file
└── README.md               # This documentation
```

## Customization

### Modifying Image Sizes (bulkDownload.py)

Edit line 25 in `bulkDownload.py`:

```python
url = url.replace("fit=188x188", "fit=1000x750")  # Change dimensions here
```

### Changing Image Pattern (findAndDownload.py)

Edit line 22 in `findAndDownload.py`:

```python
image_pattern = r'https://photo\.vaticanmedia\.va/\d+-large_default/\d+\.jpg'
```

## Error Handling

Both scripts include comprehensive error handling:

- Network connection issues
- Invalid URLs
- File write permissions
- Missing input files
- HTML parsing errors

## Output

- All images are saved in the `downloads/` folder
- Original filenames are preserved when possible
- Failed downloads are logged with error messages
- Progress is displayed for each download

## Troubleshooting

**Common Issues:**

1. **Permission denied**: Ensure write access to the current directory
2. **Module not found**: Activate virtual environment and install requirements
3. **File not found**: Check that input files (`urls.txt` or `new_urls.txt`) exist
4. **Network errors**: Verify internet connection and URL accessibility

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve these tools.

## License

This project is open source and available under the MIT License.
