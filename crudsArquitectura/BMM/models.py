from django.db import models

# Create your models here.

# Modelo BMM

class Mision(models.Model):
    nombre=models.CharField(max_length=60)
    descripcion=models.TextField(max_length=1400)

    class Meta:
        verbose_name='Mision'
        verbose_name_plural='Misiones'

    def __str__(self):
        return self.nombre
    
class Vision(models.Model):
    nombre=models.CharField(max_length=60)
    descripcion=models.TextField(max_length=1400)
    mision = models.ForeignKey(Mision, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Vision'
        verbose_name_plural='Visiones'

    def __str__(self):
        return self.nombre
    
class Estrategia(models.Model):
    nombre=models.CharField(max_length=60)
    descripcion=models.TextField(max_length=1400)
    mision = models.ForeignKey(Mision, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Estrategia'
        verbose_name_plural='Estrategias'

    def __str__(self):
        return self.nombre
    
class Tactica(models.Model):
    nombre=models.CharField(max_length=60)
    descripcion=models.TextField(max_length=1400)
    estrategia = models.ForeignKey(Estrategia, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Tactica'
        verbose_name_plural='Tacticas'

    def __str__(self):
        return self.nombre
    
    
class Objetivo(models.Model):
    nombre=models.CharField(max_length=60)
    descripcion=models.TextField(max_length=1400)
    estrategia = models.ForeignKey(Estrategia, on_delete=models.CASCADE)
    vision = models.ForeignKey(Vision, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Objetivo'
        verbose_name_plural='Objetivos'

    def __str__(self):
        return self.nombre
    
class Meta(models.Model):
    nombre=models.CharField(max_length=60)
    descripcion=models.TextField(max_length=1400)
    tactica = models.ForeignKey(Tactica, on_delete=models.CASCADE)
    objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Meta'
        verbose_name_plural='Metas'

    def __str__(self):
        return self.nombre