from django.shortcuts import render
from .forms import EventCreationForm
from .models import Event

# Create your views here.


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