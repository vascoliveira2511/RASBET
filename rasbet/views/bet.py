from ..models import Bet
from ..serializers import BetSerializer
from rest_framework import viewsets, permissions

class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.id:
            return Bet.objects.filter(user=self.request.user.id)
        else:
            return Bet.objects.all()