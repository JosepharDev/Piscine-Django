from django.shortcuts import render


def index(request):
    """Display the Markdown cheatsheet page"""
    return render(request, 'index.html')
