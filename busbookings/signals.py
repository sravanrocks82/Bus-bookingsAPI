from django.db.models.signals import post_save  
from django.dispatch import receiver
from .models import bus, seat

@receiver(post_save, sender=bus)
def create_seats(sender, instance, created, **kwargs):
    if created:
        for i in range(1, instance.total_seats + 1):
            seat.objects.create(bus=instance, seat_number=str(i))   