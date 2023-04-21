from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Flight(models.Model):
    flight_number = models.CharField(max_length=10,default='')
    departure_city = models.CharField(max_length=50,default='')
    arrival_city = models.CharField(max_length=50,default='')
    departure_time = models.DateTimeField(default=timezone.now)
    arrival_time = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f"{self.flight_number} - {self.departure_city} to {self.arrival_city}"

class Passenger(models.Model):
    first_name = models.CharField(max_length=50,default='')
    last_name = models.CharField(max_length=50,default='')
    email = models.EmailField(max_length=254,default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.flight} - {self.passenger}"



