from django.contrib import admin
from .views import fastfood_home, booking, contactus, booking_list, edit_booking, delete_booking, booking_update
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from .views import BookingCreateView, BookingUpdateView, BookingDeleteView, BookingListView

app_name = 'fastfood'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fastfood_home, name='fastfood_home'),
    path('accounts/', include('allauth.urls')),
    path('booking/', booking, name='booking'),
    path('bookings/', booking_list, name='bookings'),
    path('edit_booking/<int:booking_id>/', edit_booking, name='edit_booking'),
    path('edit_booking/', include([
        path('list/', BookingListView.as_view(), name='booking_list'),
        path('new/', BookingCreateView.as_view(), name='booking_new'),
        path('<int:pk>/edit/', BookingUpdateView.as_view(), name='booking_edit'),
        path('<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
    ])),
    path('contactus/', contactus, name='contactus'),
    path('delete_booking/', delete_booking, name='delete_booking'),
    path('update_booking/', booking_update, name='update_booking'),
]
