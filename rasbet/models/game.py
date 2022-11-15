from django.db import models


class Game(models.Model):
    name = models.CharField(
        max_length=100, primary_key=True)  # name of the game used as primary key
    homeTeam = models.CharField(max_length=100)  # name of the home team
    awayTeam = models.CharField(max_length=100)  # name of the away team
    commanceTime = models.DateTimeField()  # time of the game
    completed = models.BooleanField(default=False)  # is the game completed
    # scores of the game in the format "NxN" where N is a number
    scores = models.CharField(max_length=100, default=None, null=True)

    def __str__(self):
        return self.homeTeam + " " + self.awayTeam + " " + str(self.commanceTime) + " " + str(self.completed) + " " + str(self.scores)
