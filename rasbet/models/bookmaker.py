from django.db import models
from . import Game


class Bookmaker(models.Model):
    key = models.CharField(max_length=100)  # key of the bookmark
    lastUpdate = models.DateTimeField()  # last update of the bookmark
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, verbose_name="the related game")  # game of the bookmark

    def __str__(self):
        return self.key + " " + str(self.lastUpdate) + " " + str(self.game)
