from django.shortcuts import render, redirect
from .models import Movies
from django.http import HttpResponse
from .forms import update_op
# Create your views here.

def populate(request):
    try:
        movies = [
            Movies(episode_nb=1, title="The Phantom Menace", director=" George Lucas", producer="Rick McCallum", release_date="1999-05-19"),
            Movies(episode_nb=2, title="Attack of the Clones", director="George Lucas", producer="Rick McCallum", release_date="2002-05-16"),
            Movies(episode_nb=3, title="Revenge of the Sith", director="George Lucas", producer="Rick McCallum", release_date="2005-05-19"),
            Movies(episode_nb=4, title="A New Hope", director="George Lucas", producer="Gary Kurtz, Rick McCallum", release_date="1977-05-25"),
            Movies(episode_nb=5, title="The Empire Strikes Back", director="Irvin Kershner", producer="Gary Kurtz, Rick McCallum", release_date="1980-05-17"),
            Movies(episode_nb=6, title="Return of the Jedi", director="Richard Marquand", producer="Howard G. Kazanjian, George Lucas, Rick McCallum", release_date="1983-05-25"),
            Movies(episode_nb=7, title="The Force Awakens", director=" J. J. Abrams", producer="Kathleen Kennedy, J. J. Abrams, Bryan Burk", release_date="2015-12-11")
        ]
        objs = Movies.objects.bulk_create(movies)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse("No data available")

def display(request):
    try:
        data = Movies.objects.all()
        print(data)
        if not data.exists():
            return HttpResponse("No data available")
        return render(request, "ex07_display.html", {"data": data})
    except Exception as e:
        return HttpResponse("No data available")

def update(request):
    log_message = None
    try:
        movies = Movies.objects.all()
        if not movies.exists():
            return render(request, 'ex07_update.html', {"log_message": "No data available"})
    except Exception:
        return render(request, 'ex07_update.html', {"log_message": "No data available"})

    if request.method == 'POST':
        form = update_op(request.POST)
        if form.is_valid():
            title = form.cleaned_data['drop_down']
            text = form.cleaned_data["text"]
            row = Movies.objects.get(title=title)
            row.opening_crawl = text
            row.save()
            return redirect("update")
    else:
        form = update_op()
        return render(request, "ex07_update.html", {"form":form, "show_form":True})