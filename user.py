import data
import models


class user:  # Classe para o utilizador

    def __init__(self, name, email, bets, type):  # Construtor
        self.name = name  # Nome do utilizador
        self.email = email  # Email
        self.logged = True  # True se o utilizador estiver logado, False caso contrário
        self.bets = bets  # lista de apostas
        self.type = type  # 0 - admin, 1 - special, 2 - normal

    def getName(self):
        return self.name  # Retorna o nome do utilizador

    def getEmail(self):
        return self.email  # Retorna o email do utilizador

    def getBets(self):
        return self.bets  # Retorna a lista de apostas

    def getLogged(self):
        return self.logged  # Retorna True se o utilizador estiver logado, False caso contrário

    def getType(self):
        return self.type  # Retorna o tipo do utilizador

    def setName(self, name):
        self.name = name  # Altera o nome do utilizador

    def setEmail(self, email):
        self.email = email  # Altera o email do utilizador

    def setLogged(self, logged):
        self.logged = logged  # Altera o estado de logado do utilizador

    def setBets(self, bets):
        self.bets = bets  # Altera a lista de apostas

    def setType(self, type):
        self.type = type  # Altera o tipo do utilizador

    def logout(self):
        # Altera o estado de logado do utilizador para False
        self.setLogged(False)

    def login(self):
        # Altera o estado de logado do utilizador para True
        self.setLogged(True)

    def addBet(self, bet):
        # Adiciona uma aposta à lista de apostas
        self.bets.append(bet)

    def removeBet(self, bet):
        # Remove uma aposta da lista de apostas
        self.bets.remove(bet)

    def __eq__(self, other):  # Compara dois utilizadores
        # Retorna True se os utilizadores forem iguais, False caso contrário
        return self.name == other.name and self.email == other.email and self.logged == other.logged and self.bets == other.bets and self.type == other.type

    def __str__(self):
        # Retorna uma string com os dados do utilizador
        return "Name: " + self.name + " Email: " + self.email + " Logged: " + str(self.logged) + " Bets: " + str(self.bets) + " Type: " + str(self.type) + "\n"
