from django.urls import path 

from mediosDigitales.views import cibermedios, investigaciones, investigadores, index, agregar_cibermedio, buscar_cibermedio, buscar

urlpatterns = [
    # path('agregar-cibermedios/', agregar_cibermedios),
    # path('cibermedios/',listar_cibermedios),
    # path('agregar-investigaciones/',agregar_investigaciones),
    # path('investigaciones/',listar_investigaciones),
    # path('agregar-investigadores/',agregar_investigadores),
    # path('investigadores/',listar_investigadores),
    path('', index, name='index'),
    path('cibermedios/', cibermedios, name= "cibermedios"),
    path('investigaciones/', investigaciones, name= 'investigaciones'),
    path('investigadores/', investigadores, name= 'investigadores' ),
    path('cibermedios-formulario/', agregar_cibermedio, name="cibermedios-formulario"),
    path('busqueda-cibermedio/', buscar_cibermedio, name="busqueda-cibermedio"),
    path('buscar/', buscar, name='buscar')


]