from django.contrib import admin

# Register your models here.
from .models import Event, Role

admin.site.register(Event)
admin.site.register(Role)

class EventsInline(admin.TabularInline):
    model = Event