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
    c.execute('CREATE TABLE IF NOT EXISTS Game (id INTEGER PRIMARY KEY, name varchar(100), homeTeam varchar(100), awayTeam varchar(100), commenceTime varchar(100), completed boolean, scores varchar(100), UNIQUE(name))')
    c.execute('CREATE TABLE IF NOT EXISTS Bookmark (id INTEGER PRIMARY KEY, key varchar(100), lastUpdate varchar(100), game INTEGER, FOREIGN KEY(game) REFERENCES Game(id), UNIQUE(key, game))')
    c.execute('CREATE TABLE IF NOT EXISTS Market (id INTEGER PRIMARY KEY, key varchar(100), bookmark INTEGER, FOREIGN KEY(bookmark) REFERENCES Bookmark(id), UNIQUE(key, bookmark))')
    c.execute('CREATE TABLE IF NOT EXISTS Outcome (id INTEGER PRIMARY KEY, name varchar(100), price FLOAT, state boolean, market INTEGER, FOREIGN KEY(market) REFERENCES Market(id), UNIQUE(name, market))')
    c.execute(
        'CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY, name varchar(100), email varchar(100), password varchar(100), logged boolean, type INTEGER, wallet FLOAT, UNIQUE(email))')
    c.execute('CREATE TABLE IF NOT EXISTS Bet (id INTEGER PRIMARY KEY,outcome INTEGER, user INTEGER, amountBet FLOAT, state boolean, FOREIGN KEY(user) REFERENCES User(id), FOREIGN KEY(outcome) REFERENCES Outcome(id), UNIQUE(outcome, user))')


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
                    c.execute('INSERT INTO Outcome(name, state, price, market) VALUES (?, ?, ?, ?)',
                              (outcome['name'], not(game['completed']), outcome['price'], market_id))
    db.commit()


def deleteTables():  # Delete tables
    c.execute('DROP TABLE IF EXISTS Game')
    c.execute('DROP TABLE IF EXISTS Bookmark')
    c.execute('DROP TABLE IF EXISTS Market')
    c.execute('DROP TABLE IF EXISTS Outcome')
    c.execute('DROP TABLE IF EXISTS User')
    c.execute('DROP TABLE IF EXISTS Bet')
    db.commit()


def updateTables(games):  # Update tables
    db = sqlite3.connect('database.db')  # Connect to database
    c = db.cursor()
    for game in games:
        c.execute('INSERT OR IGNORE INTO Game(name, homeTeam, awayTeam, commenceTime, completed, scores) VALUES (?, ?, ?, ?, ?, ?)',
                  (game['id'], game['homeTeam'], game['awayTeam'], game['commenceTime'], game['completed'], game['scores']))
        game_id = c.lastrowid
        for bookmark in game['bookmakers']:
            c.execute('INSERT OR IGNORE INTO Bookmark(key, lastUpdate, game) VALUES (?, ?, ?)',
                      (bookmark['key'], bookmark['lastUpdate'], game_id))
            bookmark_id = c.lastrowid
            for market in bookmark['markets']:
                c.execute('INSERT OR IGNORE INTO Market(key, bookmark) VALUES (?, ?)',
                          (market['key'], bookmark_id))
                market_id = c.lastrowid
                for outcome in market['outcomes']:
                    c.execute('INSERT OR IGNORE INTO Outcome(name, state, price, market) VALUES (?, ?, ?, ?)',
                              (outcome['name'], not(game['completed']), outcome['price'], market_id))
    db.commit()


def main():  # Main function
    games = getData()
    createTables()
    # populateTables(games)
    updateTables(games)


if __name__ == "__main__":
    main()
