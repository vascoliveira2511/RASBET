from ..models import Outcome
from rest_framework import serializers

# Serializers define the API representation.
class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome
        fields = [ 'id', 'result', 'multiplier', 'market', 'bookmaker']
