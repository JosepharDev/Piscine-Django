from django.shortcuts import render


def index(request):
    name = "Ex00: Markdown Cheatsheet."
    return render(request, 'index.html', context={"name":name})