from re import M
from django.db import models


# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length=12)
    operating_airlines = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_date = models.DateField()
    estimated_departure_time = models.TimeField()

class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
