from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as RFTokenObtainPairSerializer


class TokenObtainPairSerializer(RFTokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(TokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token