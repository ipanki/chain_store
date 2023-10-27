from django.db import models
from django.conf import settings
from django_countries.fields import CountryField

from applications.extensions.abstract_models import AbstractInstance, AbstractCompanyInstance


class Company(AbstractCompanyInstance):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="owner")
    name = models.CharField(max_length=50)
    contacts = models.ForeignKey(
        "company.Contacts", on_delete=models.SET_NULL, related_name="companies_contacts", null=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, null=True)


class CompanyProduct(AbstractInstance):
    count = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="company", null=True)
    company = models.ForeignKey(
        "company.Company", on_delete=models.CASCADE, related_name="product", null=True)


class Contacts(AbstractInstance):
    email = models.EmailField(max_length=254)
    location = models.ForeignKey('company.Location', on_delete=models.CASCADE, related_name="locations")


class Location(AbstractInstance):
    country = CountryField()
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    home = models.CharField(max_length=10)


class Employee(AbstractInstance):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name="employee")



