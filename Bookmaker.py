import sqlite3

from Market import Market


class Bookmaker:  # Class for bookmaker

    def __init__(self, id, key, lastUpdate):  # Constructor
        self.id = id  # Bookmaker id
        self.key = key  # Bookmaker key
        self.lastUpdate = lastUpdate  # Last update time

    def getKey(self):  # Get bookmaker key
        return self.key

    def getLastUpdate(self):  # Get last update time
        return self.lastUpdate

    def setKey(self, key):  # Set bookmaker key
        self.key = key

    def setLastUpdate(self, lastUpdate):  # Set last update time
        self.lastUpdate = lastUpdate

    def bookmakerToDB(self, gameId):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO Bookmark(key,lastUpdate,game) VALUES (?, ?, ?)",
                  (self.key, self.lastUpdate, gameId))
        conn.commit()
        conn.close()

    def DBtoBookmaker(id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Bookmark WHERE id=?", (id,))
        bookmaker = c.fetchone()
        conn.commit()
        conn.close()
        return Bookmaker(bookmaker[0], bookmaker[1], bookmaker[2])

    def updateBookmakerDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("UPDATE Bookmark SET key=?, lastUpdate=? WHERE id=?",
                  (self.key, self.lastUpdate, self.id))
        conn.commit()
        conn.close()

    def deleteBookmakerDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("DELETE FROM Bookmark WHERE id=?", (self.id,))
        conn.commit()
        conn.close()

    def getMarkets(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Market WHERE bookmaker = ?", (self.id,))
        markets = c.fetchall()
        list = []
        for market in markets:
            list.append(Market.DBtoMarket(str(market[0])))
        conn.close()
        return markets

    def __str__(self):
        return "Bookmaker id: " + str(self.id) + " key: " + self.key + " lastUpdate: " + str(self.lastUpdate)
