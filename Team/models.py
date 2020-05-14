from django.db import models

class Desarrolladore(models.Model):
    nombre=models.CharField(max_length=30)
    email=models.EmailField(blank=True)
    tfno=models.CharField(max_length=15, verbose_name="Telefono")
    seniority=models.CharField(max_length=10)
    area=models.CharField(max_length=15)
    lenguajes=models.CharField(max_length=255)
    ingles=models.CharField(max_length=20, default='basico')
    estudios_Universitaros=models.CharField(max_length=255,blank=True)
    rating=models.IntegerField()
    disponible=models.BooleanField()

    def __str__(self):
        return self.nombre

