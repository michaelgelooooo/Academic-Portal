from django import forms
from .models import Faculty


class LoginForm(forms.Form):
    faculty_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Faculty ID",
                "autocomplete": "off",
            }
        ),
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Password",
                "autocomplete": "off",
            }
        ),
        required=True,
    )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ["first_name", "last_name", "email", "phone_number"]
        exclude = ["faculty_id", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control", "autocomplete": "off"})

    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")
        phone = "".join(filter(str.isdigit, phone))
        if len(phone) < 10 or len(phone) > 15:
            raise forms.ValidationError("Phone number must be between 10 and 15 digits")
        return phone
