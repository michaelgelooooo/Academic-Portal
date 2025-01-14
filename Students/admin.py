from django.contrib import admin
from .models import Student, Classes, Grades
from django import forms
from django.core.exceptions import ValidationError
import re


class UserAdminForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        help_text="Password must be at least 8 characters long and contain uppercase, lowercase letters and numbers."
    )
    
    class Meta:
        model = Student
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

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = ("student_id", "first_name", "last_name", "year_level", "email")
    search_fields = ("student_id", "first_name", "last_name", "year_level", "email")
    readonly_fields = ("student_id",)
    list_filter = ("year_level",)
    
    def get_form(self, request, obj=None, **kwargs):
        if obj:  # This is an edit form
            self.exclude = ('password',)
        else:  # This is an add form
            self.exclude = None
        return super().get_form(request, obj, **kwargs)


@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ("year_level", "adviser")
    search_fields = ("year_level", "adviser")


@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "grade")
    search_fields = ("student", "subject", "grade")
    list_filter = ("subject",)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
