from ..models import Wallet
from ..serializers import WalletSerializer
from rest_framework import viewsets, permissions

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]