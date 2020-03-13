from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm, UsernameField

from .models import Student, Organizer

class OrgUpdateForm(ModelForm):
    class Meta:
        model = Organizer
        exclude = ['user', 'idno']

class OrgRegisterForm(UserCreationForm):
    is_staff = forms.BooleanField(initial=True, widget=forms.HiddenInput)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_staff']

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['user', 'idno', 'events']


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='',
        widget=forms.TextInput(attrs={'autofocus': True,'placeholder':'Username'})
    )
    password = UsernameField(
        label='',
        widget=forms.PasswordInput(attrs={'autofocus': True,'placeholder':'Password'})
    )
