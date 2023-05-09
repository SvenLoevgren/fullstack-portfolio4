from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    num_seats = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Availability(models.Model):
    date = models.DateField()
    time = models.TimeField()
    max_seats_available = models.PositiveIntegerField()
    num_available_seats = models.PositiveIntegerField()
