from datetime import datetime
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

def fecth_market(key):
    market = Market.objects.get(key=key)
    return market

def create_market(market):
    market = Market(key=market["key"])
    market.save()
    return market

def create_bookmaker(bookmaker, game):
    bookmaker = Bookmaker(
                key=bookmaker["key"], last_update=bookmaker["lastUpdate"], game_id=game.id)
    bookmaker.save()
    return bookmaker

def fecth_bookmaker(key, game_id):
    bookmaker = Bookmaker.objects.get(key=key, game_id=game_id)
    return bookmaker

def create_game(game):
    game = Game(name=game["id"], home_team=game["homeTeam"], away_team=game["awayTeam"],
                    commence_time=game["commenceTime"], completed=game["completed"], scores=game["scores"])
    game.save()
    return game

def fecth_game(name):
    game = Game.objects.get(name=name)
    return game

def create_outcome(outcome, market, bookmaker):
    outcome = Outcome(result=outcome["name"], multiplier=outcome["price"], market_id=market.id, bookmaker_id=bookmaker.id)
    outcome.save()
    return outcome

def fetch_outcome(result, market_id, bookmaker_id):
    outcome = Outcome.objects.get(result=result, market_id=market_id, bookmaker_id=bookmaker_id)
    return outcome

def update_outcome(outcome, multiplier):
    outcome.multiplier = multiplier
    outcome.save(update_fields=['multiplier'])
    return outcome

def update_bookmaker(bookmaker, last_update):
    bookmaker.last_update = last_update
    bookmaker.save(update_fields=['last_update'])
    return bookmaker

def convert_to_datetime(datetime_string):
    if type(datetime_string) is str:
        return datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%SZ')
    else:
        return datetime_string

def run():  # Update data
    print('Starting fetching data')
    data = get_data()  # Get data
    print('Data fetched')
    for game in data:
        new_game = fecth_game(game["id"])
        
        if not new_game:
            new_game = create_game(game)

        print('Creating game')

        for bookmaker in game["bookmakers"]:
            new_bookmaker = fecth_bookmaker(bookmaker["key"], new_game.id)

            if not new_bookmaker:
                new_bookmaker = create_bookmaker(bookmaker, new_game)

            print('Creating bookmaker')

            for market in bookmaker["markets"]:
                new_market = fecth_market(market["key"])

                if not new_market:
                    new_market = create_market(market)

                print('Creating market')

                for outcome in market["outcomes"]:
                    new_outcome = fetch_outcome(outcome["name"], new_market.id, new_bookmaker.id)

                    if not new_outcome:
                        new_outcome = create_outcome(outcome, new_market, new_bookmaker)
                    elif convert_to_datetime(bookmaker['lastUpdate']).timestamp() > convert_to_datetime(new_bookmaker.last_update).timestamp():
                        new_outcome = update_outcome(new_outcome, outcome["price"])
                        new_bookmaker = update_bookmaker(new_bookmaker, bookmaker['lastUpdate'])

                    print('Creating outcome')
