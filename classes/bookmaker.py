import sqlite3


class Bookmaker:  # Class for bookmaker

    def __init__(self, key, lastUpdate, markets):  # Constructor
        self.key = key  # Bookmaker key
        self.lastUpdate = lastUpdate  # Last update time
        self.markets = markets  # List of markets

    def getKey(self):  # Get bookmaker key
        return self.key

    def getLastUpdate(self):  # Get last update time
        return self.lastUpdate

    def getMarkets(self):  # Get list of markets
        return self.markets

    def setKey(self, key):  # Set bookmaker key
        self.key = key

    def setLastUpdate(self, lastUpdate):  # Set last update time
        self.lastUpdate = lastUpdate

    def setMarkets(self, markets):  # Set list of markets
        self.markets = markets

    def bookmakerToDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO bookmakers VALUES (?, ?, ?)",
                  (self.key, self.lastUpdate, self.markets))
        conn.commit()
        conn.close()

    def __eq__(self, other):  # Compare two bookmakers
        return self.key == other.key and self.lastUpdate == other.lastUpdate and self.markets == other.markets

    def __str__(self):  # String representation of bookmaker
        return self.key + " " + str(self.lastUpdate) + " " + str(self.markets)
