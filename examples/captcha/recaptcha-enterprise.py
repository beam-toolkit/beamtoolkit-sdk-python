# if you want to run this example, you need to replace "your-api-key"
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from scrapeless import ScrapelessClient

scrapeless = ScrapelessClient(api_key="your-api-key")

def main():
  actor = "captcha.recaptcha.enterprise"
  input_data = {
    "version": "v3",
    "pageURL": "https://recaptcha-demo.appspot.com/",
    "siteKey": "6Le80pApAAAAANg24CMbhL_U2PASCW_JUnq5jPys",
    "pageAction": "scraping",
    "invisible": False
  }

  result = scrapeless.solver_captcha(actor, input=input_data, timeout=10)
  print(result)

main()