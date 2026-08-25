from django.db import models

class ProductionStages(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True)
    price = models.PositiveIntegerField()


class DroneModels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True)
    description = models.CharField(null=True)

class Drone(models.Model):
    class Statuses(models.IntegerChoices):
        IN_PROGRESS = 1
        READY = 2
        DEFECTIVE = 3
        SHIPPED = 4

    id = models.AutoField(primary_key=True)
    barcode = models.CharField(unique=True, db_index=True)
    model_id = models.ForeignKey(
        "DroneModels",
        on_delete=models.CASCADE,
        related_name='Drone'
    )
    status = models.IntegerField(choices=Statuses.choices)
    created_at = models.DateTimeField(auto_now_add=True)

class DroneStageLogs(models.Model):
    id = models.AutoField(primary_key=True)
    drone_id = models.ForeignKey(
        "Drone",
        on_delete=models.CASCADE,
        related_name='DroneStageLogs'
    )
    stage_id = models.ForeignKey(
        "ProductionStages",
        on_delete=models.CASCADE,
        related_name='DroneStageLogs'
    )
    worker_id = models.CharField(default='Worker') # Temporarily
    is_defective = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)
