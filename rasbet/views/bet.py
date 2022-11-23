from ..models import Bet
from ..serializers import BetSerializer
from rest_framework import viewsets, permissions

class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = []