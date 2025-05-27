from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path("reservation/", views.reservation_view, name="reservation"),
    path("admin/reservations/", views.admin_reservations, name="admin_reservations"),
    path("admin/reservations/cancel/<int:reservation_id>/", views.cancel_reservation, name="cancel_reservation"),
    path("my-reservations/", views.user_reservations, name="user_reservations"),
    path("my-reservations/cancel/<int:reservation_id>/", views.user_cancel_reservation, name="user_cancel_reservation"),
    path("menu/", views.menu, name="menu"),
    path("contact/", views.contact, name="contact"),
]