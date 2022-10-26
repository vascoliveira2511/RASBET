import email
from secrets import choice
import sqlite3
from turtle import pen
from classes.Bookmaker import Bookmaker
from classes.Game import Game
import classes.User as User
import data
import sys
from classes import *


games = data.getData()

user = User.User(0, 'test', 'test', 'test', False, [], 0, 2)


def checkLogin(email, password):
    """Check login"""
    if User.User.DBtoUser(email, password) == None:
        print('\nInvalid credentials')
        loginMenu()
    else:
        user = User.User.DBtoUser(email, password)
        print('\nLogged in successfully\n')
        user.login()
        user.updateDB()
        userMenu()


def login():
    """Login"""
    email = input('Email: ')
    password = input('Password: ')
    checkLogin(email, password)


def register():
    """Register"""
    username = input('Username: ')
    password = input('Password: ')
    email = input('Email: ')
    type = input('Type: ')
    print('\nRegistering...')
    user = User.User(0, username, email, password, False, [], 0, type)
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
    userMenu()


def viewGameDB(id):
    """View game"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Game WHERE id = " + id)
    data = c.fetchall()
    for row in data:
        print("\n id = ", row[0], " -> ", row[2], " vs ", row[3])
    c.close()
    bet()


def viewBookmakerBD(id):
    """View bookmaker"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Bookmark WHERE game = " + id)
    data = c.fetchall()
    for row in data:
        print("\n id = ", row[0], " -> ", row[1])
    c.close()
    bet()


def viewMarketDB(id):
    """View market"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Market WHERE bookmark = " + id)
    data = c.fetchall()
    for row in data:
        print("\n id = ", row[0], " -> ", row[1])
    c.close()
    bet()


def viewOutcomeDB(id):
    """View outcome"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Outcome WHERE market = " + id)
    data = c.fetchall()
    for row in data:
        print("\n id = ", row[0], " -> ", row[1], " -> ", row[2])
    c.close()
    bet()


def viewBets(user):
    """View bets"""
    print(user.getBets())
    userMenu()


def viewBalance(user):
    """View balance"""
    print(user.getWallet())
    userMenu()


def deposit(user):
    """Deposit"""
    amount = float(input('Amount: '))
    user.deposit(amount)
    user.updateDB()
    userMenu()


def withdraw(user):
    """Withdraw"""
    amount = float(input('Amount: '))
    user.withdraw(amount)
    user.updateDB()
    userMenu()


def deleteAccount():
    """Delete account"""
    user.deleteDB()
    loginMenu()


def changePassword(user):
    """Change password"""
    password = input('Password: ')
    user.setPassword(password)
    user.updateDB()
    userMenu()


def changeEmail(user):
    """Change email"""
    email = input('Email: ')
    user.setEmail(email)
    user.updateDB()
    userMenu()


def changeUsername(user):
    """Change username"""
    username = input('Username: ')
    user.setUsername(username)
    userMenu()


def placeBet(id):
    """Place bet"""
    user.addBet(id)
    user.updateDB()
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
    elif choice == '2':
        viewBookmakerBD(input('Game ID: '))
    elif choice == '3':
        viewMarketDB(input('Bookamer ID: '))
    elif choice == '4':
        viewOutcomeDB(input('Market ID: '))
    elif choice == '5':
        placeBet(input('Outcome ID: '))
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
    elif choice == '2':
        viewBets(user)
    elif choice == '3':
        viewBalance(user)
    elif choice == '4':
        deposit(user)
    elif choice == '5':
        withdraw(user)
    elif choice == '6':
        loginMenu()
    elif choice == '7':
        sys.exit()
    elif choice == '8':
        deleteAccount(user)
    elif choice == '9':
        changePassword(user)
    elif choice == '10':
        changeEmail(user)
    elif choice == '11':
        changeUsername(user)
    else:
        print('Invalid choice')
        userMenu()


def main():
    """Main"""
    loginMenu()


if __name__ == "__main__":
    """Main"""
    main()
