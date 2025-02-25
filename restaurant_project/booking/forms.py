from django import forms
from .models import Reservation

# Connect form directly to the Reservation model
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'time', 'guests']  # Include email for validation

    # Customize widgets for better input fields (date and time pickers)
    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),  # Date picker
        'time': forms.TimeInput(attrs={'type': 'time'}),  # Time picker
    }