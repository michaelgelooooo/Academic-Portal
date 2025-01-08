from django.contrib import admin
from .models import Student, Classes, Grades


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "first_name", "last_name", "year_level", "email")
    search_fields = ("student_id", "first_name", "last_name", "year_level", "email")
    readonly_fields = ("student_id",)
    list_filter = ("year_level",)


@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ("year_level", "adviser")
    search_fields = ("year_level", "adviser")


@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "grade")
    search_fields = ("student", "subject", "grade")
    list_filter = ("subject",)
