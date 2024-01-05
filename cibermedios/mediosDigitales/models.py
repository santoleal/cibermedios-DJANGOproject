from django.db import models
# Create your models here.

class Cibermedios(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    anio_creacion = models.DateField()
    comentario = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - País: {self.pais} - URL: {self.url} - Año Creación: {self.anio_creacion.year} - Comentario{self.comentario}"


class Investigadores(models.Model):
    nombre = models.CharField(max_length=200) 
    pais = models.CharField(max_length=200)
    biografia = models.CharField(max_length=500, blank=True, null=True)
    link = models.CharField(max_length=200)
    # Fotografía? Cómo agregarla?

    def __str__(self):
        return f"Nombre: {self.nombre} - País: {self.pais} - Bio: {self.biografia} - - Link: {self.link}"
    

class Investigaciones(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=200)
    anio_publicacion = models.DateField()
    pais_referencia = models.CharField(max_length=200)
    resumen = models.CharField(max_length=500, blank=True, null=True)
    palabras_claves = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __str__(self):
        return f"Título: {self.titulo} - Autores: {self.autores} - Año de publicación: {self.anio_publicacion.year} - País de estudio: {self.pais_referencia} - Resumen: {self.resumen} - Palabras claves: {self.palabras_claves} - Link: {self.link}"


