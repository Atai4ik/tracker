from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'username', 'email', 'last_name', 'first_name', 'password',
            'password_confirmation'
        )
