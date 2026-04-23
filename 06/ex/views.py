from django.shortcuts import render
from django.conf import settings
import random, time

# Create your views here.


def index(request):
    current_time = time.time()
    if "username" not in request.session \
        or (current_time - request.session.get('name_timestamp', 0)) > settings.NAME_VALIDITY_SECONDS:    
        
        new_name = random.choice(settings.USERNAME)
        request.session['username'] = new_name
        request.session['name_timestamp'] = current_time
        request.session.modified = True
        
        context = {
            'username': request.session['username']
        } 
        return render(request, "home.html", context)