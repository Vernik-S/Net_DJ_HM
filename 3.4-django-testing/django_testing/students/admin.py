from django.contrib import admin

# Register your models here.
from students.models import Course, Student


@admin.register(Course)
class ProductAdmin(admin.ModelAdmin):
    pass





@admin.register(Student)
class ProductAdmin(admin.ModelAdmin):
    pass