from django.db import models


class AbstractInstance(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractCompanyInstance(AbstractInstance):
    class Categories(models.TextChoices):
        FACTORY = 'factory'
        DISTRIBUTOR = 'distributor'
        DEALERSHIP = 'dealership'
        RETAIL_CHAIN = 'retail chain'
        INDIVIDUAL_ENTREPRENEUR = 'individual entrepreneur'

    category = models.CharField(max_length=30, choices=Categories.choices, null=True)
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    debt = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        abstract = True
