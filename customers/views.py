
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Vehicle, Rental, Report
from operators.models import DefectiveVehicle
from .forms import RentalForm, ReportForm, RegistrationForm
from django.contrib import messages # Import the messages module
from django.contrib.auth.hashers import make_password, check_password  # Import password hashing functions
import json


# View for Customer Dashboard
def customer_main(request):
    # Get the logged-in customer by matching email with the user email
    try:
        customer = Customer.objects.get(email=request.user.email)
    except Customer.DoesNotExist:
        return redirect('login_page')  # Redirect to login if customer not found
    
    # Fetch the rent details related to this customer
    rented_vehicles = Rent.objects.filter(customer=customer)

    return render(request, 'customer_main.html', {
        'customer': customer,
        'rented_vehicles': rented_vehicles,
    })

def return_vehicle(request):
    # Your logic for returning a vehicle
    return render(request, 'customers/return_vehicle.html')
def rent_vehicle(request):
    # Logic to handle vehicle renting
    return render(request, 'customers/rent_vehicle.html')

def report_issue(request):
    # Logic to handle vehicle renting
    return render(request, 'customers/rent_vehicle.html')

def make_payment(request):
    # Logic to handle vehicle renting
    return render(request, 'customers/rent_vehicle.html')

def customer_main(request):
    # Your logic here
    return render(request, 'customer_main.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user data
            customer = form.save(commit=False)
            customer.password =make_password(form.cleaned_data['password'])  # Store the password (hash it in practice)
            customer.save()
            messages.success(request, 'Registration successful!')
            return redirect('home') # Redirect to a success page
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

