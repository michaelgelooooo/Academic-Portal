from django.contrib import admin
from .models import Faculty, Subjects, LectureMaterial, Tasks
from django import forms
from django.core.exceptions import ValidationError
import re


class UserAdminForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        help_text="Password must be at least 8 characters long and contain uppercase, lowercase letters and numbers."
    )
    
    class Meta:
        model = Faculty
        fields = '__all__'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
            
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must contain at least one uppercase letter.")
            
        if not re.search(r'[a-z]', password):
            raise ValidationError("Password must contain at least one lowercase letter.")
            
        if not re.search(r'[0-9]', password):
            raise ValidationError("Password must contain at least one number.")
            
        return password

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = ("faculty_id", "first_name", "last_name", "email")
    search_fields = ("faculty_id", "first_name", "last_name", "email")
    readonly_fields = ("faculty_id",)
    
    def get_form(self, request, obj=None, **kwargs):
        # obj=None means this is an add form (creating new record)
        if obj:  # This is an edit form
            self.exclude = ('password',)
        else:  # This is an add form
            self.exclude = None
        return super().get_form(request, obj, **kwargs)


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
