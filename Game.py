import sqlite3


class Game:  # Class for the game itself

    def __init__(self, id, name, homeTeam, awayTeam, commenceTime, completed, scores):  # Constructor
        self.id = id
        self.name = name  # Game name
        self.homeTeam = homeTeam  # Home team
        self.awayTeam = awayTeam  # Away team
        self.commenceTime = commenceTime  # Game commence time
        self.completed = completed  # Game completed
        self.scores = scores  # Game scores

    def getId(self):  # Get game id
        return self.id

    def getName(self):  # Get game name
        return self.name

    def getHomeTeam(self):  # Get home team
        return self.homeTeam

    def getAwayTeam(self):  # Get away team
        return self.awayTeam

    def getCommenceTime(self):  # Get game commence time
        return self.commenceTime

    def getCompleted(self):  # Get game completed
        return self.completed

    def getScores(self):  # Get game scores
        return self.scores

    def setId(self, id):  # Set game id
        self.id = id

    def setHomeTeam(self, homeTeam):  # Set home team
        self.homeTeam = homeTeam

    def setAwayTeam(self, awayTeam):  # Set away team
        self.awayTeam = awayTeam

    def setCommenceTime(self, commenceTime):  # Set game commence time
        self.commenceTime = commenceTime

    def setCompleted(self, completed):  # Set game completed
        self.completed = completed

    def setScores(self, scores):  # Set game scores
        self.scores = scores

    def gameToDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO Game VALUES (?, ?, ?, ?, ?, ?)",
                  (self.id, self.homeTeam, self.awayTeam, self.commenceTime,  self.completed, self.scores))
        conn.commit()
        conn.close()

    def DBtoGame(self, id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Game WHERE id = ?", (id,))
        game = c.fetchone()
        conn.commit()
        conn.close()
        return Game(game[0], game[1], game[2], game[3], game[4], game[5], game[6])

    def updateGameDB(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("UPDATE Game SET name=?, homeTeam=?, awayTeam=?, commenceTime=?, completed=?, scores=? WHERE id=?",
                  (self.name, self.homeTeam, self.awayTeam, self.commenceTime, self.completed, self.scores, self.id))
        conn.commit()
        conn.close()