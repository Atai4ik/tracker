from django.shortcuts import render, redirect

from income.forms import IncomeForms
from income.models import UserIncome


def create_income(request):
    forms = IncomeForms()
    forms = IncomeForms(request.POST or None)
    if forms.is_valid():
        forms = forms.save(commit=False)
        forms.user = request.user
        forms.save()
        income = UserIncome.objects.get(pk=int(forms.id))
        income.update_balance()
        return redirect(request.path)
    return render(request, 'create_income.html', {'forms': forms})
