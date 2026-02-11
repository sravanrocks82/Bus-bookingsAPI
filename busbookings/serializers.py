from rest_framework import serializers
from bookings.busbookings.models import bus, login, register, seat




class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model=login
        fields='__all__'
class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model=register
        fields='__all__'
class busSerializer(serializers.ModelSerializer):
    class Meta:
        model=bus
        fields='__all__'
class seatSerializer(serializers.ModelSerializer):
    class Meta:
        model=seat
        fields='__all__'
