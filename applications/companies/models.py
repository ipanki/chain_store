from django.conf import settings
from django.db import models
from django_countries.fields import CountryField

from applications.extensions.abstract_models import (AbstractCompanyInstance,
                                                     AbstractInstance)


class Company(AbstractCompanyInstance):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="companies")
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    address = models.ForeignKey(
        "companies.Address", on_delete=models.SET_NULL, related_name="companies", null=True)


class CompanyProduct(AbstractInstance):
    count = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="companies_products", null=True)
    company = models.ForeignKey(
        "companies.Company", on_delete=models.CASCADE, related_name="products", null=True)


class Address(AbstractInstance):
    country = CountryField()
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    house = models.CharField(max_length=10)


class Employee(AbstractInstance):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, unique=True)
    company = models.ForeignKey(
        'companies.Company', on_delete=models.CASCADE, related_name="employees", null=True)

    class Meta:
        unique_together = ('email', 'company',)
