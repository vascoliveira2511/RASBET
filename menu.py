from datetime import datetime
from random import choice
from secrets import choice
import sqlite3
import string
from telnetlib import GA
from tkinter import E
from turtle import pen
from unicodedata import name
from User import User
from Bookmaker import Bookmaker
from Game import Game
from Market import Market
from Outcome import Outcome
import sys


#games = data.getData()

user = User(0, 'test', 'test', 'test', False, [], 2, 0)
game = Game(0, 'test', 'test', 'test', 'test', False, '')
bookmaker = Bookmaker(0, 'test', 'test')
market = Market(0, 'test')
outcome = Outcome(0, 'test', 0)


def checkLogin(email, password):
    """Check login"""
    global user
    user = User.DBtoUser(email, password)
    if user == None:
        print('\nInvalid credentials')
        loginMenu()
    else:
        print('\nLogged in successfully\n')
        user.login()
        user.updateDB()
        if(user.getType() == 2):
            userMenu()
        elif(user.getType() == 1):
            specialMenu()
        elif(user.getType() == 0):
            # TODO: admin menu
            specialMenu()
        else:
            print('Error')
            loginMenu()


def login():
    """Login"""
    email = input('Email: ')
    password = input('Password: ')
    checkLogin(email, password)


def register():
    """Register"""
    global user
    username = input('Username: ')
    password = input('Password: ')
    email = input('Email: ')
    type = input('Type: ')
    print('\nRegistering...')
    user = User(0, username, email, password, False, [], type, 0)
    user.userToDB()
    print('\nRegistered successfully')
    loginMenu()


def viewGamesDB():
    """View games"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Game")
    data = c.fetchall()
    for row in data:
        print("\n id = ", row[0], " -> ", row[2], " vs ", row[3])
    c.close()


def viewGameDB(id):
    """View game"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Game WHERE id = " + id)
    data = c.fetchall()
    for row in data:
        print("\n id = ", row[0], " -> ", row[2], " vs ", row[3])
    c.close()


def viewBookmakerBD(id):
    """View bookmaker"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Bookmark WHERE game = " + id)
    data = c.fetchall()
    for row in data:
        print("\n id = ", row[0], " -> ", row[1])
    c.close()


def viewMarketDB(id):
    """View market"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Market WHERE bookmark = " + id)
    data = c.fetchall()
    for row in data:
        print("\n id = ", row[0], " -> ", row[1])
    c.close()


