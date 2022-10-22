
class game:
    def __init__(self, id, homeTeam, awayTeam, commenceTime, completed, bookmakers, scores):
        self.id = id
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.commenceTime = commenceTime
        self.bookmakers = bookmakers
        self.completed = completed
        self.scores = scores

    def getId(self):
        return self.id

    def getHomeTeam(self):
        return self.homeTeam

    def getAwayTeam(self):
        return self.awayTeam

    def getCommenceTime(self):
        return self.commenceTime

    def getBookmakers(self):
        return self.bookmakers

    def getCompleted(self):
        return self.completed

    def getScores(self):
        return self.scores

    def setId(self, id):
        self.id = id

    def setHomeTeam(self, homeTeam):
        self.homeTeam = homeTeam

    def setAwayTeam(self, awayTeam):
        self.awayTeam = awayTeam

    def setCommenceTime(self, commenceTime):
        self.commenceTime = commenceTime

    def setBookmakers(self, bookmakers):
        self.bookmakers = bookmakers

    def setCompleted(self, completed):
        self.completed = completed

    def setScores(self, scores):
        self.scores = scores

    def __str__(self):
        return self.id + " " + self.homeTeam + " " + self.awayTeam + " " + str(self.commenceTime) + " " + str(self.bookmakers) + " " + str(self.completed) + " " + str(self.scores)

    def __eq__(self, other):
        return self.id == other.id and self.homeTeam == other.homeTeam and self.awayTeam == other.awayTeam and self.commenceTime == other.commenceTime and self.bookmakers == other.bookmakers and self.completed == other.completed and self.scores == other.scores
