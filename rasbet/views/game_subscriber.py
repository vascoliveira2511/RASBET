from ..models import GameSubscriber
from ..serializers import GameSubscriberSerializer
from rest_framework import viewsets, permissions

class GameSubscriberViewSet(viewsets.ModelViewSet):
    queryset = GameSubscriber.objects.all()
    serializer_class = GameSubscriberSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.id:
            return GameSubscriber.objects.filter(subscriber=self.request.user.id)
        else:
            return GameSubscriber.objects.all()