#_*_coding:utf8_*_
from django.urls import path
from .views import login, logout, home, checkID, addID , query
urlpatterns = [
	path('', home, name='home'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('checkID',checkID, name='checkID'),
    path('addID', addID, name='addID'),
    path('query', query, name='query')
]