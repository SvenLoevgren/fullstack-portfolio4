from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['customer_name', 'email', 'phone_number', 'date', 'time', 'num_seats', 'user']
    success_url = reverse_lazy('booking_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = ['customer_name', 'email', 'phone_number', 'date', 'time', 'num_seats', 'user']
    success_url = reverse_lazy('booking_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    success_url = reverse_lazy('delete_booking')
    template_name = 'fastfood/booking_confirm_delete.html'


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'fastfood/booking_list.html'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


def fastfood_home(request):
    return render(request, 'fastfood/fastfood_home.html')


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been confirmed, we will contact you via email!')
            return redirect('booking')
    else:
        form = BookingForm()
    return render(request, 'fastfood/booking.html', {'form': form})


def contactus(request):
    return render(request, 'fastfood/contactus.html')


def delete_booking(request):
    return render(request, 'fastfood/delete_booking.html')


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    context = {
        'booking_id': booking_id,
        'booking': booking
    }
    return render(request, 'fastfood/edit_booking.html', context)


def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    context = {'bookings': bookings}
    return render(request, 'fastfood/booking_list.html', context)