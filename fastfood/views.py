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


def fastfood_home(request):
    return render(request, 'fastfood/fastfood_home.html')


def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        return JsonResponse({'success': True})
    else:
        return render(request, 'fastfood/booking.html')

"""
def booking(request):
    return render(request, 'fastfood/booking.html')

-------------------------------
from django.shortcuts import render
from django.http import JsonResponse

def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Here you could add any additional validation or processing of the form data
        # For example, checking if the user is allowed to make a booking based on their account status.

        # Once the form data has been validated and processed, you can return a JSON response indicating success.
        return JsonResponse({'success': True})
    else:
        return render(request, 'booking.html')
"""


def contactus(request):
    return render(request, 'fastfood/contactus.html')
