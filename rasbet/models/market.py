from django.db import models
from . import Bookmaker


class Market(models.Model):
    key = models.CharField(max_length=100)  # key of the market
    bookmaker = models.ForeignKey(
        Bookmaker, on_delete=models.CASCADE, verbose_name="the related bookmaker")  # bookmaker of the market

    def __str__(self):
        return self.key + " " + str(self.Bookmark)
