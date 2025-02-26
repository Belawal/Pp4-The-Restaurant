from django import forms
from .models import Reservation

# Connect form directly to the Reservation model
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'time', 'guests']  # Include email for validation

        # Customize widgets for better input fields (date and time pickers)
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # Ensure date picker appears
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),  # Ensure time picker appears
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # Ensure consistent styling
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control'}),
        }
# Simple contact us form
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")