from django.contrib import admin

# Register your models here.
from measurement.models import Measurement, Sensor


class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 1


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", ]
    inlines = [MeasurementInline]


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ["sensor", "temperature", "date_m", ]
