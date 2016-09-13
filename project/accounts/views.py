# coding: utf-8
from django.contrib import auth
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect

from accounts.forms import RegistrationForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django_login(request, user)
            return redirect('/')
    return render(request, 'accounts/login.html')


def signup(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.set_password(request.POST['password'])
        user.save()
        return redirect('/')
    return render(request, 'accounts/signup.html', {'form': form})

# def register(request):
#     user = CreateUser(request.POST)
#     if user.is_valid():
#         save = user.save()
#         save.set_password(user.cleaned_data['password'])
#         save.save()
#         return redirect(request.path)
#     return render(request, 'accounts/register.html', {'forms': user})