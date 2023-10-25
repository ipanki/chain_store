from django.db import models

from applications.extensions.abstract_models import AbstractInstance


class Product(AbstractInstance):
    name = models.CharField(max_length=25)
    model = models.CharField(max_length=50)
    launch_date = models.DateField()
