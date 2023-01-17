from ..models import Event
from ..serializers import EventSerializer
from rest_framework import viewsets, permissions

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.id:
            return Event.objects.filter(owner=self.request.user.id)
        else:
            return Event.objects.all()