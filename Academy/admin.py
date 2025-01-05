from django.contrib import admin
from .models import UserAccessLogs

# Register your models here.
@admin.register(UserAccessLogs)
class UserAccessLogsAdmin(admin.ModelAdmin):
    list_display = ("user_id", "user_type", "log_type", "log_time")
    search_fields = ("user_id", "user_type", "log_type", "log_time")
    readonly_fields = ("user_id", "user_type", "log_type", "log_time")