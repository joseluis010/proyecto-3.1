
from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name='index'),
    path('explicar/', views.explicar, name='explicar'),
    path('agregar/', views.agregar_informacion, name='agregar'),
    path('buscar/', views.buscar, name='buscar'),
]

