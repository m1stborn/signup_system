#_*_coding:utf8_*_
from django.urls import path
from .views import login, logout, home, checkID, addID , confirm, logout_confirm
urlpatterns = [
	path('', home, name='home'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('checkID',checkID, name='checkID'),
    path('addID', addID, name='addID'),
    path('confirm', confirm, name="confirm"),
    path('logout_confirm', logout_confirm, name="logout_confirm" )
]