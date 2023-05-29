from django.contrib import messages  #mensaje de alerta
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

            # Verificar si la calle ya existe en la ciudad
            calle_obj, created = Calle.objects.get_or_create(nombre=calle, ciudad=ciudad_obj, pais=pais_obj )
            if created:
                # La calle ya existe, mostrar un mensaje de error o realizar alguna acción adicional
                    messages.error(request, 'La calle ha sido creada con exito.')
                    return redirect('home:agregar')

                # messages.success(request, 'Información agregada exitosamente.')  # Mensaje de éxito
                # return redirect('home:agregar')
            else:
                messages.error(request, 'La calle ya existe.')  # Mensaje de error
    else:
        form = AgregarInformacionForm()

    return render(request, 'agregar_informacion.html', {'form': form})




def buscar(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            pais = form.cleaned_data['pais']
            ciudad = form.cleaned_data['ciudad']
            
            calles = Calle.objects.filter(ciudad__nombre=ciudad, ciudad__pais__nombre=pais)
            if calles:
                return render(request, 'buscar.html', {'calles': calles})
            else:
                messages.info(request, 'No se encontraron calles en la ciudad buscada.')
        
    else:
        form = BuscarForm()

    return render(request, 'buscar.html', {'form': form})
