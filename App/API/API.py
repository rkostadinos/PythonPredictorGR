import requests
import json

uri = 'https://api.football-data.org/v4/matches'
headers = { 'X-Auth-Token': 'f3512f1017274e95a9559ea0d9a2debf'}

response = requests.get(uri, headers=headers)
for match in response.json()['matches']:
  print(match)