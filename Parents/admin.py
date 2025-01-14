from django.contrib import admin
from .models import Parent
from django import forms
from django.core.exceptions import ValidationError
import re


class UserAdminForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        help_text="Password must be at least 8 characters long and contain uppercase, lowercase letters and numbers."
    )
    
    class Meta:
        model = Parent
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

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = ("parent_id", "first_name", "last_name", "email")
    search_fields = ("parent_id", "first_name", "last_name", "email")
    readonly_fields = ("parent_id",)
    
    def get_form(self, request, obj=None, **kwargs):
        if obj:  # This is an edit form
            self.exclude = ('password',)
        else:  # This is an add form
            self.exclude = None
        return super().get_form(request, obj, **kwargs)
