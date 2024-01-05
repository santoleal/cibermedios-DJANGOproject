from django.http import HttpResponse
from django.template import Template, Context




def testeo(request):
    return HttpResponse("Hola, está llegando bein")



