"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('trips.urls'), name='trips'),
]

# admin.site.site_header = "管理人員介面"
# admin.site.site_title = "UMSRA Admin Portal"
# admin.site.index_title = "Welcome to UMSRA Researcher Portal"

admin.site.site_header = "管理人員頁面"
admin.site.site_title = "管理人員"
admin.site.site_url = "https://203.145.195.202:11111/admin/trips/visit_logs/"
admin.site.index_title = "訪客簽到系統管理"
