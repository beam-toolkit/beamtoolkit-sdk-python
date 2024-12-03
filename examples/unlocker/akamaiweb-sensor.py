# if you want to run this example, you need to replace "your-api-key"
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from scrapeless import ScrapelessClient

scrapeless = ScrapelessClient(api_key="your-api-key")

def web_unlocker():
  result = scrapeless.scraper(
    actor="unlocker.akamaiweb",
    input={
      "abck": "xxxx",
      "bmsz": "xxxx",
      "url": "https://www.scrapeless.com",
      "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }
  )

  print(result)

web_unlocker()
