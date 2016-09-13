# coding: utf-8

from django.conf.urls import url
from profiles import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^edit/$', views.update_profile, name='edit')

]