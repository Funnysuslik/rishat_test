from django.urls import path

from . import views

app_name = 'items'

urlpatterns = [
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('', views.index, name='index'),
]
