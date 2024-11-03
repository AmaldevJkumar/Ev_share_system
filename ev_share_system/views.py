from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render
from customers.models import Customer,Location
from operators.models import Operator
from managers.models import Manager
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse


def get_locations(request):
    locations = Location.objects.values('location_name', 'latitude', 'longitude')  # Adjust field names as needed
    return JsonResponse(list(locations), safe=False)


# Home page view
def home(request):
    return render(request, 'home.html')  # This will render the home.html template


def login_page(request):
    return render(request, 'login.html')




def customer_main(request):
    # Add your logic here
    return render(request, 'customer_main.html')

def operator_main(request):
    # Add your logic here
    return render(request, 'operator_main.html')

def manager_main(request):
    # Add your logic here
    return render(request, 'manager_main.html')


#login page view

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Check if role is selected
        if not role:
            messages.error(request, "Please select a role.")
            return render(request, 'login.html')

        # Authenticate based on role
        if role == 'customer':
            try:
                customer = Customer.objects.get(email=email)
                if check_password(password, customer.password):  # Check the hashed password
                    return redirect('customer_main')  # Redirect to customer page
                else:
                    messages.error(request, "Invalid email or password for Customer.")
            except Customer.DoesNotExist:
                messages.error(request, "Customer with this email does not exist.")
        
        elif role == 'operator':
            try:
                operator = Operator.objects.get(email=email)
                if check_password(password, operator.password):  # Check the hashed password
                    return redirect('operator_main')  # Redirect to operator page
                else:
                    messages.error(request, "Invalid email or password for Operator.")
            except Operator.DoesNotExist:
                messages.error(request, "Operator with this email does not exist.")

        elif role == 'manager':
            try:
                manager = Manager.objects.get(email=email)
                if check_password(password, manager.password):  # Check the hashed password
                    return redirect('manager_main')  # Redirect to manager page
                else:
                    messages.error(request, "Invalid email or password for Manager.")
            except Manager.DoesNotExist:
                messages.error(request, "Manager with this email does not exist.")

    return render(request, 'login.html')