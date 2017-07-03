import requests
import json

url = 'http://192.168.175.129/api/status'
method = 'GET'
response = requests.request(method, url)
print(response.content)
payload = json.loads(str(response.content))
print(payload['code'])
