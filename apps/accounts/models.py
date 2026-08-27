from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Roles(models.IntegerChoices):
        ADMIN = 1,
        MANAGER = 2,
        WORKER = 3

    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=20, blank=True)
    role = models.IntegerField(choices=Roles.choices)
    created_at = models.DateTimeField(auto_now_add=True)
