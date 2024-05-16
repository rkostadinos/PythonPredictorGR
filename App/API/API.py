import requests
import json
# inf2021192 Κωνσταντίνος Ράπτης
# Ο σύνδεσμος του API και το token για να μπορέσουμε να χρησιμοποιήουμε τα δεδομένα του API
uri = 'https://api.football-data.org/v4/matches'
headers = { 'X-Auth-Token': 'f3512f1017274e95a9559ea0d9a2debf'}
# βάζουμε σε μεταβλητή την απάντηση του API και χρησιμοποιήται λούπα για να εξάγουμε τα δεδομένα σε μορφή json
response = requests.get(uri, headers=headers)
for match in response.json()['matches']:
  print(match)
