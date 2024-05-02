from django.shortcuts import render
from .models import Event
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')


def events(request):
    # Generate counts of some of the main objects
    num_events = Event.objects.all().count()

    context = {
        'num_events': num_events
    }
    return render(request, 'events.html', context=context)


class EventsView(generic.ListView):
    """Generic class-based view for a list of events."""
    model = Event
    paginate_by = 10