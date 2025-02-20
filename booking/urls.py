from django.urls import path
from booking.views import home  # Import home function directly

urlpatterns = [
    path('', home, name='home'),  # Homepage URL
]