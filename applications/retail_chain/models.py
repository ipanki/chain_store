from django.conf import settings
from django.db import models

from applications.extensions.abstract_models import AbstractInstance
from applications.authentication.models import User


class RetailChain(AbstractInstance):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="retails")
    name = models.CharField(max_length=50)
    contacts = models.ForeignKey(
        "contacts.Contacts", on_delete=models.SET_NULL, related_name="retails_contacts", null=True)
    employees = models.ManyToManyField(
        User, null=True, blank=True, related_name='retails_employees')
    supplier = models.ForeignKey(
        "distributor.Distributor", on_delete=models.SET_NULL, related_name="retails_supplier", null=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, null=True)


class RetailChainProduct(AbstractInstance):
    count = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="retails_products", null=True)
    retail_chain = models.ForeignKey(
        "retail_chain.RetailChain", on_delete=models.CASCADE, related_name="retails", null=True)
