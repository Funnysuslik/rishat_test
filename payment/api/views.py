import os

import stripe
from django.http.response import HttpResponseRedirect
from rest_framework import viewsets, status
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import ItemSerializer
from items.models import (
    Item,
    # Discount,
    # Tax,
    # Order,
)


class ItemViewSet(RetrieveModelMixin, viewsets.GenericViewSet):
    """"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny,]
    pagination_class = None


class BuyView(APIView):
    """"""

    permission_classes = [AllowAny,]

    def get(self, request, *args, **kwargs):
        stripe.api_key = os.environ.get('STRIPE_TOKEN')
        address = os.environ.get('SERVER_ADDRESS')
        item = Item.objects.get(pk=kwargs.get('item_id'))
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': f'{item.currency}',
                    'product_data': {'name': f'{item.name}'},
                    'unit_amount': item.price,
                },
                'quantity': 1,
                }],
            mode='payment',
            success_url=f'http://{address}/success',
            cancel_url=f'http://{address}/cancel',
        )

        return HttpResponseRedirect(
            session.url,
            status=status.HTTP_303_SEE_OTHER
        )
