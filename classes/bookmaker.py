class bookmaker:
    def __init__(self, key, lastUpdate, markets):
        self.key = key
        self.lastUpdate = lastUpdate
        self.markets = markets

    def getKey(self):
        return self.key

    def getLastUpdate(self):
        return self.lastUpdate

    def getMarkets(self):
        return self.markets

    def setKey(self, key):
        self.key = key

    def setLastUpdate(self, lastUpdate):
        self.lastUpdate = lastUpdate

    def setMarkets(self, markets):
        self.markets = markets

    def __eq__(self, other):
        return self.key == other.key and self.lastUpdate == other.lastUpdate and self.markets == other.markets

    def __str__(self):
        return self.key + " " + str(self.lastUpdate) + " " + str(self.markets)
