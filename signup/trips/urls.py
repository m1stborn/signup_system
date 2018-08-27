#_*_coding:utf8_*_
from django.urls import path
from .views import new,hello_world,qrcode
urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('new/', new, name='new'),
    path('test2/', qrcode, name='qrcode'),
]