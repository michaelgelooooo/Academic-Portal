from django.contrib import admin
from .models import Faculty, Subjects, LectureMaterial, Tasks


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("faculty_id", "first_name", "last_name", "email")
    search_fields = ("faculty_id", "first_name", "last_name", "email")
    readonly_fields = ("faculty_id",)


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ("subject_code", "subject_name", "instructor")
    search_fields = ("subject_code", "subject_name", "instructor")
    list_filter = ("year_level",)


@admin.register(LectureMaterial)
class LectureMaterialAdmin(admin.ModelAdmin):
    list_display = ("lecture_id", "lecture_title", "subject")
    search_fields = ("lecture_id", "lecture_title", "subject")
    list_filter = ("subject",)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_id", "subject", "task_deadline")
    search_fields = ("task_id", "subject", "task_deadline")
    list_filter = ("subject",)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
