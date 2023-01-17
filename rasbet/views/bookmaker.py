from ..models import Bookmaker
from ..serializers import BookmakerSerializer
from rest_framework import viewsets, permissions

class BookmakerViewSet(viewsets.ModelViewSet):
    queryset = Bookmaker.objects.all()
    serializer_class = BookmakerSerializer
    permission_classes = []

    def get_queryset(self):
        if self.request.query_params.get('key'):
            return Bookmaker.objects.filter(game=self.request.query_params.get('game'), key=self.request.query_params.get('key'))
        else:
            return Bookmaker.objects.filter(game=self.request.query_params.get('game'))