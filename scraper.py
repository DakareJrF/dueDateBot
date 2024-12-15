import requests
from datetime import datetime
import json

url = "https://msapi.top-academy.ru/api/v2/homework/operations/list?page=1&status=1&type=0&group_id=12"

payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'ru_RU, ru',
  'Accept-Encoding': 'gzip, deflate, br, zstd',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvbXNhcGkuaXRzdGVwLm9yZyIsImlhdCI6MTczNDAxNTg3MywiYXVkIjoxLCJleHAiOjE3MzQwMzc0NzMsImFwaUFwcGxpY2F0aW9uSWQiOjEsImFwaVVzZXJUeXBlSWQiOjEsInVzZXJJZCI6NjMsImlkQ2l0eSI6NDkwfQ.IqUp0hA2LEVeKb5FHrJZAsfVmydtCO2YxBHS6Gm9UIQ',
  'Origin': 'https://journal.top-academy.ru',
  'Connection': 'keep-alive',
  'Referer': 'https://journal.top-academy.ru/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'TE': 'trailers',
  'Cookie': '_csrf=ok3GAkQW1zvn1wOgYC3FkuDTJink_k2R'
}

response1 = requests.request("GET", url, headers=headers, data=payload)

def process_response(response):
  s = []
  data = json.loads(response.text)

  for i in data:
    s.append(i['name_spec'])
    s.append(i['completion_time'])
    s.append(i['theme'])

  todays = datetime.today().strftime('%Y-%m-%d')

  indices = [index for index, element in enumerate(s) if todays in element]

  result = []
  for index in indices:
    if index > 0:
      result.append(s[index - 1])
    if index < len(s) - 1:
      result.append(s[index + 1])

  combined_strings = []
  for i in range(0, len(result), 2):
    if i + 1 < len(result):
      combined_strings.append(result[i] + " - " + result[i + 1])
    else:
      combined_strings.append(result[i])

  final_output = '\n'.join(combined_strings)
  return final_output

print(process_response(response1))