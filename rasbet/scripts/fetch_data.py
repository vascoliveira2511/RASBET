import http
import json
from ..models import Bookmaker, Game, Market, Outcome


def get_data():  # Get data from API
    conn = http.client.HTTPConnection(
        "ucras.di.uminho.pt")  # Connect to the server
    payload = ''  # Payload
    headers = {}  # Headers
    conn.request("GET", "/v1/games/", payload, headers)  # Request
    res = conn.getresponse()  # Get response
    data = res.read()  # Read response
    games = json.loads(data)  # Load data
    return games  # Return data

def create_market(market):
    market = Market(market.key)
    market

def create_bookmaker(bookmaker, game):
    bookmaker = Bookmaker(
                bookmaker.key, bookmaker.last_update, game.id)
    bookmaker

def fecth_market(key):
    market = Market.objects.filter(key=key).first()
    market

def run():  # Update data
    print('Starting fetching data')
    data = get_data()  # Get data
    print('Data fetched')
    for game in data:
        new_game = Game(name=game["id"], home_team=game["homeTeam"], away_team=game["awayTeam"],
                    commance_time=game["commenceTime"], completed=game["completed"], scores=game["scores"])
        new_game.save()  # Save data
        print('Creating game')
        for bookmaker in game.bookmakers:
            new_bookmaker = Bookmaker(
                bookmaker["key"], bookmaker["lastUpdate"], new_game.id)
            new_bookmaker.save()
            print('Creating bookmaker')
            for market in bookmaker.markets:
                new_market = fecth_market(market["key"])
                if not new_market:
                    new_market = create_market(market)
                    new_market.save()
                print('Creating market')
                for outcome in market.outcomes:
                    new_outcome = Outcome(
                        outcome["name"], outcome["price"], new_market.id, new_bookmaker.id)
                    new_outcome.save()
                    print('Creating outcome')
