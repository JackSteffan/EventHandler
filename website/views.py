from django.shortcuts import render
from .models import Event, Role
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def events(request):
    # Generate counts of some of the main objects
    num_events = Event.objects.all().count()

    context = {
        'num_events': num_events
    }
    return render(request, 'events.html', context=context)

class EventsView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view for a list of events."""
    def get(self, request):
        event = Event.objects.all()
        role = Role.objects.all()
        # Process data as needed
        context = {
            'events': event,
            'roles': role,
        }
        return render(request, 'website/event_list.html', context)
    

class HomeView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view for a list of events."""
    def get(self, request):
        event = Event.objects.all()
        role = Role.objects.all()
        # Process data as needed
        context = {
            'events': event,
            'roles': role,
        }
        return render(request, 'home.html', context)