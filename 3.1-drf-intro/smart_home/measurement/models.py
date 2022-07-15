from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя датчика")
    description = models.CharField(max_length=100, verbose_name="Описание датчика")
    photo = models.ImageField(null=True, verbose_name="Фото", upload_to="files/sensors_photos")

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurements")
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Температура")
    date_m = models.DateField(auto_now_add=True, verbose_name="Дата измерения")

    def __str__(self):
        return str(self.sensor)+":"+str(self.date_m)


