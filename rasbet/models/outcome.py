from django.db import models
from . import Market
from . import Bookmaker

class Outcome(models.Model):
    # result of the outcome in the format name of the team or Draw
    result = models.CharField(max_length=100)
    multiplier = models.FloatField()  # multiplier of the outcome
    market = models.ForeignKey(
        Market, on_delete=models.CASCADE, verbose_name="the related market")  # the related market
    bookmaker = models.ForeignKey(
        Bookmaker, on_delete=models.CASCADE, verbose_name="the related bookmaker")  # bookmaker of the market

    def __str__(self):
        return self.result + " " + str(self.multiplier) + " " + str(self.market)
