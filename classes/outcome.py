import sqlite3


class Outcome:  # Outcome of a bet

    def __init__(self, name, price):  # Constructor
        self.name = ""  # Name of the outcome
        self.price = 0  # Price of the outcome

    def getName(self):  # Get name of the outcome
        return self.name

    def getPrice(self):  # Get price of the outcome
        return self.price

    def setName(self, name):  # Set name of the outcome
        self.name = name

    def setPrice(self, price):  # Set price of the outcome
        self.price = price

    def outcomeToDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO outcomes VALUES (?, ?)",
                  (self.name, self.price))
        conn.commit()
        conn.close()

    def __eq__(self, other):  # Compare two outcomes
        return self.name == other.name and self.price == other.price

    def __str__(self):  # String representation of outcome
        return self.name + " " + str(self.price)
