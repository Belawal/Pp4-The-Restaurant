from django.shortcuts import render, redirect  # Import functions for rendering and redirecting
from django.contrib.auth import login, authenticate  # Import auth functions
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Import Django forms

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
    return render(request, "signup.html", {"form": form})  # Render signup page

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
    return render(request, "login.html", {"form": form})  # Render login page