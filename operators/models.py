# Create your models here.
from django.db import models
from customers.models import Vehicle,Location
from django.utils import timezone
import uuid


class Operator(models.Model):
    id = models.AutoField(primary_key=True)  # Ensures the ID is unique and is the primary key
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)  # Foreign key to the Location model
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, unique=True,default='')  # Ensure unique mobile number
    password = models.CharField(max_length=128,default='')  # Store hashed passwords
    joined_date = models.DateTimeField(default=timezone.now)  # Automatically set the join date

    def __str__(self):
        return self.name


class Charging(models.Model):
    CHARGING_STATUS_CHOICES = [
        ('nil', 'Nil'),          # Not in charging process yet
        ('charging', 'Charging'), # Currently charging
        ('charged', 'Charged'),   # Charging complete
        ('low_battery', 'Low Battery'), # Initial status when battery is low
    ]
    id = models.AutoField(primary_key=True) 
    vehicle = models.ForeignKey('customers.Vehicle', on_delete=models.CASCADE)  # Foreign key to the Vehicle model
    location = models.ForeignKey('customers.Location', on_delete=models.CASCADE)  # Foreign key to the Location model
    charge_level = models.IntegerField()  # Current charge level of the vehicle
    status = models.CharField(max_length=20, choices=CHARGING_STATUS_CHOICES, default='low_battery')
    updated_at = models.DateTimeField(auto_now=True)  # Track the last time this record was updated

    def __str__(self):
        return f"LowBatteryVehicle {self.vehicle.vehicle_id} - {self.status} - {self.charge_level}%"

class DefectiveVehicle(models.Model):
    STATUS_CHOICES = [
        ('reported', 'Reported'),        # Vehicle reported as defective
        ('in_repair', 'In Repair'),      # Vehicle is currently being repaired
        ('repaired', 'Repaired'),         # Vehicle has been repaired
        ('not_repairable', 'Not Repairable') # Vehicle cannot be repaired
    ]

    id = models.AutoField(primary_key=True)  # Unique ID for each defect record
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)  # Link to the Vehicle model
    defect_description = models.TextField()  # Description of the defect
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='reported')  # Current status of the defect
    reported_date = models.DateTimeField(auto_now_add=True)  # When the defect was reported
    repair_notes = models.TextField(blank=True)  # Notes related to the repair process

    def __str__(self):
        return f"DefectiveVehicle {self.id} - {self.vehicle.id} - Status: {self.status}"



