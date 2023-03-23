from django.contrib import admin

# Register your models here.
"""
travel/admin.py
"""

from django.contrib import admin
from .models import Traveler, TravelAgent, Destination, Blog, Hotel, Event, Gallery,Package

admin.site.register(Traveler)
admin.site.register(TravelAgent)
admin.site.register(Destination)
admin.site.register(Blog)
admin.site.register(Hotel)
admin.site.register(Gallery)
admin.site.register(Package)
admin.site.register(Event)
