from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

    
class bus(models.Model):
    bus_name=models.CharField(max_length=100)
    bus_number=models.CharField(max_length=100)
    bus_origin=models.CharField(max_length=100)
    bus_destination=models.CharField(max_length=100)
    total_seats=models.PositiveBigIntegerField()
    startDate=models.DateField()
    endDate=models.DateField()
    bus_time=models.TimeField()
    price=models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.bus_name    
    
    
class seat(models.Model):
    bus=models.ForeignKey(bus,on_delete=models.CASCADE)
    seat_number=models.CharField(max_length=100)
    is_booked=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.bus.bus_name} - Seat {self.seat_number}"