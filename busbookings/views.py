from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Bus, Seat
from .serializers import busSerializer, seatSerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = busSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


from django.db import transaction
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = seatSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def book(self, request, pk=None):
        with transaction.atomic():
            seat = Seat.objects.select_for_update().get(pk=pk)
            bus = seat.bus

            if seat.is_booked:
                return Response(
                    {
                        "error": f"Seat {seat.seat_number} on {bus.bus_name} is already booked"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Mark seat booked
            seat.is_booked = True
            seat.booked_by = request.user
            seat.save()


            if bus.available_seats > 0:
                bus.available_seats -= 1
                bus.save()

            return Response(
                {
                    "message": f"Seat {seat.seat_number} successfully booked on {bus.bus_name}",
                    "bus_name": bus.bus_name,
                    "seat_number": seat.seat_number,
                    "remaining_seats": bus.available_seats
                },
                status=status.HTTP_200_OK
            )