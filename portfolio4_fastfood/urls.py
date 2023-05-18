from django.contrib import admin
from fastfood.views import fastfood_home, booking, contactus
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from fastfood.views import BookingCreateView, BookingUpdateView, BookingDeleteView, BookingListView

app_name = 'fastfood'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fastfood_home, name='fastfood_home'),
    path('accounts/', include('allauth.urls')),
    path('booking/', booking, name='booking'),
    path('booking/', include('fastfood.urls')),
    path('edit_booking/', include('fastfood.urls')),
    path('contactus/', contactus, name='contactus'),
]
