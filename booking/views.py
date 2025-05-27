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
    return render(request, 'booking/menu.html', {"menu_items": menu_items})

def home(request):
    return render(request, 'booking/home.html')

def signup(request):
    """Handles user signup process"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "booking/signup.html", {"form": form})

def login_view(request):
    """Handles user login process"""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "booking/login.html", {"form": form})

def logout_view(request):
    """Handles user logout process"""
    logout(request)
    return redirect('home')

@login_required
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


@login_required
@user_passes_test(is_admin)
def admin_reservations(request):
    reservations = Reservation.objects.all() 
    return render(request, 'booking/admin_reservations.html', {'reservations': reservations})


@login_required
@user_passes_test(is_admin)
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()  # Delete the booking
    return redirect('admin_reservations')

@login_required
def user_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'booking/user_reservations.html', {'reservations': reservations})

@login_required
def user_cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    reservation.delete()
    return redirect('user_reservations')

def contact(request):
    """Handles the contact form submission."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'booking/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'booking/contact.html', {"form": form})
@login_required
def reservation_view(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            
            if Reservation.objects.filter(date=date, time=time).exists():
                form.add_error(None, "This time slot is already booked.")
            else:
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.name = request.user.get_full_name() or request.user.username
                reservation.save()
                messages.success(request, "Reservation successfully booked!")
                return redirect("user_reservations")
    else:
        # Pre-fill name if available
        initial = {'name': request.user.get_full_name()}
        form = ReservationForm(initial=initial)
    
    return render(request, "booking/reservation.html", {"form": form})
