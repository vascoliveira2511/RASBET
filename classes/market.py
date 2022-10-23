
class market:  # Class for the market

    def __init__(self, key, outcomes):  # Constructor
        self.key = key  # Market key
        self.outcomes = outcomes  # List of outcomes

    def getKey(self):  # Get market key
        return self.key

    def getOutcomes(self):  # Get list of outcomes
        return self.outcomes

    def setKey(self, key):  # Set market key
        self.key = key

    def setOutcomes(self, outcomes):  # Set list of outcomes
        self.outcomes = outcomes

    def __eq__(self, other):  # Compare two markets
        return self.key == other.key and self.outcomes == other.outcomes

    def __str__(self):  # String representation of market
        return self.key + " " + str(self.outcomes)
