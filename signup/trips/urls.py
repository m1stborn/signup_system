#_*_coding:utf8_*_
from django.urls import path
from .views import new, Q_out, home
urlpatterns = [
	path('', home, name='home'),
    path('new/', new, name='new'),
    # path('Q_in/', Q_in, name='Q_in'),
    path('Q_out', Q_out, name='Q_out'),
]