from django.urls import path
from . import views

# Pacific Trails Resort Urls
urlpatterns = [
    path("", views.index, name="index"),
    path("registration", views.registration, name="registration"),
    path("login", views.login, name="login"),
    path("yurts", views.yurts, name="yurts"),
    path("activities", views.activities, name="activities"),
    path("reservations", views.reservations, name="reservations"),
    path("details", views.details, name="details"),
    path('details/<int:reservation_id>/', views.details, name='details'),
]