from django.contrib import admin
from .models import (
    UserAccessLogs,
    UserAccountLogs,
    SubjectsChangesLogs,
    ClassChangesLogs,
    LectureMaterialsLogs,
    GradeChangesLogs,
)

class BaseLogsAdmin(admin.ModelAdmin):
    """Base class to handle common permissions for log models"""
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(UserAccessLogs)
class UserAccessLogsAdmin(BaseLogsAdmin):
    list_display = ("user_name", "user_type", "action", "log_time")
    search_fields = ("user_name", "user_type", "action", "log_time")
    readonly_fields = ("user_name", "user_type", "action", "log_time")

@admin.register(UserAccountLogs)
class UserAccountLogsAdmin(BaseLogsAdmin):
    list_display = ("user_name", "user_type", "action", "log_time")
    search_fields = ("user_name", "user_type", "action", "log_time")
    readonly_fields = ("user_name", "user_type", "action", "log_time")

@admin.register(SubjectsChangesLogs)
class SubjectsChangesLogsAdmin(BaseLogsAdmin):
    list_display = ("subject_code", "subject_name", "action", "log_time")
    search_fields = ("subject_code", "subject_name", "action", "log_time")
    readonly_fields = ("subject_code", "subject_name", "action", "log_time")

@admin.register(ClassChangesLogs)
class ClassChangesLogsAdmin(BaseLogsAdmin):
    list_display = ("class_name", "action", "log_time")
    search_fields = ("class_name", "action", "log_time")
    readonly_fields = ("class_name", "action", "log_time")

@admin.register(LectureMaterialsLogs)
class LectureMaterialsLogsAdmin(BaseLogsAdmin):
    list_display = ("material_id", "action", "log_time")
    search_fields = ("material_id", "action", "log_time")
    readonly_fields = ("material_id", "action", "log_time")

@admin.register(GradeChangesLogs)
class GradeChangesLogsAdmin(BaseLogsAdmin):
    list_display = ("student_id", "subject_code", "log_time")
    search_fields = ("student_id", "subject_code", "log_time")
    readonly_fields = ("student_id", "subject_code", "log_time")
