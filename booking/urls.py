from django.urls import path
from .view import home

urlpatterns = [
    path('', views.home, name='home'), #Homepage
]