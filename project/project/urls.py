"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from accounts import urls as accounts_urls

from advice import views
from project import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.base, name='base'),
    url(r'^advice/', views.advice, name='advice'),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^income/', include('income.urls', namespace='income')),
    url(r'^profiles/', include('profiles.urls', namespace='profile'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +\
   static(settings.STATIC_URL, document_root=settings.STATIC_URL)
