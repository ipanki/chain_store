from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        USER = 'user'
        ADMIN = 'admin'
        FACTORY_MANAGER = 'factory_manager'
        DISTRIBUTOR = 'distributor'
        DEALERSHIP = 'dealership'
        RETAIL_CHAIN_MANAGER = 'retail chain manager'
        INDIVIDUAL_ENTREPRENEUR = 'individual entrepreneur'

    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(
        max_length=30, choices=Roles.choices, default=Roles.USER)
    title = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.username
