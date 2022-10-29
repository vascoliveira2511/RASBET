from ast import Delete
import data
import sqlite3


class User:  # Class for user

    def __init__(self, id, name, email, password, logged, bets, type, wallet):  # Constructor
        self.id = id  # ID of the user
        self.name = name  # Name of the user
        self.email = email  # Email of the user
        self.password = password  # Password of the user
        self.logged = logged  # Is the user logged in?
        self.bets = bets  # List of bets
        self.type = type  # 0 - admin, 1 - special, 2 - normal user
        self.wallet = wallet  # Wallet of the user

    def getId(self):
        return self.id

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

    def userToDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO User(name, email, password, logged, type, wallet) VALUES (?, ?, ?, ?, ?, ?)", (self.name,
                  self.email, self.password, self.logged, self.type, self.wallet))
        conn.commit()
        conn.close()

    def DBtoUser(email, password):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM User WHERE email = ?", (email,))
        data = c.fetchone()
        if data is None:
            print("No user found")
            return None
        elif data[3] == password:
            # TODO: Still need to add bets
            user = User(data[0], data[1], data[2], data[3],
                        data[4], [], data[5], data[6])
            user.betsFromDB()
            return user
        elif data[3] != password:
            print("Wrong password")
            return None
        conn.commit()
        conn.close()

    def updateIDfromDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT id FROM User WHERE email = ?", (self.email,))
        data = c.fetchone()
        self.id = data[0]
        conn.commit()
        conn.close()

    def betsFromDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Bet WHERE user = ?", (self.id,))
        data = c.fetchall()
        for bet in data:
            self.bets.append(bet[1])
        conn.commit()
        conn.close()

    def insertBetDB(self, Outcomeid):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO Bet(user, outcome) VALUES (?, ?)",
                  (self.id, Outcomeid))
        conn.commit()
        conn.close()

    def updateDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("UPDATE User SET name = ?, email = ?, password = ?, logged = ?, wallet = ? WHERE id = ?",
                  (self.name, self.email, self.password, self.logged, self.wallet, self.id))
        conn.commit()
        conn.close()

    def deleteDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("DELETE FROM User WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()
