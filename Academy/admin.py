from django.contrib import admin
from .models import (
    UserAccessLogs,
    UserAccountLogs,
    SubjectsChangesLogs,
    ClassChangesLogs,
    LectureMaterialsLogs,
    GradeChangesLogs,
)
from django.contrib.auth.models import User, Group

# Unregister the User and Group models
admin.site.unregister(User)
admin.site.unregister(Group)


# Register your models here.
@admin.register(UserAccessLogs)
class UserAccessLogsAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_type", "action", "log_time")
    search_fields = ("user_name", "user_type", "action", "log_time")
    readonly_fields = ("user_name", "user_type", "action", "log_time")

    # Disable the 'Add' button in the admin
    def has_add_permission(self, request):
        return False

    # Disable editing existing records
    def has_change_permission(self, request, obj=None):
        return False

    # Disable deleting records
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(UserAccountLogs)
class UserAccountLogsAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_type", "action", "log_time")
    search_fields = ("user_name", "user_type", "action", "log_time")
    readonly_fields = ("user_name", "user_type", "action", "log_time")

    # Disable the 'Add' button in the admin
    def has_add_permission(self, request):
        return False

    # Disable editing existing records
    def has_change_permission(self, request, obj=None):
        return False

    # Disable deleting records
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SubjectsChangesLogs)
class SubjectsChangesLogsAdmin(admin.ModelAdmin):
    list_display = ("subject_code", "subject_name", "action", "log_time")
    search_fields = ("subject_code", "subject_name", "action", "log_time")
    readonly_fields = ("subject_code", "subject_name", "action", "log_time")

    # Disable the 'Add' button in the admin
    def has_add_permission(self, request):
        return False

    # Disable editing existing records
    def has_change_permission(self, request, obj=None):
        return False

    # Disable deleting records
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ClassChangesLogs)
class ClassChangesLogsAdmin(admin.ModelAdmin):
    list_display = ("class_name", "action", "log_time")
    search_fields = ("class_name", "action", "log_time")
    readonly_fields = ("class_name", "action", "log_time")

    # Disable the 'Add' button in the admin
    def has_add_permission(self, request):
        return False

    # Disable editing existing records
    def has_change_permission(self, request, obj=None):
        return False

    # Disable deleting records
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(LectureMaterialsLogs)
class LectureMaterialsLogsAdmin(admin.ModelAdmin):
    list_display = ("material_id", "action", "log_time")
    search_fields = ("material_id", "action", "log_time")
    readonly_fields = ("material_id", "action", "log_time")

    # Disable the 'Add' button in the admin
    def has_add_permission(self, request):
        return False

    # Disable editing existing records
    def has_change_permission(self, request, obj=None):
        return False

    # Disable deleting records
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(GradeChangesLogs)
class GradeChangesLogsAdmin(admin.ModelAdmin):
    list_display = ("student_id", "subject_code", "log_time")
    search_fields = ("student_id", "subject_code", "log_time")
    readonly_fields = ("student_id", "subject_code", "log_time")

    # Disable the 'Add' button in the admin
    def has_add_permission(self, request):
        return False

    # Disable editing existing records
    def has_change_permission(self, request, obj=None):
        return False

    # Disable deleting records
    def has_delete_permission(self, request, obj=None):
        return False
