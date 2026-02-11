from django.contrib import admin
from .models import bus,seat


class busAdmin(admin.ModelAdmin):
    list_display=['bus_name','bus_number','bus_origin','bus_destination','startDate','endDate','bus_time']

admin.site.register(bus,busAdmin)
admin.site.register(seat)

# Register your models here.
