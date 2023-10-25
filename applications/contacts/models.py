from django.db import models
from django.conf import settings
from django.db import models
from django_countries.fields import CountryField

from applications.extensions.abstract_models import AbstractInstance


class Contacts(AbstractInstance):
    email = models.EmailField(max_length=254)
    location = models.ForeignKey('contacts.Location', on_delete=models.CASCADE, related_name="locations")


class Location(AbstractInstance):
    country = CountryField()
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    home = models.CharField(max_length=10)
