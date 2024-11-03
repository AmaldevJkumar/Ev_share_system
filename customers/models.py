# Create your models here.
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
import uuid  # For generating unique customer IDs

class Customer(models.Model):
    id = models.AutoField(primary_key=True)  # Ensures the ID is unique and is the primary key
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50,default='loc')  # Location will be a dropdown
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, unique=True,default='')  # Ensure unique mobile number
    password = models.CharField(max_length=128,default='')  # Store hashed passwords
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Default balance is 0
    joined_date = models.DateTimeField(default=timezone.now)  # Automatically set the join date

    def __str__(self):
        return self.name


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=255, unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.location_name



class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('bike', 'Bike'),
        ('scooter', 'Scooter'),
    ]

    STATUS_CHOICES = [
        ('available', 'Available'),         # Ready for rent
        ('unavailable', 'Unavailable'),     # Currently rented
        ('maintenance', 'Maintenance'),     # Undergoing repairs or maintenance
        ('out_of_service', 'Out of Service'),  # Defective or not in use permanently
    ]
    
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_name = models.CharField(max_length=100, null=True)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPE_CHOICES)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)  # Link to Location model
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    charging_level = models.IntegerField(default=100)
    charge_per_hour = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)  # Hourly charge for renting
    miles_per_percent_charge = models.DecimalField(max_digits=5, decimal_places=2, default=0.50)  # Miles per 1% charge
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vehicle_name} ({self.vehicle_type}) - {self.vehicle_id}"


class Rental(models.Model):
    rent_id = models.AutoField(primary_key=True)  # Unique ID for each rental
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)  # Foreign key to Customer model
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)  # Foreign key to Vehicle model
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)  # Foreign key to Location model
    starting_time = models.DateTimeField(auto_now_add=True)  # Start time is set when rental is created
    ending_time = models.DateTimeField(null=True, blank=True)  # Nullable for active rentals
    total_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Total rental hours
    amount_charged = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Final amount charged

    def __str__(self):
        return f"Rental {self.rent_id} by {self.customer.name}"

class Report(models.Model):
    id = models.AutoField(primary_key=True)  # Unique ID for each report
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.id} for Vehicle {self.vehicle.id}"
