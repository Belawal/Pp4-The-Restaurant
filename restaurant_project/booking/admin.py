from django.contrib import admin
from .models import Reservation  # Importing the Reservation model

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    # Display these fields in the admin model list view
    list_display = ('name', 'email', 'date', 'time', 'guests')

    # Enable search functionality on these fields
    search_fields = ('name', 'email')

    # Add filter options for easier navigation
    list_filter = ('date', 'guests')