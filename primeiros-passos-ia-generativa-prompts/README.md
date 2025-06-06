# Crawl4AI Example

This is a simple example of how to use Crawl4AI to crawl websites and extract information.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Configure the crawler:
   - Open `crawler_example.py`
   - Modify the `start_url` variable to your target website
   - Adjust the `schema` dictionary to match the data you want to extract
   - Configure other parameters like `max_depth`, `max_pages`, etc. as needed

## Usage

Run the crawler:
```bash
python crawler_example.py
```

The results will be saved in `crawling_results.json`.

## Features

- Configurable crawling depth and page limits
- Respects robots.txt
- Extracts structured data using XPath expressions
- Saves results in JSON format
- Error handling and logging
- Customizable user agent and request delays

## Customization

You can customize the extraction schema by modifying the `schema` dictionary in the code. The current schema extracts:
- Page titles
- Paragraphs
- Links
- Image sources

To extract different data, modify the XPath expressions in the schema.

## Notes

- Always respect website terms of service and robots.txt
- Add appropriate delays between requests to avoid overwhelming servers
- Consider using a proxy service for large-scale crawling
- Monitor your crawling activity to ensure compliance with website policies 