# if you want to run this example, you need to replace "your-api-key"
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from scrapeless import ScrapelessClient

scrapeless = ScrapelessClient(api_key="your-api-key")

def br_consopt():
  result = scrapeless.scraper(
    actor="scraper.consopt",
    input={
      "taxId": "25032537000164",
    },
    proxy={
      "country": "US",
    }
  )

  print(result)

br_consopt()
