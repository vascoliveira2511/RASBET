
from ..serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView as RTTokenObtainPairView


class TokenObtainPairView(RTTokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer