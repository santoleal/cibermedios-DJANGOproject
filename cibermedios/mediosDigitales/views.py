from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from mediosDigitales.models import Cibermedios, Investigadores, Investigaciones

from mediosDigitales.forms import AgregarCibermedio, BusquedaCibermedio

# Create your views here.

## 1.  Se habilita la vista - plantilla HTML - para página de inicio 
def index(request):
    return render(request, 'index.html')


## 2.Se crea vista de los modelos creados

def cibermedios(request):
    
    return render(request, 'cibermedios.html')


def investigaciones(request):
    return render(request, "investigaciones.html")


def investigadores(request):
    return render(request, "investigadores.html")





## 2. Trabajar con ver y agregar Cibermedios desde formularios

"""
# Esta es un modo de crear un formulario HTML - POSTS
def cibermediosFormularios(request):
    print(f"path: {request.path}")
    print(f"full path: {request.get_full_path()}")
    print(f"host: {request.get_host()}")
    print(f"si es segura: {request.is_secure()}")
    print(f"método: {request.method}")
    ua = request.META.get("HTTP_USER_AGENT")
    print(f"ua: {ua}")

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        pais = request.POST.get("pais")
        url = request.POST.get("url")
        anio_creacion = request.POST.get("anio_creacion")
        comentario = request.POST.get("comentario")

        print(f'''CIBERMEDIO INGRESADO: 
              - Nombre: {nombre}
              - País: {pais} 
              - Dirección web: {url} -
              - Año de creación: {anio_creacion} 
              - Comentario: {comentario}              
              ''' )
        
        cibermedio = Cibermedios(nombre = nombre, pais = pais, url = url, anio_creacion = anio_creacion, comentario = comentario)

        cibermedio.save()

        return render(request, 'index.html')


    return render(request, "formularios/cibermediosFormularios.html")

"""

def agregar_cibermedio(request):

    if request.method == "POST":

        miFormulario = AgregarCibermedio(request.POST)

        #print("formulario: ")
        #print(cibermedio)

        print(f" ¿Es válido?: {miFormulario.is_valid} ")

        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data

            nombre = datos.get("nombre")
            pais = datos.get("pais")
            url = datos.get("url")
            anio_creacion = datos.get("anio_creacion")
            comentario = datos.get("comentario")

            nuevo_cibermedio = Cibermedios(nombre = nombre, pais = pais, url = url, anio_creacion = anio_creacion, comentario = comentario)

            nuevo_cibermedio.save()

            return render(request, 'index.html')
        
    else:
        miFormulario = AgregarCibermedio()

    return render(request, "formularios/cibermediosFormularios.html", {"miFormulario": miFormulario})







def buscar_cibermedio(request):

    formulario = BusquedaCibermedio()
    # if request.method == "GET":

    #     nombre_medio = request.GET.get("nombre")
    #     print(f"Se busca este cibermedio: {nombre_medio}") 

    return render(request, "formularios/cibermedioBusqueda.html", {"formulario": formulario})



def buscar(request):
    
    if request.method == "GET":
        pais = request.GET.get("pais")

        if pais is None:
            return HttpResponse("Debe enviar un país")
    
    cibermedio = Cibermedios.objects.filter(pais = pais)

    return render(request,"formularios/busqueda.html", {"cibermedio": cibermedio} )

    #nombre = Cibermedios.objects.filter(url__icontains = url)

        # if nombre is None:
        #     return HttpResponse("Todavía no se envían los datos a buscar")
    
    # contexto = {
    #     "nombre": nombre,
    #     "url": url
    # }

    # return render(request, "formularios/busqueda.html", contexto)









## 3.- Trabajar con ver y agregar Investigaciones
def agregar_investigaciones(request):
    return HttpResponse("Agregar Investigaciones")

def listar_investigaciones(request):
    return HttpResponse("Listar Investigaciones")



## 4.- Trabajar con ver y agregar Investigadores
def agregar_investigadores(request):
    return HttpResponse("Agregar Ivestigadores")

def listar_investigadores(request):
    return HttpResponse("Listar Ivestigadores")




