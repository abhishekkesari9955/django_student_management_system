from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'age', 'course', 'enrollment_date')
    search_fields = ('full_name', 'email', 'course')
    list_filter = ('course', 'enrollment_date')