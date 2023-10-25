from django.conf import settings
from django.db import models

from applications.extensions.abstract_models import AbstractInstance
from applications.authentication.models import User


class Distributor(AbstractInstance):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="distributors")
    name = models.CharField(max_length=50)
    contacts = models.ForeignKey(
        "contacts.Contacts", on_delete=models.SET_NULL, related_name="distributors_contacts", null=True)
    employees = models.ManyToManyField(
        User, null=True, blank=True, related_name='distributors_employees')
    supplier = models.ForeignKey(
        "factory.Factory", on_delete=models.SET_NULL, related_name="distributors_supplier", null=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, null=True)


class DistributorProduct(AbstractInstance):
    count = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="distributors_products", null=True)
    distributor = models.ForeignKey(
        "distributor.Distributor", on_delete=models.CASCADE, related_name="distributors_products", null=True)