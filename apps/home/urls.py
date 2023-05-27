
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
    path('agregar/', views.agregar_informacion, name='agregar'),
    path('buscar/', views.buscar, name='buscar'),
]