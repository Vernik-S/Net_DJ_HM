from django.contrib import admin

from .models import Student, Teacher

class TeacherInline(admin.TabularInline):
    model = Teacher
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "group", ]
    #inlines = [TeacherInline]



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "subject", ]
