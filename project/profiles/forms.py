#coding: utf-8

from django import forms
from profiles.models import DetailProfile


class ProfileEdit(forms.ModelForm):
    class Meta:
        model = DetailProfile
        fields = (
            'avatar', 'first_name', 'last_name', 'birthday', 'phone'
        )




