from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from applications.extensions.abstract_models import AbstractInstance


def validate_date(value):
    if value and value > timezone.now().date():
        raise ValidationError('Дату выхода продукта на рынок нельзя указывать в будущем')


class Product(AbstractInstance):
    name = models.CharField(max_length=25)
    model = models.CharField(max_length=50)
    launch_date = models.DateField(validators=[validate_date])
