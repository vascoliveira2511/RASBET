from django.db import models
from .game import Game

class Bookmaker(models.Model):
    key = models.CharField(max_length=100)  # key of the bookmaker
    last_update = models.DateTimeField()  # last update of the bookmaker
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, verbose_name="the related game")  # game of the bookmaker

    def __str__(self):
        return self.key + " " + str(self.last_update) + " " + str(self.game)
