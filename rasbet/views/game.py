from ..models import Game
from ..serializers import GameSerializer
from rest_framework import viewsets, permissions

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = []