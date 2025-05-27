
from django.contrib.auth.models import User  
from django.db import models
from django.contrib import admin 
from django.core.exceptions import ValidationError

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'guests')  
    list_filter = ('date', 'time')  

# Reservation model to store booking information
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    class Meta:
        db_table = "booking_reservation"
        constraints = [
            models.UniqueConstraint(fields=['date', 'time'], name='unique_reservation_slot')
        ]

    def clean(self):
        # Custom validation to catch double bookings
        if Reservation.objects.exclude(pk=self.pk).filter(date=self.date, time=self.time).exists():
            raise ValidationError("This time slot is already booked.")

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"