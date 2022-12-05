from ..models import Bookmaker
from rest_framework import serializers

# Serializers define the API representation.
class BookmakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmaker
        fields = [ 'id', 'key', 'last_update', 'game']
