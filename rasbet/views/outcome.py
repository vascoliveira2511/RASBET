from ..models import Outcome
from ..serializers import OutcomeSerializer
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class OutcomeViewSet(viewsets.ModelViewSet):
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer
    permission_classes = []

    def get_queryset(self):
        if self.request.query_params.get('bookmaker'):
            return Outcome.objects.filter(bookmaker=self.request.query_params.get('bookmaker'))
        else:
            return Outcome.objects.all()

    # def retrieve(self, request, pk=None):
    #     outcome = get_object_or_404(self.queryset, pk=pk)
    #     serializer = OutcomeSerializer(outcome)
    #     return Response(serializer.data)