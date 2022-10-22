import data
import models


class user:

    def __init__(self, name, email, bets, type):
        self.name = name
        self.email = email
        self.logged = True
        self.bets = bets
        self.type = type  # 0 - admin, 1 - special, 2 - normal

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getBets(self):
        return self.bets

    def getLogged(self):
        return self.logged

    def getType(self):
        return self.type

    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email

    def setLogged(self, logged):
        self.logged = logged

    def setBets(self, bets):
        self.bets = bets

    def setType(self, type):
        self.type = type

    def logout(self):
        self.setLogged(False)

    def login(self):
        self.setLogged(True)

    def addBet(self, bet):
        self.bets.append(bet)

    def removeBet(self, bet):
        self.bets.remove(bet)

    def __eq__(self, other):
        return self.name == other.name and self.email == other.email and self.logged == other.logged and self.bets == other.bets and self.type == other.type

    def __str__(self):
        return "Name: " + self.name + " Email: " + self.email + " Logged: " + str(self.logged) + " Bets: " + str(self.bets) + " Type: " + str(self.type) + "\n"
