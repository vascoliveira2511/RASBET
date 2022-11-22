from django.db import models

class Game(models.Model):
    name = models.CharField(
        max_length=100, unique=True)  # name of the game used as primary key
    home_team = models.CharField(max_length=100)  # name of the home team
    away_team = models.CharField(max_length=100)  # name of the away team
    commance_time = models.DateTimeField()  # time of the game
    completed = models.BooleanField(default=False)  # is the game completed
    # scores of the game in the format "NxN" where N is a number
    scores = models.CharField(max_length=100, default=None, null=True)

    def __str__(self):
        return self.home_team + " " + self.away_team + " " + str(self.commance_time) + " " + str(self.completed) + " " + str(self.scores)
