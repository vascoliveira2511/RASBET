from ..models import Game
from rest_framework import serializers

# Serializers define the API representation.
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [ 'id', 'name', 'home_team', 'away_team', 'commance_time', 'completed', 'scores']
