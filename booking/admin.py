from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'email', 'date', 'time', 'guests')
    search_fields = ('name', 'email')

    list_filter = ('date', 'guests', 'time')