from ..models import GameSubscriber, User
from rest_framework import serializers

# Serializers define the API representation.
class GameSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSubscriber
        fields = [ 'id', 'game', 'subscriber']
        extra_kwargs = {'subscriber': {'read_only': True, 'required': False}}

    def create(self, validated_data):
        user = User.objects.get(id=self.context['request'].user.id)
        game_subscriber, created = GameSubscriber.objects.get_or_create(
            game=validated_data['game'],
            subscriber=user
        )

        if game_subscriber:
            return game_subscriber
        else:
            return created
