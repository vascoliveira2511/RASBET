from django.db import models
from .market import Market
from .bookmaker import Bookmaker
from .game_subscriber import GameSubscriber

from django.db.models.signals import post_save
from django.dispatch import receiver

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

    def notify(self) -> None:
            print("Subject: Notifying observers...")
            observers = GameSubscriber.objects.filter(game=self.bookmaker.game)
            for observer in observers:
                observer.update(self)

@receiver(post_save, sender=Outcome)
def notify_observers(sender, instance, created, **kwargs):
    instance.notify()