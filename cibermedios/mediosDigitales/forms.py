from django import forms
import datetime

anio_actual = datetime.datetime.now().year

class AgregarCibermedio(forms.Form):
    nombre = forms.CharField(max_length=200)
    pais = forms.CharField(max_length=200)
    url = forms.CharField(max_length=200)
    #anio_creacion = forms.DateField(widget=forms.SelectDateWidget(years=ANIO_CREACION))
    rango_anios = [(year, year) for year in range(1990, anio_actual + 1)]
    anio_creacion = forms.ChoiceField(label='Año de Creación', help_text='Ingrese el año aproximado de creación del cibermedio (considerando sólo su versión en internet)', choices=rango_anios)
    comentario = forms.CharField(max_length=500, required=False)



class BusquedaCibermedio(forms.Form):
    pais = forms.CharField(max_length=200)




