import requests, json

response = requests.get('https://status.digitalocean.com/api/v2/status.json')
print(response.json()['status']['description'])