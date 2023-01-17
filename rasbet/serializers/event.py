from ..models import Event
from rest_framework import serializers

# Serializers define the API representation.
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [ 'id', 'owner', 'status', 'description']