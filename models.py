import data
import user


def getTeams(games):
    teams = []
    for game in games:
        teams.append(game['homeTeam'])
    return teams


def getBookmakers(games, choice):
    bookmakers = []
    for bookmaker in games[choice]['bookmakers']:

        bookmakers.append(bookmaker['key'])
    return bookmakers


def getMarkets(games, choice, chave):
    markets = []
    for market in games[choice]['bookmakers'][chave]['markets']:
        markets.append(market['key'])
    return markets


def getOutcomes(games, choice, chave, mercado):
    outcomes = []

    for outcome in games[choice]['bookmakers'][chave]['markets'][mercado]['outcomes']:
        outcomes.append(outcome['name'])
    return outcomes


def getPrices(games, choice, chave, mercado):
    prices = []

    for price in games[choice]['bookmakers'][chave]['markets'][mercado]['outcomes']:
        prices.append(price['price'])
    return prices
