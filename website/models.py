import uuid
from django.conf import settings
from django.db import models

# Create your models here.
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

class Event(models.Model):
    """Model representing an event"""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter an event name"
    )

    date = models.DateTimeField(null=True, blank=True)

    description = models.TextField(
        max_length=1000, help_text="Enter a brief description of the event")
    
    public = models.BooleanField(help_text= "Make this event public or private to members")

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular event instance."""
        return reverse('event-detail', args=[str(self.id)])
    
class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text= "Unique ID for this role")

    event = models.ForeignKey('Event', on_delete=models.RESTRICT, null=True)

    name = models.CharField(max_length=200)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        return reverse('role-detail', args=[str(self.id)])