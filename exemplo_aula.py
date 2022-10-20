from email.header import Header
import http.client
import json

conn = http.client.HTTPSConnection("ucras.di.uminho.pt")
payload = ''
headers = {}
conn.request("GET", "/v1/games", payload, headers)
res = conn.getresponse()
data = res.read()

games = json.loads(data)

away_team = games[0].get('away_team')
home_team = games[0].get('home_team')

print(f"{home_team} vs {away_team}")
