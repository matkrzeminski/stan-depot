from rest_framework import serializers

from .models import Place


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ["id", "street", "zip_code", "city", "country", "latitude", "longitude"]
