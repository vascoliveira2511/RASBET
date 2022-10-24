
class Game:  # Class for the game itself

    def __init__(self, id, homeTeam, awayTeam, commenceTime, completed, bookmakers, scores):  # Constructor
        self.id = id  # Game id
        self.homeTeam = homeTeam  # Home team
        self.awayTeam = awayTeam  # Away team
        self.commenceTime = commenceTime  # Game commence time
        self.bookmakers = bookmakers  # List of bookmakers
        self.completed = completed  # Game completed
        self.scores = scores  # Game scores

    def getId(self):  # Get game id
        return self.id

    def getHomeTeam(self):  # Get home team
        return self.homeTeam

    def getAwayTeam(self):  # Get away team
        return self.awayTeam

    def getCommenceTime(self):  # Get game commence time
        return self.commenceTime

    def getBookmakers(self):  # Get list of bookmakers
        return self.bookmakers

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

    def setBookmakers(self, bookmakers):  # Set list of bookmakers
        self.bookmakers = bookmakers

    def setCompleted(self, completed):  # Set game completed
        self.completed = completed

    def setScores(self, scores):  # Set game scores
        self.scores = scores

    def __str__(self):  # String representation of game
        return self.id + " " + self.homeTeam + " " + self.awayTeam + " " + str(self.commenceTime) + " " + str(self.bookmakers) + " " + str(self.completed) + " " + str(self.scores)

    def __eq__(self, other):  # Compare two games
        return self.id == other.id and self.homeTeam == other.homeTeam and self.awayTeam == other.awayTeam and self.commenceTime == other.commenceTime and self.bookmakers == other.bookmakers and self.completed == other.completed and self.scores == other.scores
