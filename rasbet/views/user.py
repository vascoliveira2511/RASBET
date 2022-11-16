from ..models import User
from ..serializers import UserSerializer
from rest_framework import viewsets, permissions
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]