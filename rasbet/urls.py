from django.urls import path, include
from rest_framework import routers
from .views import BetOutcomeViewSet, UserViewSet, TokenObtainPairView, RegisterView, BetViewSet, BookmakerViewSet, GameViewSet, MarketViewSet, OutcomeViewSet, WalletViewSet
from rest_framework_simplejwt.views import TokenRefreshView


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet,basename="user")
router.register(r'bets', BetViewSet,basename="bet")
router.register(r'bookmakers', BookmakerViewSet,basename="bookmaker")
router.register(r'games', GameViewSet,basename="game")
router.register(r'markets', MarketViewSet,basename="market")
router.register(r'outcomes', OutcomeViewSet,basename="outcome")
router.register(r'wallets', WalletViewSet,basename="wallet")
router.register(r'bet_outcomes', BetOutcomeViewSet,basename="bet_outcome")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]