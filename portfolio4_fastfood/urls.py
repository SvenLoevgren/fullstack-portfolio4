from django.contrib import admin
from fastfood.views import fastfood_home, booking, contactus
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from fastfood.views import BookingCreateView, BookingUpdateView, BookingDeleteView, BookingListView

app_name = 'fastfood'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fastfood_home, name='fastfood_home'),
    path('booking/', booking, name='booking'),
    path('booking/', include([
        path('', BookingListView.as_view(), name='booking_list'),
        path('new/', BookingCreateView.as_view(), name='booking_new'),
        path('<int:pk>/edit/', BookingUpdateView.as_view(), name='booking_edit'),
        path('<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
    ])),
    path('contactus/', contactus, name='contactus'),
]
