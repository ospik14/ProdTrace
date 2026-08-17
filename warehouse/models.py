from django.db import models
from django.core.validators import MinValueValidator

class Part(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(
        max_length=500, 
        blank=True, 
        null=True
    )
    


