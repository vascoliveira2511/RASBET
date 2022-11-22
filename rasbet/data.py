import http
import json
from django.db import models
from rasbet.models.bookmaker import Bookmaker
from rasbet.models.game import Game
from rasbet.models.game import Market
from rasbet.models.game import Outcome


def getData():  # Get data from API
    conn = http.client.HTTPConnection(
        "ucras.di.uminho.pt")  # Connect to the server
    payload = ''  # Payload
    headers = {}  # Headers
    conn.request("GET", "/v1/games/", payload, headers)  # Request
    res = conn.getresponse()  # Get response
    data = res.read()  # Read response
    games = json.loads(data)  # Load data
    return games  # Return data


def updateData(games):  # Update data
    data = getData()  # Get data
    for game in data:
        game = Game(game["name"], game["home_team"], game["away_team"],
                    game["commance_time"], game["completed"], game["scores"])
        game.save()  # Save data
        for bookmaker in game["bookmakers"]:
            bookmaker = Bookmaker(
                bookmaker["key"], bookmaker["last_update"], game.id)
            bookmaker.save()
            for market in bookmaker["markets"]:
                market = Market(
                    market["key"], bookmaker.id)
                market.save()
                for outcome in market["outcomes"]:
                    outcome = Outcome(
                        outcome["name"], outcome["price"], market.id, bookmaker.id)
                    outcome.save()
