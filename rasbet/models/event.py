from django.db import models
from .game import Game
from .user import User

class Event(models.Model): 
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE)  
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=100) 
    
    def __str__(self):
        return str(self.owner) + " " + str(self.description)