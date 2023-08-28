# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Event

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'category', 'date', 'location']