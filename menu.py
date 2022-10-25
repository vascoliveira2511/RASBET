import email
from secrets import choice
from turtle import pen
import classes.User as User
import data
import sys
from classes import *


games = data.getData()
user = User.User('test', 'test', 'test', [], 0, 2)


def loginMenu():
    """Login menu"""
    print('\nLogin Menu')
    print('1 - Login')
    print('2 - Register')
    print('3 - Exit')
    choice = input('Choice: ')
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
    print('0 - Play')
    print('1 - View games')
    print('2 - View bets')
    print('3 - View balance')
    print('4 - Deposit')
    print('5 - Withdraw')
    print('6 - Logout')
    print('7 - Exit')
    print('8 - Delete account')
    print('9 - Change password')
    print('10 - Change email')
    print('11 - Change username')
    choice = input('Choice: ')
    if choice == '0':
        play()
    elif choice == '1':
        viewGames()
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

    def play():
        """Play"""
        exit = 0
        while(exit == 0):
            print("\nChoose a team:")
            for i, game in enumerate(games):
                print(f"{i} - {game['homeTeam']}")
            choice = int(input("Choice: "))
            print(f"\You chose {games[choice]['homeTeam']}\n")
            print(
                f"The game is {games[choice]['homeTeam']} vs {games[choice]['awayTeam']}\n")
            print(f"The game begins at {games[choice]['commenceTime']}\n")
            print("Choose a key:")
            for i in range(0, len(games[choice]['bookmakers'])):
                print(f"{i} - {games[choice]['bookmakers'][i]['key']}")
            key = int(input("key: "))
            print(f"\nYou chose {games[choice]['bookmakers'][key]['key']}\n")
            print("Choose a market:")
            for i in range(0, len(games[choice]['bookmakers'][key]['markets'])):
                print(
                    f"{i} - {games[choice]['bookmakers'][key]['markets'][i]['key']}")
            market = int(input("market: "))
            print(
                f"\nYou chose {games[choice]['bookmakers'][key]['markets'][market]['key']}\n")
            print("Choose a bet:")
            for i in range(0, len(games[choice]['bookmakers'][key]['markets'][market]['outcomes'])):
                print(
                    f"{i} - {games[choice]['bookmakers'][key]['markets'][market]['outcomes'][i]['name']} com preço de {games[choice]['bookmakers'][key]['markets'][market]['outcomes'][i]['price']}")
            bet = int(input("bet: "))
            print("\nBet registred!\n")
            User.addBet(user, games[choice]['bookmakers'][key]
                        ['markets'][market]['outcomes'][bet])
            print("Keep playing?")
            exit = int(input("0 - Yes\n1 - No\nChoose: "))
        userMenu()


def viewGames():
    """View games"""
    for game in games:
        print(game['homeTeam'], game['awayTeam'], game['commenceTime'])
    userMenu()


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
    userMenu()


def withdraw(user):
    """Withdraw"""
    amount = float(input('Amount: '))
    user.withdraw(amount)
    userMenu()


def deleteAccount():
    """Delete account"""
    user.deleteAccount()
    loginMenu()


def changePassword(user):
    """Change password"""
    password = input('Password: ')
    user.setPassword(password)
    userMenu()


def changeEmail(user):
    """Change email"""
    email = input('Email: ')
    user.setEmail(email)
    userMenu()


def changeUsername(user):
    """Change username"""
    username = input('Username: ')
    user.setUsername(username)
    userMenu()


def checkLogin(email, password):
    """Check login"""
    if User.DBtoUser(email, password) == None:
        print('Invalid credentials')
        loginMenu()
    else:
        user = User.DBtoUser(email, password)
        print('Logged in successfully')
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
    print('Registering...')
    user = User.User(username, email, password, [], 0, 2)
    user.userToDB()
    print('Registered successfully')
    userMenu()


def main():
    """Main"""
    loginMenu()


if __name__ == "__main__":
    """Main"""
    main()
