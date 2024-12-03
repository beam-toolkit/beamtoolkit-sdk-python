# if you want to run this example, you need to replace "your-api-key"
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from scrapeless import ScrapelessClient

scrapeless = ScrapelessClient(api_key="your-api-key")

def shopee_live():
  result = scrapeless.scraper(
    actor="scraper.shopee",
    input={
      "type": "shopee.live",
      "url": "https://live.shopee.co.th/api/v1/session/13285347",
    }
  )

  print(result)

shopee_live()
