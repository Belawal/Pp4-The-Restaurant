from django import forms
from .models import Reservation

# Connect form directly to the Reservation model
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'date', 'time', 'guests']  # Removed 'email' to auto-fill it

    # Customize widgets for better input fields
    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),  # Date picker
        'time': forms.TimeInput(attrs={'type': 'time'}),  # Time picker
    }
