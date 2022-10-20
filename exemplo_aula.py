from email.header import Header
import http.client
from itertools import count
import json

conn = http.client.HTTPConnection("ucras.di.uminho.pt")  # Conexão HTTP
payload = ''  # Payload
headers = {}  # Cabeçalhos
conn.request("GET", "/v1/games/", payload, headers)  # Pedido GET
res = conn.getresponse()  # Resposta
data = res.read()  # Dados

games = json.loads(data)  # Dados em JSON

awayTeam = games[0]['awayTeam']  # Equipa visitante
homeTeam = games[0]['homeTeam']  # Equipa da casa

print(f"{awayTeam} x {homeTeam}")  # Nome das equipas
