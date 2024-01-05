from django.urls import path 

from mediosDigitales.views import agregar_cibermedios, listar_cibermedios, agregar_investigaciones, listar_investigaciones, agregar_investigadores, listar_investigadores, index

urlpatterns = [
    path('agregar-cibermedios/', agregar_cibermedios),
    path('cibermedios/',listar_cibermedios),
    path('agregar-investigaciones/',agregar_investigaciones),
    path('investigaciones/',listar_investigaciones),
    path('agregar-investigadores/',agregar_investigadores),
    path('investigadores/',listar_investigadores),
    path('', index)

]