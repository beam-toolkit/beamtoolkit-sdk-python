import time
import requests

class ScrapelessClient:
  api_url = "https://api.scrapeless.com/api/v1"

  def __init__(self, api_key: str):
    self.api_key = api_key

  def scraper(self, actor: str, input: dict = None, webhook: str = None, proxy: dict = None):
    data = self._assemble_data(actor, input, webhook, proxy)
    return self._post("/scraper/request", data)

  def unlocker(self, actor: str, input: dict = None, proxy: dict = None):
    data = self._assemble_data(actor, input, proxy=proxy)
    return self._post("/unlocker/request", data)

  def create_captcha_task(self, actor: str, input: dict = None, webhook: str = None, proxy: dict = None):
    data = self._assemble_data(actor, input, webhook, proxy)
    return self._post("/createTask", data)

  def solver_captcha(self, actor: str, input: dict = None, webhook: str = None, proxy: dict = None, timeout: float = 30):
    try:
      start_at = time.time()
      res = self.create_captcha_task(actor, input, webhook, proxy)
      if not res.get("taskId"):
        return {
          'msg': 'create captcha task error',
          'success': False,
          'data': None,
        }

      task_id = res["taskId"]
      left_time = timeout - (time.time() - start_at)

      while left_time > 0:
        start_at = time.time()
        result = self.get_captcha_task_result(task_id)
        if result.get('success'):
          return result
        time.sleep(1)

        left_time -= (time.time() - start_at)

      return {
        'msg': 'solve captcha timeout',
        'success': False,
        'taskId': task_id
      }

    except Exception as e:
      return {
        'msg': 'solve captcha error',
        'success': False,
        'data': None,
      }

  def get_scraper_result(self, task_id: str):
    return self._get(f"/scraper/result/{task_id}")

  def get_captcha_task_result(self, taskId: str):
    return self._get(f"/getTaskResult/{taskId}")

  def _assemble_data(self, actor: str, input: dict = None, webhook: str = None, proxy: dict = None):
    data = { "actor": actor, "input": input }

    if webhook:
      data["webhook"] = webhook

    if proxy:
      data["proxy"] = proxy

    return data

  def _post(self, url: str, data: dict = None):
    headers = { "x-api-token": self.api_key }

    resp = requests.post(f"{self.api_url}{url}", headers=headers, json=data)
    status_code = resp.status_code

    if status_code == 504:
      return { "message": "Gateway Timeout", "code": 504 }

    return resp.json()

  def _get(self, url: str):
    headers = { "x-api-token": self.api_key }

    resp = requests.get(f"{self.api_url}{url}", headers=headers)
    status_code = resp.status_code

    if status_code == 504:
      return { "message": "Gateway Timeout", "code": 504 }

    return resp.json()