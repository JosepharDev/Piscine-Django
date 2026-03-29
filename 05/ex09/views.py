from django.shortcuts import render
from django.http import HttpResponse
from .models import People, Planets
# Create your views here.

def display(request):
    try:
        data = People.objects.filter(homeworld__climate_in=["windy", "moderately windy"]).order_by("name")
        if not People.exists():
            return render(request, "ex09/display.html", {"error": "No data available, please use the following command line before use:",
            "command": "python manage.py loaddata ex09_initial_data.json"})
        return render(request, "ex09/display.html", {"people": people})
    except Exception as e:
            return HttpResponse(f"{e}")