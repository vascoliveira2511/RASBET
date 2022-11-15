from django.db import models
from . import Bet
from . import Outcome


class BetOutcome(models.Model):
    status = models.CharField(
        max_length=100, default="pending")  # pending, won or lost
    bet = models.ForeignKey(
        Bet, on_delete=models.CASCADE, verbose_name="the related bet")  # the bet the outcome belongs to
    outcome = models.ForeignKey(
        Outcome, on_delete=models.CASCADE, verbose_name="the related outcome")  # the outcome the bet belongs to

    def __str__(self):
        return self.status + " " + str(self.bet) + " " + str(self.outcome)
