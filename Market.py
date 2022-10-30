import sqlite3


class Market:  # Class for the market

    def __init__(self, id, key):  # Constructor
        self.id = id  # Market id
        self.key = key  # Market key

    def getId(self):  # Get market id
        return self.id

    def getKey(self):  # Get market key
        return self.key

    def setKey(self, key):  # Set market key
        self.key = key

    def marketToDB(self, bookmarkId):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO Market(key,bookmark) VALUES (?, ?)",
                  (self.key, bookmarkId))
        conn.commit()
        conn.close()

    def DBtoMarket(self, id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Market WHERE id=?", (id,))
        row = c.fetchone()
        self.id = row[0]
        self.key = row[1]
        conn.close()

    def updateMarketDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("UPDATE Market SET key=? WHERE id=?",
                  (self.key, self.id))
        conn.commit()
        conn.close()

    def deleteMarketDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("DELETE FROM Market WHERE id=?", (self.id,))
        conn.commit()
        conn.close()
