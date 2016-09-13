# coding: utf-8

from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^signup', views.signup, name='signup')
]