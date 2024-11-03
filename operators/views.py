# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle,Charging,DefectiveVehicle

# View for Operator Dashboard
def operator_dashboard(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'operators/dashboard.html', {'vehicles': vehicles})


