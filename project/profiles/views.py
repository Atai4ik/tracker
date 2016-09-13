#coding: utf-8
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from profiles.forms import ProfileEdit
from profiles.models import DetailProfile


def profile(request):
    profile = DetailProfile.objects.get(user=request.user)
    return render(request, 'profiles/profiles.html', {'profile': profile})


def signout(request):
    logout(request)
    return redirect('/')


def update_profile(request):
    form = ProfileEdit(
        request.POST or None,
        request.FILES or None,
        instance=request.user.prof
    )
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('/profiles')
    return render(request, 'profiles/edit_profile.html', {'form': form})





# class Profile
#     balance:


    #
    # def update_balance(self, sum)
    #     1 income создать
    #     2 self.balance += sum
    #     self.save()