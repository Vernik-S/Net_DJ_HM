# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, CreateAPIView, \
    RetrieveUpdateAPIView
from rest_framework.response import Response

from measurement.models import Sensor
from measurement.serializers import SensorsSerializer


class SensorsView(ListCreateAPIView, ):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


# class SensorView(CreateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorsSerializer
#
#     def perform_create(self, serializer):
#         q = serializer.save()
#         TmpLogg(entry=q.service).save() # the other variable i need