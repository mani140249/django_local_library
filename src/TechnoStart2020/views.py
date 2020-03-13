from django.shortcuts import render, redirect

from notices.models import *
from events.models import *

def home(request):
    notices = Notice.objects.all().order_by('-date_created')
    reg_events = []
    user = request.user
    if user.is_authenticated:
        reg_events = getRegEventsIds(user)
        # print(reg_events,"===========")
    tech_events = Event.objects.filter(category="technical")
    non_tech_events = Event.objects.filter(category="non-technical")
    context = {
        'notices':notices,
        'tech_events':tech_events,
        'non_tech_events':non_tech_events,
        'reg_events':reg_events,

        }
    return render(request, 'index.html', context)


def getRegEventsIds(user):
    raw_reg_events = list(EventRegistration.objects.filter(idnos__contains=user.username).values_list('reg_events', flat=True))
    reg_events = []
    for event in raw_reg_events:
        if ',' in event:
            lst = event.split(',')
            for eve in lst:
                reg_events.append(eve.strip())
            continue
        reg_events.append(event.strip())
    return reg_events
