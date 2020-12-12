from django.conf.urls import url
from .views import (CreateBookingAPIView, DeleteBookingView, BookingListView)

urlpatterns= [
    url('createBooking', CreateBookingAPIView.as_view()),
url('cancelBooking/(?P<pk>.+)', DeleteBookingView.as_view(), name='booking-cancel'),
    url('getBookingList', BookingListView.as_view())
]