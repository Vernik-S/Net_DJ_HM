# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import  ListCreateAPIView, CreateAPIView, \
    RetrieveUpdateAPIView


from measurement.models import Sensor, Measurement
from measurement.serializers import SensorsSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorsView(ListCreateAPIView, ):
    queryset = Sensor.objects.all()

    serializer_class = SensorsSerializer


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    #serializer_class = SensorsSerializer
    serializer_class = SensorDetailSerializer


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
