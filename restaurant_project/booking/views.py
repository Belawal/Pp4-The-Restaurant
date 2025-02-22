from django.shortcuts import render, redirect  # Import functions for rendering and redirecting
from django.contrib.auth import login, authenticate, logout  # Import login, authenticate, logout functions
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Import Django forms
from .forms import ReservationForm  # Import ReservationForm from forms


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

def reservation_view(request):
    """Handles reservation form submission"""
    if request.method == "POST":  # Check if form is submitted
        form = ReservationForm(request.POST)  # Get form data
        if form.is_valid():  # Validate form
            # Process reservation (save to database or send email - add later)
            return redirect("home")  # Redirect to home page after reservation
    else:
        form = ReservationForm()  # Create empty reservation form
    return render(request, "booking/reservation.html", {"form": form})  # Render reservation page