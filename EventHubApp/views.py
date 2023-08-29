from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, LoginForm
from .models import Event
from django.contrib.auth.decorators import login_required
from .forms import EventCreationForm
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'base.html')

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

@login_required
def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'event_detail.html', {'event': event})


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user  # Associate the event with the logged-in user
            event.category = form.cleaned_data['category']
            event.save()
            return redirect('event_list')  # Redirect to event list page
    else:
        form = EventCreationForm()
    return render(request, 'event_creation.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def delete_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id, user=request.user)
        event.delete()
        return redirect('event_list')  # Redirect to event list page
    except Event.DoesNotExist:
        return HttpResponseForbidden()  # Display an error message or handle as needed

def custom_admin(request):
    if request.user.is_staff:
        users = User.objects.all()
        events = Event.objects.all()
        total_events = events.count()
        total_users = users.count()

        context = {
            'users': users,
            'events': events,
            'total_events': total_events,
            'total_users': total_users,
        }
        return render(request, 'admin_dashboard.html', {'users': users, 'events': events})
    else:
        return HttpResponse("Unauthorized")

