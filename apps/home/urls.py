
from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_informacion, name='agregar_informacion'),
    path('buscar/', views.buscar, name='buscar'),
]