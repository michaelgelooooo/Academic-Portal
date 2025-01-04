from django.contrib import admin
from .models import Parent


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ("parent_id", "first_name", "last_name", "email")
    search_fields = ("parent_id", "first_name", "last_name", "email")
    readonly_fields = ("parent_id",)
