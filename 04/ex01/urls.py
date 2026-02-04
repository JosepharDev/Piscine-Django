from django.urls import path
from . import views

urlpatterns = [
    path('django/', views.django_page, name='ex01-django'),
    path('django', views.django_page),
    path('display/', views.display_page, name='ex01-display'),
    path('display', views.display_page),
    path('templates/', views.templates_page, name='ex01-templates'),
    path('templates', views.templates_page),
]
