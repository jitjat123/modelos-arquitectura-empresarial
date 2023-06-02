from django.db import models

# Create your models here.

class DireccionEjecutiva(models.Model):

    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name='Direccion ejecutiva'
        verbose_name_plural='Direcciones ejecutivas'

    def __str__(self):
        return self.nombre  
    

class Departamento(models.Model):

    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    direccion = models.ForeignKey(DireccionEjecutiva, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Departamento'
        verbose_name_plural='Departamentos'

    def __str__(self):
        return self.nombre  
    
class Trabajador(models.Model):

    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Trabajador'
        verbose_name_plural='Trabajadores'

    def __str__(self):
        return self.nombre  
    
class Actividad(models.Model):

    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    Trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Actividad'
        verbose_name_plural='Actividades'

    def __str__(self):
        return self.nombre  
    
class Recurso(models.Model):

    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Recurso'
        verbose_name_plural='Recursos'

    def __str__(self):
        return self.nombre  