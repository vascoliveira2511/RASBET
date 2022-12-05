from ..models import Wallet
from rest_framework import serializers

# Serializers define the API representation.
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = [ 'id', 'iban', 'balance']
