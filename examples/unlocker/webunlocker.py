# if you want to run this example, you need to replace "your-api-key"
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from scrapeless import ScrapelessClient

scrapeless = ScrapelessClient(api_key="your-api-key")

def web_unlocker():
  result = scrapeless.scraper(
    actor="unlocker.webunlocker",
    input={
      "url": "https://www.scrapeless.com",
      "proxy_country": "ANY",
      "method": "GET",
      "redirect": False,
    }
  )

  print(result)

web_unlocker()
