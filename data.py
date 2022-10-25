from email.header import Header
import http.client
from itertools import count
import json
import sqlite3


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


db = sqlite3.connect('database.db')  # Connect to database
c = db.cursor()


def createTables():  # Create tables
    c.execute('CREATE TABLE IF NOT EXISTS Game (id INTEGER PRIMARY KEY, name TEXT, homeTeam TEXT, awayTeam TEXT, commenceTime TEXT, completed boolean, scores TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS Bookmark (id INTEGER PRIMARY KEY, key TEXT, lastUpdate TEXT, game INTEGER, FOREIGN KEY(game) REFERENCES Game(id))')
    c.execute('CREATE TABLE IF NOT EXISTS Market (id INTEGER PRIMARY KEY, key TEXT, bookmark INTEGER, FOREIGN KEY(bookmark) REFERENCES Bookmark(id))')
    c.execute('CREATE TABLE IF NOT EXISTS Outcome (id INTEGER PRIMARY KEY, name TEXT, price FLOAT, market INTEGER, FOREIGN KEY(market) REFERENCES Market(id))')
    c.execute(
        'CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, logged boolean, type INTEGER, wallet FLOAT)')
    c.execute('CREATE TABLE IF NOT EXISTS Bet (id INTEGER PRIMARY KEY,outcome INTEGER, user INTEGER, FOREIGN KEY(user) REFERENCES User(id), FOREIGN KEY(outcome) REFERENCES Outcome(id))')


def populateTables(games):  # Populate tables
    for game in games:
        c.execute('INSERT INTO Game(name, homeTeam, awayTeam, commenceTime, completed, scores) VALUES (?, ?, ?, ?, ?, ?)',
                  (game['id'], game['homeTeam'], game['awayTeam'], game['commenceTime'], game['completed'], game['scores']))
        game_id = c.lastrowid
        for bookmark in game['bookmakers']:
            c.execute('INSERT INTO Bookmark(key, lastUpdate, game) VALUES (?, ?, ?)',
                      (bookmark['key'], bookmark['lastUpdate'], game_id))
            bookmark_id = c.lastrowid
            for market in bookmark['markets']:
                c.execute('INSERT INTO Market(key, bookmark) VALUES (?, ?)',
                          (market['key'], bookmark_id))
                market_id = c.lastrowid
                for outcome in market['outcomes']:
                    c.execute('INSERT INTO Outcome(name, price, market) VALUES (?, ?, ?)',
                              (outcome['name'], outcome['price'], market_id))
    db.commit()


def main():  # Main function
    games = getData()
    createTables()
    populateTables(games)


if __name__ == "__main__":
    main()
