from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Booking
from django.contrib import messages
from .forms import BookingForm
from django.http import JsonResponse

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

# <a href="{% url 'your_app_name:booking_list' %}">View Bookings</a>


def fastfood_home(request):
    return render(request, 'fastfood/fastfood_home.html')


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been confirmed, we will contact you via email - or you can contact us if you need to change your booking!')
            return redirect('booking')
    else:
        form = BookingForm()
    return render(request, 'fastfood/booking.html', {'form': form})


def contactus(request):
    return render(request, 'fastfood/contactus.html')
