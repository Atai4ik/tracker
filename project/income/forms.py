from django import forms

from income.models import UserIncome


class IncomeForms(forms.ModelForm):
    class Meta:
        model = UserIncome
        exclude = ()
        fields = ('user', 'amount', 'source', 'comment')