from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *
from users.models import *

@login_required
def eventRegister(request, eventId):
    user = request.user

    try:
        eventName = Event.objects.get(id=eventId).title
        reg = EventRegistration.objects.get(idnos=user.username)
        reg.reg_events += ','+eventName
        reg.save()
    except:
        reg = EventRegistration.objects.create(idnos=user.username, reg_events=eventName)
    return redirect('home')

def eventRegisterMany(request, users_cnt, eventId):
    usernames = []
    error = None
    for cnt in range(1,users_cnt+1):
        try:
            uname = request.POST.get("user_1",'')
            print("=======================",uname)
            if uname is '':
                continue
            print("=======================",uname)
            usr = User.objects.get(username=uname)
            usernames.append(uname)
        except:
            error = f'------>User-{uname} not listed in the DB.'
            break

    if error is None and len(usernames)!=0:
        usernames = sorted(usernames)
        usernames = ','.join(usernames)
        try:
            eventName = Event.objects.get(id=eventId).title
            reg = EventRegistration.objects.get(idnos=usernames)
            reg.reg_events += ','+eventName
            reg.save()
            print('saved successfully')
        except:
            print('------------------>error')
            reg = EventRegistration.objects.create(idnos=usernames, reg_events=eventName)
            print('saved successfully')
        return redirect('home')
    return redirect('home')
