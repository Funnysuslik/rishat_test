from django.contrib import admin

from .models import (
    Item,
    Discount,
    Tax,
    Order,
)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'slug',
        'description',
        'price',
        'currency'
    )


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'amount',
    )


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'percents',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
    )
