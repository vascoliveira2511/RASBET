from django.db import models
from .bet import Bet
from .outcome import Outcome

class BetOutcome(models.Model):
    bet = models.ForeignKey(
        Bet, on_delete=models.CASCADE, verbose_name="the related bet")  # the bet the outcome belongs to
    outcome = models.ForeignKey(
        Outcome, on_delete=models.CASCADE, verbose_name="the related outcome")  # the outcome the bet belongs to

    def __str__(self):
        return str(self.bet) + " " + str(self.outcome)
