# if you want to run this example, you need to replace "your-api-key"
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from scrapeless import ScrapelessClient

scrapeless = ScrapelessClient(api_key="your-api-key")

def iberia():
  result = scrapeless.scraper(
    actor="scraper.iberia",
    input={
      "proxy": "72.46.64.6:65173:ssxiqsom:VA8ji024fz",
      "username": "00000116280546",
      "password": "i72sV7CWbDZ+7",
      "body": "{\"slices\":[{\"origin\":\"NYC\",\"destination\":\"SHA\",\"date\":\"2024-11-03\"}],\"passengers\":[{\"passengerType\":\"ADULT\",\"count\":1}],\"marketCode\":\"US\",\"preferredCabin\":\"\"}"
    },
    proxy={
      "country": "US",
    }
  )

  print(result)

iberia()
