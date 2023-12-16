from django.shortcuts import render, redirect
from django.http import HttpResponse
import sendgrid
import os
from sendgrid.helpers.mail import *
from sendgrid import SendGridAPIClient
from .models import User, Reservation
from django.utils.dateparse import parse_date
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout


# Create your views here.
# Index view
@login_required(login_url="login")
def index(request):
    return render(request, "index.html")


# Registration view
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #  log the user in
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, "registration.html", {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("index")


# Yurts view
def yurts(request):
    return render(request, "yurts.html")


# Activities View
def activities(request):
    return render(request, "activities.html")


# Reservations View
def reservations(request):

    if request.method == 'POST':
        # Extracting form data
        first_name = request.POST.get('myFName')
        last_name = request.POST.get('myLName')
        email = request.POST.get('myEmail')
        phone_number = request.POST.get('myPhone')
        arrival_date = parse_date(request.POST.get('myDate'))
        nights = int(request.POST.get('myNights'))
        comments = request.POST.get('myComments')

        # Create Reservation instance
        reservation = Reservation(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            arrival_date=arrival_date,
            nights=nights,
            comments=comments
        )
        reservation.save()  # Save the reservation to the database

        # Create User instance and link it to the reservation
        user = User(
            user_firstname=first_name,
            user_lastname=last_name,
            user_email=email,
            reservation=reservation
        )
        user.save()  # Save the user to the database

        email_content = f"""
                <strong>Your reservation has been confirmed.</strong><br><br>
                Here are your reservation details:<br>
                Name: {first_name} {last_name}<br>
                Email: {email}<br>
                Phone: {phone_number}<br>
                Arrival Date: {arrival_date}<br>
                Nights: {nights}<br>
                Comments: {comments}
                """
        try:
            message = Mail(
                from_email='ndhage64.work@gmail.com',
                to_emails=email,
                subject='Pacific Trails Resort Reservation Confirmation for ' + first_name + last_name,
                html_content=email_content)
            sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

        reservation.save()
        return redirect('details', reservation_id=reservation.reservation_id)

    return render(request, "reservations.html")


# Details View
def details(request, reservation_id):
    reservation = Reservation.objects.get(reservation_id=reservation_id)
    return render(request, "reservationDetails.html", {'reservation': reservation})
