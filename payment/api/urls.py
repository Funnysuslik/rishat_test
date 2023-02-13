from django.urls import path, include
from rest_framework import routers

from .views import (
    ItemViewSet,
    BuyView,
)

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'items', ItemViewSet)

urlpatterns = [
    path(
        'buy/<int:item_id>/',
        BuyView.as_view(),
        name='buy',
    ),
    path('', include(router_v1.urls)),
]
