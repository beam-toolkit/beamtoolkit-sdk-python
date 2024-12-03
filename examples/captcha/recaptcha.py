# you can run this example by executing `python examples/captcha/captcha.py` in the terminal
# if you want to run this example, you need to replace "your-api-key"
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import time
from scrapeless import ScrapelessClient

scrapeless = ScrapelessClient(api_key="your-api-key")

def solve_captcha():
  actor = "captcha.recaptcha"
  input_data = {
    "version": "v2",
    "pageURL": "https://www.google.com",
    "siteKey": "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
    "pageAction": ""
  }

  result = scrapeless.captcha(actor, input=input_data)
  return result

def get_captcha_result(taskId):
  result = scrapeless.get_captcha_result(taskId)
  return result

def main():
  captcha_result = solve_captcha()
  taskId = captcha_result["taskId"]

  while True:
    captcha_result = get_captcha_result(taskId)
    if captcha_result["success"] == True:
      print(captcha_result)
      break
    time.sleep(5)

main()