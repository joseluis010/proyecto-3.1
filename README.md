# Baños Públicos 
Este proyecto es una aplicación web para buscar y agregar información sobre baños públicos en diferentes ciudades. Permite a los usuarios encontrar baños cercanos y agregar nuevos baños a la base de datos.

## Características

- Búsqueda de baños: Los usuarios pueden buscar baños públicos en una ciudad específica. La búsqueda se realiza por país y ciudad, y muestra los resultados de la dirección de los baños encontrados en la ciudad seleccionada.

- Agregar información: Los usuarios pueden agregar nuevos baños públicos a la base de datos. Deben proporcionar información como país, ciudad y dirección del baño.

- Validación de datos: El sistema valida los datos ingresados por los usuarios para garantizar la integridad de la información. Se verifican campos obligatorios y se realizan comprobaciones adicionales para asegurarse de que los datos sean válidos y consistentes.

- Mensajes de retroalimentación: Se utilizan mensajes de retroalimentación para informar a los usuarios sobre el resultado de sus acciones. Los mensajes pueden ser de éxito, error o información, y se muestran en la interfaz de usuario para proporcionar una mejor experiencia de uso.



## Paso a Paso

- Al clonar en git primero debemos ejecutar estos 3 comandos :

 º python manage.py makemigrations

 º python manage.py migrate

 º python manage.py runserver




- Creo una aplicación llamada HOME en la carpeta "apps"
- La agrego en config/settings.py  en 
    INSTALLED_APPS = [ ...  "home", ]
- En config/urls.py dejo estos valores: 

    from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(("home.urls", "home"))),
]

- En apps/home/ creamos urls.py y agregamos estos valores
    
from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name='index'),
    PARA INGRESAR AL INDEX O PANTALLA PRINCIPAL.

    path('agregar/', views.agregar_informacion, name='agregar'),
    PARA INGRESAR AL ÁREA DONDE INGRESAMOS LOS DATOS DE LOS BAÑOS PÚBLICOS.


    path('buscar/', views.buscar, name='buscar'),
    PARA INGRESAR AL BUSCADOR DE BAÑOS.
]   


- En apps/home/models.py creamos 3 clases: PAIS, CIUDAD, CALLE
    donde CIUDAD depende de PAIS y CALLE de ambas 2.


- En apps/home/forms.py creamos dos clases para crear formularios:
º ºAgregarInformacionForm
    donde agregamos: pais, ciudad y calle 
    
º BuscarForm
    donde buscamos las calles indicando los campos pais y ciudad


º si la calle no existe la crea y devuelve un mensaje de que fue creado y refresca la pagina
    º si la calle ya existe nos devuelve un mensaje de que la calle ya existe y no refresca la pagina, nos permite ver si el error fue de tipeo.

- En apps/home/views.py tenemos 4 funciones una para mostrar el index, la explicacion del programa y otras 2 para agregar informacion sobre los baños y para buscar calles que tengan baños 
  
  º nos pide agregar el país y la ciudad, si hay calles creadas nos muestra todas.
    º si no hay calles creadas nos devuelve un mensaje de que no se encontraron calles    

- En apps/home/admin.py     
    creo los campos en admin: Pais, Ciudad y Calle
    en el superusercreate pusimos: admin y pass: 1234


- Tengo 6 templates
º base.html 
º index.html
º explicar.html
º footer.html
º agregar_informacion.html
º buscar.html

## Cosas a mejorar

- me hubiera gustado agregarle una plantilla de Bootstrap, pero no comprendí bien esa área, cuando intentaba hacer cambios me daba error mi programa, por eso es que no lo continué.
- La parte de formularios me costó bastante entender, tanto el código que hay que agregar en el html como en el controlador.
Hubo mucho de copia y pego y aún intentando buscar la info, no he logrado entenderlo.