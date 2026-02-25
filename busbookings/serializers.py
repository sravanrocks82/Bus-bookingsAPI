from rest_framework import serializers
from .models import Bus, Seat
from django.contrib.auth.models import User



# class loginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=login
#         fields='__all__'
# class registerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=register
#         fields='__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
class busSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields='__all__'
class seatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seat
        fields='__all__'
