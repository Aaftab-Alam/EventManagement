from django.shortcuts import render
from django.http import HttpResponse
from .models import Tickets

# Create your views here.

def bookTicket(request, eventId):
    ticket= Tickets(
        eventId=eventId,
        bookedBy=request.session.get('id')
    )
    ticket.save()
    return HttpResponse(eventId)