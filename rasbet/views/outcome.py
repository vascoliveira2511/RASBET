from ..models import Outcome
from ..serializers import OutcomeSerializer
from rest_framework import viewsets, permissions

class OutcomeViewSet(viewsets.ModelViewSet):
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer
    permission_classes = []

    def get_queryset(self):
        return Outcome.objects.filter(bookmaker=self.request.query_params.get('bookmaker'))