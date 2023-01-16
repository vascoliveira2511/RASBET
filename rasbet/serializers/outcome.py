from ..models import Outcome, Bookmaker, Game
from rest_framework import serializers

# Serializers define the API representation.
class OutcomeSerializer(serializers.ModelSerializer):
    home_team = serializers.SerializerMethodField()
    away_team = serializers.SerializerMethodField()

    class Meta:
        model = Outcome
        fields = [ 'id', 'result', 'multiplier', 'market', 'bookmaker', 'home_team', 'away_team']

    def get_home_team(self, obj):
        bookmaker = Bookmaker.objects.get(id=obj.bookmaker.id)
        return Game.objects.get(id=bookmaker.game.id).home_team

    def get_away_team(self, obj):
        bookmaker = Bookmaker.objects.get(id=obj.bookmaker.id)
        return Game.objects.get(id=bookmaker.game.id).away_team