from django.shortcuts import render, redirect, get_object_or_404  # Import functions for rendering and redirecting, and fetching objects
from django.contrib.auth import login, authenticate, logout  # Import login, authenticate, logout functions
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Import Django forms
from django.contrib.auth.decorators import login_required, user_passes_test  # Import decorators for access control
from .models import Reservation  # Import Reservation model
from .forms import ReservationForm  # Import ReservationForm from forms
from .forms import ContactForm # Import ContactForm from forms
from django.contrib import messages  # Import for flash messages

def menu(request):
    """Displays the restaurant menu."""
    menu_items = [
        {"name": "Margherita Pizza", "description": "Classic pizza with fresh mozzarella and basil.", "price": 12.99},
        {"name": "Spaghetti Carbonara", "description": "Traditional pasta with eggs, cheese, pancetta, and pepper.", "price": 14.99},
        {"name": "Caesar Salad", "description": "Crisp romaine lettuce with Caesar dressing and croutons.", "price": 9.99},
        {"name": "Grilled Salmon", "description": "Fresh salmon fillet with a lemon butter sauce.", "price": 18.99},
    ]
    return render(request, 'booking/menu.html', {"menu_items": menu_items})  # Render the menu page

def home(request):
    return render(request, 'booking/home.html')  # Renders the homepage

def signup(request):
    """Handles user signup process"""
    if request.method == "POST":  # Check if form is submitted
        form = UserCreationForm(request.POST)  # Get form data
        if form.is_valid():  # Validate form
            user = form.save()  # Save new user
            login(request, user)  # Log in new user
            return redirect("home")  # Redirect to home page
    else:
        form = UserCreationForm()  # Create empty signup form
    return render(request, "booking/signup.html", {"form": form})  # Render signup page

def login_view(request):
    """Handles user login process"""
    if request.method == "POST":  # Check if form is submitted
        form = AuthenticationForm(data=request.POST)  # Get login form data
        if form.is_valid():  # Validate form
            user = form.get_user()  # Get authenticated user
            login(request, user)  # Log in the user
            return redirect("home")  # Redirect to home page
    else:
        form = AuthenticationForm()  # Create empty login form
    return render(request, "booking/login.html", {"form": form})  # Render login page

def logout_view(request):
    """Handles user logout process"""
    logout(request)  # Log out the current user
    return redirect('home')  # Redirect to home page

@login_required  # Ensures only logged-in users can book
def reservation_view(request):
    """Handles reservation form submission"""
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect("home")
    else:
        form = ReservationForm()
    return render(request, "booking/reservation.html", {"form": form})

def is_admin(user):
    return user.is_staff

# Admin view: Show all reservations
@login_required
@user_passes_test(is_admin)
def admin_reservations(request):
    reservations = Reservation.objects.all()  # Get all reservations
    return render(request, 'booking/admin_reservations.html', {'reservations': reservations})

# Admin view: Cancel a reservation
@login_required
@user_passes_test(is_admin)
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()  # Delete the booking
    return redirect('admin_reservations')

# User view: Show their own bookings
@login_required
def user_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)  # Get current user's bookings
    return render(request, 'booking/user_reservations.html', {'reservations': reservations})

# User view: Cancel their own booking
@login_required
def user_cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    reservation.delete()  # Delete the user's booking
    return redirect('user_reservations')

def contact(request):
    """Handles the contact form submission."""
    if request.method == "POST":
        form = ContactForm(request.POST)  # Get form data
        if form.is_valid():  # Validate form
            # For now, we only show a success message—no email sending
            return render(request, 'booking/contact_success.html')
    else:
        form = ContactForm()  # Display empty form
    return render(request, 'booking/contact.html', {"form": form})  # Render contact page

@login_required
def reservation_view(request):
    """Handles reservation form submission with user authentication"""
    if not request.user.is_authenticated:
        messages.info(request, "Please log in to book a reservation.")  # Show login message
        return redirect('login')  # Redirect to login page

    if request.method == "POST":  # Check if form is submitted
        form = ReservationForm(request.POST)  # Get reservation form data
        if form.is_valid():  # Validate form
            # Ensure reservation email matches logged-in user's email
            if form.cleaned_data['email'] != request.user.email:
                form.add_error('email', 'Email must match your signup email.')
            else:
                reservation = Reservation(
                    user=request.user,
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    date=form.cleaned_data['date'],
                    time=form.cleaned_data['time'],
                    guests=form.cleaned_data['guests']
                )
                reservation.save()  # Save the reservation
                return redirect("user_reservations")
    else:
        form = ReservationForm()  # Create an empty form

    return render(request, "booking/reservation.html", {"form": form})
