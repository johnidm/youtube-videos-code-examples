"""
This is a simple example of how to use the crawl4ai library to crawl a website.

To run this example, you need to have the crawl4ai library installed.
You can install it using pip:

pip install crawl4ai

Then, you can run the example using:
"""
import asyncio
from crawl4ai import AsyncWebCrawler
import json
from typing import Dict, List

async def main(start_url):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=start_url)

        print(result.markdown)  

    # crawler = Crawler(
    #     max_depth=2,    
    #     max_pages=10,
    #     delay=1,
    #     timeout=30,
    #     user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    # )

    # schema = {
    #     "title": "//h1/text()",
    #     "paragraphs": "//p/text()",
    #     "links": "//a/@href",
    #     "images": "//img/@src"
    # }


    # try:
    #     results = crawler.crawl(
    #         start_url=start_url,
    #         schema=schema,
    #         follow_links=True,
    #         respect_robots=True
    #     )

    #     save_results(results)


# def save_results(results: List[Dict]):
#     """Save the crawling results to a JSON file."""
#     with open("crawling_results.json", "w", encoding="utf-8") as f:
#         json.dump(results, f, ensure_ascii=False, indent=2)
#     print(f"Results saved to crawling_results.json")



if __name__ == "__main__":
    start_url = "https://www.hostgator.com.br/blog/"
    asyncio.run(main(start_url)) 