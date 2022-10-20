from email.header import Header
import http.client
from itertools import count
import json


def getData():
    conn = http.client.HTTPConnection("ucras.di.uminho.pt")  # Conexão HTTP
    payload = ''  # Payload
    headers = {}  # Cabeçalhos
    conn.request("GET", "/v1/games/", payload, headers)  # Pedido GET
    res = conn.getresponse()  # Resposta
    data = res.read()  # Dados
    games = json.loads(data)  # Dados em JSON
    return games


def main():
    games = getData()


if __name__ == "__main__":
    main()
