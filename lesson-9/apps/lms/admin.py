from django.contrib import admin

from apps.lms.models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
