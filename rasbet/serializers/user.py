from ..models import User
from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'id', 'username', 'first_name', 'last_name', 'email', 'password', 'wallet', 'is_staff']
