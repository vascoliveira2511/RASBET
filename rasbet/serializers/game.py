from ..models import Game
from rest_framework import serializers

# Serializers define the API representation.
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [ 'id', 'name', 'home_team', 'away_team', 'commence_time', 'completed', 'scores']

    # def get_home_team(self, obj):
    #     bookmaker = Bookmaker.objects.get(id=obj.bookmaker.id)
    #     return Game.objects.get(id=bookmaker.game.id).home_team

    # def notify(self) -> None:
    #         """
    #         Trigger an update in each subscriber.
    #         """

    #         print("Subject: Notifying observers...")
    #         observers = GameObserver.objects..filter(game=self.id)
    #         for observer in observers:
    #             observer.update(self)