from django.contrib import admin
from .models import Drone, DroneModels

admin.site.register(DroneModels)
admin.site.register(Drone)