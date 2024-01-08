from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.

class Cibermedios(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    anio_creacion = models.IntegerField(
        validators=[MinValueValidator(1980), MaxValueValidator(2025)])
    comentario = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} / {self.pais} / {self.url}"

    class Meta():
        verbose_name = "Cibermedio"
        verbose_name_plural = "Cibermedios"
        ordering = ('nombre',)


class Investigadores(models.Model):
    nombre = models.CharField(max_length=200) 
    pais = models.CharField(max_length=200)
    biografia = models.CharField(max_length=500, blank=True, null=True)
    link = models.CharField(max_length=200)
    # Fotografía? Cómo agregarla?

    def __str__(self):
        return f"{self.nombre} / {self.pais}"
    

    class Meta():
        verbose_name = "Investigador/a"
        verbose_name_plural = "Investigadores/as"
        ordering = ("nombre",)

class Investigaciones(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=200)
    anio_publicacion = models.DateField()
    pais_referencia = models.CharField(max_length=200)
    resumen = models.CharField(max_length=500, blank=True, null=True)
    palabras_claves = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __str__(self):
        return f"Título: {self.titulo} / Autores: {self.autores} / Año de publicación: {self.anio_publicacion.year} "

    class Meta():
        verbose_name = "Investigación"
        verbose_name_plural = "Investigaciones"
        ordering = ("titulo",)
