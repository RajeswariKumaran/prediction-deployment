import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.get(BASE + '/predictdiabetes/6,148,72,35,0,33.6,0.627,50')
print(response.json())