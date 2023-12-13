from django.shortcuts import render
from django.http import HttpResponse

import sendgrid
import os
from sendgrid.helpers.mail import *


# Create your views here.
# Index view
def index(request):
    return render(request, "index.html")


# Yurts view
def yurts(request):
    return render(request, "yurts.html")


# Activities View
def activities(request):
    return render(request, "activities.html")


# Reservations View
def reservations(request):
    return render(request, "reservations.html")


# Details View
def details(request):
    return render(request, "reservationDetails.html")
