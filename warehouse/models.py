from django.db import models
from django.core.validators import MinValueValidator


class Part(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    description = models.CharField(
        max_length=500, 
        blank=True, 
        null=True
    )
    
class StockOperation(models.Model):
    class Operations(models.IntegerChoices):
        IN = 1
        OUT = 2
        WRITE_OFF = 3

    id = models.AutoField(primary_key=True)
    part = models.ForeignKey(
        'Part',
        on_delete=models.CASCADE,
        related_name='stockoperation'
    )
    operation_type = models.IntegerField(
        choices=Operations.choices
    )
    quantity = models.PositiveIntegerField()
    performed_by = models.CharField(default='Admin') # Temporarily
    recipient = models.CharField(default='User') # Temporarily
    created_at = models.DateTimeField(auto_now_add=True)
