from rest_framework import serializers

from my_holiday.destination.models import Place


class DestinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = ["id", "hotel_name", "description", "location"]