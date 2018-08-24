#_*_coding:utf8_*_
from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]