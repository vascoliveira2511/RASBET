import data
import user


def getTeams(games):  # Função para obter as equipas
    teams = []  # Lista de equipas
    for game in games:  # Para cada jogo
        teams.append(game['homeTeam'])  # Adicionar a equipa da casa à lista
    return teams  # Devolver a lista de equipas


def getBookmakers(games, choice):  # Função para obter as casas de apostas
    bookmakers = []  # Lista de bookmakers
    for bookmaker in games[choice]['bookmakers']:  # Para cada bookmaker
        # Adicionar o nome da casa de apostas à lista
        bookmakers.append(bookmaker['key'])
    return bookmakers  # Devolver a lista de bookmakers


def getMarkets(games, choice, chave):  # Função para obter os mercados
    markets = []  # Lista de mercados
    for market in games[choice]['bookmakers'][chave]['markets']:  # Para cada mercado
        markets.append(market['key'])  # Adicionar o nome do mercado à lista
    return markets  # Devolver a lista de mercados


def getOutcomes(games, choice, chave, mercado):  # Função para obter as apostas
    outcomes = []  # Lista de apostas
    # Para cada aposta
    for outcome in games[choice]['bookmakers'][chave]['markets'][mercado]['outcomes']:
        outcomes.append(outcome['name'])  # Adicionar o nome da aposta à lista
    return outcomes  # Devolver a lista de apostas


def getPrices(games, choice, chave, mercado):  # Função para obter os preços
    prices = []  # Lista de preços
    # Para cada preço
    for price in games[choice]['bookmakers'][chave]['markets'][mercado]['outcomes']:
        prices.append(price['price'])  # Adicionar o preço à lista
    return prices  # Devolver a lista de preços
