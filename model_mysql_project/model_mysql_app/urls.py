from django.urls import __path__
from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit', views.home)
]