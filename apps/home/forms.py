from django import forms
from .models import Pais, Ciudad

class AgregarInformacionForm(forms.Form):
    pais = forms.CharField(label='País', max_length=100)
    ciudad = forms.CharField(label='Ciudad', max_length=100)
    calle = forms.CharField(label='Calle', max_length=100)

class BuscarForm(forms.Form):
    pais = forms.CharField(label='Pais', max_length=100)
    ciudad = forms.CharField(label='Ciudad', max_length=100)
