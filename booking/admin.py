from django.contrib import admin
from .models import Reservation  # Importing the Reservation model


@admin.register(Reservation) # Register your models here.
class ReservationAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'email', 'date', 'time', 'guests') # Display these fields in the admin model list view

    search_fields = ('name', 'email')  # Enable search functionality on these fields

    list_filter = ('date', 'guests')  # Add filter options for easier navigation