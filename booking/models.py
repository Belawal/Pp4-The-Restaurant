# models.py

from django.contrib.auth.models import User  # Import User model for linking reservations to users
from django.db import models  # Import Django's model class

# Reservation model to store booking information
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Links booking to a user
    name = models.CharField(max_length=100)  # Stores guest's name
    email = models.EmailField()  # Stores guest's email
    date = models.DateField()  # Stores booking date
    time = models.TimeField()  # Stores booking time
    guests = models.IntegerField()  # Number of guests

    class Meta:  
        db_table = "booking_reservation"  # Set custom database table name

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"  # Human-readable representation of the reservation

    # Method to check for double bookings
    # @classmethod
    # def is_double_booking(cls, date, time):
    #     return cls.objects.filter(date=date, time=time).exists()  # Returns True if booking exists

# Admin view to manage reservations
from django.contrib import admin  # Import Django's admin interface

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'guests')  # Show these fields in admin panel
    list_filter = ('date', 'time')  # Filter by date and time for easy viewing
