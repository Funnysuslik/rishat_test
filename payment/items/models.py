from django.db import models
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    RegexValidator,
)


class Item(models.Model):
    """representation of items table."""

    name = models.CharField(
        max_length=20,
    )
    slug = models.SlugField(
        max_length=200,
        validators=[
            RegexValidator('^[-a-zA-Z0-9_]+$'),
        ],
        unique=True,
    )
    description = models.TextField()
    price = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(999),
        ],
    )
    currency = models.CharField(
        max_length=20,
    )


class Discount(models.Model):
    """"""
    amount = models.IntegerField()


class Tax(models.Model):
    """"""
    percents = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(99),
        ],
    )


class Order(models.Model):
    """Representation of oreders table."""

    items = models.ManyToManyField(
        Item,
        related_name='orders',
    )
    discount = models.ForeignKey(
        Discount,
        related_name='orders',
        on_delete=models.CASCADE,
    )
    taxs = models.ForeignKey(
        Tax,
        related_name='orders',
        on_delete=models.CASCADE,
    )
