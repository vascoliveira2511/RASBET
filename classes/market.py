
class bet:

    def __init__(self, key, outcomes):
        self.key = key
        self.outcomes = outcomes

    def getKey(self):
        return self.key

    def getOutcomes(self):
        return self.outcomes

    def setKey(self, key):
        self.key = key

    def setOutcomes(self, outcomes):
        self.outcomes = outcomes

    def __eq__(self, other):
        return self.key == other.key and self.outcomes == other.outcomes

    def __str__(self):
        return self.key + " " + str(self.outcomes)
