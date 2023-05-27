from django.shortcuts import render, redirect
from .models import Pais, Ciudad, Calle
from .forms import AgregarInformacionForm, BuscarForm


def index(request):
    return render(request, 'index.html')


def agregar_informacion(request):
    if request.method == 'POST':
        form = AgregarInformacionForm(request.POST)
        if form.is_valid():
            pais = form.cleaned_data['pais']
            ciudad = form.cleaned_data['ciudad']
            calle = form.cleaned_data['calle']

            pais_obj, created = Pais.objects.get_or_create(nombre=pais)
            ciudad_obj, created = Ciudad.objects.get_or_create(nombre=ciudad, pais=pais_obj)
            Calle.objects.create(nombre=calle, ciudad=ciudad_obj)

            return redirect('agregar')
    else:
        form = AgregarInformacionForm()

    return render(request, 'agregar_informacion.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            ciudad = form.cleaned_data['ciudad']
            calles = Calle.objects.filter(ciudad__nombre=ciudad)

            return render(request, 'buscar.html', {'calles': calles})
    else:
        form = BuscarForm()

    return render(request, 'buscar.html', {'form': form})
