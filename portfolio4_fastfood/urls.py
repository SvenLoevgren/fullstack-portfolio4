""" from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.BookingList.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', views.BookingDetail.as_view(), name='booking-detail'),
    path('availability/', views.AvailabilityList.as_view(), name='availability-list'),
    path('availability/<int:pk>/', views.AvailabilityDetail.as_view(), name='availability-detail'),
]
"""
from django.contrib import admin
from fastfood.views import fastfood_home, booking, contactus
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from .models import MyModel
# from .serializers import MyModelSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fastfood_home, name='fastfood_home'),
    path('booking/', booking, name='booking'),
    path('contactus/', contactus, name='contactus'),
]

# path('mymodel/', ListCreateAPIView.as_view(queryset=MyModel.objects.all(), serializer_class=MyModelSerializer)),
# path('mymodel/<int:pk>/', RetrieveUpdateDestroyAPIView.as_view(queryset=MyModel.objects.all(), serializer_class=MyModelSerializer)),
# path('api/', include('fastfood.urls'))
