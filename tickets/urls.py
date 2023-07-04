from django.urls import path
from tickets import views


urlpatterns = [
    path('bookingId-<slug:eventId>/', views.bookTicket, name="bookTicket"),
]