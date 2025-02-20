from django.urls import path
from booking import views

urlpatterns = [
    path('', home, name='home'),  # Homepage URL
]