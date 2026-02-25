from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user   
class Bus(models.Model):
    bus_name=models.CharField(max_length=100)
    bus_number=models.CharField(max_length=100)
    bus_origin=models.CharField(max_length=100)
    bus_destination=models.CharField(max_length=100)
    total_seats=models.PositiveBigIntegerField()
    available_seats = models.PositiveIntegerField()
    startDate=models.DateField()
    endDate=models.DateField()
    bus_time=models.TimeField()
    price=models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.bus_name 
    @property
    def available_seats(self):
        return self.seats.filter(is_booked=False).count()   
    
    
class Seat(models.Model):
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE)
    seat_number=models.CharField(max_length=100)
    is_booked=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.bus.bus_name} - Seat {self.seat_number}"