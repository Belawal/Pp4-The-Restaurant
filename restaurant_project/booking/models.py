from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)  # Customer's name
    email = models.EmailField()  # Customer's email
    phone = models.CharField(max_length=15)  # Phone number
    date = models.DateField()  # Booking date
    time = models.TimeField()  # Booking time
    guests = models.PositiveIntegerField()  # Number of guests
    special_requests = models.TextField(blank=True, null=True)  # Optional requests

    def __str__(self): 
        return f"Booking for {self.name} on {self.date} at {self.time}"