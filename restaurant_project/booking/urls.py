from django.urls import path # Import path for URL mapping
from . import views  # Import views from current app

urlpatterns = [
    path("", views.home, name="home"),  # Route for homepage
    path("signup/", views.signup, name="signup"),  # Route for user signup
    path("login/", views.login_view, name="login"),  # Route for user login
    path('logout/', views.logout_view, name='logout'),  # Logout page
]