from django.db import models
from .game import Game
from .user import User
from .event import Event

class GameSubscriber(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE)  
    subscriber = models.ForeignKey(
        User, on_delete=models.CASCADE)          

    def __str__(self):
        return str(self.game) + " " + str(self.subscriber)
    
    def update(self, outcome):
        print("Creating event!!!")
        event = Event(owner=self.subscriber, status='new', description=f'O jogo {self.game.home_team} - {self.game.away_team} tem novas odds!')
        event.save()