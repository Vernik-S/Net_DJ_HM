from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Sensor


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
