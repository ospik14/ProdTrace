from django.db import models

class User(models.Model):
    class Roles(models.IntegerChoices):
        ADMIN = 1,
        MANAGER = 2,
        WORKER = 3

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField()
    full_name = models.CharField(unique=True)
    role = models.IntegerField(choices=Roles.choices)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
