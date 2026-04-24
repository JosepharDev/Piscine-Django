from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
import random, time
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    username = get_or_create_username(request)
    context = {
                'username': username
            } 
    return render(request, "base.html", context)

def get_or_create_username(request):
    current_time = time.time()
    if "username" not in request.session \
        or (current_time - request.session.get('name_timestamp', 0)) > settings.NAME_VALIDITY_SECONDS:    
        
        new_name = random.choice(settings.USERNAME)
        request.session['username'] = new_name
        request.session['name_timestamp'] = current_time
        request.session.modified = True
        return new_name
    return request.session['username']

def get_name(request):
    username = get_or_create_username(request)
    return JsonResponse({'username': username})

def logout_view(request):
    logout(request) 
    return redirect("login")

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, "login.html", {"form":form,"error": "Invalid credentials"})
        return render(request, 'login.html', {
            'form': form,
            'error': 'Please correct the form'
        })
    else:
        form = LoginForm()
    username = get_or_create_username(request)
    return render(request, 'login.html', {'form': form, "username": username})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save to the database yet
            user.set_password(form.cleaned_data['password'])
            user.save()  # Now save to the database
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    username = get_or_create_username(request)
    return render(request, 'register.html', {'form': form, "username": username})