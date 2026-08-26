from django.contrib import admin
from .models import Drone, DroneModels, DroneStageLogs, ProductionStages

admin.site.register(DroneModels)
admin.site.register(Drone)
admin.site.register(DroneStageLogs)
admin.site.register(ProductionStages)