from ast import Delete
import data
import sqlite3


class User:  # Class for user

    def __init__(self, name, email, password, bets, wallet, type):  # Constructor
        self.name = name  # Name of the user
        self.email = email  # Email of the user
        self.password = password  # Password of the user
        self.logged = True  # Is the user logged in?
        self.bets = bets  # List of bets
        self.type = type  # 0 - admin, 1 - special, 2 - normal user
        self.wallet = wallet  # Wallet of the user

    def getName(self):  # Get name of the user
        return self.name

    def getEmail(self):  # Get email of the user
        return self.email

    def getWallet(self):  # Get wallet of the user
        return self.wallet

    def getBets(self):  # Get list of bets
        return self.bets

    def getLogged(self):  # Get logged status
        return self.logged

    def getType(self):  # Get type of the user
        return self.type

    def getPassword(self):  # Get password of the user
        return self.password

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

    def setWallet(self, wallet):  # Set wallet of the user
        self.wallet = wallet

    def setPassword(self, password):  # Set password of the user
        self.password = password

    def deposit(self, amount):  # Deposit money to the wallet
        self.wallet += amount

    def withdraw(self, amount):  # Withdraw money from the wallet
        self.wallet -= amount

    def logout(self):  # Logout the user
        self.setLogged(False)

    def login(self):  # Login the user
        self.setLogged(True)

    def addBet(self, bet):  # Add bet to the list of bets
        self.bets.append(bet)

    def removeBet(self, bet):  # Remove bet from the list of bets
        self.bets.remove(bet)

    def deleteAccount(self):
        del self

    def userToDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", (self.name,
                  self.email, self.password, self.bets, self.wallet, self.type))
        conn.commit()
        conn.close()

    def __eq__(self, other):  # Compare two users
        return self.name == other.name and self.email == other.email and self.logged == other.logged and self.bets == other.bets and self.type == other.type and self.wallet == other.wallet

    def __str__(self):  # String representation of user
        return "Name: " + self.name + " Email: " + self.email + " Logged: " + str(self.logged) + " Bets: " + str(self.bets) + " Type: " + str(self.type) + " Wallet: " + str(self.wallet) + "\n"
