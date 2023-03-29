from django.shortcuts import render
# from rest_framework import generics
# from .models import Booking, Availability
# from .serializers import BookingSerializer, AvailabilitySerializer

"""
class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class AvailabilityList(generics.ListCreateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

class AvailabilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

"""

# Create your views here.


def fastfood_home(request):
    return render(request, 'fastfood/fastfood_home.html')


def booking(request):
    return render(request, 'fastfood/booking.html')


def contactus(request):
    return render(request, 'fastfood/contactus.html')
