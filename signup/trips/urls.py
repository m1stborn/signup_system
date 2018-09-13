#_*_coding:utf8_*_
from django.urls import path
from .views import login, logout, home
urlpatterns = [
	path('', home, name='home'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]