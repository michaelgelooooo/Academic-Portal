from django.contrib import admin
from .models import UserAccessLogs, UserAccountLogs

# Register your models here.
@admin.register(UserAccessLogs)
class UserAccessLogsAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_type", "log_type", "log_time")
    search_fields = ("user_name", "user_type", "log_type", "log_time")
    readonly_fields = ("user_name", "user_type", "log_type", "log_time")

@admin.register(UserAccountLogs)
class UserAccountLogsAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_type", "log_type", "log_time")
    search_fields = ("user_name", "user_type", "log_type", "log_time")
    readonly_fields = ("user_name", "user_type", "log_type", "log_time")