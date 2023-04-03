from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Booking

class BookingCreateView(CreateView):
    model = Booking
    fields = ['customer_name', 'email', 'phone_number', 'date', 'time', 'num_seats']
    success_url = reverse_lazy('booking_list')

class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['customer_name', 'email', 'phone_number', 'date', 'time', 'num_seats']
    success_url = reverse_lazy('booking_list')

class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy('booking_list')

class BookingListView(ListView):
    model = Booking


def fastfood_home(request):
    return render(request, 'fastfood/fastfood_home.html')


def booking(request):
    return render(request, 'fastfood/booking.html')


def contactus(request):
    return render(request, 'fastfood/contactus.html')
