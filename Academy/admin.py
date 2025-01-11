from django.contrib import admin
from .models import (
    Announcements,
    SupportChat,
    SupportMessage,
    UserAccessLogs,
    UserAccountLogs,
    SubjectsChangesLogs,
    ClassChangesLogs,
    LectureMaterialsLogs,
    GradeChangesLogs,
    TaskChangesLog,
)


@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ("announcement_title", "announcement_content", "announcement_date")
    search_fields = ("announcement_title", "announcement_content", "announcement_date")
    readonly_fields = ("announcement_date",)


@admin.register(SupportChat)
class SupportChatAdmin(admin.ModelAdmin):
    list_display = ("chat_recipient", "created_at")
    seach_fields = ("chat_recipient", "created_at")
    readonly_fields = ("created_at",)


@admin.register(SupportMessage)
class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ("conversation", "sender", "timestamp")
    seach_fields = ("conversation", "sender", "timestamp")
    readonly_fields = ("timestamp",)


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


@admin.register(TaskChangesLog)
class TaskChangesLogAdmin(BaseLogsAdmin):
    list_display = ("task_id", "action", "log_time")
    search_fields = ("task_id", "action", "log_time")
    readonly_fields = ("task_id", "action", "log_time")
