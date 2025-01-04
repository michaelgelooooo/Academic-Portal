from django import forms

class LoginForm(forms.Form):
    student_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Student ID',
                'autocomplete': 'off'
            }
        ),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password',
                'autocomplete': 'off'
            }
        ),
        required=True
    )