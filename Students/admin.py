from django.contrib import admin
from .models import Student, Classes


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "first_name", "last_name", "email")
    search_fields = ("student_id", "first_name", "last_name", "email")
    readonly_fields = ("student_id",)


@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ("year_level", "adviser")
    search_fields = ("year_level", "adviser")