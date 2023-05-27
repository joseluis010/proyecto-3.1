from django import forms

class AgregarInformacionForm(forms.Form):
    pais = forms.CharField(label='País', max_length=100)
    ciudad = forms.CharField(label='Ciudad', max_length=100)
    calle = forms.CharField(label='Calle', max_length=100)

class BuscarForm(forms.Form):
    ciudad = forms.CharField(label='Ciudad', max_length=100)
