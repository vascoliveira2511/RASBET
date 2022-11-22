from ..models import Bookmaker
from ..serializers import BookmakerSerializer
from rest_framework import viewsets, permissions

class BookmakerViewSet(viewsets.ModelViewSet):
    queryset = Bookmaker.objects.all()
    serializer_class = BookmakerSerializer
    permission_classes = []