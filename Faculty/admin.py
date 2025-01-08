from django.contrib import admin
from .models import Faculty, Subjects


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("faculty_id", "first_name", "last_name", "email")
    search_fields = ("faculty_id", "first_name", "last_name", "email")
    readonly_fields = ("faculty_id",)


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ("subject_code", "subject_name", "instructor")
    search_fields = ("subject_code", "subject_name", "instructor")
