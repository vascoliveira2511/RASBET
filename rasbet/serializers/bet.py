from ..models import Bet
from rest_framework import serializers

# Serializers define the API representation.
class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = [ 'id', 'stake', 'multiplier', 'time', 'prize', 'user']
