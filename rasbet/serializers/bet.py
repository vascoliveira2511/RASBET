from ..models import Bet, Outcome, BetOutcome
from rest_framework import serializers
import datetime

# Serializers define the API representation.
class BetSerializer(serializers.ModelSerializer):
    outcomes = serializers.ListField(child=serializers.IntegerField(), required=False)
    class Meta:
        model = Bet
        fields = [ 'id', 'stake', 'multiplier', 'prize', 'user', 'status', 'outcomes', 'time']
        # extra_kwargs = {
        #     "multiplier": {"required": False, "allow_null": True}, 
        #     "prize": {"required": False, "allow_null": True},
        #     "status": {"required": False, "allow_null": True},
        #     "time": {"required": False, "allow_null": True}
        #     }


    def create(self, validated_data):
        outcomes_data = validated_data.pop('outcomes')
        multiplier = 1

        for outcome_id in outcomes_data:
            outcome = Outcome.objects.get(pk=outcome_id)
            multiplier *= outcome.multiplier

        bet = Bet.objects.create(time=datetime.datetime.now(),multiplier=multiplier,prize=0**validated_data)
        for outcome_id in outcomes_data:
            outcome = Outcome.objects.get(pk=outcome_id)
            BetOutcome.objects.create(bet=bet, outcome=outcome)
            
        return bet