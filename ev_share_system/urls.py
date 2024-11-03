"""
URL configuration for ev_share_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from . import views
from .views import customer_main, operator_main, manager_main


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('', views.home, name='home'),  # Set the root URL to render the home page
    #path('login_page/', auth_views.LoginView.as_view(template_name='login.html'), name='login_page'),
    path('login_page',views.login_page,name='login_page'),
    path('login/',views.login, name='login'),
    path('get_locations/', views.get_locations, name='get_locations'),
    path('register/', include('customers.urls')),
    path('customers/', include('customers.urls')),  # Customer app URLs
    path('operators/', include('operators.urls')),  # Operator app URLs
    path('managers/', include('managers.urls')),  # Manager app URLs
    path('customer_main/', customer_main, name='customer_main'),
    path('operator_main/', operator_main, name='operator_main'),
    path('manager_main/', manager_main, name='manager_main'),
]


