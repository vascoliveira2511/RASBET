from ..models import BetOutcome
from ..serializers import BetOutcomeSerializer
from rest_framework import viewsets, permissions

class BetOutcomeViewSet(viewsets.ModelViewSet):
    queryset = BetOutcome.objects.all()
    serializer_class = BetOutcomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.query_params.get('bet'):
            return BetOutcome.objects.filter(bet=self.request.query_params.get('bet'))
        else:
            return BetOutcome.objects.all()