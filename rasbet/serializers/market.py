from ..models import Market
from rest_framework import serializers

# Serializers define the API representation.
class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = [ 'id', 'key']
