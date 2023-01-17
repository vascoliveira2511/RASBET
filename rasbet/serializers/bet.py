from ..models import Bet, Outcome, BetOutcome
from rest_framework import serializers
import datetime

# Serializers define the API representation.
class BetSerializer(serializers.ModelSerializer):
    outcomes = serializers.ListField(child=serializers.IntegerField(), required=False)
    class Meta:
        model = Bet
        fields = [ 'id', 'stake', 'multiplier', 'prize', 'user', 'status', 'outcomes', 'time']
        extra_kwargs = {'time': {'read_only': True, 'required': False},'status': {'read_only': True, 'required': False}}


    def create(self, validated_data):
        outcomes_data = validated_data.pop('outcomes')

        for outcome_id in outcomes_data:
            outcome = Outcome.objects.get(pk=outcome_id)

        bet = Bet.objects.create(time=datetime.datetime.now(), **validated_data)
        for outcome_id in outcomes_data:
            outcome = Outcome.objects.get(pk=outcome_id)
            BetOutcome.objects.create(bet=bet, outcome=outcome)
            
        return bet