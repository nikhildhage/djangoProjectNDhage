from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    reservation = models.ForeignKey('Reservation', on_delete=models.SET_NULL, null=True)


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    arrival_date = models.DateField()
    nights = models.IntegerField()
    comments = models.TextField(null=True, blank=True)
