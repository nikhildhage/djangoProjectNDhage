from django.shortcuts import render
from django.http import HttpResponse
import sendgrid
import os
from sendgrid.helpers.mail import *
from sendgrid import SendGridAPIClient


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
    print("nothing")
    if request.method == 'POST':
        message = Mail(
            from_email='nikhil.dhage@gmail.com',
            to_emails='shivba.d@gmail.com',
            subject='Pacific Trails Resort',
            html_content='<strong>Hello from Pacific Trails Resort</strong>')
        try:
            sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

    return render(request, "reservations.html")


# Details View
def details(request):
    return render(request, "reservationDetails.html")
