from django.contrib import admin
from .models import Manufacturer, Fuel, Vehicle

admin.site.register(Manufacturer)
admin.site.register(Fuel)
admin.site.register(Vehicle)