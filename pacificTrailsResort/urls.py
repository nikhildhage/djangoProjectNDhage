from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("yurts", views.yurts, name="yurts"),
    path("activities", views.activities, name="activities"),
    path("reservations", views.reservations, name="reservations"),
    path("details", views.details, name="details"),
]