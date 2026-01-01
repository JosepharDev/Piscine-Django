from . import views
from django.urls import path

urlpatterns = [
    path('django', views.into_django),
    path('display', views.display),
    path('templates', views.templates)
]