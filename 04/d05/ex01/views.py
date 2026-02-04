from django.shortcuts import render


def django_page(request):
    """Display Django introduction page"""
    return render(request, 'django.html')


def display_page(request):
    """Display process of static page"""
    return render(request, 'display.html')


def templates_page(request):
    """Display template engine information"""
    return render(request, 'templates.html')
