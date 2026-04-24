from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('getname', views.get_name),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout')
]
