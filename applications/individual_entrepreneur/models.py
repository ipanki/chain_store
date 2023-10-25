from django.conf import settings
from django.db import models

from applications.extensions.abstract_models import AbstractInstance
from applications.authentication.models import User


class IndividualEntrepreneur(AbstractInstance):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="individual_entrepreneurs")
    name = models.CharField(max_length=50)
    contacts = models.ForeignKey(
        "contacts.Contacts", on_delete=models.SET_NULL, related_name="individual_entrepreneurs_contacts", null=True)
    employees = models.ManyToManyField(
        User, null=True, blank=True, related_name='individual_entrepreneurs_employees')
    supplier = models.ForeignKey(
        "retail_chain.RetailChain", on_delete=models.SET_NULL, related_name="individual_entrepreneurs_supplier", null=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, null=True)


class IndividualEntrepreneurProduct(AbstractInstance):
    count = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="individual_entrepreneurs_products", null=True)
    individual_entrepreneur = models.ForeignKey(
        "individual_entrepreneur.IndividualEntrepreneur", on_delete=models.CASCADE, related_name="individual_entrepreneurs", null=True)
