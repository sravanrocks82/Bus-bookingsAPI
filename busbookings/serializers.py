from rest_framework import serializers
from .models import Bus, Seat




# class loginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=login
#         fields='__all__'
# class registerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=register
#         fields='__all__'
class busSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields='__all__'
class seatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seat
        fields='__all__'
