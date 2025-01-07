from django.contrib import admin
from .models import UserAccessLogs, UserAccountLogs, SubjectsChangesLogs, ClassChangesLogs


# Register your models here.
@admin.register(UserAccessLogs)
class UserAccessLogsAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_type", "action", "log_time")
    search_fields = ("user_name", "user_type", "action", "log_time")
    readonly_fields = ("user_name", "user_type", "action", "log_time")


@admin.register(UserAccountLogs)
class UserAccountLogsAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_type", "action", "log_time")
    search_fields = ("user_name", "user_type", "action", "log_time")
    readonly_fields = ("user_name", "user_type", "action", "log_time")


@admin.register(SubjectsChangesLogs)
class SubjectsChangesLogsAdmin(admin.ModelAdmin):
    list_display = ("subject_code", "subject_name", "action", "log_time")
    search_fields = ("subject_code", "subject_name", "action", "log_time")
    readonly_fields = ("subject_code", "subject_name", "action", "log_time")

@admin.register(ClassChangesLogs)
class ClassChangesLogsAdmin(admin.ModelAdmin):
    list_display = ("class_name", "action", "log_time")
    search_fields = ("class_name", "action", "log_time")
    readonly_fields = ("class_name", "action", "log_time")
