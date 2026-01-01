from django.shortcuts import render
from django.shortcuts import render


def into_django(request):
    title = "Ex01: Django, framework web."
    return render(request, 'into_django.html', context={"title":title})


def display(request):
    title = "Ex01: Display process of a static page."
    return render(request, 'display.html', context={"title":title})


def templates(request):
    title = "Ex01: Template engine."
    return render(request, 'templates.html', context={"title":title})