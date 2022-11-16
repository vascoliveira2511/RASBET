from django.db import models
from . import User

class Bet(models.Model):

    stake = models.FloatField()  # the amount of money the user bets
    multiplier = models.FloatField()  # the multiplier of the outcome
    time = models.DateTimeField()  # the time the bet was made
    status = models.CharField(
        max_length=100, default="pending")  # pending, won or lost
    won = models.FloatField(default=0.0)  # the amount of money the user won
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="the related user")  # the user who made the bet

    def __str__(self):
        return str(self.stake) + " " + str(self.multiplier) + " " + str(self.time) + " " + self.status + " " + str(self.won) + " " + str(self.user)
