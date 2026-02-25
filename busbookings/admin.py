from django.contrib import admin
from .models import Bus,Seat


class busAdmin(admin.ModelAdmin):
    list_display=['bus_name','bus_number','bus_origin','bus_destination','startDate','endDate','bus_time']

admin.site.register(Bus,busAdmin)
admin.site.register(Seat)

# Register your models here.
