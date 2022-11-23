from ..models import BetOutcome
from rest_framework import serializers

# Serializers define the API representation.
class BetOutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetOutcome
        fields = [ 'id', 'bet', 'outcome']
