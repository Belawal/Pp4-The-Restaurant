from django import forms  # Import Django forms

class ReservationForm(forms.Form):  # Create a form for reservations
    name = forms.CharField(max_length=100, label='Your Name')  # Field for user's name
    email = forms.EmailField(label='Your Email')  # Field for user's email
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Reservation Date')  # Field for date
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label='Reservation Time')  # Field for time
    guests = forms.IntegerField(min_value=1, label='Number of Guests')  # Field for number of guests
