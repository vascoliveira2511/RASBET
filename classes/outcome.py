class outcome:

    def __init__(self, name, price):
        self.name = ""
        self.price = 0

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __str__(self):
        return self.name + " " + str(self.price)
