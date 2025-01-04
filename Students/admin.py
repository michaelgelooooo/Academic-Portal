from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "first_name", "last_name", "email")
    search_fields = ("student_id", "first_name", "last_name", "email")
    readonly_fields = ("student_id",)
