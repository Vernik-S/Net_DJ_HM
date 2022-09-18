from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        #print(settings.MAX_STUDENTS_PER_COURSE)
        #print(data)
        if len(data["students"]) > settings.MAX_STUDENTS_PER_COURSE:
            raise ValidationError(f"Max count of students is {settings.MAX_STUDENTS_PER_COURSE}")
        return data