def viewOutcomeDB(id):
    """View outcome"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Outcome WHERE market = " + id)
    data = c.fetchall()
    for row in data:
        print("\n id = ", row[0], " -> ", row[1], " -> ", row[2])
    c.close()


def viewBets(user):
    """View bets"""
    data = user.getBetsDB()
    for row in data:
        print("\n", row)


def viewBalance(user):
    """View balance"""
    print("\n", user.getWallet())


def deposit(user):
    """Deposit"""
    amount = float(input('Amount: '))
    user.deposit(amount)


def withdraw(user):
    """Withdraw"""
    amount = float(input('Amount: '))
    user.withdraw(amount)


def deleteAccount():
    """Delete account"""
    user.deleteDB()


def changePassword(user):
    """Change password"""
    password = input('Password: ')
    user.setPassword(password)


def changeEmail(user):
    """Change email"""
    email = input('Email: ')
    user.setEmail(email)


def changeUsername(user):
    """Change username"""
    username = input('Username: ')
    user.setUsername(username)


def placeBet():
    """Place bet"""
    id = input('Outcome ID: ')
    outcome.DBtoOutcome(id)
    price = outcome.getPrice()
    if user.getWallet() < price:
        print('\nNot enough money')
    else:
        user.withdraw(price)
        user.insertBetDB(id)
        user.addBet(id)
        print('\nBet placed successfully')
    bet()


def bet():
    """Bet"""
    print('\nBetting Menu\n')
    print('1 - View Games')
    print('2 - View Bookmakers for a Game')
    print('3 - View Markets for a Bookmaker')
    print('4 - View Outcomes for a Market')
    print('5 - Place a Bet')
    print('6 - Back')
    choice = input('\nChoice: ')
    if choice == '1':
        viewGamesDB()
        bet()
    elif choice == '2':
        viewBookmakerBD(input('Game ID: '))
        bet()
    elif choice == '3':
        viewMarketDB(input('Bookamer ID: '))
        bet()
    elif choice == '4':
        viewOutcomeDB(input('Market ID: '))
        bet()
    elif choice == '5':
        placeBet()
        bet()
    elif choice == '6':
        userMenu()
    else:
        print('Invalid choice')
        bet()


def loginMenu():
    """Login menu"""
    print('\nLogin Menu\n')
    print('1 - Login')
    print('2 - Register')
    print('3 - Exit')
    choice = input('\nChoice: ')
    if choice == '1':
        login()
    elif choice == '2':
        register()
    elif choice == '3':
        sys.exit()
    else:
        print('Invalid choice')
        loginMenu()


def addGame():
    """Add game"""
    name = ''.join(choice(string.ascii_uppercase + string.digits)
                   for _ in range(32))
    homeTeam = input('Home Team: ')
    awayTeam = input('Away Team: ')
    commenceTime = input('Commence Time: ')
    completed = False
    scores = ''
    game = Game(0, name, homeTeam, awayTeam,
                commenceTime, completed, scores)
    game.gameToDB()
    specialMenu()


def addBookmaker(gameId):
    """Add bookmaker"""
    name = input('Name: ')
    bookmaker = Bookmaker(0, name)
    bookmaker.bookmarkToDB(gameId)
    specialMenu()


def addMarket(bookmarkId):
    """Add market"""
    name = input('Name: ')
    market = Market(0, name)
    market.marketToDB(bookmarkId)
    specialMenu()


def addOutcome(marketId):
    """Add outcome"""
    name = input('Name: ')
    price = input('Price: ')
    outcome = Outcome(0, name, price)
    outcome.outcomeToDB(marketId)
    specialMenu()


def alterGame():
    """Alter game"""
    viewGamesDB()
    id = input('Game ID: ')
    viewGameDB(id)
    print('\n1 - Alter away team')
    print('2 - Alter home team')
    print('3 - Alter commence time')
    print('4 - Alter completed')
    print('5 - Alter scores')
    print('6 - Back')
    choice = input('\nChoice: ')
    if choice == '1':
        awayTeam = input('Away Team: ')
        game.setAwayTeam(awayTeam)
    elif choice == '2':
        homeTeam = input('Home Team: ')
        game.setHomeTeam(homeTeam)
    elif choice == '3':
        commenceTime = input('Commence Time: ')
        game.setCommenceTime(commenceTime)
    elif choice == '4':
        completed = input('Completed: ')
        game.setCompleted(completed)
    elif choice == '5':
        scores = input('Scores: ')
        game.setScores(scores)
    elif choice == '6':
        game.gameToDB()
        specialMenu()


def alterBookmaker(bookmarkId):
    """Alter bookmaker"""
    bookmaker.DBtoBookmaker(bookmarkId)
    print('\n1 - Alter name')
    print('2 - Back')
    choice = input('\nChoice: ')
    if choice == '1':
        name = input('Name: ')
        bookmaker.setName(name)
        bookmaker.setLastUpdate(datetime.now())
    elif choice == '2':
        bookmaker.updateDB()
        specialMenu()


def alterMarket(marketId):
    """Alter market"""
    market.DBtoMarket(marketId)
    print('\n1 - Alter name')
    print('2 - Back')
    choice = input('\nChoice: ')
    if choice == '1':
        name = input('Name: ')
        market.setName(name)
    elif choice == '2':
        market.updateDB()
        specialMenu()


def alterOutcome(outcomeId):
    """Alter outcome"""
    outcome.DBtoOutcome(outcomeId)
    print('\n1 - Alter name')
    print('2 - Alter price')
    print('3 - Back')
    choice = input('\nChoice: ')
    if choice == '1':
        name = input('Name: ')
        outcome.setName(name)
    elif choice == '2':
        price = input('Price: ')
        outcome.setPrice(price)
    elif choice == '3':
        outcome.updateDB()
        specialMenu()


def deleteGame(id):
    """Delete game"""
    viewGamesDB()
    game.DBtoGame(id)
    game.deleteDB()
    specialMenu()


def deleteBookmaker(id):
    """Delete bookmaker"""
    bookmaker.DBtoBookmaker(id)
    bookmaker.deleteDB()
    specialMenu()


def deleteMarket(id):
    """Delete market"""
    market.DBtoMarket(id)
    market.deleteDB()
    specialMenu()


def deleteOutcome(id):
    """Delete outcome"""
    outcome.DBtoOutcome(id)
    outcome.deleteDB()
    specialMenu()


def userMenu():
    """User menu"""
    print('\nUser Menu\n')
    print('0 - Bet')
    print('1 - View games')
    print('2 - View bets')
    print('3 - View balance')
    print('4 - Deposit')
    print('5 - Withdraw')
    print('6 - Logout')
    print('7 - Exit')
    print('\nOPTIONS\n')
    print('8 - Delete account')
    print('9 - Change password')
    print('10 - Change email')
    print('11 - Change username')
    choice = input('\nChoice: ')
    if choice == '0':
        bet()
    elif choice == '1':
        viewGamesDB()
        userMenu()
    elif choice == '2':
        viewBets(user)
        userMenu()
    elif choice == '3':
        viewBalance(user)
        userMenu()
    elif choice == '4':
        deposit(user)
        userMenu()
    elif choice == '5':
        withdraw(user)
        userMenu()
    elif choice == '6':
        user.logout()
        # TODO: Need to fix this
        user.updateDB()
        loginMenu()
    elif choice == '7':
        user.logout()
        # TODO: Need to fix this
        user.updateDB()
        sys.exit()
    elif choice == '8':
        deleteAccount(user)
        loginMenu()
    elif choice == '9':
        changePassword(user)
        userMenu()
    elif choice == '10':
        changeEmail(user)
        userMenu()
    elif choice == '11':
        changeUsername(user)
        userMenu()
    else:
        print('Invalid choice')
        userMenu()


def specialMenu():
    print('\nSpecial Menu\n')
    print('1 - View Games')
    print('2 - View Bookmakers for a Game')
    print('3 - View Markets for a Bookmaker')
    print('4 - View Outcomes for a Market')
    print('5 - Add Game')
    print('6 - Add Bookmaker to a Game')
    print('7 - Add Market to a Bookmaker')
    print('8 - Add Outcome to a Market')
    print('9 - Alter Game')
    print('10 - Alter Bookmaker for a Game')
    print('11 - Alter Market for a Bookmaker')
    print('12 - Alter Outcome for a Market')
    print('13 - Delete Game')
    print('14 - Delete Bookmaker for a Game')
    print('15 - Delete Market for a Bookmaker')
    print('16 - Delete Outcome for a Market')
    print('17 - logout')
    choice = input('\nChoice: ')
    if choice == '1':
        viewGamesDB()
        specialMenu()
    elif choice == '2':
        viewBookmakerBD(input('Game ID: '))
        specialMenu()
    elif choice == '3':
        viewMarketDB(input('Bookamer ID: '))
        specialMenu()
    elif choice == '4':
        viewOutcomeDB(input('Market ID: '))
        specialMenu()
    elif choice == '5':
        addGame()
        specialMenu()
    elif choice == '6':
        addBookmaker(input('Game ID: '))
        specialMenu()
    elif choice == '7':
        addMarket(input('Bookamer ID: '))
        specialMenu()
    elif choice == '8':
        addOutcome(input('Market ID: '))
        specialMenu()
    elif choice == '9':
        alterGame(input('Game ID: '))
        specialMenu()
    elif choice == '10':
        alterBookmaker(input('Bookamer ID: '))
        specialMenu()
    elif choice == '11':
        alterMarket(input('Market ID: '))
        specialMenu()
    elif choice == '12':
        alterOutcome(input('Outcome ID: '))
        specialMenu()
    elif choice == '13':
        deleteGame(input('Game ID: '))
        specialMenu()
    elif choice == '14':
        deleteBookmaker(input('Bookamer ID: '))
        specialMenu()
    elif choice == '15':
        deleteMarket(input('Market ID: '))
        specialMenu()
    elif choice == '16':
        deleteOutcome(input('Outcome ID: '))
        specialMenu()
    elif choice == '17':
        user.logout()
        user.updateDB()
        loginMenu()


def main():
    """Main"""
    loginMenu()


if __name__ == "__main__":
    """Main"""
    main()
