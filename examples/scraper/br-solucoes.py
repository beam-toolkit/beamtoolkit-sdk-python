# if you want to run this example, you need to replace "your-api-key"
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from scrapeless import ScrapelessClient

scrapeless = ScrapelessClient(api_key="your-api-key")

def br_solucoes():
  result = scrapeless.scraper(
    actor="scraper.solucoes",
    input={
      "taxId": "37.335.118/0001-80",
    },
    proxy={
      "country": "US",
    }
  )

  print(result)

br_solucoes()
