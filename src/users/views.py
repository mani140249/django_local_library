from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages

from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm


from .forms import *

def organizerRegister(request):
    if request.method == 'POST':
        form = OrgRegisterForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account has been created! You are now able to login')
            return redirect('login')
    else:
        form = OrgRegisterForm()
        return render(request, 'users/org_register.html', { 'form':form})

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = OrgUpdateForm(request.POST, instance=request.user.organizer) if user.is_staff else StudentUpdateForm(request.POST,instance=request.user.student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile has been updated!')
            return redirect('profile')
    else:
        form = OrgUpdateForm(instance=request.user.organizer) if user.is_staff else StudentUpdateForm(instance=request.user.student)

    return render(request, 'users/profile.html', { "form":form })


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
