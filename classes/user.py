import data
import models


class user:  # Class for user

    def __init__(self, name, email, bets, type):  # Constructor
        self.name = name  # Name of the user
        self.email = email  # Email of the user
        self.logged = True  # Is the user logged in?
        self.bets = bets  # List of bets
        self.type = type  # 0 - admin, 1 - special, 2 - normal user

    def getName(self):  # Get name of the user
        return self.name

    def getEmail(self):  # Get email of the user
        return self.email

    def getBets(self):  # Get list of bets
        return self.bets

    def getLogged(self):  # Get logged status
        return self.logged

    def getType(self):  # Get type of the user
        return self.type

    def setName(self, name):  # Set name of the user
        self.name = name

    def setEmail(self, email):  # Set email of the user
        self.email = email

    def setLogged(self, logged):  # Set logged status
        self.logged = logged

    def setBets(self, bets):  # Set list of bets
        self.bets = bets

    def setType(self, type):  # Set type of the user
        self.type = type

    def logout(self):  # Logout the user
        self.setLogged(False)

    def login(self):  # Login the user
        self.setLogged(True)

    def addBet(self, bet):  # Add bet to the list of bets
        self.bets.append(bet)

    def removeBet(self, bet):  # Remove bet from the list of bets
        self.bets.remove(bet)

    def __eq__(self, other):  # Compare two users
        return self.name == other.name and self.email == other.email and self.logged == other.logged and self.bets == other.bets and self.type == other.type

    def __str__(self):  # String representation of user
        return "Name: " + self.name + " Email: " + self.email + " Logged: " + str(self.logged) + " Bets: " + str(self.bets) + " Type: " + str(self.type) + "\n"
