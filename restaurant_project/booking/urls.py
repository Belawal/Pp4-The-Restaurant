from django.urls import path  # Import path for URL mapping
from . import views  # Import views from current app

urlpatterns = [
    path("", views.home, name="home"),  # Route for homepage
    path("signup/", views.signup, name="signup"),  # Route for user signup
    path("login/", views.login_view, name="login"),  # Route for user login
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('reservation/', views.reservation_view, name='reservation'),  # Route for reservation form


# Admin and user reservation management
    path("admin/reservations/", views.admin_reservations, name="admin_reservations"),  # Admin reservation view
    path("admin/reservations/cancel/<int:reservation_id>/", views.cancel_reservation, name="cancel_reservation"),  # Admin cancel
    path("my-reservations/", views.user_reservations, name="user_reservations"),  # User reservation view
    path("my-reservations/cancel/<int:reservation_id>/", views.user_cancel_reservation, name="user_cancel_reservation"),  # User cancel
]