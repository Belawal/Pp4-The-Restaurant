from django.urls import path  # Import path for URL mapping
from . import views  # Import views from current app
from .views import login_view #Import login_view from 

urlpatterns = [
    path("", views.home, name="home"),  # Route for homepage
    path("signup/", views.signup, name="signup"),  # Route for user signup
    path("login/", views.login_view, name="login"),  # Route for user login
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path("reservation/", views.reservation_view, name="reservation"),  # Route for reservation form
    path("admin/reservations/", views.admin_reservations, name="admin_reservations"),  # Admin reservation view
    path("admin/reservations/cancel/<int:reservation_id>/", views.cancel_reservation, name="cancel_reservation"),  # Admin cancel
    path("my-reservations/", views.user_reservations, name="user_reservations"),  # User reservation view
    path("my-reservations/cancel/<int:reservation_id>/", views.user_cancel_reservation, name="user_cancel_reservation"),  # User cancel
    path("menu/", views.menu, name="menu"),  # Route for the menu page
    path("contact/", views.contact, name="contact"),  # Route for the contact page
]