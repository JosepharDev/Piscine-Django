from django.shortcuts import render
from .models import People, Planets
from django.http import HttpResponse
# Create your views here.
def display(request):
    try:
        if not People.objects.exists():
            pass
    except Exception:
        command = "No data available, please make migrations first"
        return HttpResponse(f"""<!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Django 05</title>
        </head>
        <body>
            {command}
        </body>
        </html>
        """)
    people = People.objects.filter(homeworld__climate__icontains="windy").order_by("name").select_related("homeworld")
    context = {
        "people": people,
        "loaddata_command": "python3 manage.py loaddata ex09_initial_data.json"
    }
    return render(request, "display.html", context)