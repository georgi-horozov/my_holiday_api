from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from my_holiday.destination.models import Place

from .serializers import DestinationSerializer


class DestinationViewSet(viewsets.ModelViewSet):
    serializer_class = DestinationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Place.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)