from django.conf import settings
from django.db import models

from applications.extensions.abstract_models import AbstractInstance
from applications.authentication.models import User


class Factory(AbstractInstance):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="factories")
    name = models.CharField(max_length=50)
    contacts = models.ForeignKey(
        "contacts.Contacts", on_delete=models.SET_NULL, related_name="factories_contacts", null=True)
    employees = models.ManyToManyField(
        User, null=True, blank=True, related_name='factory_employees')


class FactoryProduct(AbstractInstance):
    count = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="products_in_stock", null=True)
    factory = models.ForeignKey(
        "factory.Factory", on_delete=models.CASCADE, related_name="factories_products", null=True)
