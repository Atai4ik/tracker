from django.conf.urls import url
from income import views


urlpatterns = [
    url(r'^$', views.create_income, name='create'),

]