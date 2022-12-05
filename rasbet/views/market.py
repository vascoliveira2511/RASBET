from ..models import Market
from ..serializers import MarketSerializer
from rest_framework import viewsets, permissions

class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = []