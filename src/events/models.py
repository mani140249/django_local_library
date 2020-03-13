from django.db import models
from django.contrib.auth.models import User

event_types = [('technical','TECHNICAL'), ('non-technical','NON-TECHNICAL')]
class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=50, blank=True)
    cover = models.ImageField(upload_to='event_covers/', default='event_covers/default.jpg')
    category = models.CharField(max_length=20, choices=event_types)
    rules = models.TextField()
    no_of_participants = models.IntegerField()
    organizers = models.TextField()
    winners = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title}'

class EventRegistration(models.Model):
    idnos = models.CharField(max_length=100)
    reg_events = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
