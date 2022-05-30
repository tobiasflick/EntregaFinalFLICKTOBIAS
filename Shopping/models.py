from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

class Locales(models.Model):
    cantLocales=models.IntegerField(default=0)
    nomLocales=models.CharField(max_length=100,default=0)
    class Meta:
        verbose_name="Local"
        verbose_name_plural="Locales"

class PatioComidas(models.Model):
    cantLocales=models.IntegerField(default=0)
    nomLocales=models.CharField(max_length=100, default=0)
    class Meta:
        verbose_name="Patio de Comidas"
        verbose_name_plural="Patio de Comidas"

class Cine(models.Model):
    cine="Cinemark"
    cantPelis=models.IntegerField(default=0)
    peliculas=models.CharField(max_length=100, default=0)
    class Meta:
        verbose_name="Cine"
        verbose_name_plural="Cines"

class RegistroPromos(models.Model):
    nombre=models.CharField(max_length=100)
    email=models.EmailField()
    edad=models.IntegerField(default=0)
    class Meta:
        verbose_name="Usuario_Promo"
        verbose_name_plural="Usuarios_Promos"
    def __str__(self):
        return f"Nombre: {self.nombre} - Email {self.email} - Edad {self.edad}"

class Usuarios(models.Model):
    nombre=models.CharField(max_length=100)
    edad=models.IntegerField(default=0)
    email=models.EmailField()
    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"
    
class Avatares(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)

    


