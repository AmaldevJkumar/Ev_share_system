from django.urls import path
from .views import  rent_vehicle,report_issue,return_vehicle,make_payment
from . import views

urlpatterns = [
    path('', views.customer_main, name='customer_main'),
    path('customer_main/', views.customer_main, name='customer_main'),
    path('register/', views.register, name='register'),
    path('rent_vehicle/', rent_vehicle, name='rent_vehicle'),  
    path('return/', return_vehicle, name='return_vehicle'),
    path('report_issue/', report_issue, name='report_issue'),
    path('make_payment/', views.make_payment, name='make_payment'),
    #path('report_defect/', views.report_defect, name='report_defect'),
]
