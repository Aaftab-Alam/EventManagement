from django.shortcuts import render, redirect
from .forms import EventCreationForm
from .models import Event
from users.is_loggedin import login_required
from django.http import HttpResponse


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            event = Event(
                name=form.cleaned_data['name'],
                date=form.cleaned_data['date'],
                location=form.cleaned_data['location'],
                time=form.cleaned_data['time'],
                description=form.cleaned_data['description']
            )
            event.save()
            return render(request, 'success.html')  # Display a success page
    else:
        form = EventCreationForm()
    return render(request, 'create_event.html', {'form': form})


def display_events(request):
    events_list = Event.objects.all()
    return render(request, 'display_events.html', {'events_list': events_list})
